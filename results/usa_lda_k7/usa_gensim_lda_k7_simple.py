#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
美國醫院評論 Gensim LDA K=7 分析（簡化版，避免multiprocessing問題）
"""

import pickle
import pandas as pd
import numpy as np
from gensim.models import LdaModel
from gensim.models.coherencemodel import CoherenceModel
from gensim import corpora
import warnings
warnings.filterwarnings('ignore')

# 英文文本處理
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

print("="*80)
print("USA Hospital Reviews - Gensim LDA K=7 Analysis (Simple Version)")
print("美國醫院評論 - Gensim LDA K=7 分析（簡化版）")
print("="*80)

# 文本前處理函數
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

df_en['cleaned_text'] = df_en['評論內容'].apply(preprocess_english_text)
df_en['tokens'] = df_en['cleaned_text'].apply(lambda x: tokenize_and_lemmatize(x, stop_words))
df_en = df_en[df_en['tokens'].str.len() > 0].copy()

texts = df_en['tokens'].tolist()
print(f"✓ Valid reviews: {len(df_en):,}")

# 建立字典和語料庫
print("\nBuilding dictionary and corpus...")
dictionary = corpora.Dictionary(texts)
original_size = len(dictionary)

dictionary.filter_extremes(no_below=3, no_above=0.5, keep_n=None)
dictionary.compactify()

print(f"  Original vocabulary: {original_size}")
print(f"  Filtered vocabulary: {len(dictionary)}")

corpus = [dictionary.doc2bow(text) for text in texts]
print(f"✓ Corpus created: {len(corpus)} documents")

# 訓練K=7的LDA模型
print("\n" + "="*80)
print("Training K=7 LDA Model...")
print("="*80)

lda_model = LdaModel(
    corpus=corpus,
    id2word=dictionary,
    num_topics=7,
    alpha='symmetric',
    eta='auto',
    iterations=100,
    passes=10,
    random_state=42
)

print("\n✓ Model training complete!")

# 計算coherence（使用workers=1避免multiprocessing問題）
print("\nCalculating coherence score...")
coherence_model = CoherenceModel(
    model=lda_model,
    texts=texts,
    dictionary=dictionary,
    coherence='c_v',
    processes=1  # 避免multiprocessing問題
)
coherence_score = coherence_model.get_coherence()
perplexity_score = lda_model.log_perplexity(corpus)

print(f"\n{'='*80}")
print("MODEL QUALITY METRICS | 模型品質指標")
print(f"{'='*80}")
print(f"Coherence Score: {coherence_score:.4f}")
print(f"Perplexity: {perplexity_score:.4f}")

# 顯示主題關鍵詞
print(f"\n{'='*80}")
print("TOPIC KEYWORDS | 主題關鍵詞")
print(f"{'='*80}")

topics_keywords = []
for idx in range(7):
    topic_words = lda_model.show_topic(idx, topn=10)
    keywords = ', '.join([word for word, prob in topic_words])
    topics_keywords.append({
        'topic_id': idx + 1,
        'keywords': keywords,
        'top_words': [word for word, prob in topic_words[:5]]
    })
    print(f"\nTopic {idx+1} | 主題 {idx+1}:")
    print(f"  {keywords}")

# 為每篇評論分配主題
print(f"\n{'='*80}")
print("Assigning topics to reviews...")
print("='*80)")

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

# 統計每個主題的評論數量和平均評分
print(f"\n{'='*80}")
print("TOPIC STATISTICS | 主題統計")
print(f"{'='*80}")

topic_stats = df_result.groupby('dominant_topic').agg({
    '評分': ['count', 'mean']
})
topic_stats.columns = ['review_count', 'avg_rating']

topic_summary = []
for topic_id in range(1, 8):
    if topic_id in topic_stats.index:
        count = int(topic_stats.loc[topic_id, 'review_count'])
        rating = topic_stats.loc[topic_id, 'avg_rating']
        percentage = (count / len(df_result)) * 100

        topic_summary.append({
            'Topic_ID': topic_id,
            'Keywords': topics_keywords[topic_id-1]['keywords'],
            'Review_Count': count,
            'Percentage': f"{percentage:.1f}%",
            'Avg_Rating': f"{rating:.2f}"
        })

        print(f"\nTopic {topic_id} | 主題 {topic_id}:")
        print(f"  Reviews: {count} ({percentage:.1f}%)")
        print(f"  評論數: {count} ({percentage:.1f}%)")
        print(f"  Avg Rating: {rating:.2f} stars")
        print(f"  平均評分: {rating:.2f} 星")

# 儲存模型
model_file = 'usa_gensim_lda_k7_simple_model.pkl'
with open(model_file, 'wb') as f:
    pickle.dump({
        'lda_model': lda_model,
        'dictionary': dictionary,
        'coherence_score': coherence_score,
        'perplexity_score': perplexity_score,
        'topics_keywords': topics_keywords,
        'topic_stats': topic_stats,
        'topic_summary': topic_summary
    }, f)
print(f"\n✓ Model saved: {model_file}")

# 儲存主題摘要到CSV
summary_df = pd.DataFrame(topic_summary)
summary_df.to_csv('usa_k7_topic_summary.csv', index=False, encoding='utf-8-sig')
print(f"✓ Topic summary saved: usa_k7_topic_summary.csv")

# 與台灣結果比較
print(f"\n{'='*80}")
print("COMPARISON WITH TAIWAN | 與台灣比較")
print(f"{'='*80}")

print("\nLoading Taiwan K=7 results...")
with open('code/lda_k7_lda_model.pkl', 'rb') as f:
    tw_model = pickle.load(f)

print(f"\n{'Model':<15} {'Coherence':<15} {'Perplexity':<15} {'Topics'}")
print("-" * 60)
print(f"{'Taiwan':<15} {tw_model['coherence_score']:<15.4f} {tw_model['perplexity_score']:<15.4f} {7}")
print(f"{'USA':<15} {coherence_score:<15.4f} {perplexity_score:<15.4f} {7}")
print(f"{'Difference':<15} {coherence_score - tw_model['coherence_score']:<15.4f} {perplexity_score - tw_model['perplexity_score']:<15.4f}")

if coherence_score > tw_model['coherence_score']:
    print(f"\n✓ USA model has higher coherence (+{coherence_score - tw_model['coherence_score']:.4f})")
else:
    print(f"\n! Taiwan model has higher coherence (+{tw_model['coherence_score'] - coherence_score:.4f})")

print(f"\n{'='*80}")
print("Analysis Complete! | 分析完成！")
print(f"{'='*80}")
print("\n✅ Both Taiwan and USA now use the same methodology (Gensim LDA with K=7)")
print("✅ 台灣與美國現在使用相同方法（Gensim LDA，K=7）")
print("\n📁 Generated files:")
print("   - usa_gensim_lda_k7_simple_model.pkl")
print("   - usa_k7_topic_summary.csv")
