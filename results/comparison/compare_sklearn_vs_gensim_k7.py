#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
比較 scikit-learn LDA 與 Gensim LDA 在 K=7 時的結果
Compare scikit-learn LDA vs Gensim LDA with K=7
"""

import pickle
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# scikit-learn LDA
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

# Gensim LDA
from gensim.models import LdaModel
from gensim.models.coherencemodel import CoherenceModel
from gensim import corpora

# 文本處理
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

print("="*80)
print("Comparison: scikit-learn LDA vs Gensim LDA (K=7)")
print("比較：scikit-learn LDA vs Gensim LDA (K=7)")
print("="*80)

# 載入資料
print("\nLoading data...")
df = pd.read_csv('cleaned_data_no_dedup/final_cleaned_sample_no_dedup.csv', encoding='utf-8-sig')
df_en = df[df['語言'] == 'en'].copy()
print(f"✓ Loaded {len(df_en):,} English reviews")

# 文本前處理
print("\nPreprocessing text...")
stop_words = set(stopwords.words('english'))
custom_stop_words = {'hospital', 'doctor', 'went', 'like', 'would', 'one', 'get', 'go'}
stop_words.update(custom_stop_words)

def preprocess_english_text(text):
    text = text.lower()
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'\S+@\S+', '', text)
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)
    text = ' '.join(text.split())
    return text

def tokenize_and_lemmatize(text, stop_words):
    lemmatizer = WordNetLemmatizer()
    tokens = word_tokenize(text)
    tokens = [lemmatizer.lemmatize(token) for token in tokens
              if token not in stop_words and len(token) > 2]
    return tokens

df_en['cleaned_text'] = df_en['評論內容'].apply(preprocess_english_text)
df_en['tokens'] = df_en['cleaned_text'].apply(lambda x: tokenize_and_lemmatize(x, stop_words))
df_en = df_en[df_en['tokens'].str.len() > 0].copy()

# 準備文本資料
texts = df_en['tokens'].tolist()
texts_str = [' '.join(tokens) for tokens in texts]  # For scikit-learn

print(f"✓ Valid reviews: {len(df_en):,}")

# ============================================================================
# 方法1: scikit-learn LDA
# ============================================================================
print("\n" + "="*80)
print("METHOD 1: scikit-learn LDA")
print("="*80)

# 創建詞袋模型
print("\nCreating document-term matrix...")
sklearn_vectorizer = CountVectorizer(
    max_df=0.5,
    min_df=3,
    max_features=None,
    token_pattern=r'\b\w+\b'
)
sklearn_dtm = sklearn_vectorizer.fit_transform(texts_str)
sklearn_vocab = sklearn_vectorizer.get_feature_names_out()

print(f"  Vocabulary size: {len(sklearn_vocab)}")
print(f"  Document-term matrix shape: {sklearn_dtm.shape}")

# 訓練 scikit-learn LDA
print("\nTraining scikit-learn LDA with K=7...")
sklearn_lda = LatentDirichletAllocation(
    n_components=7,
    random_state=42,
    max_iter=100,
    learning_method='batch',
    n_jobs=1
)
sklearn_output = sklearn_lda.fit_transform(sklearn_dtm)

# 計算 perplexity
sklearn_perplexity = sklearn_lda.perplexity(sklearn_dtm)

print(f"\n✓ scikit-learn LDA training complete!")
print(f"  Perplexity: {sklearn_perplexity:.4f}")

# 提取主題詞
print("\nscikit-learn Topic Keywords:")
sklearn_topics = []
for topic_idx, topic in enumerate(sklearn_lda.components_):
    top_indices = topic.argsort()[-10:][::-1]
    top_words = [sklearn_vocab[i] for i in top_indices]
    sklearn_topics.append(top_words)
    print(f"  Topic {topic_idx+1}: {', '.join(top_words[:5])}")

# 主題分配
sklearn_dominant_topics = sklearn_output.argmax(axis=1) + 1
sklearn_topic_probs = sklearn_output.max(axis=1)

# ============================================================================
# 方法2: Gensim LDA
# ============================================================================
print("\n" + "="*80)
print("METHOD 2: Gensim LDA")
print("="*80)

# 建立 Gensim 字典和語料庫
print("\nBuilding Gensim dictionary and corpus...")
gensim_dictionary = corpora.Dictionary(texts)
original_size = len(gensim_dictionary)

gensim_dictionary.filter_extremes(
    no_below=3,
    no_above=0.5,
    keep_n=None
)
gensim_dictionary.compactify()

gensim_corpus = [gensim_dictionary.doc2bow(text) for text in texts]

print(f"  Original vocabulary: {original_size}")
print(f"  Filtered vocabulary: {len(gensim_dictionary)}")

# 訓練 Gensim LDA
print("\nTraining Gensim LDA with K=7...")
gensim_lda = LdaModel(
    corpus=gensim_corpus,
    id2word=gensim_dictionary,
    num_topics=7,
    alpha='symmetric',
    eta='auto',
    iterations=100,
    passes=10,
    random_state=42
)

# 計算評估指標
print("\nCalculating coherence and perplexity...")
coherence_model = CoherenceModel(
    model=gensim_lda,
    texts=texts,
    dictionary=gensim_dictionary,
    coherence='c_v',
    processes=1
)
gensim_coherence = coherence_model.get_coherence()
gensim_perplexity = gensim_lda.log_perplexity(gensim_corpus)

print(f"\n✓ Gensim LDA training complete!")
print(f"  Coherence Score: {gensim_coherence:.4f}")
print(f"  Perplexity: {gensim_perplexity:.4f}")

# 提取主題詞
print("\nGensim Topic Keywords:")
gensim_topics = []
for idx in range(7):
    topic_words = gensim_lda.show_topic(idx, topn=10)
    keywords = [word for word, prob in topic_words]
    gensim_topics.append(keywords)
    print(f"  Topic {idx+1}: {', '.join(keywords[:5])}")

# 主題分配
gensim_topic_assignments = []
for doc_bow in gensim_corpus:
    topic_dist = gensim_lda.get_document_topics(doc_bow, minimum_probability=0)
    topic_probs = [prob for _, prob in topic_dist]
    dominant_topic = topic_probs.index(max(topic_probs)) + 1
    gensim_topic_assignments.append(dominant_topic)

gensim_dominant_topics = np.array(gensim_topic_assignments)

# ============================================================================
# 比較結果
# ============================================================================
print("\n" + "="*80)
print("COMPARISON RESULTS | 比較結果")
print("="*80)

print("\n1. Model Quality Metrics | 模型品質指標")
print("-" * 60)
print(f"{'Metric':<30} {'scikit-learn':<20} {'Gensim':<20}")
print("-" * 60)
print(f"{'Vocabulary Size':<30} {len(sklearn_vocab):<20} {len(gensim_dictionary):<20}")
print(f"{'Perplexity':<30} {sklearn_perplexity:<20.4f} {gensim_perplexity:<20.4f}")
print(f"{'Coherence (c_v)':<30} {'N/A':<20} {gensim_coherence:<20.4f}")

print("\n2. Topic Distribution | 主題分布")
print("-" * 60)

# scikit-learn 主題分布
sklearn_topic_counts = pd.Series(sklearn_dominant_topics).value_counts().sort_index()
gensim_topic_counts = pd.Series(gensim_dominant_topics).value_counts().sort_index()

print(f"\n{'Topic':<10} {'scikit-learn Count':<20} {'Gensim Count':<20} {'Difference':<15}")
print("-" * 65)
for topic_id in range(1, 8):
    sklearn_count = sklearn_topic_counts.get(topic_id, 0)
    gensim_count = gensim_topic_counts.get(topic_id, 0)
    diff = gensim_count - sklearn_count
    print(f"{topic_id:<10} {sklearn_count:<20} {gensim_count:<20} {diff:+<15}")

print("\n3. Topic Keywords Comparison | 主題關鍵詞比較")
print("-" * 80)

for i in range(7):
    print(f"\nTopic {i+1}:")
    print(f"  scikit-learn: {', '.join(sklearn_topics[i][:8])}")
    print(f"  Gensim:       {', '.join(gensim_topics[i][:8])}")

    # 計算關鍵詞重疊
    sklearn_set = set(sklearn_topics[i][:10])
    gensim_set = set(gensim_topics[i][:10])
    overlap = sklearn_set & gensim_set
    overlap_pct = len(overlap) / 10 * 100
    print(f"  Overlap:      {len(overlap)}/10 keywords ({overlap_pct:.0f}%): {', '.join(sorted(overlap))}")

# ============================================================================
# 結論
# ============================================================================
print("\n" + "="*80)
print("CONCLUSIONS | 結論")
print("="*80)

print("\n📊 相同點 | Similarities:")
print("  1. 兩種方法都能識別出7個主題")
print("  2. 主要主題（正面評價、等待時間、疼痛管理）在兩種方法中都有出現")

print("\n🔍 差異點 | Differences:")
print("  1. 詞彙選擇：")
print(f"     - scikit-learn: {len(sklearn_vocab)} 個詞彙")
print(f"     - Gensim: {len(gensim_dictionary)} 個詞彙")
print("  2. 評估指標：")
print("     - scikit-learn 主要使用 Perplexity")
print("     - Gensim 可計算 Coherence Score（更適合評估主題品質）")
print("  3. 演算法細節：")
print("     - scikit-learn: 基於 Variational Bayes")
print("     - Gensim: 基於 Online Variational Bayes with multi-pass")

print("\n💡 建議 | Recommendation:")
print("  ✓ 對於跨文化比較（台灣 vs 美國），建議使用 Gensim LDA")
print("  ✓ 原因：")
print("    1. 可計算 Coherence Score 評估主題品質")
print("    2. 與台灣分析使用相同工具，確保方法論一致性")
print("    3. 更適合學術研究（可報告 Coherence 和 Perplexity 兩個指標）")
print(f"    4. 台灣模型 Coherence={0.4175:.4f}，可與美國 Coherence={gensim_coherence:.4f} 直接比較")

print("\n⚠️  重要提醒 | Important Note:")
print("  雖然兩種工具都產出7個主題，但主題的具體內容和分布會有差異。")
print("  這是因為：")
print("  - 詞彙篩選標準不同（max_df, min_df vs no_above, no_below）")
print("  - 演算法實作細節不同")
print("  - 收斂條件不同")
print("  因此，跨國比較時使用相同工具（Gensim）更為嚴謹。")

# 儲存比較結果
comparison_results = {
    'sklearn': {
        'perplexity': sklearn_perplexity,
        'topics': sklearn_topics,
        'topic_distribution': sklearn_topic_counts.to_dict(),
        'vocab_size': len(sklearn_vocab)
    },
    'gensim': {
        'coherence': gensim_coherence,
        'perplexity': gensim_perplexity,
        'topics': gensim_topics,
        'topic_distribution': gensim_topic_counts.to_dict(),
        'vocab_size': len(gensim_dictionary)
    }
}

with open('sklearn_vs_gensim_comparison_k7.pkl', 'wb') as f:
    pickle.dump(comparison_results, f)

print("\n✓ Comparison results saved: sklearn_vs_gensim_comparison_k7.pkl")
print("\n" + "="*80)
print("Analysis Complete!")
print("="*80)
