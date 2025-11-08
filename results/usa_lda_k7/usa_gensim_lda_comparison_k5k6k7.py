#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
美國醫院評論 - 比較5、6、7個主題的LDA模型
使用Gensim LDA，與台灣分析相同方法
"""

import pickle
import pandas as pd
import numpy as np
from gensim.models import LdaModel
from gensim.models.coherencemodel import CoherenceModel
from gensim import corpora
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# 英文文本處理
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

print("="*80)
print("USA Hospital Reviews - LDA Model Comparison (K=5, 6, 7)")
print("美國醫院評論 - LDA模型比較（K=5, 6, 7）")
print("="*80)

# 文本前處理函數
def preprocess_english_text(text):
    """英文文本前處理"""
    text = text.lower()
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'\S+@\S+', '', text)
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)
    text = ' '.join(text.split())
    return text

def tokenize_and_lemmatize(text, stop_words):
    """分詞與詞形還原"""
    lemmatizer = WordNetLemmatizer()
    tokens = word_tokenize(text)
    tokens = [lemmatizer.lemmatize(token) for token in tokens
              if token not in stop_words and len(token) > 2]
    return tokens

# 載入資料
print("\nLoading data | 載入資料...")
df = pd.read_csv('cleaned_data_no_dedup/final_cleaned_sample_no_dedup.csv', encoding='utf-8-sig')
df_en = df[df['語言'] == 'en'].copy()
print(f"✓ Loaded {len(df_en):,} English reviews")
print(f"✓ 已載入 {len(df_en):,} 筆英文評論")

# 文本前處理
print("\nPreprocessing text | 文本前處理中...")
stop_words = set(stopwords.words('english'))
custom_stop_words = {'hospital', 'doctor', 'went', 'like', 'would', 'one', 'get', 'go'}
stop_words.update(custom_stop_words)

df_en['cleaned_text'] = df_en['評論內容'].apply(preprocess_english_text)
df_en['tokens'] = df_en['cleaned_text'].apply(lambda x: tokenize_and_lemmatize(x, stop_words))
df_en = df_en[df_en['tokens'].str.len() > 0].copy()

texts = df_en['tokens'].tolist()
print(f"✓ Valid reviews: {len(df_en):,}")
print(f"✓ 有效評論: {len(df_en):,}")

# 建立字典和語料庫
print("\nBuilding dictionary and corpus | 建立字典和語料庫...")
dictionary = corpora.Dictionary(texts)
original_size = len(dictionary)

dictionary.filter_extremes(
    no_below=3,
    no_above=0.5,
    keep_n=None
)
dictionary.compactify()

print(f"  Original vocabulary: {original_size} | 原始詞彙數: {original_size}")
print(f"  Filtered vocabulary: {len(dictionary)} | 過濾後詞彙數: {len(dictionary)}")

corpus = [dictionary.doc2bow(text) for text in texts]
print(f"✓ Corpus created: {len(corpus)} documents | 語料庫建立完成: {len(corpus)} 筆文檔")

# 訓練並比較不同主題數的模型
results = []

for num_topics in [5, 6, 7]:
    print("\n" + "="*80)
    print(f"Training K={num_topics} Model | 訓練 K={num_topics} 模型")
    print("="*80)

    # 訓練LDA模型
    lda_model = LdaModel(
        corpus=corpus,
        id2word=dictionary,
        num_topics=num_topics,
        alpha='symmetric',
        eta='auto',
        iterations=100,
        passes=10,
        random_state=42
    )

    # 計算coherence
    coherence_model = CoherenceModel(
        model=lda_model,
        texts=texts,
        dictionary=dictionary,
        coherence='c_v'
    )
    coherence_score = coherence_model.get_coherence()
    perplexity_score = lda_model.log_perplexity(corpus)

    print(f"\n  Coherence Score: {coherence_score:.4f}")
    print(f"  Perplexity: {perplexity_score:.4f}")

    # 顯示主題關鍵詞
    print(f"\n  Top Keywords per Topic:")
    for idx in range(num_topics):
        topic_words = lda_model.show_topic(idx, topn=5)
        keywords = ', '.join([word for word, prob in topic_words])
        print(f"    Topic {idx+1}: {keywords}")

    # 為每篇評論分配主題
    topic_assignments = []
    for doc_bow in corpus:
        topic_dist = lda_model.get_document_topics(doc_bow, minimum_probability=0)
        topic_probs = [prob for _, prob in topic_dist]
        dominant_topic = topic_probs.index(max(topic_probs)) + 1
        topic_assignments.append({
            'dominant_topic': dominant_topic,
            'topic_probability': max(topic_probs)
        })

    df_result = pd.concat([df_en.reset_index(drop=True), pd.DataFrame(topic_assignments)], axis=1)

    # 計算主題分布
    topic_dist = df_result['dominant_topic'].value_counts(normalize=True).sort_index() * 100

    print(f"\n  Topic Distribution:")
    for topic_id in range(1, num_topics + 1):
        if topic_id in topic_dist.index:
            count = len(df_result[df_result['dominant_topic'] == topic_id])
            percentage = topic_dist[topic_id]
            avg_rating = df_result[df_result['dominant_topic'] == topic_id]['評分'].mean()
            print(f"    Topic {topic_id}: {count} reviews ({percentage:.1f}%), Avg Rating: {avg_rating:.2f}")

    results.append({
        'num_topics': num_topics,
        'coherence': coherence_score,
        'perplexity': perplexity_score,
        'model': lda_model,
        'topic_distribution': topic_dist
    })

    # 儲存模型
    model_file = f'usa_gensim_lda_k{num_topics}_model.pkl'
    with open(model_file, 'wb') as f:
        pickle.dump({
            'lda_model': lda_model,
            'dictionary': dictionary,
            'coherence_score': coherence_score,
            'perplexity_score': perplexity_score
        }, f)
    print(f"  ✓ Model saved: {model_file}")

# 比較結果
print("\n" + "="*80)
print("COMPARISON RESULTS | 比較結果")
print("="*80)

comparison_df = pd.DataFrame([{
    'Topics': r['num_topics'],
    'Coherence Score': f"{r['coherence']:.4f}",
    'Perplexity': f"{r['perplexity']:.4f}"
} for r in results])

print("\n" + comparison_df.to_string(index=False))

# 找出最佳模型
best_idx = np.argmax([r['coherence'] for r in results])
best_model = results[best_idx]

print("\n" + "="*80)
print("RECOMMENDATION | 建議")
print("="*80)
print(f"\n🏆 Best Model: K={best_model['num_topics']}")
print(f"🏆 最佳模型: K={best_model['num_topics']}")
print(f"   Coherence Score: {best_model['coherence']:.4f}")
print(f"   Perplexity: {best_model['perplexity']:.4f}")

print("\n📊 Reasoning | 理由:")
if best_model['num_topics'] == 7:
    print("   ✓ K=7 matches Taiwan's analysis (台灣分析使用7個主題)")
    print("   ✓ Enables direct cross-cultural comparison (可直接進行跨文化比較)")
    print("   ✓ Highest coherence score (最高一致性分數)")
elif best_model['num_topics'] == 6:
    print("   ✓ Good balance between detail and interpretability")
    print("   ✓ 細緻度與可解釋性的良好平衡")
elif best_model['num_topics'] == 5:
    print("   ✓ More focused and stable topics")
    print("   ✓ 主題更聚焦且穩定")

print("\n💡 Suggestion | 建議:")
print("   For cross-cultural comparison with Taiwan (K=7), we recommend using K=7")
print("   為與台灣（K=7）進行跨文化比較，建議使用 K=7")
print("   This ensures methodological consistency and enables direct topic mapping.")
print("   這確保方法論一致性並能直接進行主題映射。")

# 視覺化比較
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Coherence comparison
axes[0].bar(['K=5', 'K=6', 'K=7'], [r['coherence'] for r in results],
            color=['#3498db', '#2ecc71', '#e74c3c'], edgecolor='black', linewidth=1.5)
axes[0].set_ylabel('Coherence Score', fontsize=12, fontweight='bold')
axes[0].set_title('Coherence Score Comparison\n一致性分數比較', fontsize=13, fontweight='bold')
axes[0].grid(axis='y', alpha=0.3, linestyle='--')

# 添加數值標籤
for i, r in enumerate(results):
    axes[0].text(i, r['coherence'] + 0.01, f"{r['coherence']:.4f}",
                 ha='center', va='bottom', fontsize=11, fontweight='bold')

# Perplexity comparison (注意：越低越好，但這裡顯示絕對值)
axes[1].bar(['K=5', 'K=6', 'K=7'], [abs(r['perplexity']) for r in results],
            color=['#3498db', '#2ecc71', '#e74c3c'], edgecolor='black', linewidth=1.5)
axes[1].set_ylabel('Perplexity (absolute value)', fontsize=12, fontweight='bold')
axes[1].set_title('Perplexity Comparison\n困惑度比較', fontsize=13, fontweight='bold')
axes[1].grid(axis='y', alpha=0.3, linestyle='--')

# 添加數值標籤
for i, r in enumerate(results):
    axes[1].text(i, abs(r['perplexity']) + 0.05, f"{r['perplexity']:.2f}",
                 ha='center', va='bottom', fontsize=11, fontweight='bold')

plt.tight_layout()
plt.savefig('usa_lda_k5k6k7_comparison.png', dpi=300, bbox_inches='tight')
print(f"\n✓ Comparison chart saved: usa_lda_k5k6k7_comparison.png")
print(f"✓ 比較圖表已儲存: usa_lda_k5k6k7_comparison.png")
plt.close()

print("\n" + "="*80)
print("Analysis Complete! | 分析完成！")
print("="*80)
print("\n📁 Generated files:")
print("   - usa_gensim_lda_k5_model.pkl")
print("   - usa_gensim_lda_k6_model.pkl")
print("   - usa_gensim_lda_k7_model.pkl")
print("   - usa_lda_k5k6k7_comparison.png")
