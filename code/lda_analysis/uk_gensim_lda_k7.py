#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
英國醫院評論 Gensim LDA K=7 分析
參考美國醫院的分析方法，使用相同的 LDA 參數
"""

import pickle
import pandas as pd
import numpy as np
from gensim.models import LdaModel
from gensim.models.coherencemodel import CoherenceModel
from gensim import corpora
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# 英文文本處理
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# 下載必要的 NLTK 資源（如果尚未下載）
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', quiet=True)

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords', quiet=True)

try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet', quiet=True)

print("="*80)
print("UK Hospital Reviews - Gensim LDA K=7 Analysis")
print("英國醫院評論 - Gensim LDA K=7 分析")
print("="*80)

# 文本前處理函數
def preprocess_english_text(text):
    """清理英文文本"""
    text = str(text).lower()
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'\S+@\S+', '', text)
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)
    text = ' '.join(text.split())
    return text

def tokenize_and_lemmatize(text, stop_words):
    """Tokenization + Lemmatization"""
    lemmatizer = WordNetLemmatizer()
    tokens = word_tokenize(text)
    tokens = [lemmatizer.lemmatize(token) for token in tokens
              if token not in stop_words and len(token) > 2]
    return tokens

# 載入資料
print("\n📂 Loading data...")
data_file = Path("data/processed/hospitals/uk/uk_hospitals_cleaned_recent_1year.csv")
df = pd.read_csv(data_file, encoding='utf-8-sig')
print(f"✓ Loaded {len(df):,} reviews from {df['hospital_name'].nunique()} hospitals")

# 基本統計
print(f"\n{'='*80}")
print("DATA STATISTICS | 資料統計")
print(f"{'='*80}")
print(f"Total reviews: {len(df):,}")
print(f"Hospitals: {df['hospital_name'].nunique()}")
print(f"Average rating: {df['評分'].mean():.2f} stars")
print(f"Date range: Recent 1 year")

print(f"\nRating distribution:")
rating_dist = df['評分'].value_counts().sort_index()
for rating, count in rating_dist.items():
    percentage = count / len(df) * 100
    print(f"  {int(rating)} star: {count:>5,} ({percentage:>5.1f}%)")

# 文本前處理
print(f"\n{'='*80}")
print("TEXT PREPROCESSING | 文本前處理")
print(f"{'='*80}")

# 設定停用詞
stop_words = set(stopwords.words('english'))

# 英國醫院特定停用詞
custom_stop_words = {
    # 一般停用詞
    'hospital', 'doctor', 'went', 'like', 'would', 'one', 'get', 'go',
    'nhs', 'said', 'told', 'came', 'made', 'asked', 'took', 'could',

    # 醫療相關但太常見
    'appointment', 'patient', 'staff', 'ward', 'treatment', 'care',
    'visit', 'visited', 'time', 'day', 'week', 'month', 'year',

    # 評論常見詞
    'really', 'very', 'much', 'also', 'even', 'still', 'back', 'way',
    'thing', 'lot', 'bit', 'quite', 'rather', 'well', 'good', 'bad'
}
stop_words.update(custom_stop_words)

print(f"Stop words: {len(stop_words)} words")

# 清理和 tokenize
print("\nProcessing text...")
df['cleaned_text'] = df['評論內容'].apply(preprocess_english_text)
df['tokens'] = df['cleaned_text'].apply(lambda x: tokenize_and_lemmatize(x, stop_words))
df = df[df['tokens'].str.len() > 0].copy()

texts = df['tokens'].tolist()
print(f"✓ Valid reviews after preprocessing: {len(df):,}")

# 建立字典和語料庫
print(f"\n{'='*80}")
print("BUILDING DICTIONARY & CORPUS | 建立字典和語料庫")
print(f"{'='*80}")

dictionary = corpora.Dictionary(texts)
original_size = len(dictionary)

# 過濾極端詞彙
dictionary.filter_extremes(no_below=3, no_above=0.5, keep_n=None)
dictionary.compactify()

print(f"Original vocabulary size: {original_size:,}")
print(f"Filtered vocabulary size: {len(dictionary):,}")
print(f"Removed: {original_size - len(dictionary):,} words")

corpus = [dictionary.doc2bow(text) for text in texts]
print(f"✓ Corpus created: {len(corpus):,} documents")

# 訓練 K=7 的 LDA 模型
print(f"\n{'='*80}")
print("TRAINING LDA MODEL (K=7) | 訓練 LDA 模型 (K=7)")
print(f"{'='*80}")

print("\nModel parameters:")
print("  - Topics (K): 7")
print("  - Alpha: symmetric")
print("  - Eta: auto")
print("  - Iterations: 100")
print("  - Passes: 10")
print("  - Random state: 42")

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

# 計算模型品質指標
print(f"\n{'='*80}")
print("CALCULATING MODEL QUALITY METRICS | 計算模型品質指標")
print(f"{'='*80}")

# Coherence Score
coherence_model = CoherenceModel(
    model=lda_model,
    texts=texts,
    dictionary=dictionary,
    coherence='c_v',
    processes=1
)
coherence_score = coherence_model.get_coherence()

# Perplexity
perplexity_score = lda_model.log_perplexity(corpus)

print(f"\nCoherence Score: {coherence_score:.4f}")
print(f"Perplexity: {perplexity_score:.4f}")

# 顯示主題關鍵詞
print(f"\n{'='*80}")
print("TOPIC KEYWORDS | 主題關鍵詞")
print(f"{'='*80}")

topics_keywords = []
for idx in range(7):
    topic_words = lda_model.show_topic(idx, topn=15)
    keywords = ', '.join([word for word, prob in topic_words])
    topics_keywords.append({
        'topic_id': idx + 1,
        'keywords': keywords,
        'top_words': [word for word, prob in topic_words[:10]]
    })
    print(f"\nTopic {idx+1}:")
    for word, prob in topic_words[:10]:
        print(f"  {word:<20} {prob:.4f}")

# 為每篇評論分配主題
print(f"\n{'='*80}")
print("ASSIGNING TOPICS TO REVIEWS | 分配主題到評論")
print(f"{'='*80}")

topic_assignments = []
for doc_bow in corpus:
    topic_dist = lda_model.get_document_topics(doc_bow, minimum_probability=0)
    topic_probs = [prob for _, prob in topic_dist]
    dominant_topic = topic_probs.index(max(topic_probs)) + 1
    topic_assignments.append({
        'dominant_topic': dominant_topic,
        'topic_probability': max(topic_probs)
    })

df_result = pd.concat([df.reset_index(drop=True), pd.DataFrame(topic_assignments)], axis=1)

# 統計每個主題的評論數量和平均評分
print(f"\n{'='*80}")
print("TOPIC STATISTICS | 主題統計")
print(f"{'='*80}")

topic_stats = df_result.groupby('dominant_topic').agg({
    '評分': ['count', 'mean', 'std'],
    'topic_probability': 'mean'
})
topic_stats.columns = ['review_count', 'avg_rating', 'rating_std', 'avg_probability']

topic_summary = []
for topic_id in range(1, 8):
    if topic_id in topic_stats.index:
        count = int(topic_stats.loc[topic_id, 'review_count'])
        rating = topic_stats.loc[topic_id, 'avg_rating']
        rating_std = topic_stats.loc[topic_id, 'rating_std']
        prob = topic_stats.loc[topic_id, 'avg_probability']
        percentage = (count / len(df_result)) * 100

        topic_summary.append({
            'Topic_ID': topic_id,
            'Top_Keywords': ', '.join(topics_keywords[topic_id-1]['top_words'][:5]),
            'Review_Count': count,
            'Percentage': f"{percentage:.1f}%",
            'Avg_Rating': f"{rating:.2f}",
            'Rating_Std': f"{rating_std:.2f}",
            'Avg_Probability': f"{prob:.3f}"
        })

        print(f"\nTopic {topic_id}:")
        print(f"  Keywords: {', '.join(topics_keywords[topic_id-1]['top_words'][:5])}")
        print(f"  Reviews: {count:,} ({percentage:.1f}%)")
        print(f"  Avg Rating: {rating:.2f} ± {rating_std:.2f} stars")
        print(f"  Avg Probability: {prob:.3f}")

# 創建輸出目錄
output_dir = Path("results/uk_lda_k7")
output_dir.mkdir(parents=True, exist_ok=True)

# 儲存模型
model_file = output_dir / 'uk_gensim_lda_k7_model.pkl'
with open(model_file, 'wb') as f:
    pickle.dump({
        'lda_model': lda_model,
        'dictionary': dictionary,
        'coherence_score': coherence_score,
        'perplexity_score': perplexity_score,
        'topics_keywords': topics_keywords,
        'topic_stats': topic_stats,
        'topic_summary': topic_summary,
        'data_info': {
            'total_reviews': len(df),
            'total_hospitals': df['hospital_name'].nunique(),
            'avg_rating': df['評分'].mean(),
            'date_range': 'Recent 1 year'
        }
    }, f)
print(f"\n✓ Model saved: {model_file}")

# 儲存主題摘要
summary_df = pd.DataFrame(topic_summary)
summary_file = output_dir / 'uk_k7_topic_summary.csv'
summary_df.to_csv(summary_file, index=False, encoding='utf-8-sig')
print(f"✓ Topic summary saved: {summary_file}")

# 儲存完整結果（包含每筆評論的主題分配）
result_file = output_dir / 'uk_k7_reviews_with_topics.csv'
df_result.to_csv(result_file, index=False, encoding='utf-8-sig')
print(f"✓ Full results saved: {result_file}")

# 儲存每家醫院的主題分布
print(f"\n{'='*80}")
print("HOSPITAL-LEVEL TOPIC DISTRIBUTION | 醫院層級主題分布")
print(f"{'='*80}")

hospital_topic_dist = df_result.groupby(['hospital_name', 'dominant_topic']).size().unstack(fill_value=0)
hospital_topic_dist['total'] = hospital_topic_dist.sum(axis=1)

# 計算百分比
for col in range(1, 8):
    if col in hospital_topic_dist.columns:
        hospital_topic_dist[f'Topic_{col}_%'] = (hospital_topic_dist[col] / hospital_topic_dist['total'] * 100).round(1)

hospital_dist_file = output_dir / 'uk_k7_hospital_topic_distribution.csv'
hospital_topic_dist.to_csv(hospital_dist_file, encoding='utf-8-sig')
print(f"✓ Hospital topic distribution saved: {hospital_dist_file}")

# 顯示前 5 家醫院的主題分布
print(f"\nTop 5 hospitals by review count:")
top_hospitals = df_result['hospital_name'].value_counts().head(5)
for hospital, count in top_hospitals.items():
    print(f"\n{hospital} ({count} reviews):")
    hospital_reviews = df_result[df_result['hospital_name'] == hospital]
    topic_dist = hospital_reviews['dominant_topic'].value_counts().sort_index()
    for topic, cnt in topic_dist.items():
        pct = cnt / count * 100
        print(f"  Topic {topic}: {cnt:>3} ({pct:>5.1f}%)")

print(f"\n{'='*80}")
print("ANALYSIS COMPLETE! | 分析完成！")
print(f"{'='*80}")
print(f"\n✅ Successfully analyzed {len(df):,} UK hospital reviews")
print(f"✅ Identified 7 service quality dimensions using LDA")
print(f"\n📁 Generated files:")
print(f"   1. {model_file.name}")
print(f"   2. {summary_file.name}")
print(f"   3. {result_file.name}")
print(f"   4. {hospital_dist_file.name}")
print(f"\n📊 Model Quality:")
print(f"   Coherence Score: {coherence_score:.4f}")
print(f"   Perplexity: {perplexity_score:.4f}")
