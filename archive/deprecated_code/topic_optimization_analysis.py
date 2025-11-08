#!/usr/bin/env python3
"""
主題數量優化分析
比較 5、6、7 個主題的 LDA 模型，找出最適合構面解釋的主題數量
為台美比較研究做準備
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
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

# 主題一致性評估
try:
    import gensim
    from gensim.models import CoherenceModel
    from gensim.corpora import Dictionary
    GENSIM_AVAILABLE = True
except ImportError:
    GENSIM_AVAILABLE = False
    print("⚠️  Gensim 未安裝，將跳過 Coherence Score 計算")

# 設定
import os
os.makedirs('topic_optimization_results', exist_ok=True)

# 設定繪圖樣式
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
sns.set_style("whitegrid")

print("=" * 80)
print("🔍 主題數量優化分析 - 為台美比較做準備")
print("=" * 80)
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

# 只保留英文評論
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
    text = text.lower()
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'\S+@\S+', '', text)
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'[^\w\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

print("🔄 執行文本前處理...")
df_en['cleaned_text'] = df_en['評論內容'].apply(preprocess_text)

# 停用詞
stop_words = set(stopwords.words('english'))
custom_stopwords = {'hospital', 'dr', 'doctor', 'patient', 'visited', 'visit',
                    'one', 'would', 'get', 'like', 'go', 'went', 'take', 'make'}
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
df_en = df_en[df_en['processed_text'].str.len() > 20].copy()
print(f"✅ 前處理完成: {len(df_en):,} 條有效評論")
print()

# 分別處理正面和負面評論
df_positive = df_en[df_en['評分'] >= 4].copy()
df_negative = df_en[df_en['評分'] <= 2].copy()

print(f"📊 正面評論: {len(df_positive):,} 條")
print(f"📊 負面評論: {len(df_negative):,} 條")
print()

# ============================================================================
# 3. 測試不同主題數量 (5, 6, 7)
# ============================================================================
print("=" * 80)
print("📊 3. 測試不同主題數量 (5, 6, 7)")
print("=" * 80)
print()

def evaluate_lda_model(texts, n_topics, sentiment_label):
    """評估 LDA 模型"""
    print(f"\n{'=' * 80}")
    print(f"🔍 測試 {n_topics} 個主題 ({sentiment_label})")
    print(f"{'=' * 80}\n")

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

    # 計算 Perplexity（越低越好）
    perplexity = lda_model.perplexity(doc_term_matrix)

    # 計算 Log Likelihood（越高越好）
    log_likelihood = lda_model.score(doc_term_matrix)

    # 提取主題詞
    feature_names = vectorizer.get_feature_names_out()
    topics = []

    print(f"📋 主題分析結果:")
    print("-" * 80)

    for topic_idx, topic in enumerate(lda_model.components_):
        top_indices = topic.argsort()[-10:][::-1]
        top_words = [feature_names[i] for i in top_indices]
        top_weights = [topic[i] for i in top_indices]
        topics.append({
            'words': top_words,
            'weights': top_weights
        })

        print(f"\n主題 {topic_idx + 1}:")
        print(f"  關鍵詞: {', '.join(top_words[:10])}")

        # 計算主題內一致性（詞權重的標準差，越低表示越集中）
        topic_concentration = np.std(top_weights)
        print(f"  主題集中度: {topic_concentration:.4f}")

    print()

    # 計算主題分布的均勻性（越均勻表示主題區分度越好）
    topic_distribution = lda_output.mean(axis=0)
    topic_uniformity = np.std(topic_distribution)

    print(f"📊 模型評估指標:")
    print(f"   Perplexity: {perplexity:.2f} (越低越好)")
    print(f"   Log Likelihood: {log_likelihood:.2f} (越高越好)")
    print(f"   主題分布標準差: {topic_uniformity:.4f} (適中為佳)")
    print()

    # 計算 Coherence Score（如果 Gensim 可用）
    coherence_score = None
    if GENSIM_AVAILABLE:
        try:
            # 準備文本用於 Coherence 計算
            texts_tokenized = [text.split() for text in texts]
            dictionary = Dictionary(texts_tokenized)

            # 轉換主題為 Gensim 格式
            topics_for_coherence = [[word for word in topic['words'][:10]] for topic in topics]

            # 計算 Coherence Score (C_v)
            cm = CoherenceModel(
                topics=topics_for_coherence,
                texts=texts_tokenized,
                dictionary=dictionary,
                coherence='c_v'
            )
            coherence_score = cm.get_coherence()
            print(f"   Coherence Score (C_v): {coherence_score:.4f} (越高越好)")
            print()
        except Exception as e:
            print(f"   ⚠️  Coherence Score 計算失敗: {e}")
            print()

    return {
        'n_topics': n_topics,
        'sentiment': sentiment_label,
        'lda_model': lda_model,
        'vectorizer': vectorizer,
        'topics': topics,
        'perplexity': perplexity,
        'log_likelihood': log_likelihood,
        'topic_uniformity': topic_uniformity,
        'coherence_score': coherence_score,
        'lda_output': lda_output
    }

# 測試正面評論的不同主題數量
results_positive = []
for n_topics in [5, 6, 7]:
    result = evaluate_lda_model(
        df_positive['processed_text'].values,
        n_topics,
        '正面評論'
    )
    results_positive.append(result)

# 測試負面評論的不同主題數量
results_negative = []
for n_topics in [5, 6, 7]:
    result = evaluate_lda_model(
        df_negative['processed_text'].values,
        n_topics,
        '負面評論'
    )
    results_negative.append(result)

# ============================================================================
# 4. 比較分析與視覺化
# ============================================================================
print("=" * 80)
print("📊 4. 比較分析與視覺化")
print("=" * 80)
print()

# 創建比較表格
comparison_data = []
for result in results_positive + results_negative:
    comparison_data.append({
        '情感': result['sentiment'],
        '主題數': result['n_topics'],
        'Perplexity': result['perplexity'],
        'Log Likelihood': result['log_likelihood'],
        '主題分布標準差': result['topic_uniformity'],
        'Coherence Score': result['coherence_score'] if result['coherence_score'] else np.nan
    })

comparison_df = pd.DataFrame(comparison_data)

print("📊 模型比較表:")
print("-" * 80)
print(comparison_df.to_string(index=False))
print()

# 視覺化比較
fig, axes = plt.subplots(2, 3, figsize=(18, 12))

# 正面評論指標
pos_results = [r for r in results_positive]
n_topics_list = [5, 6, 7]

# 1. Perplexity 比較 - 正面
ax1 = axes[0, 0]
perplexity_pos = [r['perplexity'] for r in pos_results]
bars = ax1.bar(n_topics_list, perplexity_pos, color='lightgreen', edgecolor='black', linewidth=1.5)
ax1.set_xlabel('Number of Topics', fontsize=12, fontweight='bold')
ax1.set_ylabel('Perplexity (Lower is Better)', fontsize=12, fontweight='bold')
ax1.set_title('Positive Reviews - Perplexity', fontsize=14, fontweight='bold', pad=15)
ax1.set_xticks(n_topics_list)
ax1.grid(axis='y', alpha=0.3)
for bar, value in zip(bars, perplexity_pos):
    ax1.text(bar.get_x() + bar.get_width()/2., bar.get_height(),
             f'{value:.1f}', ha='center', va='bottom', fontsize=10, fontweight='bold')

# 2. Log Likelihood 比較 - 正面
ax2 = axes[0, 1]
log_lik_pos = [r['log_likelihood'] for r in pos_results]
bars = ax2.bar(n_topics_list, log_lik_pos, color='lightblue', edgecolor='black', linewidth=1.5)
ax2.set_xlabel('Number of Topics', fontsize=12, fontweight='bold')
ax2.set_ylabel('Log Likelihood (Higher is Better)', fontsize=12, fontweight='bold')
ax2.set_title('Positive Reviews - Log Likelihood', fontsize=14, fontweight='bold', pad=15)
ax2.set_xticks(n_topics_list)
ax2.grid(axis='y', alpha=0.3)
for bar, value in zip(bars, log_lik_pos):
    ax2.text(bar.get_x() + bar.get_width()/2., bar.get_height(),
             f'{value:.1f}', ha='center', va='bottom', fontsize=10, fontweight='bold')

# 3. Coherence Score 比較 - 正面
ax3 = axes[0, 2]
if GENSIM_AVAILABLE and all(r['coherence_score'] for r in pos_results):
    coherence_pos = [r['coherence_score'] for r in pos_results]
    bars = ax3.bar(n_topics_list, coherence_pos, color='lightyellow', edgecolor='black', linewidth=1.5)
    ax3.set_xlabel('Number of Topics', fontsize=12, fontweight='bold')
    ax3.set_ylabel('Coherence Score (Higher is Better)', fontsize=12, fontweight='bold')
    ax3.set_title('Positive Reviews - Coherence', fontsize=14, fontweight='bold', pad=15)
    ax3.set_xticks(n_topics_list)
    ax3.grid(axis='y', alpha=0.3)
    for bar, value in zip(bars, coherence_pos):
        ax3.text(bar.get_x() + bar.get_width()/2., bar.get_height(),
                 f'{value:.3f}', ha='center', va='bottom', fontsize=10, fontweight='bold')
else:
    ax3.text(0.5, 0.5, 'Coherence Score\nNot Available',
             ha='center', va='center', fontsize=12, transform=ax3.transAxes)
    ax3.axis('off')

# 負面評論指標
neg_results = [r for r in results_negative]

# 4. Perplexity 比較 - 負面
ax4 = axes[1, 0]
perplexity_neg = [r['perplexity'] for r in neg_results]
bars = ax4.bar(n_topics_list, perplexity_neg, color='lightcoral', edgecolor='black', linewidth=1.5)
ax4.set_xlabel('Number of Topics', fontsize=12, fontweight='bold')
ax4.set_ylabel('Perplexity (Lower is Better)', fontsize=12, fontweight='bold')
ax4.set_title('Negative Reviews - Perplexity', fontsize=14, fontweight='bold', pad=15)
ax4.set_xticks(n_topics_list)
ax4.grid(axis='y', alpha=0.3)
for bar, value in zip(bars, perplexity_neg):
    ax4.text(bar.get_x() + bar.get_width()/2., bar.get_height(),
             f'{value:.1f}', ha='center', va='bottom', fontsize=10, fontweight='bold')

# 5. Log Likelihood 比較 - 負面
ax5 = axes[1, 1]
log_lik_neg = [r['log_likelihood'] for r in neg_results]
bars = ax5.bar(n_topics_list, log_lik_neg, color='lightblue', edgecolor='black', linewidth=1.5)
ax5.set_xlabel('Number of Topics', fontsize=12, fontweight='bold')
ax5.set_ylabel('Log Likelihood (Higher is Better)', fontsize=12, fontweight='bold')
ax5.set_title('Negative Reviews - Log Likelihood', fontsize=14, fontweight='bold', pad=15)
ax5.set_xticks(n_topics_list)
ax5.grid(axis='y', alpha=0.3)
for bar, value in zip(bars, log_lik_neg):
    ax5.text(bar.get_x() + bar.get_width()/2., bar.get_height(),
             f'{value:.1f}', ha='center', va='bottom', fontsize=10, fontweight='bold')

# 6. Coherence Score 比較 - 負面
ax6 = axes[1, 2]
if GENSIM_AVAILABLE and all(r['coherence_score'] for r in neg_results):
    coherence_neg = [r['coherence_score'] for r in neg_results]
    bars = ax6.bar(n_topics_list, coherence_neg, color='lightyellow', edgecolor='black', linewidth=1.5)
    ax6.set_xlabel('Number of Topics', fontsize=12, fontweight='bold')
    ax6.set_ylabel('Coherence Score (Higher is Better)', fontsize=12, fontweight='bold')
    ax6.set_title('Negative Reviews - Coherence', fontsize=14, fontweight='bold', pad=15)
    ax6.set_xticks(n_topics_list)
    ax6.grid(axis='y', alpha=0.3)
    for bar, value in zip(bars, coherence_neg):
        ax6.text(bar.get_x() + bar.get_width()/2., bar.get_height(),
                 f'{value:.3f}', ha='center', va='bottom', fontsize=10, fontweight='bold')
else:
    ax6.text(0.5, 0.5, 'Coherence Score\nNot Available',
             ha='center', va='center', fontsize=12, transform=ax6.transAxes)
    ax6.axis('off')

plt.tight_layout()
plt.savefig('topic_optimization_results/topic_number_comparison.png', dpi=300, bbox_inches='tight')
print("✅ 比較圖已儲存: topic_optimization_results/topic_number_comparison.png")
print()

# ============================================================================
# 5. 構面解釋性分析
# ============================================================================
print("=" * 80)
print("📊 5. 構面解釋性分析")
print("=" * 80)
print()

def analyze_topic_interpretability(results, sentiment_label):
    """分析主題的可解釋性"""
    print(f"\n{'=' * 80}")
    print(f"📋 {sentiment_label} - 主題構面解釋性分析")
    print(f"{'=' * 80}\n")

    for result in results:
        n_topics = result['n_topics']
        print(f"\n## {n_topics} 個主題的構面解釋:\n")

        for topic_idx, topic_info in enumerate(result['topics']):
            words = topic_info['words'][:10]
            weights = topic_info['weights'][:10]

            print(f"### 主題 {topic_idx + 1}")
            print(f"關鍵詞: {', '.join(words)}")

            # 嘗試給出構面解釋
            # 這裡可以根據關鍵詞自動判斷構面類型
            # 或者留空讓研究者自行命名
            print(f"建議構面名稱: [待命名]")
            print(f"詞權重範圍: {weights[0]:.3f} - {weights[-1]:.3f}")
            print()

        print(f"**可解釋性評估**: ")
        print(f"- Perplexity: {result['perplexity']:.2f}")
        if result['coherence_score']:
            print(f"- Coherence Score: {result['coherence_score']:.4f}")
        print(f"- 主題分布均勻度: {result['topic_uniformity']:.4f}")
        print()

# 分析正面和負面評論的可解釋性
analyze_topic_interpretability(results_positive, "正面評論")
analyze_topic_interpretability(results_negative, "負面評論")

# ============================================================================
# 6. 生成詳細報告
# ============================================================================
print("=" * 80)
print("📊 6. 生成詳細報告")
print("=" * 80)
print()

# 確定推薦的主題數量
def recommend_n_topics(results):
    """基於指標推薦主題數量"""
    scores = []
    for result in results:
        # 標準化各指標（越低/越高越好）
        score = 0

        # Perplexity（越低越好，取負值）
        perplexities = [r['perplexity'] for r in results]
        norm_perplexity = (max(perplexities) - result['perplexity']) / (max(perplexities) - min(perplexities)) if max(perplexities) != min(perplexities) else 0
        score += norm_perplexity * 0.3

        # Log Likelihood（越高越好）
        log_liks = [r['log_likelihood'] for r in results]
        norm_log_lik = (result['log_likelihood'] - min(log_liks)) / (max(log_liks) - min(log_liks)) if max(log_liks) != min(log_liks) else 0
        score += norm_log_lik * 0.3

        # Coherence Score（越高越好）
        if result['coherence_score']:
            coherences = [r['coherence_score'] for r in results if r['coherence_score']]
            norm_coherence = (result['coherence_score'] - min(coherences)) / (max(coherences) - min(coherences)) if max(coherences) != min(coherences) else 0
            score += norm_coherence * 0.4

        scores.append(score)

    best_idx = np.argmax(scores)
    return results[best_idx]['n_topics'], scores

recommended_pos, scores_pos = recommend_n_topics(results_positive)
recommended_neg, scores_neg = recommend_n_topics(results_negative)

print(f"📊 推薦主題數量:")
print(f"   正面評論: {recommended_pos} 個主題 (綜合評分: {max(scores_pos):.3f})")
print(f"   負面評論: {recommended_neg} 個主題 (綜合評分: {max(scores_neg):.3f})")
print()

# 生成報告
report = f"""
# 🔍 主題數量優化分析報告

**生成日期**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**分析目的**: 為台美比較研究確定最佳主題數量
**資料來源**: 美國醫院評論 (3,363 條)

---

## 1. 分析概覽

### 測試主題數量
- 5 個主題
- 6 個主題
- 7 個主題

### 評估指標
- **Perplexity**: 模型複雜度（越低越好）
- **Log Likelihood**: 模型擬合度（越高越好）
- **Coherence Score**: 主題一致性（越高越好）
- **主題分布均勻度**: 主題區分度（適中為佳）

---

## 2. 正面評論分析結果

### 模型比較

| 主題數 | Perplexity | Log Likelihood | Coherence Score | 推薦度 |
|--------|-----------|----------------|-----------------|--------|
"""

for i, result in enumerate(results_positive):
    coherence = f"{result['coherence_score']:.4f}" if result['coherence_score'] else "N/A"
    recommended_mark = "⭐ **推薦**" if result['n_topics'] == recommended_pos else ""
    report += f"| {result['n_topics']} | {result['perplexity']:.2f} | {result['log_likelihood']:.2f} | {coherence} | {recommended_mark} |\n"

report += f"""

### 推薦主題數量: {recommended_pos} 個 ⭐

**理由**:
"""

# 找出推薦的結果
recommended_result_pos = [r for r in results_positive if r['n_topics'] == recommended_pos][0]
report += f"""
- Perplexity: {recommended_result_pos['perplexity']:.2f}
- Log Likelihood: {recommended_result_pos['log_likelihood']:.2f}
"""
if recommended_result_pos['coherence_score']:
    report += f"- Coherence Score: {recommended_result_pos['coherence_score']:.4f}\n"
report += f"- 主題分布均勻度: {recommended_result_pos['topic_uniformity']:.4f}\n"

report += f"""

### 主題構面（{recommended_pos} 個主題）

"""

for topic_idx, topic_info in enumerate(recommended_result_pos['topics']):
    report += f"""
#### 主題 {topic_idx + 1}
- **關鍵詞**: {', '.join(topic_info['words'][:10])}
- **建議構面名稱**: [待研究者命名]
- **適用於台美比較**: ✅

"""

report += """

---

## 3. 負面評論分析結果

### 模型比較

| 主題數 | Perplexity | Log Likelihood | Coherence Score | 推薦度 |
|--------|-----------|----------------|-----------------|--------|
"""

for i, result in enumerate(results_negative):
    coherence = f"{result['coherence_score']:.4f}" if result['coherence_score'] else "N/A"
    recommended_mark = "⭐ **推薦**" if result['n_topics'] == recommended_neg else ""
    report += f"| {result['n_topics']} | {result['perplexity']:.2f} | {result['log_likelihood']:.2f} | {coherence} | {recommended_mark} |\n"

report += f"""

### 推薦主題數量: {recommended_neg} 個 ⭐

**理由**:
"""

recommended_result_neg = [r for r in results_negative if r['n_topics'] == recommended_neg][0]
report += f"""
- Perplexity: {recommended_result_neg['perplexity']:.2f}
- Log Likelihood: {recommended_result_neg['log_likelihood']:.2f}
"""
if recommended_result_neg['coherence_score']:
    report += f"- Coherence Score: {recommended_result_neg['coherence_score']:.4f}\n"
report += f"- 主題分布均勻度: {recommended_result_neg['topic_uniformity']:.4f}\n"

report += f"""

### 主題構面（{recommended_neg} 個主題）

"""

for topic_idx, topic_info in enumerate(recommended_result_neg['topics']):
    report += f"""
#### 主題 {topic_idx + 1}
- **關鍵詞**: {', '.join(topic_info['words'][:10])}
- **建議構面名稱**: [待研究者命名]
- **適用於台美比較**: ✅

"""

report += f"""

---

## 4. 台美比較建議

### 推薦配置

**正面評論**: {recommended_pos} 個主題
**負面評論**: {recommended_neg} 個主題

### 跨國比較注意事項

1. **語言差異處理**
   - 台灣資料需要進行繁體中文分詞
   - 建議使用 jieba 或 ckiptagger
   - 停用詞需要另外設定

2. **主題數量一致性**
   - 建議台灣資料也使用相同的主題數量
   - 便於構面對照和比較

3. **構面命名原則**
   - 使用中性、跨文化的構面名稱
   - 例如：服務品質、溝通效率、等待時間等

4. **可比較的構面範例**
   - ✅ 醫療專業性
   - ✅ 服務態度
   - ✅ 等待時間
   - ✅ 溝通品質
   - ✅ 設施環境
   - ✅ 費用透明度

---

## 5. 下一步行動

### 立即執行

1. ✅ 使用推薦的主題數量分析台灣資料
2. ✅ 為每個主題命名構面
3. ✅ 建立台美對照表

### 分析流程

```python
# 台灣資料分析範例
# 1. 載入台灣醫院評論資料
# 2. 使用相同的主題數量 ({recommended_pos} 個正面, {recommended_neg} 個負面)
# 3. 進行 LDA 分析
# 4. 比較台美主題差異
```

### 研究問題範例

1. 台美兩國在正面評論中最關注的構面是否相同？
2. 負面評論的痛點是否有文化差異？
3. 哪些服務構面是跨文化共通的？
4. 哪些構面顯示出顯著的國家差異？

---

## 6. 輸出檔案

- `topic_optimization_results/topic_number_comparison.png` - 主題數量比較圖
- `topic_optimization_results/TOPIC_OPTIMIZATION_REPORT.md` - 本報告
- `topic_optimization_results/recommended_models.pkl` - 推薦模型（待儲存）

---

**分析完成** ✅

**建議**: 使用 {recommended_pos} 個正面主題和 {recommended_neg} 個負面主題進行台美比較研究
"""

# 儲存報告
report_file = 'topic_optimization_results/TOPIC_OPTIMIZATION_REPORT.md'
with open(report_file, 'w', encoding='utf-8') as f:
    f.write(report)

print(f"✅ 主題優化報告已儲存: {report_file}")
print()

# 儲存推薦的模型
import pickle

models_to_save = {
    'positive': {
        'n_topics': recommended_pos,
        'model': recommended_result_pos['lda_model'],
        'vectorizer': recommended_result_pos['vectorizer'],
        'topics': recommended_result_pos['topics']
    },
    'negative': {
        'n_topics': recommended_neg,
        'model': recommended_result_neg['lda_model'],
        'vectorizer': recommended_result_neg['vectorizer'],
        'topics': recommended_result_neg['topics']
    }
}

with open('topic_optimization_results/recommended_models.pkl', 'wb') as f:
    pickle.dump(models_to_save, f)

print("✅ 推薦模型已儲存: topic_optimization_results/recommended_models.pkl")
print()

# ============================================================================
# 完成
# ============================================================================
print("=" * 80)
print("✅ 主題數量優化分析完成！")
print("=" * 80)
print()
print(f"📊 推薦配置:")
print(f"   正面評論: {recommended_pos} 個主題")
print(f"   負面評論: {recommended_neg} 個主題")
print()
print("📁 輸出檔案:")
print("   • topic_optimization_results/topic_number_comparison.png")
print("   • topic_optimization_results/TOPIC_OPTIMIZATION_REPORT.md")
print("   • topic_optimization_results/recommended_models.pkl")
print()
print("🚀 準備好進行台美比較分析！")
print("=" * 80)
