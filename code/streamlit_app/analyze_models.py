#!/usr/bin/env python3
"""
分析台灣 K=7 和美國 K=6 LDA 模型，生成主題標籤
"""

import pickle
from pathlib import Path
import pandas as pd

# 路徑設定
BASE_DIR = Path(__file__).resolve().parent.parent.parent
TAIWAN_MODEL_PATH = BASE_DIR / "results/taiwan_lda_k7/lda_k7_lda_model.pkl"
USA_MODEL_PATH = BASE_DIR / "results/usa_lda_k7/usa_gensim_lda_k6_model.pkl"
USA_DATA_PATH = BASE_DIR / "results/usa_lda_k7/usa_k6_topic_analysis_20251107_122236.csv"

print("=" * 80)
print("🔍 台灣 K=7 LDA 模型分析")
print("=" * 80)

# 載入台灣模型
with open(TAIWAN_MODEL_PATH, 'rb') as f:
    taiwan_data = pickle.load(f)
    taiwan_model = taiwan_data['lda_model']
    taiwan_dictionary = taiwan_model.id2word

print(f"\n台灣模型資訊：")
print(f"  主題數量: {taiwan_model.num_topics}")
print(f"  詞彙數量: {len(taiwan_dictionary)}")

print("\n台灣 7 個主題的關鍵詞：")
for topic_id in range(taiwan_model.num_topics):
    words = taiwan_model.show_topic(topic_id, topn=15)
    words_str = ", ".join([f"{w}({p:.3f})" for w, p in words])
    print(f"\nTopic {topic_id}:")
    print(f"  {words_str}")

print("\n" + "=" * 80)
print("🔍 美國 K=6 LDA 模型分析")
print("=" * 80)

# 載入美國模型
with open(USA_MODEL_PATH, 'rb') as f:
    usa_data = pickle.load(f)
    usa_model = usa_data['lda_model']
    usa_dictionary = usa_data['dictionary']

print(f"\n美國模型資訊：")
print(f"  主題數量: {usa_model.num_topics}")
print(f"  詞彙數量: {len(usa_dictionary)}")

print("\n美國 6 個主題的關鍵詞：")
for topic_id in range(usa_model.num_topics):
    words = usa_model.show_topic(topic_id, topn=15)
    words_str = ", ".join([f"{w}({p:.3f})" for w, p in words])
    print(f"\nTopic {topic_id}:")
    print(f"  {words_str}")

# 載入美國評論資料，分析主題分佈
print("\n" + "=" * 80)
print("📊 美國主題分佈與評分分析")
print("=" * 80)

usa_df = pd.read_csv(USA_DATA_PATH)
print(f"\n美國評論總數: {len(usa_df)}")

# 統計每個主題的評論數和平均評分
topic_stats = usa_df.groupby('dominant_topic').agg({
    '評分': ['count', 'mean'],
    'topic_probability': 'mean'
}).round(2)

topic_stats.columns = ['評論數', '平均評分', '平均機率']
topic_stats['比例(%)'] = (topic_stats['評論數'] / len(usa_df) * 100).round(1)

print("\n美國各主題統計：")
print(topic_stats)

print("\n" + "=" * 80)
print("✅ 分析完成！")
print("=" * 80)
