#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
英國醫院評論資料前處理
功能：
1. 合併 20 家英國醫院的 Google 評論資料
2. 篩選最近一年的評論
3. 刪除空白評論
4. 準備 LDA 分析的資料
"""

import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

print("="*80)
print("UK Hospital Reviews - Data Preprocessing")
print("英國醫院評論 - 資料前處理")
print("="*80)

# 設定路徑
data_dir = Path("google_reviews_output/hospitals/uk/")
output_dir = Path("data/processed/hospitals/uk/")
output_dir.mkdir(parents=True, exist_ok=True)

print(f"\n📂 資料來源: {data_dir}")
print(f"📂 輸出目錄: {output_dir}")

# 載入所有醫院的評論
print("\n" + "="*80)
print("載入評論資料...")
print("="*80)

all_reviews = []
csv_files = list(data_dir.glob("*.csv"))
# 排除 stats 檔案
csv_files = [f for f in csv_files if "_stats.csv" not in f.name]

print(f"找到 {len(csv_files)} 個醫院資料檔案\n")

for csv_file in sorted(csv_files):
    hospital_name = csv_file.stem
    try:
        df = pd.read_csv(csv_file, encoding='utf-8-sig')
        print(f"✓ {hospital_name:<40} {len(df):>6,} 條評論")

        # 新增醫院名稱欄位
        df['hospital_name'] = hospital_name
        all_reviews.append(df)

    except Exception as e:
        print(f"✗ {hospital_name:<40} 載入失敗: {e}")

# 合併所有資料
df_all = pd.concat(all_reviews, ignore_index=True)
print(f"\n{'='*80}")
print(f"✓ 總計載入 {len(df_all):,} 條評論，來自 {len(all_reviews)} 家醫院")
print(f"{'='*80}")

# 檢視資料結構
print("\n資料欄位:")
print(df_all.columns.tolist())
print(f"\n資料維度: {df_all.shape}")

# 統計資訊
print(f"\n{'='*80}")
print("原始資料統計")
print(f"{'='*80}")
print(f"總評論數: {len(df_all):,}")
print(f"評論內容空白: {df_all['評論內容'].isna().sum():,} ({df_all['評論內容'].isna().sum()/len(df_all)*100:.1f}%)")
print(f"評論內容為空字串: {(df_all['評論內容'].str.strip() == '').sum():,}")

# 評分分布
print(f"\n評分分布:")
rating_dist = df_all['評分'].value_counts().sort_index()
for rating, count in rating_dist.items():
    percentage = count / len(df_all) * 100
    print(f"  {rating} 星: {count:>6,} ({percentage:>5.1f}%)")
print(f"  平均評分: {df_all['評分'].mean():.2f} 星")

# 處理日期
print(f"\n{'='*80}")
print("處理評論日期...")
print(f"{'='*80}")

def parse_relative_date(date_str):
    """解析相對日期（例如：'a day ago', '3 weeks ago'）"""
    if pd.isna(date_str):
        return None

    date_str = str(date_str).lower().strip()
    now = datetime.now()

    # 處理各種相對時間格式
    if 'hour' in date_str or 'hours' in date_str:
        hours = int(''.join(filter(str.isdigit, date_str))) if any(c.isdigit() for c in date_str) else 1
        return now - timedelta(hours=hours)
    elif 'day' in date_str or 'days' in date_str:
        days = int(''.join(filter(str.isdigit, date_str))) if any(c.isdigit() for c in date_str) else 1
        return now - timedelta(days=days)
    elif 'week' in date_str or 'weeks' in date_str:
        weeks = int(''.join(filter(str.isdigit, date_str))) if any(c.isdigit() for c in date_str) else 1
        return now - timedelta(weeks=weeks)
    elif 'month' in date_str or 'months' in date_str:
        months = int(''.join(filter(str.isdigit, date_str))) if any(c.isdigit() for c in date_str) else 1
        return now - timedelta(days=months*30)
    elif 'year' in date_str or 'years' in date_str:
        years = int(''.join(filter(str.isdigit, date_str))) if any(c.isdigit() for c in date_str) else 1
        return now - timedelta(days=years*365)
    else:
        return None

df_all['parsed_date'] = df_all['評論日期'].apply(parse_relative_date)

# 統計有效日期
valid_dates = df_all['parsed_date'].notna().sum()
print(f"✓ 成功解析 {valid_dates:,} 條評論的日期 ({valid_dates/len(df_all)*100:.1f}%)")

# 篩選最近一年的評論
one_year_ago = datetime.now() - timedelta(days=365)
df_recent = df_all[df_all['parsed_date'] >= one_year_ago].copy()

print(f"\n篩選結果:")
print(f"  原始評論數: {len(df_all):,}")
print(f"  最近一年評論: {len(df_recent):,} ({len(df_recent)/len(df_all)*100:.1f}%)")
print(f"  日期範圍: {one_year_ago.strftime('%Y-%m-%d')} ~ {datetime.now().strftime('%Y-%m-%d')}")

# 清理資料
print(f"\n{'='*80}")
print("清理資料...")
print(f"{'='*80}")

# 1. 刪除空白評論
df_clean = df_recent.copy()
before_count = len(df_clean)

# 刪除評論內容為空或只有空白的
df_clean = df_clean[df_clean['評論內容'].notna()].copy()
df_clean = df_clean[df_clean['評論內容'].str.strip() != ''].copy()

after_count = len(df_clean)
removed = before_count - after_count

print(f"刪除空白評論: {removed:,} 條")
print(f"保留評論數: {after_count:,}")

# 2. 確保評分有效
df_clean = df_clean[df_clean['評分'].notna()].copy()
df_clean = df_clean[df_clean['評分'].between(1, 5)].copy()

print(f"✓ 評分有效檢查: {len(df_clean):,} 條評論")

# 3. 統計清理後的資料
print(f"\n{'='*80}")
print("清理後資料統計")
print(f"{'='*80}")
print(f"總評論數: {len(df_clean):,}")
print(f"來自醫院數: {df_clean['hospital_name'].nunique()}")
print(f"平均評分: {df_clean['評分'].mean():.2f} 星")

print(f"\n評分分布:")
rating_dist_clean = df_clean['評分'].value_counts().sort_index()
for rating, count in rating_dist_clean.items():
    percentage = count / len(df_clean) * 100
    print(f"  {rating} 星: {count:>6,} ({percentage:>5.1f}%)")

print(f"\n每家醫院的評論數:")
hospital_counts = df_clean['hospital_name'].value_counts()
for hospital, count in hospital_counts.items():
    print(f"  {hospital:<40} {count:>5,} 條")

# 儲存清理後的資料
output_file = output_dir / "uk_hospitals_cleaned_recent_1year.csv"
df_clean.to_csv(output_file, index=False, encoding='utf-8-sig')
print(f"\n{'='*80}")
print(f"✓ 清理後資料已儲存: {output_file}")
print(f"{'='*80}")

# 生成摘要統計
summary_stats = {
    '統計項目': [
        '原始評論總數',
        '最近一年評論數',
        '刪除空白評論數',
        '最終有效評論數',
        '涵蓋醫院數',
        '平均評分',
        '日期範圍起始',
        '日期範圍結束',
        '處理日期'
    ],
    '數值': [
        f"{len(df_all):,}",
        f"{len(df_recent):,}",
        f"{removed:,}",
        f"{len(df_clean):,}",
        f"{df_clean['hospital_name'].nunique()}",
        f"{df_clean['評分'].mean():.2f}",
        one_year_ago.strftime('%Y-%m-%d'),
        datetime.now().strftime('%Y-%m-%d'),
        datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    ]
}

summary_df = pd.DataFrame(summary_stats)
summary_file = output_dir / "uk_hospitals_preprocessing_summary.csv"
summary_df.to_csv(summary_file, index=False, encoding='utf-8-sig')
print(f"✓ 處理摘要已儲存: {summary_file}")

print(f"\n{'='*80}")
print("資料前處理完成！")
print(f"{'='*80}")
print(f"\n📁 生成的檔案:")
print(f"   1. {output_file}")
print(f"   2. {summary_file}")
print(f"\n下一步: 執行 LDA 分析")
