#!/usr/bin/env python3
"""
探索性資料分析（EDA）
分析醫院評論的基本特徵、分布和相關性
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# 設定中文字體和風格
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
sns.set_style("whitegrid")
sns.set_palette("husl")

# 讀取資料
print("=" * 80)
print("📊 探索性資料分析（EDA）")
print("=" * 80)
print()

print("📂 讀取資料...")
df = pd.read_csv('cleaned_data_no_dedup/final_cleaned_sample_no_dedup.csv', encoding='utf-8-sig')
print(f"✅ 資料載入完成: {len(df):,} 條評論")
print()

# 轉換日期欄位
df['實際日期_parsed'] = pd.to_datetime(df['實際日期_parsed'])

# ============================================================================
# 1. 基本統計資訊
# ============================================================================
print("=" * 80)
print("📊 1. 基本統計資訊")
print("=" * 80)
print()

print("📋 資料維度:")
print(f"   樣本數: {len(df):,} 條")
print(f"   特徵數: {len(df.columns)} 個")
print()

print("📋 資料欄位:")
for i, col in enumerate(df.columns, 1):
    print(f"   {i:2d}. {col}")
print()

print("📊 評分分布:")
rating_dist = df['評分'].value_counts().sort_index()
for rating, count in rating_dist.items():
    percentage = (count / len(df)) * 100
    stars = "⭐" * int(rating)
    bar = "█" * int(percentage)
    print(f"   {stars:12s} {count:5d} 條 ({percentage:5.1f}%)  {bar}")
print()

print("📊 評論長度統計:")
print(f"   平均長度: {df['評論長度'].mean():.1f} 字元")
print(f"   中位數:   {df['評論長度'].median():.0f} 字元")
print(f"   最短:     {df['評論長度'].min()} 字元")
print(f"   最長:     {df['評論長度'].max():,} 字元")
print(f"   標準差:   {df['評論長度'].std():.1f} 字元")
print()

print("🏥 醫院數量統計:")
print(f"   共 {df['醫院名稱'].nunique()} 家醫院")
print()

print("📅 時間範圍:")
print(f"   最早評論: {df['實際日期_parsed'].min().strftime('%Y-%m-%d')}")
print(f"   最新評論: {df['實際日期_parsed'].max().strftime('%Y-%m-%d')}")
print(f"   時間跨度: {(df['實際日期_parsed'].max() - df['實際日期_parsed'].min()).days} 天")
print()

print("🌐 語言分布:")
lang_dist = df['語言'].value_counts()
for lang, count in lang_dist.items():
    percentage = (count / len(df)) * 100
    print(f"   {lang}: {count:5d} 條 ({percentage:5.1f}%)")
print()

# ============================================================================
# 2. 視覺化分析
# ============================================================================
print("=" * 80)
print("📊 2. 生成視覺化圖表")
print("=" * 80)
print()

# 創建輸出目錄
import os
os.makedirs('eda_results', exist_ok=True)

# 設定圖表大小
fig = plt.figure(figsize=(20, 24))

# 2.1 評分分布
print("📈 2.1 生成評分分布圖...")
ax1 = plt.subplot(4, 3, 1)
rating_counts = df['評分'].value_counts().sort_index()
colors = ['#e74c3c', '#e67e22', '#f39c12', '#2ecc71', '#27ae60']
bars = ax1.bar(rating_counts.index, rating_counts.values, color=colors, edgecolor='black', linewidth=1.5)
ax1.set_xlabel('Rating (Stars)', fontsize=12, fontweight='bold')
ax1.set_ylabel('Count', fontsize=12, fontweight='bold')
ax1.set_title('Rating Distribution', fontsize=14, fontweight='bold', pad=20)
ax1.set_xticks([1, 2, 3, 4, 5])
ax1.grid(axis='y', alpha=0.3)

# 在條形圖上顯示數量和百分比
for bar in bars:
    height = bar.get_height()
    percentage = (height / len(df)) * 100
    ax1.text(bar.get_x() + bar.get_width()/2., height,
             f'{int(height)}\n({percentage:.1f}%)',
             ha='center', va='bottom', fontsize=10, fontweight='bold')

# 2.2 評分分布（餅圖）
print("📈 2.2 生成評分分布餅圖...")
ax2 = plt.subplot(4, 3, 2)
wedges, texts, autotexts = ax2.pie(rating_counts.values,
                                     labels=[f'{int(x)} Star' for x in rating_counts.index],
                                     autopct='%1.1f%%',
                                     colors=colors,
                                     startangle=90,
                                     explode=[0.05 if x in [1, 5] else 0 for x in rating_counts.index])
ax2.set_title('Rating Distribution (Pie Chart)', fontsize=14, fontweight='bold', pad=20)
for text in texts:
    text.set_fontsize(11)
    text.set_fontweight('bold')
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)
    autotext.set_fontweight('bold')

# 2.3 評論長度分布
print("📈 2.3 生成評論長度分布圖...")
ax3 = plt.subplot(4, 3, 3)
ax3.hist(df['評論長度'], bins=50, color='steelblue', edgecolor='black', alpha=0.7)
ax3.axvline(df['評論長度'].mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: {df["評論長度"].mean():.0f}')
ax3.axvline(df['評論長度'].median(), color='green', linestyle='--', linewidth=2, label=f'Median: {df["評論長度"].median():.0f}')
ax3.set_xlabel('Review Length (characters)', fontsize=12, fontweight='bold')
ax3.set_ylabel('Frequency', fontsize=12, fontweight='bold')
ax3.set_title('Review Length Distribution', fontsize=14, fontweight='bold', pad=20)
ax3.legend(fontsize=10)
ax3.grid(axis='y', alpha=0.3)

# 2.4 評論長度分布（箱形圖）
print("📈 2.4 生成評論長度箱形圖...")
ax4 = plt.subplot(4, 3, 4)
bp = ax4.boxplot(df['評論長度'], vert=True, patch_artist=True,
                  boxprops=dict(facecolor='lightblue', edgecolor='black', linewidth=1.5),
                  medianprops=dict(color='red', linewidth=2),
                  whiskerprops=dict(color='black', linewidth=1.5),
                  capprops=dict(color='black', linewidth=1.5))
ax4.set_ylabel('Review Length (characters)', fontsize=12, fontweight='bold')
ax4.set_title('Review Length Box Plot', fontsize=14, fontweight='bold', pad=20)
ax4.grid(axis='y', alpha=0.3)

# 2.5 評分與評論長度的關係
print("📈 2.5 生成評分與評論長度關係圖...")
ax5 = plt.subplot(4, 3, 5)
rating_length = df.groupby('評分')['評論長度'].mean().sort_index()
bars = ax5.bar(rating_length.index, rating_length.values, color=colors, edgecolor='black', linewidth=1.5)
ax5.set_xlabel('Rating (Stars)', fontsize=12, fontweight='bold')
ax5.set_ylabel('Average Review Length', fontsize=12, fontweight='bold')
ax5.set_title('Average Review Length by Rating', fontsize=14, fontweight='bold', pad=20)
ax5.set_xticks([1, 2, 3, 4, 5])
ax5.grid(axis='y', alpha=0.3)

for bar in bars:
    height = bar.get_height()
    ax5.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.0f}',
             ha='center', va='bottom', fontsize=10, fontweight='bold')

# 2.6 評分與評論長度（箱形圖）
print("📈 2.6 生成評分與評論長度箱形圖...")
ax6 = plt.subplot(4, 3, 6)
data_by_rating = [df[df['評分'] == i]['評論長度'].values for i in [1, 2, 3, 4, 5]]
bp = ax6.boxplot(data_by_rating, labels=['1', '2', '3', '4', '5'], patch_artist=True)
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_edgecolor('black')
    patch.set_linewidth(1.5)
for element in ['whiskers', 'fliers', 'caps']:
    plt.setp(bp[element], color='black', linewidth=1.5)
plt.setp(bp['medians'], color='red', linewidth=2)
ax6.set_xlabel('Rating (Stars)', fontsize=12, fontweight='bold')
ax6.set_ylabel('Review Length (characters)', fontsize=12, fontweight='bold')
ax6.set_title('Review Length Distribution by Rating', fontsize=14, fontweight='bold', pad=20)
ax6.grid(axis='y', alpha=0.3)

# 2.7 Top 10 醫院評論數量
print("📈 2.7 生成 Top 10 醫院評論數量圖...")
ax7 = plt.subplot(4, 3, 7)
top_hospitals = df['醫院名稱'].value_counts().head(10)
bars = ax7.barh(range(len(top_hospitals)), top_hospitals.values, color='teal', edgecolor='black', linewidth=1.5)
ax7.set_yticks(range(len(top_hospitals)))
ax7.set_yticklabels([name.replace('_', ' ') for name in top_hospitals.index], fontsize=10)
ax7.set_xlabel('Number of Reviews', fontsize=12, fontweight='bold')
ax7.set_title('Top 10 Hospitals by Review Count', fontsize=14, fontweight='bold', pad=20)
ax7.invert_yaxis()
ax7.grid(axis='x', alpha=0.3)

for i, (bar, value) in enumerate(zip(bars, top_hospitals.values)):
    percentage = (value / len(df)) * 100
    ax7.text(value, i, f' {value} ({percentage:.1f}%)',
             va='center', fontsize=9, fontweight='bold')

# 2.8 Top 10 醫院平均評分
print("📈 2.8 生成 Top 10 醫院平均評分圖...")
ax8 = plt.subplot(4, 3, 8)
top_10_names = df['醫院名稱'].value_counts().head(10).index
top_10_ratings = df[df['醫院名稱'].isin(top_10_names)].groupby('醫院名稱')['評分'].mean()
top_10_ratings = top_10_ratings.sort_values(ascending=True)

colors_rating = ['#e74c3c' if x < 3 else '#f39c12' if x < 4 else '#2ecc71' for x in top_10_ratings.values]
bars = ax8.barh(range(len(top_10_ratings)), top_10_ratings.values, color=colors_rating, edgecolor='black', linewidth=1.5)
ax8.set_yticks(range(len(top_10_ratings)))
ax8.set_yticklabels([name.replace('_', ' ') for name in top_10_ratings.index], fontsize=10)
ax8.set_xlabel('Average Rating', fontsize=12, fontweight='bold')
ax8.set_title('Average Rating of Top 10 Hospitals', fontsize=14, fontweight='bold', pad=20)
ax8.set_xlim(0, 5)
ax8.axvline(x=3, color='orange', linestyle='--', linewidth=1, alpha=0.5)
ax8.axvline(x=4, color='green', linestyle='--', linewidth=1, alpha=0.5)
ax8.invert_yaxis()
ax8.grid(axis='x', alpha=0.3)

for i, (bar, value) in enumerate(zip(bars, top_10_ratings.values)):
    ax8.text(value, i, f' {value:.2f}',
             va='center', fontsize=10, fontweight='bold')

# 2.9 時間序列分析（按月統計）
print("📈 2.9 生成時間序列圖...")
ax9 = plt.subplot(4, 3, 9)
df['年月'] = df['實際日期_parsed'].dt.to_period('M')
monthly_counts = df.groupby('年月').size()
monthly_counts.index = monthly_counts.index.to_timestamp()
ax9.plot(monthly_counts.index, monthly_counts.values, marker='o', linewidth=2, markersize=8, color='steelblue')
ax9.fill_between(monthly_counts.index, monthly_counts.values, alpha=0.3, color='steelblue')
ax9.set_xlabel('Month', fontsize=12, fontweight='bold')
ax9.set_ylabel('Number of Reviews', fontsize=12, fontweight='bold')
ax9.set_title('Review Count Over Time (Monthly)', fontsize=14, fontweight='bold', pad=20)
ax9.tick_params(axis='x', rotation=45)
ax9.grid(True, alpha=0.3)

# 2.10 時間序列分析（按月平均評分）
print("📈 2.10 生成月度平均評分時間序列圖...")
ax10 = plt.subplot(4, 3, 10)
monthly_avg_rating = df.groupby('年月')['評分'].mean()
monthly_avg_rating.index = monthly_avg_rating.index.to_timestamp()
ax10.plot(monthly_avg_rating.index, monthly_avg_rating.values, marker='o', linewidth=2, markersize=8, color='coral')
ax10.axhline(y=df['評分'].mean(), color='red', linestyle='--', linewidth=1.5, label=f'Overall Mean: {df["評分"].mean():.2f}')
ax10.set_xlabel('Month', fontsize=12, fontweight='bold')
ax10.set_ylabel('Average Rating', fontsize=12, fontweight='bold')
ax10.set_title('Average Rating Over Time (Monthly)', fontsize=14, fontweight='bold', pad=20)
ax10.set_ylim(0, 5)
ax10.tick_params(axis='x', rotation=45)
ax10.legend(fontsize=10)
ax10.grid(True, alpha=0.3)

# 2.11 語言分布
print("📈 2.11 生成語言分布圖...")
ax11 = plt.subplot(4, 3, 11)
lang_dist = df['語言'].value_counts()
colors_lang = plt.cm.Set3(range(len(lang_dist)))
wedges, texts, autotexts = ax11.pie(lang_dist.values,
                                      labels=lang_dist.index,
                                      autopct='%1.1f%%',
                                      colors=colors_lang,
                                      startangle=90)
ax11.set_title('Language Distribution', fontsize=14, fontweight='bold', pad=20)
for text in texts:
    text.set_fontsize(11)
    text.set_fontweight('bold')
for autotext in autotexts:
    autotext.set_fontsize(10)
    autotext.set_fontweight('bold')

# 2.12 評分分布（按語言）
print("📈 2.12 生成不同語言的評分分布圖...")
ax12 = plt.subplot(4, 3, 12)
lang_rating = df.groupby('語言')['評分'].mean().sort_values(ascending=False)
bars = ax12.bar(range(len(lang_rating)), lang_rating.values, color='orchid', edgecolor='black', linewidth=1.5)
ax12.set_xticks(range(len(lang_rating)))
ax12.set_xticklabels(lang_rating.index, fontsize=11, fontweight='bold')
ax12.set_ylabel('Average Rating', fontsize=12, fontweight='bold')
ax12.set_title('Average Rating by Language', fontsize=14, fontweight='bold', pad=20)
ax12.set_ylim(0, 5)
ax12.axhline(y=df['評分'].mean(), color='red', linestyle='--', linewidth=1.5, alpha=0.7, label=f'Overall: {df["評分"].mean():.2f}')
ax12.legend(fontsize=10)
ax12.grid(axis='y', alpha=0.3)

for bar, value in zip(bars, lang_rating.values):
    height = bar.get_height()
    ax12.text(bar.get_x() + bar.get_width()/2., height,
             f'{value:.2f}',
             ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.tight_layout(pad=3.0)
plt.savefig('eda_results/eda_visualizations.png', dpi=300, bbox_inches='tight')
print("✅ 圖表已儲存: eda_results/eda_visualizations.png")
print()

# ============================================================================
# 3. 相關性分析
# ============================================================================
print("=" * 80)
print("📊 3. 相關性分析")
print("=" * 80)
print()

# 計算數值變量之間的相關係數
print("📊 評分與評論長度的相關性:")
correlation = df['評分'].corr(df['評論長度'])
print(f"   Pearson 相關係數: {correlation:.4f}")

if abs(correlation) < 0.1:
    print(f"   → 幾乎無相關")
elif abs(correlation) < 0.3:
    print(f"   → 弱相關")
elif abs(correlation) < 0.7:
    print(f"   → 中度相關")
else:
    print(f"   → 強相關")
print()

# 創建相關性矩陣熱圖
fig2, ax = plt.subplots(figsize=(10, 8))
numeric_cols = ['評分', '評論長度', '照片數']
corr_matrix = df[numeric_cols].corr()

sns.heatmap(corr_matrix, annot=True, fmt='.3f', cmap='coolwarm',
            center=0, square=True, linewidths=2, cbar_kws={"shrink": 0.8},
            ax=ax, vmin=-1, vmax=1)
ax.set_title('Correlation Matrix', fontsize=16, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig('eda_results/correlation_matrix.png', dpi=300, bbox_inches='tight')
print("✅ 相關性矩陣已儲存: eda_results/correlation_matrix.png")
print()

# ============================================================================
# 4. 統計檢定
# ============================================================================
print("=" * 80)
print("📊 4. 統計檢定")
print("=" * 80)
print()

from scipy import stats

# 檢定不同評分的評論長度是否有顯著差異
print("📊 ANOVA 檢定: 不同評分的評論長度差異")
groups = [df[df['評分'] == i]['評論長度'].values for i in [1, 2, 3, 4, 5]]
f_stat, p_value = stats.f_oneway(*groups)
print(f"   F-statistic: {f_stat:.4f}")
print(f"   p-value: {p_value:.4e}")
if p_value < 0.05:
    print(f"   → 結論: 不同評分的評論長度有顯著差異 (p < 0.05)")
else:
    print(f"   → 結論: 不同評分的評論長度無顯著差異 (p >= 0.05)")
print()

# ============================================================================
# 5. 生成 EDA 報告
# ============================================================================
print("=" * 80)
print("📊 5. 生成 EDA 報告")
print("=" * 80)
print()

report = f"""
# 📊 探索性資料分析（EDA）報告

**生成日期**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**資料來源**: cleaned_data_no_dedup/final_cleaned_sample_no_dedup.csv
**樣本數**: {len(df):,} 條

---

## 1. 資料概覽

### 基本資訊
- **樣本數**: {len(df):,} 條評論
- **特徵數**: {len(df.columns)} 個欄位
- **醫院數**: {df['醫院名稱'].nunique()} 家
- **時間跨度**: {df['實際日期_parsed'].min().strftime('%Y-%m-%d')} 至 {df['實際日期_parsed'].max().strftime('%Y-%m-%d')} ({(df['實際日期_parsed'].max() - df['實際日期_parsed'].min()).days} 天)

### 資料品質
- **缺失值**: {df.isnull().sum().sum()} 個
- **重複值**: 未移除（本版本保留所有資料）

---

## 2. 評分分析

### 評分分布
| 評分 | 數量 | 百分比 |
|------|------|--------|
{chr(10).join([f"| {rating} 星 | {count:,} | {(count/len(df)*100):.1f}% |" for rating, count in df['評分'].value_counts().sort_index().items()])}

### 評分統計
- **平均評分**: {df['評分'].mean():.2f} 星
- **中位數評分**: {df['評分'].median():.1f} 星
- **標準差**: {df['評分'].std():.2f}

### 主要發現
- **極化現象**: {(df['評分'].isin([1, 5]).sum() / len(df) * 100):.1f}% 的評論是極端評分（1星或5星）
- **正面評論**: {(df['評分'] >= 4).sum() / len(df) * 100:.1f}% 的評論是正面的（4-5星）
- **負面評論**: {(df['評分'] <= 2).sum() / len(df) * 100:.1f}% 的評論是負面的（1-2星）

---

## 3. 評論長度分析

### 長度統計
- **平均長度**: {df['評論長度'].mean():.1f} 字元
- **中位數長度**: {df['評論長度'].median():.0f} 字元
- **最短評論**: {df['評論長度'].min()} 字元
- **最長評論**: {df['評論長度'].max():,} 字元
- **標準差**: {df['評論長度'].std():.1f} 字元

### 長度與評分的關係
| 評分 | 平均長度 |
|------|----------|
{chr(10).join([f"| {rating} 星 | {length:.1f} 字元 |" for rating, length in df.groupby('評分')['評論長度'].mean().sort_index().items()])}

**相關性**: Pearson r = {df['評分'].corr(df['評論長度']):.4f}

---

## 4. 醫院分析

### Top 10 醫院（按評論數）
| 排名 | 醫院名稱 | 評論數 | 百分比 | 平均評分 |
|------|----------|--------|--------|----------|
{chr(10).join([f"| {i+1} | {hospital.replace('_', ' ')} | {count:,} | {(count/len(df)*100):.1f}% | {df[df['醫院名稱']==hospital]['評分'].mean():.2f} |"
              for i, (hospital, count) in enumerate(df['醫院名稱'].value_counts().head(10).items())])}

### 醫院評分差異
- **最高平均評分**: {df.groupby('醫院名稱')['評分'].mean().max():.2f} 星
- **最低平均評分**: {df.groupby('醫院名稱')['評分'].mean().min():.2f} 星
- **評分標準差**: {df.groupby('醫院名稱')['評分'].mean().std():.2f}

---

## 5. 時間趨勢分析

### 月度統計
- **評論最多的月份**: {df.groupby('年月').size().idxmax().strftime('%Y-%m')} ({df.groupby('年月').size().max()} 條)
- **評論最少的月份**: {df.groupby('年月').size().idxmin().strftime('%Y-%m')} ({df.groupby('年月').size().min()} 條)
- **平均月度評論數**: {df.groupby('年月').size().mean():.1f} 條

### 評分趨勢
- **整體平均評分**: {df['評分'].mean():.2f} 星
- **最高月度平均**: {df.groupby('年月')['評分'].mean().max():.2f} 星
- **最低月度平均**: {df.groupby('年月')['評分'].mean().min():.2f} 星

---

## 6. 語言分析

### 語言分布
| 語言 | 數量 | 百分比 | 平均評分 |
|------|------|--------|----------|
{chr(10).join([f"| {lang} | {count:,} | {(count/len(df)*100):.1f}% | {df[df['語言']==lang]['評分'].mean():.2f} |"
              for lang, count in df['語言'].value_counts().items()])}

---

## 7. 統計檢定結果

### ANOVA 檢定：不同評分的評論長度差異
- **F-statistic**: {f_stat:.4f}
- **p-value**: {p_value:.4e}
- **結論**: {'不同評分的評論長度有顯著差異 (p < 0.05)' if p_value < 0.05 else '不同評分的評論長度無顯著差異 (p >= 0.05)'}

---

## 8. 主要發現與洞察

### 🔍 關鍵發現

1. **評分極化現象明顯**
   - {(df['評分'].isin([1, 5]).sum() / len(df) * 100):.1f}% 的評論是極端評分（1星或5星）
   - 中間評分（2-4星）僅佔 {(df['評分'].isin([2, 3, 4]).sum() / len(df) * 100):.1f}%
   - 這是 Google Maps 評論的典型特徵

2. **評論長度與評分的關係**
   - 相關係數: {df['評分'].corr(df['評論長度']):.4f}
   - {'負面評論往往更長，用戶更傾向於詳細描述負面體驗' if df['評分'].corr(df['評論長度']) < 0 else '正面評論往往更長，用戶更傾向於詳細描述正面體驗' if df['評分'].corr(df['評論長度']) > 0 else '評論長度與評分無明顯相關性'}

3. **醫院分布不均**
   - Top 1 醫院（{df['醫院名稱'].value_counts().index[0].replace('_', ' ')}）佔 {(df['醫院名稱'].value_counts().iloc[0] / len(df) * 100):.1f}%
   - 建議在後續分析中考慮分層或加權處理

4. **時間趨勢**
   - 評論數量呈現{'上升' if df.groupby('年月').size().values[-1] > df.groupby('年月').size().values[0] else '下降'}趨勢
   - 平均評分相對{'穩定' if df.groupby('年月')['評分'].mean().std() < 0.5 else '波動'}

---

## 9. 後續分析建議

### 📌 建議進行的分析

1. **文本分析**
   - 詞頻分析（TF-IDF）
   - 主題建模（LDA, BERTopic）
   - 情感分析

2. **深度分析**
   - Aspect-Based Sentiment Analysis (ABSA)
   - 識別服務品質維度
   - 醫院間比較分析

3. **預測建模**
   - 評分預測模型
   - 關鍵詞與評分的關係

---

**圖表輸出位置**: eda_results/

---

**報告生成完成** ✅
"""

# 儲存報告
report_file = 'eda_results/EDA_REPORT.md'
with open(report_file, 'w', encoding='utf-8') as f:
    f.write(report)

print(f"✅ EDA 報告已儲存: {report_file}")
print()

# ============================================================================
# 完成
# ============================================================================
print("=" * 80)
print("✅ 探索性資料分析（EDA）完成！")
print("=" * 80)
print()
print("📁 輸出檔案:")
print("   • eda_results/eda_visualizations.png - 視覺化圖表")
print("   • eda_results/correlation_matrix.png - 相關性矩陣")
print("   • eda_results/EDA_REPORT.md - 完整報告")
print()
print("🚀 下一步: 主題建模（LDA, BERTopic）")
print("=" * 80)
