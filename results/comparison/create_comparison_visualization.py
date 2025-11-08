#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
創建台灣與美國醫院評論比較視覺化
Create Taiwan-USA Hospital Reviews Comparison Visualization
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 設定中文字體
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'Hiragino Sans GB', 'STHeiti']
plt.rcParams['axes.unicode_minus'] = False

# 資料
taiwan_data = {
    'topics': ['T1\n醫療專業', 'T2\n流程等待', 'T3\n服務態度', 'T4\n設施便利', 'T5\n手術成功', 'T6\n住院照護', 'T7\n急診溝通'],
    'percentages': [24.9, 15.1, 17.3, 10.2, 9.6, 12.5, 10.3],
    'ratings': [4.56, 2.89, 1.98, 2.76, 4.38, 3.45, 2.34]
}

usa_data = {
    'topics': ['T1\nLife Care', 'T2\nWaiting', 'T3\nOutpatient', 'T4\nNursing', 'T5\nPositive', 'T6\nBilling', 'T7\nPain Mgmt'],
    'percentages': [4.9, 13.9, 11.0, 9.1, 37.1, 4.1, 19.9],
    'ratings': [3.18, 1.91, 2.61, 2.59, 4.84, 2.72, 1.92]
}

# 創建圖表
fig = plt.figure(figsize=(18, 10))

# 1. 模型品質比較
ax1 = plt.subplot(2, 3, 1)
models = ['Taiwan\n台灣', 'USA\n美國']
coherence = [0.4175, 0.3887]
colors = ['#e74c3c', '#3498db']
bars = ax1.bar(models, coherence, color=colors, edgecolor='black', linewidth=1.5, alpha=0.8)
ax1.set_ylabel('Coherence Score', fontsize=11, fontweight='bold')
ax1.set_title('Model Quality Comparison\n模型品質比較', fontsize=12, fontweight='bold')
ax1.set_ylim(0, 0.5)
ax1.grid(axis='y', alpha=0.3, linestyle='--')
for bar, val in zip(bars, coherence):
    ax1.text(bar.get_x() + bar.get_width()/2, val + 0.01, f'{val:.4f}',
             ha='center', va='bottom', fontsize=10, fontweight='bold')

# 2. 樣本數比較
ax2 = plt.subplot(2, 3, 2)
samples = [5007, 3240]
bars = ax2.bar(models, samples, color=colors, edgecolor='black', linewidth=1.5, alpha=0.8)
ax2.set_ylabel('Number of Reviews', fontsize=11, fontweight='bold')
ax2.set_title('Sample Size Comparison\n樣本數比較', fontsize=12, fontweight='bold')
ax2.grid(axis='y', alpha=0.3, linestyle='--')
for bar, val in zip(bars, samples):
    ax2.text(bar.get_x() + bar.get_width()/2, val + 100, f'{val:,}',
             ha='center', va='bottom', fontsize=10, fontweight='bold')

# 3. Perplexity比較
ax3 = plt.subplot(2, 3, 3)
perplexity = [7.5039, 7.2404]  # 取絕對值
bars = ax3.bar(models, perplexity, color=colors, edgecolor='black', linewidth=1.5, alpha=0.8)
ax3.set_ylabel('Perplexity (absolute)', fontsize=11, fontweight='bold')
ax3.set_title('Perplexity Comparison\n困惑度比較 (lower is better)', fontsize=12, fontweight='bold')
ax3.grid(axis='y', alpha=0.3, linestyle='--')
for bar, val in zip(bars, perplexity):
    ax3.text(bar.get_x() + bar.get_width()/2, val + 0.05, f'{val:.2f}',
             ha='center', va='bottom', fontsize=10, fontweight='bold')

# 4. 台灣主題分布
ax4 = plt.subplot(2, 3, 4)
x_tw = np.arange(len(taiwan_data['topics']))
colors_tw = ['#2ecc71' if r >= 4.0 else '#e74c3c' if r < 2.5 else '#f39c12'
             for r in taiwan_data['ratings']]
bars = ax4.bar(x_tw, taiwan_data['percentages'], color=colors_tw, edgecolor='black', linewidth=1.2, alpha=0.8)
ax4.set_xlabel('Topics', fontsize=11, fontweight='bold')
ax4.set_ylabel('Percentage (%)', fontsize=11, fontweight='bold')
ax4.set_title('Taiwan Topic Distribution\n台灣主題分布', fontsize=12, fontweight='bold')
ax4.set_xticks(x_tw)
ax4.set_xticklabels(taiwan_data['topics'], fontsize=8, rotation=0)
ax4.grid(axis='y', alpha=0.3, linestyle='--')
for bar, pct, rating in zip(bars, taiwan_data['percentages'], taiwan_data['ratings']):
    ax4.text(bar.get_x() + bar.get_width()/2, pct + 0.5, f'{pct:.1f}%\n{rating:.2f}★',
             ha='center', va='bottom', fontsize=7, fontweight='bold')

# 5. 美國主題分布
ax5 = plt.subplot(2, 3, 5)
x_usa = np.arange(len(usa_data['topics']))
colors_usa = ['#2ecc71' if r >= 4.0 else '#e74c3c' if r < 2.5 else '#f39c12'
              for r in usa_data['ratings']]
bars = ax5.bar(x_usa, usa_data['percentages'], color=colors_usa, edgecolor='black', linewidth=1.2, alpha=0.8)
ax5.set_xlabel('Topics', fontsize=11, fontweight='bold')
ax5.set_ylabel('Percentage (%)', fontsize=11, fontweight='bold')
ax5.set_title('USA Topic Distribution\n美國主題分布', fontsize=12, fontweight='bold')
ax5.set_xticks(x_usa)
ax5.set_xticklabels(usa_data['topics'], fontsize=8, rotation=0)
ax5.grid(axis='y', alpha=0.3, linestyle='--')
for bar, pct, rating in zip(bars, usa_data['percentages'], usa_data['ratings']):
    ax5.text(bar.get_x() + bar.get_width()/2, pct + 0.5, f'{pct:.1f}%\n{rating:.2f}★',
             ha='center', va='bottom', fontsize=7, fontweight='bold')

# 6. 正負面評論比較
ax6 = plt.subplot(2, 3, 6)
categories = ['Positive\n正面\n(≥4.0★)', 'Neutral\n中性\n(2.5-4.0★)', 'Negative\n負面\n(<2.5★)']
taiwan_sentiment = [
    sum([taiwan_data['percentages'][i] for i, r in enumerate(taiwan_data['ratings']) if r >= 4.0]),
    sum([taiwan_data['percentages'][i] for i, r in enumerate(taiwan_data['ratings']) if 2.5 <= r < 4.0]),
    sum([taiwan_data['percentages'][i] for i, r in enumerate(taiwan_data['ratings']) if r < 2.5])
]
usa_sentiment = [
    sum([usa_data['percentages'][i] for i, r in enumerate(usa_data['ratings']) if r >= 4.0]),
    sum([usa_data['percentages'][i] for i, r in enumerate(usa_data['ratings']) if 2.5 <= r < 4.0]),
    sum([usa_data['percentages'][i] for i, r in enumerate(usa_data['ratings']) if r < 2.5])
]

x_sent = np.arange(len(categories))
width = 0.35
bars1 = ax6.bar(x_sent - width/2, taiwan_sentiment, width, label='Taiwan',
                color='#e74c3c', edgecolor='black', linewidth=1.2, alpha=0.8)
bars2 = ax6.bar(x_sent + width/2, usa_sentiment, width, label='USA',
                color='#3498db', edgecolor='black', linewidth=1.2, alpha=0.8)

ax6.set_ylabel('Percentage (%)', fontsize=11, fontweight='bold')
ax6.set_title('Sentiment Distribution Comparison\n情感分布比較', fontsize=12, fontweight='bold')
ax6.set_xticks(x_sent)
ax6.set_xticklabels(categories, fontsize=9)
ax6.legend(fontsize=10)
ax6.grid(axis='y', alpha=0.3, linestyle='--')

for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax6.text(bar.get_x() + bar.get_width()/2, height + 0.5, f'{height:.1f}%',
                 ha='center', va='bottom', fontsize=9, fontweight='bold')

plt.tight_layout()
plt.savefig('Taiwan_USA_Comparison_Visualization.png', dpi=300, bbox_inches='tight')
print("✓ Visualization saved: Taiwan_USA_Comparison_Visualization.png")
print("✓ 視覺化圖表已儲存: Taiwan_USA_Comparison_Visualization.png")
