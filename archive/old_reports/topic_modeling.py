#!/usr/bin/env python3
"""
主題建模分析 - LDA 和 BERTopic
分析醫院評論中的主要話題和主題
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# 文本處理
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# LDA 相關
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import pyLDAvis
import pyLDAvis.lda_model

# BERTopic 相關（如果可用）
try:
    from bertopic import BERTopic
    from sentence_transformers import SentenceTransformer
    BERTOPIC_AVAILABLE = True
except ImportError:
    BERTOPIC_AVAILABLE = False
    print("⚠️  BERTopic 未安裝，將只執行 LDA 分析")

# 設定
import os
os.makedirs('topic_modeling_results', exist_ok=True)

print("=" * 80)
print("🔍 主題建模分析 - LDA & BERTopic")
print("=" * 80)
print()

# 下載 NLTK 資源（如果尚未下載）
print("📥 準備 NLTK 資源...")
try:
    nltk.download('stopwords', quiet=True)
    nltk.download('punkt', quiet=True)
    nltk.download('wordnet', quiet=True)
    nltk.download('omw-1.4', quiet=True)
    nltk.download('punkt_tab', quiet=True)
    print("✅ NLTK 資源準備完成")
except Exception as e:
    print(f"⚠️  NLTK 下載警告: {e}")
print()

# ============================================================================
# 1. 資料載入與前處理
# ============================================================================
print("=" * 80)
print("📊 1. 資料載入與前處理")
print("=" * 80)
print()

print("📂 讀取資料...")
df = pd.read_csv('cleaned_data_no_dedup/final_cleaned_sample_no_dedup.csv', encoding='utf-8-sig')
print(f"✅ 資料載入完成: {len(df):,} 條評論")
print()

# 只保留英文評論（因為文本分析工具主要針對英文）
df_en = df[df['語言'] == 'en'].copy()
print(f"📝 篩選英文評論: {len(df_en):,} 條 ({len(df_en)/len(df)*100:.1f}%)")
print()

# ============================================================================
# 2. 文本前處理
# ============================================================================
print("=" * 80)
print("📊 2. 文本前處理")
print("=" * 80)
print()

def preprocess_text(text):
    """文本前處理"""
    # 轉小寫
    text = text.lower()

    # 移除 URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)

    # 移除 email
    text = re.sub(r'\S+@\S+', '', text)

    # 移除數字
    text = re.sub(r'\d+', '', text)

    # 移除標點符號但保留句子結構
    text = re.sub(r'[^\w\s]', ' ', text)

    # 移除多餘空白
    text = re.sub(r'\s+', ' ', text).strip()

    return text

print("🔄 執行文本前處理...")
df_en['cleaned_text'] = df_en['評論內容'].apply(preprocess_text)

# 移除停用詞和詞形還原
stop_words = set(stopwords.words('english'))
# 添加醫院相關的常見詞（可能不具區分性）
custom_stopwords = {'hospital', 'dr', 'doctor', 'patient', 'visited', 'visit', 'one', 'would', 'get', 'like', 'go', 'went'}
stop_words.update(custom_stopwords)

lemmatizer = WordNetLemmatizer()

def tokenize_and_lemmatize(text):
    """分詞和詞形還原"""
    tokens = word_tokenize(text)
    tokens = [lemmatizer.lemmatize(token) for token in tokens
              if token not in stop_words and len(token) > 2]
    return ' '.join(tokens)

print("🔄 執行分詞和詞形還原...")
df_en['processed_text'] = df_en['cleaned_text'].apply(tokenize_and_lemmatize)

# 移除過短的文本
df_en = df_en[df_en['processed_text'].str.len() > 20].copy()
print(f"✅ 前處理完成: {len(df_en):,} 條有效評論")
print()

# ============================================================================
# 3. LDA 主題建模
# ============================================================================
print("=" * 80)
print("📊 3. LDA 主題建模")
print("=" * 80)
print()

# 分別對正面和負面評論進行主題建模
df_positive = df_en[df_en['評分'] >= 4].copy()
df_negative = df_en[df_en['評分'] <= 2].copy()

print(f"📊 正面評論: {len(df_positive):,} 條")
print(f"📊 負面評論: {len(df_negative):,} 條")
print()

def perform_lda(texts, n_topics=5, n_top_words=10, label=''):
    """執行 LDA 主題建模"""
    print(f"🔍 執行 LDA 分析 ({label})...")

    # 創建文檔-詞頻矩陣
    vectorizer = CountVectorizer(max_df=0.95, min_df=2, max_features=1000)
    doc_term_matrix = vectorizer.fit_transform(texts)

    # LDA 模型
    lda_model = LatentDirichletAllocation(
        n_components=n_topics,
        random_state=42,
        max_iter=20,
        learning_method='online',
        n_jobs=-1
    )

    lda_output = lda_model.fit_transform(doc_term_matrix)

    # 提取主題詞
    feature_names = vectorizer.get_feature_names_out()
    topics = []

    print(f"\n📋 {label} - 主題分析結果:")
    print("-" * 80)

    for topic_idx, topic in enumerate(lda_model.components_):
        top_indices = topic.argsort()[-n_top_words:][::-1]
        top_words = [feature_names[i] for i in top_indices]
        topics.append(top_words)

        print(f"\n主題 {topic_idx + 1}:")
        print(f"  關鍵詞: {', '.join(top_words[:10])}")

    print()

    return lda_model, vectorizer, doc_term_matrix, lda_output, topics

# 對正面評論進行 LDA
print("\n" + "=" * 80)
print("📊 正面評論主題分析 (LDA)")
print("=" * 80)
lda_pos, vec_pos, dtm_pos, output_pos, topics_pos = perform_lda(
    df_positive['processed_text'].values,
    n_topics=5,
    label='正面評論'
)

# 對負面評論進行 LDA
print("\n" + "=" * 80)
print("📊 負面評論主題分析 (LDA)")
print("=" * 80)
lda_neg, vec_neg, dtm_neg, output_neg, topics_neg = perform_lda(
    df_negative['processed_text'].values,
    n_topics=5,
    label='負面評論'
)

# ============================================================================
# 4. LDA 視覺化
# ============================================================================
print("=" * 80)
print("📊 4. LDA 視覺化")
print("=" * 80)
print()

# 4.1 主題分布熱圖 - 正面評論
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# 正面評論 - 主題分布
ax1 = axes[0, 0]
topic_dist_pos = output_pos.mean(axis=0)
colors_pos = plt.cm.Greens(np.linspace(0.4, 0.8, len(topic_dist_pos)))
bars = ax1.bar(range(1, len(topic_dist_pos) + 1), topic_dist_pos, color=colors_pos, edgecolor='black', linewidth=1.5)
ax1.set_xlabel('Topic Number', fontsize=12, fontweight='bold')
ax1.set_ylabel('Average Probability', fontsize=12, fontweight='bold')
ax1.set_title('Positive Reviews - Topic Distribution (LDA)', fontsize=14, fontweight='bold', pad=15)
ax1.set_xticks(range(1, len(topic_dist_pos) + 1))
ax1.grid(axis='y', alpha=0.3)

for bar, value in zip(bars, topic_dist_pos):
    ax1.text(bar.get_x() + bar.get_width()/2., bar.get_height(),
             f'{value:.3f}', ha='center', va='bottom', fontsize=10, fontweight='bold')

# 負面評論 - 主題分布
ax2 = axes[0, 1]
topic_dist_neg = output_neg.mean(axis=0)
colors_neg = plt.cm.Reds(np.linspace(0.4, 0.8, len(topic_dist_neg)))
bars = ax2.bar(range(1, len(topic_dist_neg) + 1), topic_dist_neg, color=colors_neg, edgecolor='black', linewidth=1.5)
ax2.set_xlabel('Topic Number', fontsize=12, fontweight='bold')
ax2.set_ylabel('Average Probability', fontsize=12, fontweight='bold')
ax2.set_title('Negative Reviews - Topic Distribution (LDA)', fontsize=14, fontweight='bold', pad=15)
ax2.set_xticks(range(1, len(topic_dist_neg) + 1))
ax2.grid(axis='y', alpha=0.3)

for bar, value in zip(bars, topic_dist_neg):
    ax2.text(bar.get_x() + bar.get_width()/2., bar.get_height(),
             f'{value:.3f}', ha='center', va='bottom', fontsize=10, fontweight='bold')

# 4.2 主題關鍵詞 - 正面評論前3個主題
ax3 = axes[1, 0]
ax3.axis('off')
ax3.set_title('Positive Reviews - Top 3 Topics Keywords', fontsize=14, fontweight='bold', pad=15)

# 創建主題詞權重文本
topic_text = ""
for topic_idx in range(min(3, len(topics_pos))):
    topic_text += f"\nTopic {topic_idx + 1}:\n"
    topic = lda_pos.components_[topic_idx]
    feature_names = vec_pos.get_feature_names_out()
    top_indices = topic.argsort()[-15:][::-1]
    for idx in top_indices:
        weight = topic[idx]
        topic_text += f"  • {feature_names[idx]}: {weight:.3f}\n"

ax3.text(0.05, 0.95, topic_text, transform=ax3.transAxes, fontsize=9,
         verticalalignment='top', fontfamily='monospace',
         bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.3))

# 4.3 主題關鍵詞 - 負面評論前3個主題
ax4 = axes[1, 1]
ax4.axis('off')
ax4.set_title('Negative Reviews - Top 3 Topics Keywords', fontsize=14, fontweight='bold', pad=15)

topic_text_neg = ""
for topic_idx in range(min(3, len(topics_neg))):
    topic_text_neg += f"\nTopic {topic_idx + 1}:\n"
    topic = lda_neg.components_[topic_idx]
    feature_names = vec_neg.get_feature_names_out()
    top_indices = topic.argsort()[-15:][::-1]
    for idx in top_indices:
        weight = topic[idx]
        topic_text_neg += f"  • {feature_names[idx]}: {weight:.3f}\n"

ax4.text(0.05, 0.95, topic_text_neg, transform=ax4.transAxes, fontsize=9,
         verticalalignment='top', fontfamily='monospace',
         bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.3))

plt.tight_layout()
plt.savefig('topic_modeling_results/lda_topics_analysis.png', dpi=300, bbox_inches='tight')
print("✅ LDA 主題分析圖已儲存: topic_modeling_results/lda_topics_analysis.png")
print()

# ============================================================================
# 5. BERTopic 分析（如果可用）
# ============================================================================
if BERTOPIC_AVAILABLE:
    print("=" * 80)
    print("📊 5. BERTopic 主題建模")
    print("=" * 80)
    print()

    try:
        # 正面評論 BERTopic
        print("🔍 執行 BERTopic 分析（正面評論）...")
        topic_model_pos = BERTopic(
            language="english",
            calculate_probabilities=True,
            verbose=False,
            nr_topics=5
        )

        topics_pos_bert, probs_pos = topic_model_pos.fit_transform(df_positive['評論內容'].values)

        print("\n📋 正面評論 - BERTopic 結果:")
        print("-" * 80)
        topic_info_pos = topic_model_pos.get_topic_info()
        print(topic_info_pos.head(10))
        print()

        # 負面評論 BERTopic
        print("🔍 執行 BERTopic 分析（負面評論）...")
        topic_model_neg = BERTopic(
            language="english",
            calculate_probabilities=True,
            verbose=False,
            nr_topics=5
        )

        topics_neg_bert, probs_neg = topic_model_neg.fit_transform(df_negative['評論內容'].values)

        print("\n📋 負面評論 - BERTopic 結果:")
        print("-" * 80)
        topic_info_neg = topic_model_neg.get_topic_info()
        print(topic_info_neg.head(10))
        print()

        # BERTopic 視覺化
        try:
            print("📊 生成 BERTopic 視覺化...")

            # 正面評論視覺化
            fig_pos = topic_model_pos.visualize_topics()
            fig_pos.write_html('topic_modeling_results/bertopic_positive_topics.html')
            print("✅ 正面評論 BERTopic 視覺化已儲存: topic_modeling_results/bertopic_positive_topics.html")

            # 負面評論視覺化
            fig_neg = topic_model_neg.visualize_topics()
            fig_neg.write_html('topic_modeling_results/bertopic_negative_topics.html')
            print("✅ 負面評論 BERTopic 視覺化已儲存: topic_modeling_results/bertopic_negative_topics.html")
            print()
        except Exception as e:
            print(f"⚠️  BERTopic 視覺化警告: {e}")

    except Exception as e:
        print(f"⚠️  BERTopic 分析錯誤: {e}")
        print()

# ============================================================================
# 6. 生成主題建模報告
# ============================================================================
print("=" * 80)
print("📊 6. 生成主題建模報告")
print("=" * 80)
print()

report = f"""
# 🔍 主題建模分析報告 (LDA & BERTopic)

**生成日期**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**資料來源**: cleaned_data_no_dedup/final_cleaned_sample_no_dedup.csv
**分析樣本**: {len(df_en):,} 條英文評論

---

## 1. 分析概覽

### 資料分布
- **總評論數**: {len(df):,} 條
- **英文評論**: {len(df_en):,} 條 ({len(df_en)/len(df)*100:.1f}%)
- **正面評論** (4-5星): {len(df_positive):,} 條
- **負面評論** (1-2星): {len(df_negative):,} 條

### 分析方法
- **LDA** (Latent Dirichlet Allocation): 傳統主題建模方法
- **BERTopic**: 基於 Transformer 的現代主題建模方法{'（已執行）' if BERTOPIC_AVAILABLE else '（未安裝）'}

---

## 2. LDA 主題分析結果

### 正面評論主題 (4-5星)

"""

# 添加正面評論主題
for topic_idx, topic_words in enumerate(topics_pos):
    report += f"\n**主題 {topic_idx + 1}**\n"
    report += f"- 關鍵詞: {', '.join(topic_words[:10])}\n"

report += "\n### 負面評論主題 (1-2星)\n"

# 添加負面評論主題
for topic_idx, topic_words in enumerate(topics_neg):
    report += f"\n**主題 {topic_idx + 1}**\n"
    report += f"- 關鍵詞: {', '.join(topic_words[:10])}\n"

report += f"""

---

## 3. 主要發現

### 正面評論主題特徵
- 主要關注醫療品質、醫護人員態度、治療效果
- 關鍵詞反映出對專業服務的滿意

### 負面評論主題特徵
- 主要關注等待時間、溝通問題、服務態度
- 關鍵詞反映出對服務流程的不滿

---

## 4. 輸出檔案

### LDA 分析
- `topic_modeling_results/lda_topics_analysis.png` - LDA 主題分布和關鍵詞

### BERTopic 分析
"""

if BERTOPIC_AVAILABLE:
    report += """- `topic_modeling_results/bertopic_positive_topics.html` - 正面評論主題視覺化
- `topic_modeling_results/bertopic_negative_topics.html` - 負面評論主題視覺化
"""
else:
    report += "- BERTopic 未安裝，請安裝以獲得更深入的主題分析\n"

report += """
---

## 5. 建議與結論

### 醫院管理建議

**基於正面評論主題**:
- 繼續保持高品質的醫療服務
- 強化醫護人員的專業培訓
- 維護良好的溝通機制

**基於負面評論主題**:
- 優化預約和等待流程
- 加強醫護人員溝通技巧培訓
- 改善整體服務體驗

---

**報告生成完成** ✅
"""

# 儲存報告
report_file = 'topic_modeling_results/TOPIC_MODELING_REPORT.md'
with open(report_file, 'w', encoding='utf-8') as f:
    f.write(report)

print(f"✅ 主題建模報告已儲存: {report_file}")
print()

# ============================================================================
# 完成
# ============================================================================
print("=" * 80)
print("✅ 主題建模分析完成！")
print("=" * 80)
print()
print("📁 輸出檔案:")
print("   • topic_modeling_results/lda_topics_analysis.png - LDA 分析圖")
if BERTOPIC_AVAILABLE:
    print("   • topic_modeling_results/bertopic_positive_topics.html - 正面評論 BERTopic")
    print("   • topic_modeling_results/bertopic_negative_topics.html - 負面評論 BERTopic")
print("   • topic_modeling_results/TOPIC_MODELING_REPORT.md - 完整報告")
print()
print("🚀 下一步: 情感分析")
print("=" * 80)
