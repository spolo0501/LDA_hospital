#!/usr/bin/env python3
"""
合併並分析 Chapter 2.5 的所有搜尋結果
"""

import pandas as pd
import os
from collections import Counter

# 設定目錄
base_dir = "/Users/simon/Library/CloudStorage/Dropbox/paper/Working paper/Hospitals/LDA_hospital/Literature_Review/Chapter_2.5_Text_Mining"

# 所有 CSV 檔案（基本搜尋 + 補充搜尋）
csv_files = [
    # 基本搜尋
    "2.5-1_Topic_modeling_應用.csv",
    "2.5-2_LDA_在醫療.csv",
    "2.5-3_文本挖掘方法.csv",
    "2.5-4_NLP_應用.csv",
    # 補充搜尋
    "2.5-S1_LDA患者評論分析.csv",
    "2.5-S2_主題模型線上評論.csv",
    "2.5-S3_文本挖掘服務品質.csv",
    "2.5-S4_情感分析患者滿意度.csv",
    "2.5-S5_NLP患者體驗品質.csv"
]

print("="*80)
print("Chapter 2.5 文獻搜尋結果合併與分析")
print("="*80 + "\n")

# 讀取所有 CSV
all_papers = []
for csv_file in csv_files:
    file_path = os.path.join(base_dir, csv_file)
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        print(f"✅ {csv_file}: {len(df)} 篇")
        all_papers.append(df)
    else:
        print(f"⚠️  {csv_file}: 檔案不存在")

# 合併
combined = pd.concat(all_papers, ignore_index=True)
print(f"\n📊 合併前總數: {len(combined)} 篇")

# 去重（依據 DOI）
combined_dedup = combined.drop_duplicates(subset=['doi'], keep='first')
print(f"📊 去重後總數: {len(combined_dedup)} 篇")
print(f"   (移除 {len(combined) - len(combined_dedup)} 篇重複文獻)\n")

# 計算相關性分數
print("🔍 計算相關性分數...")

relevant_keywords = {
    "topic_modeling": ["topic modeling", "topic model", "latent dirichlet", "lda", "probabilistic topic"],
    "text_mining": ["text mining", "text analysis", "data mining", "content analysis"],
    "nlp": ["natural language processing", "nlp", "language model", "word embedding", "bert", "gpt"],
    "healthcare_quality": ["healthcare quality", "service quality", "patient satisfaction", "quality of care"],
    "patient_feedback": ["patient feedback", "patient review", "patient comment", "patient experience", "patient report"],
    "machine_learning": ["machine learning", "deep learning", "neural network", "supervised learning", "unsupervised learning"]
}

def calculate_relevance_score(row):
    score = 0
    text = f"{str(row['title']).lower()} {str(row['abstract']).lower()} {str(row['keywords']).lower()}"

    # 關鍵字匹配
    for category, keywords in relevant_keywords.items():
        for keyword in keywords:
            if keyword in text:
                score += 1

    # 引用數加分
    citations = row['citations'] if pd.notna(row['citations']) else 0
    if citations >= 20:
        score += 3
    elif citations >= 10:
        score += 2
    elif citations >= 5:
        score += 1

    return score

combined_dedup['relevance_score'] = combined_dedup.apply(calculate_relevance_score, axis=1)

# 按相關性排序
combined_sorted = combined_dedup.sort_values(by='relevance_score', ascending=False)

# 保存結果
output_all = os.path.join(base_dir, "Chapter_2.5_COMBINED_ALL.csv")
output_sorted = os.path.join(base_dir, "Chapter_2.5_COMBINED_SORTED_BY_RELEVANCE.csv")

combined_dedup.to_csv(output_all, index=False, encoding='utf-8-sig')
combined_sorted.to_csv(output_sorted, index=False, encoding='utf-8-sig')

print(f"✅ 已保存: Chapter_2.5_COMBINED_ALL.csv")
print(f"✅ 已保存: Chapter_2.5_COMBINED_SORTED_BY_RELEVANCE.csv\n")

# 統計分析
print("="*80)
print("📊 文獻統計分析")
print("="*80 + "\n")

# 年份分布
print("📅 年份分布:")
years = combined_sorted['year'].value_counts().sort_index(ascending=False)
for year, count in years.head(10).items():
    print(f"  {year}: {count} 篇")

# 引用數統計
print(f"\n📈 引用數統計:")
citations = combined_sorted['citations'].dropna()
if len(citations) > 0:
    print(f"  - 總引用數: {int(citations.sum())}")
    print(f"  - 平均引用: {citations.mean():.1f}")
    print(f"  - 最高引用: {int(citations.max())}")
    print(f"  - 中位數: {int(citations.median())}")

# 相關性分數分布
print(f"\n🎯 相關性分數分布:")
score_dist = combined_sorted['relevance_score'].value_counts().sort_index(ascending=False)
for score, count in score_dist.head(10).items():
    print(f"  分數 {score}: {count} 篇")

# 高相關性文獻（分數 >= 3）
high_relevance = combined_sorted[combined_sorted['relevance_score'] >= 3]
print(f"\n⭐ 高度相關文獻 (分數 >= 3): {len(high_relevance)} 篇")

# Top 20 高相關文獻
print(f"\n📚 Top 20 高相關性文獻:")
print("="*80)
for i, row in combined_sorted.head(20).iterrows():
    print(f"{row.name+1}. [{int(row['citations'])} 引用 | 分數 {row['relevance_score']}]")
    print(f"   {row['title'][:90]}...")
    print(f"   {row['journal']}, {row['year']}")
    print()

# 期刊分布（Top 10）
print("📖 期刊分布 (Top 10):")
journals = combined_sorted['journal'].value_counts()
for journal, count in journals.head(10).items():
    print(f"  {journal}: {count} 篇")

print("\n" + "="*80)
print("✅ 分析完成！")
print("="*80)
