#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
台灣、美國、英國醫院服務品質三國比較分析
Taiwan, USA, UK Hospital Service Quality Comparison (K=7)
"""

import pickle
import pandas as pd
import numpy as np
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

print("="*80)
print("Three-Country Hospital Service Quality Comparison")
print("台灣、美國、英國醫院服務品質比較分析")
print("="*80)

# 載入三國的 LDA 模型
print("\n📂 Loading LDA models...")

# 台灣
tw_model_path = Path("results/taiwan_lda_k7/lda_k7_lda_model.pkl")
with open(tw_model_path, 'rb') as f:
    tw_model = pickle.load(f)
print(f"✓ Taiwan model loaded")

# 美國
usa_model_path = Path("results/usa_lda_k7/usa_gensim_lda_k7_model.pkl")
with open(usa_model_path, 'rb') as f:
    usa_model = pickle.load(f)
print(f"✓ USA model loaded")

# 英國
uk_model_path = Path("results/uk_lda_k7/uk_gensim_lda_k7_model.pkl")
with open(uk_model_path, 'rb') as f:
    uk_model = pickle.load(f)
print(f"✓ UK model loaded")

# 模型品質比較
print(f"\n{'='*80}")
print("MODEL QUALITY COMPARISON | 模型品質比較")
print(f"{'='*80}")

comparison_data = []

# 台灣
tw_info = tw_model.get('data_info', {})
comparison_data.append({
    'Country': 'Taiwan 🇹🇼',
    'Reviews': tw_info.get('total_reviews', 'N/A'),
    'Hospitals': tw_info.get('total_hospitals', 26),
    'Avg_Rating': f"{tw_info.get('avg_rating', 0):.2f}",
    'Coherence': f"{tw_model['coherence_score']:.4f}",
    'Perplexity': f"{tw_model['perplexity_score']:.4f}",
    'Language': '中文 (Chinese)'
})

# 美國
usa_info = usa_model.get('data_info', {})
comparison_data.append({
    'Country': 'USA 🇺🇸',
    'Reviews': usa_info.get('total_reviews', 'N/A'),
    'Hospitals': usa_info.get('total_hospitals', 'N/A'),
    'Avg_Rating': f"{usa_info.get('avg_rating', 0):.2f}" if 'avg_rating' in usa_info else 'N/A',
    'Coherence': f"{usa_model['coherence_score']:.4f}",
    'Perplexity': f"{usa_model['perplexity_score']:.4f}",
    'Language': 'English'
})

# 英國
uk_info = uk_model.get('data_info', {})
comparison_data.append({
    'Country': 'UK 🇬🇧',
    'Reviews': uk_info.get('total_reviews', 2135),
    'Hospitals': uk_info.get('total_hospitals', 20),
    'Avg_Rating': f"{uk_info.get('avg_rating', 3.35):.2f}",
    'Coherence': f"{uk_model['coherence_score']:.4f}",
    'Perplexity': f"{uk_model['perplexity_score']:.4f}",
    'Language': 'English'
})

comparison_df = pd.DataFrame(comparison_data)
print("\n")
print(comparison_df.to_string(index=False))

# 主題關鍵詞比較
print(f"\n{'='*80}")
print("TOPIC KEYWORDS COMPARISON | 主題關鍵詞比較")
print(f"{'='*80}")

print("\n" + "─"*80)
print("🇹🇼 TAIWAN | 台灣")
print("─"*80)
tw_topics = tw_model['topics_keywords']
for topic in tw_topics:
    keywords = ', '.join(topic['top_words'][:8]) if isinstance(topic, dict) else ', '.join(topic[:8])
    print(f"Topic {topic['topic_id'] if isinstance(topic, dict) else tw_topics.index(topic)+1}: {keywords}")

print("\n" + "─"*80)
print("🇺🇸 USA | 美國")
print("─"*80)
usa_topics = usa_model['topics_keywords']
for topic in usa_topics:
    keywords = ', '.join(topic['top_words'][:8]) if isinstance(topic, dict) else ', '.join(topic[:8])
    print(f"Topic {topic['topic_id'] if isinstance(topic, dict) else usa_topics.index(topic)+1}: {keywords}")

print("\n" + "─"*80)
print("🇬🇧 UK | 英國")
print("─"*80)
uk_topics = uk_model['topics_keywords']
for topic in uk_topics:
    keywords = ', '.join(topic['top_words'][:8]) if isinstance(topic, dict) else ', '.join(topic[:8])
    print(f"Topic {topic['topic_id'] if isinstance(topic, dict) else uk_topics.index(topic)+1}: {keywords}")

# 主題標註（手動）
print(f"\n{'='*80}")
print("TOPIC LABELING & ALIGNMENT | 主題標註與對齊")
print(f"{'='*80}")

# 台灣主題標註
tw_labels = {
    1: "醫療專業與態度 (Medical Professionalism & Attitude)",
    2: "診療效率與流程 (Treatment Efficiency & Process)",
    3: "環境設施 (Facility & Environment)",
    4: "特定醫療服務 (Specific Medical Services)",
    5: "整體就醫經驗 (Overall Medical Experience)",
    6: "等待時間 (Waiting Time)",
    7: "服務品質整體評價 (Overall Service Quality)"
}

# 美國主題標註
usa_labels = {
    1: "醫護專業與技術 (Medical Staff Professionalism)",
    2: "急診與緊急醫療 (Emergency Care)",
    3: "護理照護品質 (Nursing Care Quality)",
    4: "醫療流程與溝通 (Medical Process & Communication)",
    5: "病患經驗與滿意度 (Patient Experience & Satisfaction)",
    6: "特定科別服務 (Specialized Department Services)",
    7: "整體醫療品質 (Overall Medical Quality)"
}

# 英國主題標註
uk_labels = {
    1: "醫護專業與照護品質 (Professional Care & Medical Excellence)",
    2: "等待時間與資源需求 (Waiting Time & Resource Needs)",
    3: "服務態度與友善度 (Service Attitude & Friendliness)",
    4: "特定醫療問題 (Specific Medical Issues)",
    5: "感激與正面情緒 (Gratitude & Positive Emotions)",
    6: "負面等待經驗 (Negative Waiting Experience)",
    7: "部門運作與管理 (Department Operations & Management)"
}

print("\n🇹🇼 Taiwan Topics:")
for i, label in tw_labels.items():
    print(f"  T{i}: {label}")

print("\n🇺🇸 USA Topics:")
for i, label in usa_labels.items():
    print(f"  U{i}: {label}")

print("\n🇬🇧 UK Topics:")
for i, label in uk_labels.items():
    print(f"  K{i}: {label}")

# 主題統計比較
print(f"\n{'='*80}")
print("TOPIC STATISTICS COMPARISON | 主題統計比較")
print(f"{'='*80}")

# 台灣主題統計
print("\n🇹🇼 TAIWAN")
tw_summary = tw_model.get('topic_summary', [])
for topic in tw_summary:
    print(f"  Topic {topic['Topic_ID']}: {topic['Review_Count']:>5} reviews ({topic['Percentage']:>6}) - "
          f"Avg Rating: {topic['Avg_Rating']}")

# 美國主題統計
print("\n🇺🇸 USA")
usa_summary = usa_model.get('topic_summary', [])
for topic in usa_summary:
    print(f"  Topic {topic['Topic_ID']}: {topic['Review_Count']:>5} reviews ({topic['Percentage']:>6}) - "
          f"Avg Rating: {topic['Avg_Rating']}")

# 英國主題統計
print("\n🇬🇧 UK")
uk_summary = uk_model.get('topic_summary', [])
for topic in uk_summary:
    print(f"  Topic {topic['Topic_ID']}: {topic['Review_Count']:>5} reviews ({topic['Percentage']:>6}) - "
          f"Avg Rating: {topic['Avg_Rating']}")

# 跨國主題對齊（基於語義相似性）
print(f"\n{'='*80}")
print("CROSS-COUNTRY TOPIC ALIGNMENT | 跨國主題對齊")
print(f"{'='*80}")

alignment = {
    "醫護專業能力": {
        "Taiwan": ["T1", "T7"],
        "USA": ["U1", "U3", "U7"],
        "UK": ["K1"]
    },
    "等待時間問題": {
        "Taiwan": ["T6"],
        "USA": [],
        "UK": ["K2", "K6", "K7"]
    },
    "診療流程效率": {
        "Taiwan": ["T2"],
        "USA": ["U4"],
        "UK": ["K7"]
    },
    "環境與設施": {
        "Taiwan": ["T3"],
        "USA": [],
        "UK": []
    },
    "服務態度關懷": {
        "Taiwan": ["T1"],
        "USA": ["U5"],
        "UK": ["K3", "K5"]
    },
    "特定醫療服務": {
        "Taiwan": ["T4"],
        "USA": ["U2", "U6"],
        "UK": ["K4"]
    },
    "整體就醫經驗": {
        "Taiwan": ["T5"],
        "USA": ["U5"],
        "UK": ["K1", "K5"]
    }
}

for dimension, countries in alignment.items():
    print(f"\n📊 {dimension}")
    print(f"   Taiwan: {', '.join(countries['Taiwan']) if countries['Taiwan'] else '無對應'}")
    print(f"   USA:    {', '.join(countries['USA']) if countries['USA'] else '無對應'}")
    print(f"   UK:     {', '.join(countries['UK']) if countries['UK'] else '無對應'}")

# 創建比較摘要表
print(f"\n{'='*80}")
print("SUMMARY COMPARISON TABLE | 摘要比較表")
print(f"{'='*80}")

summary_table = []

# 台灣
tw_topics_count = len(tw_summary)
tw_avg_reviews_per_topic = sum([t['Review_Count'] for t in tw_summary]) / tw_topics_count
tw_rating_range = f"{min([float(t['Avg_Rating']) for t in tw_summary]):.2f} - {max([float(t['Avg_Rating']) for t in tw_summary]):.2f}"

# 美國
usa_topics_count = len(usa_summary)
usa_avg_reviews_per_topic = sum([t['Review_Count'] for t in usa_summary]) / usa_topics_count
usa_rating_range = f"{min([float(t['Avg_Rating']) for t in usa_summary]):.2f} - {max([float(t['Avg_Rating']) for t in usa_summary]):.2f}"

# 英國
uk_topics_count = len(uk_summary)
uk_avg_reviews_per_topic = sum([t['Review_Count'] for t in uk_summary]) / uk_topics_count
uk_rating_range = f"{min([float(t['Avg_Rating']) for t in uk_summary]):.2f} - {max([float(t['Avg_Rating']) for t in uk_summary]):.2f}"

summary_table.append({
    'Metric': 'Total Topics',
    'Taiwan': tw_topics_count,
    'USA': usa_topics_count,
    'UK': uk_topics_count
})

summary_table.append({
    'Metric': 'Avg Reviews/Topic',
    'Taiwan': f"{tw_avg_reviews_per_topic:.0f}",
    'USA': f"{usa_avg_reviews_per_topic:.0f}",
    'UK': f"{uk_avg_reviews_per_topic:.0f}"
})

summary_table.append({
    'Metric': 'Rating Range',
    'Taiwan': tw_rating_range,
    'USA': usa_rating_range,
    'UK': uk_rating_range
})

summary_df = pd.DataFrame(summary_table)
print("\n")
print(summary_df.to_string(index=False))

# 儲存比較結果
output_dir = Path("results/comparison")
output_dir.mkdir(parents=True, exist_ok=True)

# 儲存比較摘要
comparison_summary = {
    'model_quality': comparison_df,
    'taiwan_topics': tw_summary,
    'usa_topics': usa_summary,
    'uk_topics': uk_summary,
    'taiwan_labels': tw_labels,
    'usa_labels': usa_labels,
    'uk_labels': uk_labels,
    'alignment': alignment
}

with open(output_dir / 'three_country_comparison.pkl', 'wb') as f:
    pickle.dump(comparison_summary, f)

print(f"\n{'='*80}")
print("COMPARISON COMPLETE | 比較分析完成")
print(f"{'='*80}")
print(f"\n✅ Three-country comparison analysis completed")
print(f"✅ 三國比較分析已完成")
print(f"\n📁 Output directory: {output_dir}")
print(f"📁 輸出目錄: {output_dir}")
