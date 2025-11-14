#!/usr/bin/env python3
"""
台美醫院評論比較分析 - HTML 報告生成器
Taiwan-USA Hospital Review Comparison - HTML Report Generator

自動生成包含所有分析結果的靜態 HTML 報告
"""

import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import base64
from io import BytesIO
from datetime import datetime
import sys

# 添加配置路徑
sys.path.append(str(Path(__file__).parent.parent / "streamlit_app"))
from comparison_config import *

# 設定中文字體（macOS）
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'Arial', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

print("=" * 80)
print("🌏 台美醫院評論比較分析 - HTML 報告生成器")
print("=" * 80)
print()

# ============================================
# 輔助函數
# ============================================

def fig_to_base64(fig):
    """將 matplotlib 圖表轉換為 base64 字串"""
    buf = BytesIO()
    fig.savefig(buf, format='png', dpi=150, bbox_inches='tight')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')
    plt.close(fig)
    return img_base64

def create_html_header():
    """生成 HTML 頭部"""
    return """
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>台美醫院評論跨文化比較分析報告</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Arial', 'Microsoft JhengHei', sans-serif;
            line-height: 1.6;
            color: #333;
            background-color: #f5f5f5;
            padding: 20px;
        }

        .container {
            max-width: 1400px;
            margin: 0 auto;
            background: white;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }

        h1 {
            color: #2c3e50;
            text-align: center;
            padding-bottom: 20px;
            border-bottom: 3px solid #3498db;
            margin-bottom: 30px;
        }

        h2 {
            color: #34495e;
            margin-top: 40px;
            margin-bottom: 20px;
            padding-left: 15px;
            border-left: 5px solid #3498db;
        }

        h3 {
            color: #555;
            margin-top: 25px;
            margin-bottom: 15px;
        }

        .meta-info {
            text-align: center;
            color: #7f8c8d;
            margin-bottom: 30px;
            padding: 15px;
            background: #ecf0f1;
            border-radius: 5px;
        }

        .section {
            margin-bottom: 50px;
        }

        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin: 30px 0;
        }

        .stat-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 25px;
            border-radius: 10px;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }

        .stat-card h3 {
            color: white;
            font-size: 1.1em;
            margin-bottom: 10px;
        }

        .stat-value {
            font-size: 2.5em;
            font-weight: bold;
            margin: 10px 0;
        }

        .stat-label {
            font-size: 0.9em;
            opacity: 0.9;
        }

        .chart-container {
            margin: 30px 0;
            text-align: center;
        }

        .chart-container img {
            max-width: 100%;
            height: auto;
            border-radius: 5px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            background: white;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        th {
            background: #3498db;
            color: white;
            padding: 12px;
            text-align: left;
        }

        td {
            padding: 10px 12px;
            border-bottom: 1px solid #ecf0f1;
        }

        tr:hover {
            background: #f8f9fa;
        }

        .taiwan { color: #1f77b4; font-weight: bold; }
        .usa { color: #d62728; font-weight: bold; }
        .positive { color: #2ecc71; }
        .negative { color: #e74c3c; }
        .neutral { color: #f39c12; }

        .info-box {
            background: #e8f4f8;
            border-left: 4px solid #3498db;
            padding: 15px;
            margin: 20px 0;
            border-radius: 5px;
        }

        .warning-box {
            background: #fff3cd;
            border-left: 4px solid #f39c12;
            padding: 15px;
            margin: 20px 0;
            border-radius: 5px;
        }

        .success-box {
            background: #d4edda;
            border-left: 4px solid #2ecc71;
            padding: 15px;
            margin: 20px 0;
            border-radius: 5px;
        }

        .topic-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin: 20px 0;
        }

        .topic-card {
            border: 2px solid #ecf0f1;
            border-radius: 8px;
            padding: 20px;
            background: white;
        }

        .topic-card h4 {
            margin-bottom: 10px;
            color: #2c3e50;
        }

        .keywords {
            color: #7f8c8d;
            font-size: 0.9em;
            margin-top: 10px;
        }

        .footer {
            text-align: center;
            color: #7f8c8d;
            margin-top: 50px;
            padding-top: 20px;
            border-top: 1px solid #ecf0f1;
        }

        @media print {
            body { background: white; }
            .container { box-shadow: none; }
        }
    </style>
</head>
<body>
    <div class="container">
"""

def create_html_footer():
    """生成 HTML 尾部"""
    return """
        <div class="footer">
            <p>📊 報告生成時間：{datetime}</p>
            <p>🌏 台美醫院評論跨文化比較分析系統</p>
            <p>Taiwan-USA Hospital Review Cross-Cultural Comparison System</p>
            <p style="margin-top: 10px; font-size: 0.9em;">
                本報告使用 Gensim LDA 主題模型分析<br>
                台灣資料：5,007 則評論 | 美國資料：3,240 則評論
            </p>
        </div>
    </div>
</body>
</html>
""".format(datetime=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# ============================================
# 載入資料
# ============================================

print("📂 載入 LDA 模型...")

# 台灣模型
with open(TAIWAN_MODEL_PATH, 'rb') as f:
    taiwan_data = pickle.load(f)
    taiwan_model = taiwan_data['lda_model']

print("  ✅ 台灣 K=7 模型")

# 美國模型
with open(USA_MODEL_PATH, 'rb') as f:
    usa_data = pickle.load(f)
    usa_model = usa_data['lda_model']

print("  ✅ 美國 K=6 模型")

# 美國評論資料
usa_df = pd.read_csv(USA_DATA_PATH)
print("  ✅ 美國評論資料")

print()

# ============================================
# 生成圖表
# ============================================

print("📊 生成分析圖表...")

charts = {}

# 1. 模型品質比較
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

countries = ['Taiwan\nK=7', 'USA\nK=6']
coherence = [DATASET_INFO['taiwan']['coherence'], DATASET_INFO['usa']['coherence']]
colors = [COLORS['taiwan']['primary'], COLORS['usa']['primary']]

ax1.bar(countries, coherence, color=colors, alpha=0.7, edgecolor='black', linewidth=1.5)
ax1.set_ylabel('Coherence Score', fontsize=12, fontweight='bold')
ax1.set_title('Model Coherence Comparison', fontsize=14, fontweight='bold')
ax1.set_ylim([0, 0.45])
ax1.grid(axis='y', alpha=0.3)

for i, v in enumerate(coherence):
    ax1.text(i, v + 0.01, f'{v:.4f}', ha='center', fontweight='bold', fontsize=11)

perplexity = [abs(DATASET_INFO['taiwan']['perplexity']), abs(DATASET_INFO['usa']['perplexity'])]
ax2.bar(countries, perplexity, color=colors, alpha=0.7, edgecolor='black', linewidth=1.5)
ax2.set_ylabel('Perplexity (Absolute)', fontsize=12, fontweight='bold')
ax2.set_title('Model Perplexity Comparison', fontsize=14, fontweight='bold')
ax2.grid(axis='y', alpha=0.3)

for i, v in enumerate(perplexity):
    ax2.text(i, v + 0.1, f'{v:.2f}', ha='center', fontweight='bold', fontsize=11)

plt.tight_layout()
charts['model_quality'] = fig_to_base64(fig)
print("  ✅ 模型品質比較圖")

# 2. 資料集規模比較
fig, ax = plt.subplots(figsize=(10, 5))

countries = ['Taiwan', 'USA']
reviews = [DATASET_INFO['taiwan']['reviews'], DATASET_INFO['usa']['reviews']]
colors = [COLORS['taiwan']['primary'], COLORS['usa']['primary']]

bars = ax.barh(countries, reviews, color=colors, alpha=0.7, edgecolor='black', linewidth=1.5)
ax.set_xlabel('Number of Reviews', fontsize=12, fontweight='bold')
ax.set_title('Dataset Size Comparison', fontsize=14, fontweight='bold')
ax.grid(axis='x', alpha=0.3)

for i, (bar, v) in enumerate(zip(bars, reviews)):
    ax.text(v + 50, i, f'{v:,}', va='center', fontweight='bold', fontsize=11)

plt.tight_layout()
charts['dataset_size'] = fig_to_base64(fig)
print("  ✅ 資料集規模圖")

# 3. 主題比例對比
usa_counts = usa_df['dominant_topic'].value_counts().sort_index()
usa_proportions = (usa_counts / len(usa_df) * 100).values
taiwan_proportions = np.array([24.9, 15.1, 17.3, 10.2, 9.6, 12.5, 10.3])

fig, ax = plt.subplots(figsize=(14, 6))

x = np.arange(7)
width = 0.35

tw_bars = ax.bar(x - width/2, taiwan_proportions, width,
                 label='🇹🇼 Taiwan (K=7)', color=COLORS['taiwan']['primary'],
                 alpha=0.7, edgecolor='black', linewidth=1)

us_bars = ax.bar(x[:6] + width/2, usa_proportions, width,
                 label='🇺🇸 USA (K=6)', color=COLORS['usa']['primary'],
                 alpha=0.7, edgecolor='black', linewidth=1)

ax.set_ylabel('Proportion (%)', fontsize=12, fontweight='bold')
ax.set_xlabel('Topic ID', fontsize=12, fontweight='bold')
ax.set_title('Topic Proportion Comparison', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels([f'T{i}' for i in range(7)])
ax.legend(fontsize=11)
ax.grid(axis='y', alpha=0.3)

for bar in tw_bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
            f'{height:.1f}%', ha='center', va='bottom', fontsize=9)

for bar in us_bars:
    height = bar.get_height()
    if height > 0:
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.1f}%', ha='center', va='bottom', fontsize=9)

plt.tight_layout()
charts['topic_proportion'] = fig_to_base64(fig)
print("  ✅ 主題比例對比圖")

# 4. 美國評分箱型圖
usa_ratings = []
usa_labels = []

for topic_id in range(6):
    ratings = usa_df[usa_df['dominant_topic'] == topic_id]['評分'].values
    usa_ratings.append(ratings)
    usa_labels.append(f"T{topic_id}\n{USA_TOPICS[topic_id]['label_zh']}")

fig, ax = plt.subplots(figsize=(12, 6))

bp = ax.boxplot(usa_ratings, labels=usa_labels, patch_artist=True,
                showmeans=True, meanline=True, widths=0.6)

for patch in bp['boxes']:
    patch.set_facecolor(COLORS['usa']['light'])
    patch.set_edgecolor(COLORS['usa']['primary'])
    patch.set_linewidth(1.5)

for median in bp['medians']:
    median.set_color(COLORS['usa']['dark'])
    median.set_linewidth(2)

for mean in bp['means']:
    mean.set_color('red')
    mean.set_linewidth(2)

ax.set_ylabel('Rating (1-5 stars)', fontsize=12, fontweight='bold')
ax.set_xlabel('Topics', fontsize=12, fontweight='bold')
ax.set_title('🇺🇸 USA Topic Rating Distribution', fontsize=14, fontweight='bold')
ax.grid(axis='y', alpha=0.3)
ax.set_ylim([0, 5.5])

plt.tight_layout()
charts['usa_ratings'] = fig_to_base64(fig)
print("  ✅ 美國評分分佈圖")

print()

# ============================================
# 生成 HTML 報告
# ============================================

print("📝 生成 HTML 報告...")

html_content = create_html_header()

# 標題和元資訊
html_content += f"""
<h1>🌏 台美醫院評論跨文化比較分析報告</h1>

<div class="meta-info">
    <strong>Taiwan-USA Hospital Review Cross-Cultural Comparison Analysis Report</strong><br>
    報告生成時間：{datetime.now().strftime("%Y年%m月%d日 %H:%M:%S")}<br>
    分析方法：Gensim LDA Topic Modeling
</div>
"""

# 1. 執行摘要
html_content += """
<div class="section">
    <h2>📋 Executive Summary | 執行摘要</h2>

    <div class="info-box">
        <p><strong>研究目的</strong>：透過 LDA 主題模型分析，比較台灣與美國醫院評論的服務品質主題差異，揭示兩國在醫療服務品質、文化期望與制度差異上的不同。</p>
    </div>

    <div class="stats-grid">
        <div class="stat-card">
            <h3>🇹🇼 台灣資料</h3>
            <div class="stat-value">5,007</div>
            <div class="stat-label">則評論 | 26家醫院</div>
        </div>

        <div class="stat-card">
            <h3>🇺🇸 美國資料</h3>
            <div class="stat-value">3,240</div>
            <div class="stat-label">則評論</div>
        </div>

        <div class="stat-card">
            <h3>📊 主題模型</h3>
            <div class="stat-value">K=7 vs K=6</div>
            <div class="stat-label">台灣7主題 | 美國6主題</div>
        </div>

        <div class="stat-card">
            <h3>🎯 模型品質</h3>
            <div class="stat-value">0.42 / 0.40</div>
            <div class="stat-label">Coherence Score</div>
        </div>
    </div>
</div>
"""

# 2. 資料集與模型品質
html_content += f"""
<div class="section">
    <h2>📊 Dataset & Model Quality | 資料集與模型品質</h2>

    <div class="chart-container">
        <img src="data:image/png;base64,{charts['model_quality']}" alt="Model Quality Comparison">
    </div>

    <div class="info-box">
        <p><strong>解讀</strong>：</p>
        <ul>
            <li>🇹🇼 台灣模型的 <strong>Coherence Score 較高</strong> (0.4175 > 0.4029)，表示主題內部語義關聯性更強</li>
            <li>🇺🇸 美國模型的 <strong>Perplexity 較低</strong>，預測能力略優</li>
            <li>兩個模型品質都在可接受範圍內 (Coherence > 0.35)</li>
        </ul>
    </div>

    <div class="chart-container">
        <img src="data:image/png;base64,{charts['dataset_size']}" alt="Dataset Size Comparison">
    </div>
</div>
"""

# 3. 主題標籤總覽
html_content += """
<div class="section">
    <h2>🎯 Topic Labels | 主題標籤總覽</h2>

    <h3 class="taiwan">🇹🇼 Taiwan Topics (K=7)</h3>

    <div class="topic-grid">
"""

for topic_id in range(7):
    info = TAIWAN_TOPICS[topic_id]
    sentiment_class = info['sentiment']
    html_content += f"""
        <div class="topic-card">
            <h4>🇹🇼 Topic {topic_id}: {info['label_zh']}</h4>
            <p><strong>English</strong>: {info['label_en']}</p>
            <p><strong>情緒</strong>: <span class="{sentiment_class}">{sentiment_class}</span></p>
            <p class="keywords"><strong>關鍵詞</strong>: {', '.join(info['keywords'][:5])}</p>
            <p style="font-size: 0.9em; color: #555; margin-top: 10px;">{info['description']}</p>
        </div>
    """

html_content += """
    </div>

    <h3 class="usa">🇺🇸 USA Topics (K=6)</h3>

    <div class="topic-grid">
"""

for topic_id in range(6):
    info = USA_TOPICS[topic_id]
    sentiment_class = info['sentiment']
    html_content += f"""
        <div class="topic-card">
            <h4>🇺🇸 Topic {topic_id}: {info['label_zh']}</h4>
            <p><strong>English</strong>: {info['label_en']}</p>
            <p><strong>Sentiment</strong>: <span class="{sentiment_class}">{sentiment_class}</span></p>
            <p class="keywords"><strong>Keywords</strong>: {', '.join(info['keywords'][:5])}</p>
            <p style="font-size: 0.9em; color: #555; margin-top: 10px;">{info['description']}</p>
        </div>
    """

html_content += """
    </div>
</div>
"""

# 4. 主題比例比較
html_content += f"""
<div class="section">
    <h2>📈 Topic Proportion Comparison | 主題比例比較</h2>

    <div class="chart-container">
        <img src="data:image/png;base64,{charts['topic_proportion']}" alt="Topic Proportion Comparison">
    </div>

    <div class="info-box">
        <p><strong>重點發現</strong>：</p>
        <ul>
            <li>🇹🇼 台灣最大主題是「<strong>醫療專業認可</strong>」(24.9%)，反映正面評價為主</li>
            <li>🇺🇸 美國最大主題是「<strong>整體正面評價</strong>」(34.8%)，比例更高</li>
            <li>🇹🇼 台灣「<strong>服務態度問題</strong>」主題顯著 (17.3%)，是文化特色</li>
            <li>🇺🇸 美國「<strong>急診等候時間</strong>」問題突出 (16.4%)</li>
        </ul>
    </div>
</div>
"""

# 5. 評分分析
html_content += f"""
<div class="section">
    <h2>⭐ Rating Analysis | 評分分析</h2>

    <div class="chart-container">
        <img src="data:image/png;base64,{charts['usa_ratings']}" alt="USA Rating Distribution">
    </div>

    <h3>📊 美國各主題統計數據</h3>

    <table>
        <thead>
            <tr>
                <th>Topic</th>
                <th>評論數</th>
                <th>平均評分</th>
                <th>評分標準差</th>
                <th>比例(%)</th>
            </tr>
        </thead>
        <tbody>
"""

usa_stats = usa_df.groupby('dominant_topic').agg({
    '評分': ['count', 'mean', 'std'],
    'topic_probability': 'mean'
}).round(2)

usa_stats.columns = ['評論數', '平均評分', '評分標準差', '平均機率']
usa_stats['比例(%)'] = (usa_stats['評論數'] / len(usa_df) * 100).round(1)

# 將索引從 1-6 轉換為 0-5
usa_stats_dict = {}
for idx in usa_stats.index:
    usa_stats_dict[idx - 1] = usa_stats.loc[idx]

for topic_id in range(6):
    info = USA_TOPICS[topic_id]
    if topic_id in usa_stats_dict:
        stats = usa_stats_dict[topic_id]
    else:
        # 如果該主題沒有資料，使用預設值
        stats = pd.Series({'評論數': 0, '平均評分': 0, '評分標準差': 0, '比例(%)': 0})
    html_content += f"""
            <tr>
                <td>🇺🇸 T{topic_id}: {info['label_zh']}</td>
                <td>{int(stats['評論數']):,}</td>
                <td>{stats['平均評分']:.2f} ★</td>
                <td>{stats['評分標準差']:.2f}</td>
                <td>{stats['比例(%)']:.1f}%</td>
            </tr>
    """

html_content += """
        </tbody>
    </table>
</div>
"""

# 6. 文化差異重點
html_content += """
<div class="section">
    <h2>🌍 Cultural Insights | 文化差異重點</h2>

    <h3>🇹🇼 台灣獨特主題</h3>

    <div class="warning-box">
        <h4>😠 服務態度問題 (17.3%)</h4>
        <p>台灣病患對醫護人員的「態度」特別敏感，形成獨立且比例顯著的主題。</p>
        <p><strong>關鍵詞</strong>：態度、病人、護理師、不是、服務</p>
        <p><strong>文化意義</strong>：反映台灣醫療文化中對「服務態度」的高度重視，與儒家文化強調「禮」的傳統相關。</p>
    </div>

    <div class="info-box">
        <h4>🏥 設施與便利性 (10.2%)</h4>
        <p>停車場、動線、電梯等設施便利性在台灣醫療體驗中佔重要地位。</p>
        <p><strong>關鍵詞</strong>：停車場、方便、電梯、動線、流程</p>
        <p><strong>文化意義</strong>：台灣都市化程度高，醫院多位於市區，停車與交通便利性成為重要考量。</p>
    </div>

    <h3>🇺🇸 美國獨特主題</h3>

    <div class="warning-box">
        <h4>💰 預約與帳單問題 (4.1%)</h4>
        <p>醫療帳單 (bill, billing) 和保險 (insurance) 問題是美國醫療系統的獨特痛點。</p>
        <p><strong>Keywords</strong>: appointment, bill, billing, insurance, service</p>
        <p><strong>Cultural Significance</strong>：反映美國商業化醫療保險制度的複雜性，是台灣全民健保體系所沒有的問題。</p>
    </div>

    <div class="info-box">
        <h4>😣 門診與疼痛管理 (14.7%)</h4>
        <p>Pain management 是美國醫療評論的顯著關注點。</p>
        <p><strong>Keywords</strong>: clinic, care, pain, doctor, help</p>
        <p><strong>Cultural Significance</strong>：美國醫療文化強調疼痛管理與病患舒適度，形成獨立主題。</p>
    </div>

    <h3>🤝 共同關注點</h3>

    <div class="success-box">
        <h4>✅ 正面評價為主導</h4>
        <ul>
            <li>🇹🇼 台灣：<strong>醫療專業認可</strong> (24.9%, 4.56★)</li>
            <li>🇺🇸 美國：<strong>整體正面評價</strong> (34.8%, 3.96★)</li>
        </ul>
        <p><strong>差異</strong>：兩國都有佔最大比例的正面主題，但台灣的評分更高。</p>
    </div>

    <div class="warning-box">
        <h4>⏰ 等候時間普遍不滿</h4>
        <ul>
            <li>🇹🇼 台灣：<strong>就診流程與等候</strong> (15.1%, 2.89★)</li>
            <li>🇺🇸 美國：<strong>急診等候時間</strong> (16.4%, 3.29★)</li>
        </ul>
        <p><strong>差異</strong>：兩國都有顯著的等候時間問題，美國更集中在急診室。</p>
    </div>
</div>
"""

# 7. 主題對應關係
html_content += """
<div class="section">
    <h2>🔗 Topic Mapping | 主題對應關係</h2>

    <table>
        <thead>
            <tr>
                <th>相似度</th>
                <th>🇹🇼 台灣主題</th>
                <th>🇺🇸 美國主題</th>
                <th>共同特徵</th>
            </tr>
        </thead>
        <tbody>
"""

for mapping in TOPIC_MAPPING:
    if mapping['taiwan_topic'] is not None and mapping['usa_topic'] is not None:
        tw_info = TAIWAN_TOPICS[mapping['taiwan_topic']]
        us_info = USA_TOPICS[mapping['usa_topic']]
        stars = "★" * mapping['similarity'] + "☆" * (5 - mapping['similarity'])

        html_content += f"""
            <tr>
                <td style="text-align: center; font-size: 1.2em;">{stars}</td>
                <td>🇹🇼 {tw_info['label_zh']}</td>
                <td>🇺🇸 {us_info['label_zh']}</td>
                <td>{mapping['common_features']}</td>
            </tr>
        """

html_content += """
        </tbody>
    </table>
</div>
"""

# 8. 研究結論
html_content += """
<div class="section">
    <h2>💡 Conclusions | 研究結論</h2>

    <h3>主要發現</h3>

    <div class="success-box">
        <h4>1. 文化差異顯著</h4>
        <p>台灣與美國在醫療服務品質的關注點存在明顯差異：</p>
        <ul>
            <li>台灣特別重視「服務態度」和「設施便利性」</li>
            <li>美國特別關注「醫療帳單」和「疼痛管理」</li>
        </ul>
    </div>

    <div class="info-box">
        <h4>2. 共同痛點：等候時間</h4>
        <p>兩國都有顯著的等候時間不滿問題，反映醫療資源需求與供給的普遍矛盾。</p>
    </div>

    <div class="success-box">
        <h4>3. 正面評價為主</h4>
        <p>兩國評論都以正面評價為主導（台灣24.9%，美國34.8%），顯示整體醫療品質獲得肯定。</p>
    </div>

    <h3>管理意涵</h3>

    <div class="info-box">
        <h4>對台灣醫療機構的建議</h4>
        <ul>
            <li><strong>加強服務態度訓練</strong>：針對「態度」問題設計專門的溝通技巧培訓</li>
            <li><strong>優化設施便利性</strong>：改善停車、動線設計，提升病患體驗</li>
            <li><strong>縮短等候時間</strong>：優化掛號流程，提高就診效率</li>
        </ul>
    </div>

    <div class="info-box">
        <h4>對美國醫療機構的建議</h4>
        <ul>
            <li><strong>簡化帳單流程</strong>：提供更清楚的費用說明，改善保險流程</li>
            <li><strong>加強疼痛管理</strong>：投入更多資源於疼痛評估與管理</li>
            <li><strong>改善急診等候</strong>：優化急診室流程，縮短等候時間</li>
        </ul>
    </div>

    <h3>研究限制</h3>

    <div class="warning-box">
        <ul>
            <li>評論資料來自 Google Maps，可能存在取樣偏誤</li>
            <li>台灣與美國的評論數量不同（5,007 vs 3,240）</li>
            <li>主題數量不同（K=7 vs K=6），影響直接比較</li>
            <li>評論語言不同（中文 vs 英文），可能影響主題呈現方式</li>
        </ul>
    </div>
</div>
"""

# 添加尾部
html_content += create_html_footer()

# 儲存 HTML
output_path = BASE_DIR / "reports" / f"Taiwan_USA_Comparison_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
output_path.parent.mkdir(parents=True, exist_ok=True)

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("=" * 80)
print("✅ HTML 報告生成完成！")
print(f"📁 檔案位置: {output_path}")
print(f"📊 檔案大小: {output_path.stat().st_size / 1024 / 1024:.2f} MB")
print()
print("🌐 開啟方式：")
print(f"   1. 用瀏覽器開啟: {output_path}")
print(f"   2. 或執行: open \"{output_path}\"")
print("=" * 80)
