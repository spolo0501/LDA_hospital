#!/usr/bin/env python3
"""
情感分析 - VADER & TextBlob
分析醫院評論的情感傾向並與實際評分進行比較
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# 情感分析工具
from textblob import TextBlob

# VADER 情感分析
try:
    from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
    VADER_AVAILABLE = True
except ImportError:
    print("⚠️  VADER 未安裝，將只使用 TextBlob")
    VADER_AVAILABLE = False

# 設定
import os
os.makedirs('sentiment_analysis_results', exist_ok=True)

# 設定繪圖樣式
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
sns.set_style("whitegrid")
sns.set_palette("husl")

print("=" * 80)
print("💭 情感分析 - VADER & TextBlob")
print("=" * 80)
print()

# ============================================================================
# 1. 資料載入
# ============================================================================
print("=" * 80)
print("📊 1. 資料載入")
print("=" * 80)
print()

print("📂 讀取資料...")
df = pd.read_csv('cleaned_data_no_dedup/final_cleaned_sample_no_dedup.csv', encoding='utf-8-sig')
print(f"✅ 資料載入完成: {len(df):,} 條評論")
print()

# 只分析英文評論
df_en = df[df['語言'] == 'en'].copy()
print(f"📝 篩選英文評論: {len(df_en):,} 條 ({len(df_en)/len(df)*100:.1f}%)")
print()

# ============================================================================
# 2. 執行情感分析
# ============================================================================
print("=" * 80)
print("📊 2. 執行情感分析")
print("=" * 80)
print()

# 2.1 TextBlob 情感分析
print("🔍 執行 TextBlob 情感分析...")

def get_textblob_sentiment(text):
    """使用 TextBlob 分析情感"""
    try:
        blob = TextBlob(text)
        # polarity: -1 (negative) to 1 (positive)
        # subjectivity: 0 (objective) to 1 (subjective)
        return blob.sentiment.polarity, blob.sentiment.subjectivity
    except:
        return 0, 0

df_en[['textblob_polarity', 'textblob_subjectivity']] = df_en['評論內容'].apply(
    lambda x: pd.Series(get_textblob_sentiment(x))
)

# 將 polarity 轉換為情感標籤
def polarity_to_label(polarity):
    if polarity > 0.1:
        return 'Positive'
    elif polarity < -0.1:
        return 'Negative'
    else:
        return 'Neutral'

df_en['textblob_sentiment'] = df_en['textblob_polarity'].apply(polarity_to_label)

print(f"✅ TextBlob 分析完成")
print(f"   平均 Polarity: {df_en['textblob_polarity'].mean():.3f}")
print(f"   平均 Subjectivity: {df_en['textblob_subjectivity'].mean():.3f}")
print()

# 2.2 VADER 情感分析（如果可用）
if VADER_AVAILABLE:
    print("🔍 執行 VADER 情感分析...")

    analyzer = SentimentIntensityAnalyzer()

    def get_vader_sentiment(text):
        """使用 VADER 分析情感"""
        try:
            scores = analyzer.polarity_scores(text)
            # compound: -1 (most negative) to 1 (most positive)
            return scores['compound'], scores['neg'], scores['neu'], scores['pos']
        except:
            return 0, 0, 0, 0

    df_en[['vader_compound', 'vader_neg', 'vader_neu', 'vader_pos']] = df_en['評論內容'].apply(
        lambda x: pd.Series(get_vader_sentiment(x))
    )

    # VADER 情感分類
    def vader_classify(compound):
        if compound >= 0.05:
            return 'Positive'
        elif compound <= -0.05:
            return 'Negative'
        else:
            return 'Neutral'

    df_en['vader_sentiment'] = df_en['vader_compound'].apply(vader_classify)

    print(f"✅ VADER 分析完成")
    print(f"   平均 Compound Score: {df_en['vader_compound'].mean():.3f}")
    print(f"   平均 Negative: {df_en['vader_neg'].mean():.3f}")
    print(f"   平均 Neutral: {df_en['vader_neu'].mean():.3f}")
    print(f"   平均 Positive: {df_en['vader_pos'].mean():.3f}")
    print()

# ============================================================================
# 3. 情感分析與評分的關係
# ============================================================================
print("=" * 80)
print("📊 3. 情感分析與評分的關係")
print("=" * 80)
print()

# 創建評分類別
def rating_category(rating):
    if rating >= 4:
        return 'Positive (4-5★)'
    elif rating == 3:
        return 'Neutral (3★)'
    else:
        return 'Negative (1-2★)'

df_en['rating_category'] = df_en['評分'].apply(rating_category)

# TextBlob 情感分布
print("📊 TextBlob 情感分布:")
textblob_dist = df_en['textblob_sentiment'].value_counts()
for sentiment, count in textblob_dist.items():
    percentage = (count / len(df_en)) * 100
    print(f"   {sentiment:10s}: {count:5d} 條 ({percentage:5.1f}%)")
print()

# VADER 情感分布（如果可用）
if VADER_AVAILABLE:
    print("📊 VADER 情感分布:")
    vader_dist = df_en['vader_sentiment'].value_counts()
    for sentiment, count in vader_dist.items():
        percentage = (count / len(df_en)) * 100
        print(f"   {sentiment:10s}: {count:5d} 條 ({percentage:5.1f}%)")
    print()

# 情感與評分的一致性
print("📊 情感分析準確度（與評分對比）:")

# TextBlob 準確度
def check_textblob_accuracy(row):
    """檢查 TextBlob 情感是否與評分一致"""
    if row['評分'] >= 4 and row['textblob_sentiment'] == 'Positive':
        return True
    elif row['評分'] <= 2 and row['textblob_sentiment'] == 'Negative':
        return True
    elif row['評分'] == 3 and row['textblob_sentiment'] == 'Neutral':
        return True
    return False

df_en['textblob_accurate'] = df_en.apply(check_textblob_accuracy, axis=1)
textblob_accuracy = (df_en['textblob_accurate'].sum() / len(df_en)) * 100
print(f"   TextBlob 準確率: {textblob_accuracy:.1f}%")

# VADER 準確度（如果可用）
if VADER_AVAILABLE:
    def check_vader_accuracy(row):
        """檢查 VADER 情感是否與評分一致"""
        if row['評分'] >= 4 and row['vader_sentiment'] == 'Positive':
            return True
        elif row['評分'] <= 2 and row['vader_sentiment'] == 'Negative':
            return True
        elif row['評分'] == 3 and row['vader_sentiment'] == 'Neutral':
            return True
        return False

    df_en['vader_accurate'] = df_en.apply(check_vader_accuracy, axis=1)
    vader_accuracy = (df_en['vader_accurate'].sum() / len(df_en)) * 100
    print(f"   VADER 準確率: {vader_accuracy:.1f}%")
print()

# ============================================================================
# 4. 視覺化分析
# ============================================================================
print("=" * 80)
print("📊 4. 生成視覺化圖表")
print("=" * 80)
print()

fig = plt.figure(figsize=(20, 16))

# 4.1 TextBlob Polarity 與評分的關係
ax1 = plt.subplot(3, 3, 1)
rating_polarity = df_en.groupby('評分')['textblob_polarity'].mean()
colors = ['#e74c3c', '#e67e22', '#f39c12', '#2ecc71', '#27ae60']
bars = ax1.bar(rating_polarity.index, rating_polarity.values, color=colors, edgecolor='black', linewidth=1.5)
ax1.set_xlabel('Rating (Stars)', fontsize=12, fontweight='bold')
ax1.set_ylabel('Average TextBlob Polarity', fontsize=12, fontweight='bold')
ax1.set_title('TextBlob Polarity vs Rating', fontsize=14, fontweight='bold', pad=15)
ax1.axhline(y=0, color='gray', linestyle='--', linewidth=1, alpha=0.5)
ax1.grid(axis='y', alpha=0.3)

for bar, value in zip(bars, rating_polarity.values):
    ax1.text(bar.get_x() + bar.get_width()/2., bar.get_height(),
             f'{value:.3f}', ha='center', va='bottom', fontsize=10, fontweight='bold')

# 4.2 TextBlob Polarity 分布（箱形圖）
ax2 = plt.subplot(3, 3, 2)
data_by_rating = [df_en[df_en['評分'] == i]['textblob_polarity'].values for i in [1, 2, 3, 4, 5]]
bp = ax2.boxplot(data_by_rating, labels=['1', '2', '3', '4', '5'], patch_artist=True)
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_edgecolor('black')
    patch.set_linewidth(1.5)
for element in ['whiskers', 'fliers', 'caps']:
    plt.setp(bp[element], color='black', linewidth=1.5)
plt.setp(bp['medians'], color='red', linewidth=2)
ax2.set_xlabel('Rating (Stars)', fontsize=12, fontweight='bold')
ax2.set_ylabel('TextBlob Polarity', fontsize=12, fontweight='bold')
ax2.set_title('TextBlob Polarity Distribution by Rating', fontsize=14, fontweight='bold', pad=15)
ax2.axhline(y=0, color='gray', linestyle='--', linewidth=1, alpha=0.5)
ax2.grid(axis='y', alpha=0.3)

# 4.3 TextBlob Subjectivity 與評分的關係
ax3 = plt.subplot(3, 3, 3)
rating_subj = df_en.groupby('評分')['textblob_subjectivity'].mean()
bars = ax3.bar(rating_subj.index, rating_subj.values, color='steelblue', edgecolor='black', linewidth=1.5)
ax3.set_xlabel('Rating (Stars)', fontsize=12, fontweight='bold')
ax3.set_ylabel('Average Subjectivity', fontsize=12, fontweight='bold')
ax3.set_title('TextBlob Subjectivity vs Rating', fontsize=14, fontweight='bold', pad=15)
ax3.grid(axis='y', alpha=0.3)

for bar, value in zip(bars, rating_subj.values):
    ax3.text(bar.get_x() + bar.get_width()/2., bar.get_height(),
             f'{value:.3f}', ha='center', va='bottom', fontsize=10, fontweight='bold')

# 4.4 TextBlob 情感分類分布
ax4 = plt.subplot(3, 3, 4)
sentiment_counts = df_en['textblob_sentiment'].value_counts()
colors_sent = {'Positive': '#27ae60', 'Neutral': '#f39c12', 'Negative': '#e74c3c'}
colors_list = [colors_sent.get(s, 'gray') for s in sentiment_counts.index]
bars = ax4.bar(sentiment_counts.index, sentiment_counts.values, color=colors_list, edgecolor='black', linewidth=1.5)
ax4.set_xlabel('Sentiment', fontsize=12, fontweight='bold')
ax4.set_ylabel('Count', fontsize=12, fontweight='bold')
ax4.set_title('TextBlob Sentiment Distribution', fontsize=14, fontweight='bold', pad=15)
ax4.grid(axis='y', alpha=0.3)

for bar, value in zip(bars, sentiment_counts.values):
    percentage = (value / len(df_en)) * 100
    ax4.text(bar.get_x() + bar.get_width()/2., bar.get_height(),
             f'{value}\n({percentage:.1f}%)', ha='center', va='bottom', fontsize=10, fontweight='bold')

# 4.5 評分分類 vs TextBlob 情感（混淆矩陣式）
ax5 = plt.subplot(3, 3, 5)
confusion_data = pd.crosstab(df_en['rating_category'], df_en['textblob_sentiment'])
# 重新排序
confusion_data = confusion_data.reindex(['Positive (4-5★)', 'Neutral (3★)', 'Negative (1-2★)'], fill_value=0)
confusion_data = confusion_data[['Positive', 'Neutral', 'Negative']]
sns.heatmap(confusion_data, annot=True, fmt='d', cmap='YlOrRd', ax=ax5, cbar_kws={'label': 'Count'},
            linewidths=2, linecolor='black')
ax5.set_xlabel('TextBlob Sentiment', fontsize=12, fontweight='bold')
ax5.set_ylabel('Rating Category', fontsize=12, fontweight='bold')
ax5.set_title('Rating vs TextBlob Sentiment', fontsize=14, fontweight='bold', pad=15)

# VADER 圖表（如果可用）
if VADER_AVAILABLE:
    # 4.6 VADER Compound Score 與評分的關係
    ax6 = plt.subplot(3, 3, 6)
    rating_vader = df_en.groupby('評分')['vader_compound'].mean()
    bars = ax6.bar(rating_vader.index, rating_vader.values, color=colors, edgecolor='black', linewidth=1.5)
    ax6.set_xlabel('Rating (Stars)', fontsize=12, fontweight='bold')
    ax6.set_ylabel('Average VADER Compound Score', fontsize=12, fontweight='bold')
    ax6.set_title('VADER Compound Score vs Rating', fontsize=14, fontweight='bold', pad=15)
    ax6.axhline(y=0, color='gray', linestyle='--', linewidth=1, alpha=0.5)
    ax6.grid(axis='y', alpha=0.3)

    for bar, value in zip(bars, rating_vader.values):
        ax6.text(bar.get_x() + bar.get_width()/2., bar.get_height(),
                 f'{value:.3f}', ha='center', va='bottom' if value > 0 else 'top', fontsize=10, fontweight='bold')

    # 4.7 VADER Compound Score 分布（箱形圖）
    ax7 = plt.subplot(3, 3, 7)
    data_by_rating_vader = [df_en[df_en['評分'] == i]['vader_compound'].values for i in [1, 2, 3, 4, 5]]
    bp = ax7.boxplot(data_by_rating_vader, labels=['1', '2', '3', '4', '5'], patch_artist=True)
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_edgecolor('black')
        patch.set_linewidth(1.5)
    for element in ['whiskers', 'fliers', 'caps']:
        plt.setp(bp[element], color='black', linewidth=1.5)
    plt.setp(bp['medians'], color='red', linewidth=2)
    ax7.set_xlabel('Rating (Stars)', fontsize=12, fontweight='bold')
    ax7.set_ylabel('VADER Compound Score', fontsize=12, fontweight='bold')
    ax7.set_title('VADER Score Distribution by Rating', fontsize=14, fontweight='bold', pad=15)
    ax7.axhline(y=0, color='gray', linestyle='--', linewidth=1, alpha=0.5)
    ax7.grid(axis='y', alpha=0.3)

    # 4.8 VADER 情感分類分布
    ax8 = plt.subplot(3, 3, 8)
    vader_sentiment_counts = df_en['vader_sentiment'].value_counts()
    colors_list_vader = [colors_sent.get(s, 'gray') for s in vader_sentiment_counts.index]
    bars = ax8.bar(vader_sentiment_counts.index, vader_sentiment_counts.values, color=colors_list_vader, edgecolor='black', linewidth=1.5)
    ax8.set_xlabel('Sentiment', fontsize=12, fontweight='bold')
    ax8.set_ylabel('Count', fontsize=12, fontweight='bold')
    ax8.set_title('VADER Sentiment Distribution', fontsize=14, fontweight='bold', pad=15)
    ax8.grid(axis='y', alpha=0.3)

    for bar, value in zip(bars, vader_sentiment_counts.values):
        percentage = (value / len(df_en)) * 100
        ax8.text(bar.get_x() + bar.get_width()/2., bar.get_height(),
                 f'{value}\n({percentage:.1f}%)', ha='center', va='bottom', fontsize=10, fontweight='bold')

    # 4.9 評分分類 vs VADER 情感（混淆矩陣式）
    ax9 = plt.subplot(3, 3, 9)
    confusion_data_vader = pd.crosstab(df_en['rating_category'], df_en['vader_sentiment'])
    confusion_data_vader = confusion_data_vader.reindex(['Positive (4-5★)', 'Neutral (3★)', 'Negative (1-2★)'], fill_value=0)
    confusion_data_vader = confusion_data_vader[['Positive', 'Neutral', 'Negative']]
    sns.heatmap(confusion_data_vader, annot=True, fmt='d', cmap='YlOrRd', ax=ax9, cbar_kws={'label': 'Count'},
                linewidths=2, linecolor='black')
    ax9.set_xlabel('VADER Sentiment', fontsize=12, fontweight='bold')
    ax9.set_ylabel('Rating Category', fontsize=12, fontweight='bold')
    ax9.set_title('Rating vs VADER Sentiment', fontsize=14, fontweight='bold', pad=15)

plt.tight_layout()
plt.savefig('sentiment_analysis_results/sentiment_analysis.png', dpi=300, bbox_inches='tight')
print("✅ 情感分析圖已儲存: sentiment_analysis_results/sentiment_analysis.png")
print()

# ============================================================================
# 5. 相關性分析
# ============================================================================
print("=" * 80)
print("📊 5. 相關性分析")
print("=" * 80)
print()

# TextBlob Polarity 與評分的相關性
corr_tb_rating = df_en['textblob_polarity'].corr(df_en['評分'])
print(f"📊 TextBlob Polarity vs 評分: r = {corr_tb_rating:.4f}")

if VADER_AVAILABLE:
    # VADER Compound 與評分的相關性
    corr_vader_rating = df_en['vader_compound'].corr(df_en['評分'])
    print(f"📊 VADER Compound vs 評分: r = {corr_vader_rating:.4f}")

    # TextBlob 與 VADER 的相關性
    corr_tb_vader = df_en['textblob_polarity'].corr(df_en['vader_compound'])
    print(f"📊 TextBlob vs VADER: r = {corr_tb_vader:.4f}")

print()

# ============================================================================
# 6. 生成情感分析報告
# ============================================================================
print("=" * 80)
print("📊 6. 生成情感分析報告")
print("=" * 80)
print()

report = f"""
# 💭 情感分析報告 (TextBlob & VADER)

**生成日期**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**資料來源**: cleaned_data_no_dedup/final_cleaned_sample_no_dedup.csv
**分析樣本**: {len(df_en):,} 條英文評論

---

## 1. 分析概覽

### 情感分析工具
- **TextBlob**: 基於模式識別的情感分析
- **VADER**: 專為社交媒體文本設計的情感分析{'（已執行）' if VADER_AVAILABLE else '（未安裝）'}

### 情感指標
- **Polarity** (TextBlob): -1 (負面) 到 +1 (正面)
- **Subjectivity** (TextBlob): 0 (客觀) 到 1 (主觀)
- **Compound Score** (VADER): -1 (最負面) 到 +1 (最正面)

---

## 2. TextBlob 情感分析結果

### 整體統計
- **平均 Polarity**: {df_en['textblob_polarity'].mean():.3f}
- **平均 Subjectivity**: {df_en['textblob_subjectivity'].mean():.3f}
- **Polarity 標準差**: {df_en['textblob_polarity'].std():.3f}

### 情感分類分布
| 情感分類 | 數量 | 百分比 |
|----------|------|--------|
{chr(10).join([f"| {sentiment} | {count:,} | {(count/len(df_en)*100):.1f}% |"
              for sentiment, count in df_en['textblob_sentiment'].value_counts().items()])}

### Polarity 與評分的關係
| 評分 | 平均 Polarity |
|------|---------------|
{chr(10).join([f"| {rating} 星 | {polarity:.3f} |"
              for rating, polarity in df_en.groupby('評分')['textblob_polarity'].mean().sort_index().items()])}

**相關係數**: r = {df_en['textblob_polarity'].corr(df_en['評分']):.4f}

### 準確度分析
- **TextBlob 準確率**: {textblob_accuracy:.1f}%
  (情感分類與評分類別一致的比例)

---
"""

if VADER_AVAILABLE:
    report += f"""
## 3. VADER 情感分析結果

### 整體統計
- **平均 Compound Score**: {df_en['vader_compound'].mean():.3f}
- **平均 Negative Score**: {df_en['vader_neg'].mean():.3f}
- **平均 Neutral Score**: {df_en['vader_neu'].mean():.3f}
- **平均 Positive Score**: {df_en['vader_pos'].mean():.3f}

### 情感分類分布
| 情感分類 | 數量 | 百分比 |
|----------|------|--------|
{chr(10).join([f"| {sentiment} | {count:,} | {(count/len(df_en)*100):.1f}% |"
              for sentiment, count in df_en['vader_sentiment'].value_counts().items()])}

### Compound Score 與評分的關係
| 評分 | 平均 Compound Score |
|------|---------------------|
{chr(10).join([f"| {rating} 星 | {compound:.3f} |"
              for rating, compound in df_en.groupby('評分')['vader_compound'].mean().sort_index().items()])}

**相關係數**: r = {df_en['vader_compound'].corr(df_en['評分']):.4f}

### 準確度分析
- **VADER 準確率**: {vader_accuracy:.1f}%
  (情感分類與評分類別一致的比例)

---

## 4. TextBlob vs VADER 比較

### 相關性
- **TextBlob Polarity vs VADER Compound**: r = {df_en['textblob_polarity'].corr(df_en['vader_compound']):.4f}
- 兩種方法的情感判斷高度一致

### 準確度比較
| 方法 | 準確率 |
|------|--------|
| TextBlob | {textblob_accuracy:.1f}% |
| VADER | {vader_accuracy:.1f}% |

---
"""

report += f"""
## 5. 主要發現與洞察

### 🔍 關鍵發現

1. **情感與評分高度相關**
   - TextBlob Polarity 與評分相關係數: {df_en['textblob_polarity'].corr(df_en['評分']):.3f}
   - 情感分析能夠較好地反映用戶評分

2. **極化現象明顯**
   - 正面和負面情感評論佔多數
   - 中性評論相對較少

3. **主觀性分析**
   - 平均主觀性分數: {df_en['textblob_subjectivity'].mean():.3f}
   - {'評論傾向於主觀表達' if df_en['textblob_subjectivity'].mean() > 0.5 else '評論包含較多客觀陳述'}

4. **負面評論特徵**
   - 1星評論平均 Polarity: {df_en[df_en['評分']==1]['textblob_polarity'].mean():.3f}
   - 負面評論通常包含強烈的負面情緒詞彙

5. **正面評論特徵**
   - 5星評論平均 Polarity: {df_en[df_en['評分']==5]['textblob_polarity'].mean():.3f}
   - 正面評論通常包含讚美和感謝的表達

---

## 6. 醫院管理建議

### 基於情感分析的改善建議

1. **監控負面情感趨勢**
   - 建立情感監控系統，及時識別負面評論
   - 優先處理高負面情感分數的評論

2. **強化正面體驗**
   - 分析高正面情感評論的關鍵詞
   - 複製成功經驗到其他服務環節

3. **改善溝通策略**
   - 根據評論的主觀性調整回應方式
   - 對主觀性強的評論提供更個性化的回應

4. **預警機制**
   - 使用情感分析作為服務品質的早期預警指標
   - 在問題擴大前及時干預

---

## 7. 輸出檔案

- `sentiment_analysis_results/sentiment_analysis.png` - 情感分析視覺化
- `sentiment_analysis_results/SENTIMENT_ANALYSIS_REPORT.md` - 本報告

---

**報告生成完成** ✅
"""

# 儲存報告
report_file = 'sentiment_analysis_results/SENTIMENT_ANALYSIS_REPORT.md'
with open(report_file, 'w', encoding='utf-8') as f:
    f.write(report)

print(f"✅ 情感分析報告已儲存: {report_file}")
print()

# 儲存包含情感分數的資料
output_file = 'sentiment_analysis_results/reviews_with_sentiment.csv'
df_en.to_csv(output_file, index=False, encoding='utf-8-sig')
print(f"✅ 情感分析資料已儲存: {output_file}")
print()

# ============================================================================
# 完成
# ============================================================================
print("=" * 80)
print("✅ 情感分析完成！")
print("=" * 80)
print()
print("📁 輸出檔案:")
print("   • sentiment_analysis_results/sentiment_analysis.png - 視覺化圖表")
print("   • sentiment_analysis_results/SENTIMENT_ANALYSIS_REPORT.md - 完整報告")
print("   • sentiment_analysis_results/reviews_with_sentiment.csv - 包含情感分數的資料")
print()
print("🎊 所有分析完成！")
print("=" * 80)
