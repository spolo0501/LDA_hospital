#!/usr/bin/env python3
"""
台美醫院評論跨文化比較分析系統
Taiwan-USA Hospital Review Cross-Cultural Comparison System

Author: Claude Code
Date: 2025-11-12
"""

import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# 導入配置
from comparison_config import *

# 設定頁面配置
st.set_page_config(**PAGE_CONFIG)

# ============================================
# 資料載入函數
# ============================================

@st.cache_resource
def load_taiwan_model():
    """載入台灣 LDA K=7 模型"""
    with open(TAIWAN_MODEL_PATH, 'rb') as f:
        data = pickle.load(f)
    return data['lda_model'], data

@st.cache_resource
def load_usa_model():
    """載入美國 LDA K=6 模型"""
    with open(USA_MODEL_PATH, 'rb') as f:
        data = pickle.load(f)
    return data['lda_model'], data

@st.cache_data
def load_usa_reviews():
    """載入美國評論資料"""
    df = pd.read_csv(USA_DATA_PATH)
    return df

# ============================================
# 資料處理函數
# ============================================

def get_topic_statistics(df, country="usa"):
    """計算主題統計"""
    stats = df.groupby('dominant_topic').agg({
        '評分': ['count', 'mean', 'std'],
        'topic_probability': 'mean'
    }).round(2)

    stats.columns = ['評論數', '平均評分', '評分標準差', '平均機率']
    stats['比例(%)'] = (stats['評論數'] / len(df) * 100).round(1)

    return stats

def create_comparison_dataframe():
    """建立台美比較資料表"""
    comparison_data = []

    # 台灣資料
    for topic_id, info in TAIWAN_TOPICS.items():
        comparison_data.append({
            "國家": "🇹🇼 台灣",
            "主題ID": topic_id,
            "主題標籤": f"{info['emoji']} {info['label_zh']}",
            "英文標籤": info['label_en'],
            "情緒": info['sentiment'],
            "關鍵詞": ", ".join(info['keywords'][:5])
        })

    # 美國資料
    for topic_id, info in USA_TOPICS.items():
        comparison_data.append({
            "國家": "🇺🇸 美國",
            "主題ID": topic_id,
            "主題標籤": f"{info['emoji']} {info['label_zh']}",
            "英文標籤": info['label_en'],
            "情緒": info['sentiment'],
            "關鍵詞": ", ".join(info['keywords'][:5])
        })

    return pd.DataFrame(comparison_data)

# ============================================
# 視覺化函數
# ============================================

def plot_model_quality_comparison():
    """繪製模型品質比較圖"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

    # Coherence Score
    countries = ['Taiwan\nK=7', 'USA\nK=6']
    coherence = [DATASET_INFO['taiwan']['coherence'], DATASET_INFO['usa']['coherence']]
    colors = [COLORS['taiwan']['primary'], COLORS['usa']['primary']]

    ax1.bar(countries, coherence, color=colors, alpha=0.7, edgecolor='black')
    ax1.set_ylabel('Coherence Score', fontsize=12)
    ax1.set_title('Model Coherence Comparison', fontsize=14, fontweight='bold')
    ax1.set_ylim([0, 0.45])
    ax1.grid(axis='y', alpha=0.3)

    # 添加數值標籤
    for i, v in enumerate(coherence):
        ax1.text(i, v + 0.01, f'{v:.4f}', ha='center', fontweight='bold')

    # Perplexity (絕對值)
    perplexity = [abs(DATASET_INFO['taiwan']['perplexity']),
                  abs(DATASET_INFO['usa']['perplexity'])]

    ax2.bar(countries, perplexity, color=colors, alpha=0.7, edgecolor='black')
    ax2.set_ylabel('Perplexity (Absolute Value)', fontsize=12)
    ax2.set_title('Model Perplexity Comparison', fontsize=14, fontweight='bold')
    ax2.grid(axis='y', alpha=0.3)

    # 添加數值標籤
    for i, v in enumerate(perplexity):
        ax2.text(i, v + 0.1, f'{v:.2f}', ha='center', fontweight='bold')

    plt.tight_layout()
    return fig

def plot_dataset_size_comparison():
    """繪製資料集規模比較"""
    fig, ax = plt.subplots(figsize=(8, 5))

    countries = ['Taiwan', 'USA']
    reviews = [DATASET_INFO['taiwan']['reviews'], DATASET_INFO['usa']['reviews']]
    colors = [COLORS['taiwan']['primary'], COLORS['usa']['primary']]

    bars = ax.barh(countries, reviews, color=colors, alpha=0.7, edgecolor='black')
    ax.set_xlabel('Number of Reviews', fontsize=12)
    ax.set_title('Dataset Size Comparison', fontsize=14, fontweight='bold')
    ax.grid(axis='x', alpha=0.3)

    # 添加數值標籤
    for i, (bar, v) in enumerate(zip(bars, reviews)):
        ax.text(v + 50, i, f'{v:,}', va='center', fontweight='bold')

    plt.tight_layout()
    return fig

def plot_sentiment_distribution(usa_df):
    """繪製情緒分佈比較"""
    # 計算美國各主題的情緒
    usa_sentiment_counts = {'positive': 0, 'negative': 0, 'neutral': 0}

    for topic_id in range(6):
        topic_reviews = len(usa_df[usa_df['dominant_topic'] == topic_id])
        sentiment = USA_TOPICS[topic_id]['sentiment']
        usa_sentiment_counts[sentiment] += topic_reviews

    # 計算台灣各主題的情緒（使用比例估算）
    taiwan_total = DATASET_INFO['taiwan']['reviews']
    taiwan_sentiment_counts = {'positive': 0, 'negative': 0, 'neutral': 0}

    # 從主題分佈估算（這裡需要實際資料，暫時使用模擬）
    # 實際應用時需要載入台灣評論資料
    taiwan_topic_dist = [0.249, 0.151, 0.173, 0.102, 0.096, 0.125, 0.103]  # 從報告中獲取
    for topic_id in range(7):
        reviews = int(taiwan_total * taiwan_topic_dist[topic_id])
        sentiment = TAIWAN_TOPICS[topic_id]['sentiment']
        taiwan_sentiment_counts[sentiment] += reviews

    # 轉換為百分比
    taiwan_pct = {k: v/taiwan_total*100 for k, v in taiwan_sentiment_counts.items()}
    usa_pct = {k: v/len(usa_df)*100 for k, v in usa_sentiment_counts.items()}

    # 繪圖
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    sentiments = ['Positive', 'Neutral', 'Negative']
    taiwan_values = [taiwan_pct['positive'], taiwan_pct['neutral'], taiwan_pct['negative']]
    usa_values = [usa_pct['positive'], usa_pct['neutral'], usa_pct['negative']]
    sentiment_colors = [COLORS['sentiment']['positive'],
                       COLORS['sentiment']['neutral'],
                       COLORS['sentiment']['negative']]

    # 台灣
    wedges1, texts1, autotexts1 = ax1.pie(taiwan_values, labels=sentiments, autopct='%1.1f%%',
                                            colors=sentiment_colors, startangle=90)
    ax1.set_title('🇹🇼 Taiwan Sentiment Distribution', fontsize=12, fontweight='bold')

    # 美國
    wedges2, texts2, autotexts2 = ax2.pie(usa_values, labels=sentiments, autopct='%1.1f%%',
                                            colors=sentiment_colors, startangle=90)
    ax2.set_title('🇺🇸 USA Sentiment Distribution', fontsize=12, fontweight='bold')

    plt.tight_layout()
    return fig

def plot_topic_mapping_sankey():
    """繪製主題對應桑基圖"""
    # 建立節點標籤（簡短版本，方便顯示）
    taiwan_labels = [
        "T0: 醫療專業認可",
        "T1: 就診流程等候",
        "T2: 服務態度問題",
        "T3: 設施便利性",
        "T4: 手術治療成功",
        "T5: 住院照護",
        "T6: 急診溝通"
    ]

    usa_labels = [
        "T0: 重症照護",
        "T1: 急診等候",
        "T2: 疼痛管理",
        "T3: 護理品質",
        "T4: 正面評價",
        "T5: 帳單問題"
    ]

    # 合併標籤
    nodes = taiwan_labels + usa_labels

    # 節點顏色
    node_colors = [COLORS['taiwan']['primary']] * 7 + [COLORS['usa']['primary']] * 6

    # 建立連線
    sources = []
    targets = []
    values = []
    link_colors = []
    link_labels = []

    for mapping in TOPIC_MAPPING:
        if mapping['taiwan_topic'] is not None and mapping['usa_topic'] is not None:
            sources.append(mapping['taiwan_topic'])
            targets.append(mapping['usa_topic'] + 7)  # 美國節點索引從7開始
            values.append(mapping['similarity'] * 20)  # 放大相似度以便視覺化

            # 根據相似度設定顏色
            similarity = mapping['similarity']
            if similarity >= 4:
                color = f'rgba(46, 204, 113, 0.4)'  # 綠色（高相似度）
            elif similarity >= 3:
                color = f'rgba(243, 156, 18, 0.4)'  # 橘色（中等相似度）
            else:
                color = f'rgba(231, 76, 60, 0.3)'   # 紅色（低相似度）
            link_colors.append(color)

            # 連線標籤
            stars = "★" * similarity
            link_labels.append(f"{stars}")

    fig = go.Figure(data=[go.Sankey(
        node=dict(
            pad=20,
            thickness=25,
            line=dict(color="white", width=2),
            label=nodes,
            color=node_colors,
            customdata=[f"🇹🇼 台灣"] * 7 + [f"🇺🇸 美國"] * 6,
            hovertemplate='%{label}<br>%{customdata}<extra></extra>'
        ),
        link=dict(
            source=sources,
            target=targets,
            value=values,
            color=link_colors,
            customdata=link_labels,
            hovertemplate='相似度: %{customdata}<br>連線強度: %{value}<extra></extra>'
        ),
        textfont=dict(size=14, family="Arial, sans-serif")
    )])

    fig.update_layout(
        title={
            'text': "台美醫院評論主題對應關係<br><sub>連線顏色：綠色=高相似度, 橘色=中等相似度, 紅色=低相似度</sub>",
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 16}
        },
        font=dict(size=13, family="Arial, sans-serif"),
        height=700,
        margin=dict(l=20, r=20, t=80, b=20)
    )

    return fig

def plot_keyword_comparison(taiwan_model, usa_model, topic_tw, topic_us):
    """繪製特定主題的關鍵詞權重對比"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # 台灣關鍵詞
    tw_words = taiwan_model.show_topic(topic_tw, topn=15)
    tw_keywords = [w for w, _ in tw_words]
    tw_weights = [p for _, p in tw_words]

    ax1.barh(range(len(tw_keywords)), tw_weights, color=COLORS['taiwan']['primary'], alpha=0.7)
    ax1.set_yticks(range(len(tw_keywords)))
    ax1.set_yticklabels(tw_keywords)
    ax1.invert_yaxis()
    ax1.set_xlabel('Weight', fontsize=11)
    ax1.set_title(f"🇹🇼 {TAIWAN_TOPICS[topic_tw]['label_zh']}\nTop 15 Keywords",
                  fontsize=12, fontweight='bold')
    ax1.grid(axis='x', alpha=0.3)

    # 美國關鍵詞
    us_words = usa_model.show_topic(topic_us, topn=15)
    us_keywords = [w for w, _ in us_words]
    us_weights = [p for _, p in us_words]

    ax2.barh(range(len(us_keywords)), us_weights, color=COLORS['usa']['primary'], alpha=0.7)
    ax2.set_yticks(range(len(us_keywords)))
    ax2.set_yticklabels(us_keywords)
    ax2.invert_yaxis()
    ax2.set_xlabel('Weight', fontsize=11)
    ax2.set_title(f"🇺🇸 {USA_TOPICS[topic_us]['label_zh']}\nTop 15 Keywords",
                  fontsize=12, fontweight='bold')
    ax2.grid(axis='x', alpha=0.3)

    plt.tight_layout()
    return fig

def plot_rating_comparison(usa_df):
    """繪製評分對比箱型圖"""
    # 準備美國資料
    usa_ratings = []
    usa_labels = []

    for topic_id in range(6):
        ratings = usa_df[usa_df['dominant_topic'] == topic_id]['評分'].values
        usa_ratings.append(ratings)
        usa_labels.append(f"T{topic_id}\n{USA_TOPICS[topic_id]['emoji']}")

    # 繪圖
    fig, ax = plt.subplots(figsize=(12, 6))

    bp = ax.boxplot(usa_ratings, labels=usa_labels, patch_artist=True,
                    showmeans=True, meanline=True)

    # 設定顏色
    for patch in bp['boxes']:
        patch.set_facecolor(COLORS['usa']['light'])
        patch.set_edgecolor(COLORS['usa']['primary'])

    for median in bp['medians']:
        median.set_color(COLORS['usa']['dark'])
        median.set_linewidth(2)

    for mean in bp['means']:
        mean.set_color('red')
        mean.set_linewidth(2)

    ax.set_ylabel('Rating (1-5 stars)', fontsize=12)
    ax.set_xlabel('Topics', fontsize=12)
    ax.set_title('🇺🇸 USA Topic Rating Distribution', fontsize=14, fontweight='bold')
    ax.grid(axis='y', alpha=0.3)
    ax.set_ylim([0, 5.5])

    plt.tight_layout()
    return fig

def plot_topic_proportion_comparison(usa_df):
    """繪製主題比例對比圖"""
    # 美國主題比例
    usa_counts = usa_df['dominant_topic'].value_counts().sort_index()
    usa_proportions = (usa_counts / len(usa_df) * 100).values

    # 台灣主題比例（估算）
    taiwan_proportions = np.array([24.9, 15.1, 17.3, 10.2, 9.6, 12.5, 10.3])

    fig, ax = plt.subplots(figsize=(12, 6))

    x = np.arange(max(7, 6))
    width = 0.35

    # 繪製台灣
    tw_bars = ax.bar(x[:7] - width/2, taiwan_proportions, width,
                     label='🇹🇼 Taiwan (K=7)',
                     color=COLORS['taiwan']['primary'], alpha=0.7)

    # 繪製美國
    us_bars = ax.bar(x[:6] + width/2, usa_proportions, width,
                     label='🇺🇸 USA (K=6)',
                     color=COLORS['usa']['primary'], alpha=0.7)

    ax.set_ylabel('Proportion (%)', fontsize=12)
    ax.set_xlabel('Topic ID', fontsize=12)
    ax.set_title('Topic Proportion Comparison', fontsize=14, fontweight='bold')
    ax.set_xticks(x[:7])
    ax.legend()
    ax.grid(axis='y', alpha=0.3)

    # 添加數值標籤
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
    return fig

# ============================================
# 主程式
# ============================================

def main():
    # 載入資料
    taiwan_model, taiwan_data = load_taiwan_model()
    usa_model, usa_data = load_usa_model()
    usa_df = load_usa_reviews()

    # 標題
    st.title("🌏 台美醫院評論跨文化比較分析系統")
    st.markdown("### Taiwan-USA Hospital Review Cross-Cultural Comparison")
    st.markdown("---")

    # 側邊欄
    with st.sidebar:
        st.markdown(SIDEBAR_INFO)

        st.markdown("---")
        st.markdown("### 📑 頁面導航")
        page = st.radio(
            "選擇分析頁面",
            ["🏠 跨文化概覽", "🔗 主題對應映射", "🔍 關鍵詞比較", "📊 評分與情緒分析"],
            label_visibility="collapsed"
        )

    # ============================================
    # 頁面 1: 跨文化概覽
    # ============================================

    if page == "🏠 跨文化概覽":
        st.header("🏠 跨文化概覽 (Cross-Cultural Overview)")

        # 資料集基本資訊
        st.subheader("📊 資料集基本資訊")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                label="🇹🇼 台灣評論數",
                value=f"{DATASET_INFO['taiwan']['reviews']:,}",
                delta=f"+{DATASET_INFO['taiwan']['reviews'] - DATASET_INFO['usa']['reviews']:,} vs USA"
            )
            st.metric(
                label="🇹🇼 台灣主題數",
                value=f"K = {DATASET_INFO['taiwan']['topics']}"
            )
            st.metric(
                label="🇹🇼 Coherence Score",
                value=f"{DATASET_INFO['taiwan']['coherence']:.4f}",
                delta=f"+{DATASET_INFO['taiwan']['coherence'] - DATASET_INFO['usa']['coherence']:.4f}"
            )

        with col2:
            st.metric(
                label="🇺🇸 美國評論數",
                value=f"{DATASET_INFO['usa']['reviews']:,}"
            )
            st.metric(
                label="🇺🇸 美國主題數",
                value=f"K = {DATASET_INFO['usa']['topics']}"
            )
            st.metric(
                label="🇺🇸 Coherence Score",
                value=f"{DATASET_INFO['usa']['coherence']:.4f}"
            )

        with col3:
            st.metric(
                label="總評論數",
                value=f"{DATASET_INFO['taiwan']['reviews'] + DATASET_INFO['usa']['reviews']:,}"
            )
            st.metric(
                label="主題數差異",
                value=f"{DATASET_INFO['taiwan']['topics'] - DATASET_INFO['usa']['topics']}"
            )
            st.metric(
                label="樣本比例",
                value=f"{DATASET_INFO['taiwan']['reviews'] / DATASET_INFO['usa']['reviews']:.2f}:1",
                delta="Taiwan : USA"
            )

        st.markdown("---")

        # 模型品質比較
        st.subheader("🎯 模型品質比較")
        fig_quality = plot_model_quality_comparison()
        st.pyplot(fig_quality)

        st.info("""
        **解讀**：
        - 🇹🇼 台灣模型的 Coherence 較高 (0.4175 > 0.4029)，表示主題內部語義關聯性更強
        - 🇺🇸 美國模型的 Perplexity 較低，預測能力略優
        - 兩個模型品質都在可接受範圍內 (Coherence > 0.35)
        """)

        st.markdown("---")

        # 資料集規模比較
        st.subheader("📏 資料集規模比較")
        col1, col2 = st.columns([1, 1])

        with col1:
            fig_size = plot_dataset_size_comparison()
            st.pyplot(fig_size)

        with col2:
            st.markdown("""
            ### 資料集特徵

            #### 🇹🇼 台灣
            - **評論數**：5,007 則
            - **醫院數**：26 家醫療中心
            - **語言**：繁體中文
            - **主題模型**：K=7 (7個主題)

            #### 🇺🇸 美國
            - **評論數**：3,240 則
            - **語言**：English
            - **主題模型**：K=6 (6個主題)

            #### 📊 比較
            - 台灣樣本數多 **54%**
            - 台灣主題數多 1 個
            - 兩國都使用 Gensim LDA 方法
            """)

        st.markdown("---")

        # 情緒分佈比較
        st.subheader("😊😐😠 情緒分佈比較")
        fig_sentiment = plot_sentiment_distribution(usa_df)
        st.pyplot(fig_sentiment)

        st.markdown("---")

        # 文化差異重點
        st.subheader("🔍 文化差異重點")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 🇹🇼 台灣獨特主題")
            for insight in CULTURAL_INSIGHTS['taiwan_unique']:
                with st.expander(f"{TAIWAN_TOPICS[insight['topic']]['emoji']} {insight['insight']} ({insight['percentage']}%)"):
                    st.markdown(f"**主題**: {TAIWAN_TOPICS[insight['topic']]['label_zh']}")
                    st.markdown(f"**說明**: {insight['description']}")
                    st.markdown(f"**比例**: {insight['percentage']}%")

        with col2:
            st.markdown("### 🇺🇸 美國獨特主題")
            for insight in CULTURAL_INSIGHTS['usa_unique']:
                with st.expander(f"{USA_TOPICS[insight['topic']]['emoji']} {insight['insight']} ({insight['percentage']}%)"):
                    st.markdown(f"**主題**: {USA_TOPICS[insight['topic']]['label_zh']}")
                    st.markdown(f"**說明**: {insight['description']}")
                    st.markdown(f"**比例**: {insight['percentage']}%")

        st.markdown("### 🤝 共同關注點")
        for insight in CULTURAL_INSIGHTS['common']:
            taiwan_topic = TAIWAN_TOPICS[insight['taiwan_topic']]
            usa_topic = USA_TOPICS[insight['usa_topic']]
            st.success(f"""
            **{insight['insight']}**
            - 🇹🇼 {taiwan_topic['emoji']} {taiwan_topic['label_zh']}
            - 🇺🇸 {usa_topic['emoji']} {usa_topic['label_zh']}
            - {insight['description']}
            """)

    # ============================================
    # 頁面 2: 主題對應映射
    # ============================================

    elif page == "🔗 主題對應映射":
        st.header("🔗 主題對應映射 (Topic Alignment Mapping)")

        # 桑基圖
        st.subheader("📊 主題對應關係桑基圖")
        st.markdown("連線粗細代表主題相似度，從台灣主題（左）連到美國主題（右）")

        fig_sankey = plot_topic_mapping_sankey()
        st.plotly_chart(fig_sankey, use_container_width=True)

        st.markdown("---")

        # 主題對應詳細表格
        st.subheader("📋 主題對應關係詳細說明")

        for mapping in TOPIC_MAPPING:
            if mapping['taiwan_topic'] is not None and mapping['usa_topic'] is not None:
                taiwan_info = TAIWAN_TOPICS[mapping['taiwan_topic']]
                usa_info = USA_TOPICS[mapping['usa_topic']]
                similarity_stars = "★" * mapping['similarity'] + "☆" * (5 - mapping['similarity'])

                with st.expander(f"{similarity_stars} {taiwan_info['label_zh']} ↔️ {usa_info['label_zh']}"):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown(f"### 🇹🇼 {taiwan_info['emoji']} {taiwan_info['label_zh']}")
                        st.markdown(f"**English**: {taiwan_info['label_en']}")
                        st.markdown(f"**情緒**: {taiwan_info['sentiment']}")
                        st.markdown(f"**關鍵詞**: {', '.join(taiwan_info['keywords'][:5])}")
                        st.markdown(f"**說明**: {taiwan_info['description']}")
                    with col2:
                        st.markdown(f"### 🇺🇸 {usa_info['emoji']} {usa_info['label_zh']}")
                        st.markdown(f"**English**: {usa_info['label_en']}")
                        st.markdown(f"**情緒**: {usa_info['sentiment']}")
                        st.markdown(f"**Keywords**: {', '.join(usa_info['keywords'][:5])}")
                        st.markdown(f"**說明**: {usa_info['description']}")

                    st.success(f"**🔗 共同特徵**: {mapping['common_features']}")

        # 獨特主題
        st.markdown("---")
        st.subheader("🎯 文化獨特主題")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 🇹🇼 台灣獨有")
            # Topic 2: 服務態度問題
            taiwan_unique = TAIWAN_TOPICS[2]
            st.warning(f"""
            **{taiwan_unique['emoji']} {taiwan_unique['label_zh']}**

            {taiwan_unique['description']}

            **關鍵詞**: {', '.join(taiwan_unique['keywords'][:5])}

            **文化意義**: 台灣病患對醫護人員的服務態度特別敏感，形成獨立且比例顯著的主題（17.3%）
            """)

            # Topic 3: 設施與便利性
            taiwan_facility = TAIWAN_TOPICS[3]
            st.info(f"""
            **{taiwan_facility['emoji']} {taiwan_facility['label_zh']}**

            {taiwan_facility['description']}

            **關鍵詞**: {', '.join(taiwan_facility['keywords'][:5])}

            **文化意義**: 停車、動線等設施便利性在台灣醫療體驗中佔重要地位
            """)

        with col2:
            st.markdown("### 🇺🇸 美國獨有")
            # Topic 5: 預約與帳單
            usa_unique = USA_TOPICS[5]
            st.warning(f"""
            **{usa_unique['emoji']} {usa_unique['label_zh']}**

            {usa_unique['description']}

            **Keywords**: {', '.join(usa_unique['keywords'][:5])}

            **Cultural Significance**: 醫療帳單和保險問題是美國醫療系統的獨特痛點（4.1%）
            """)

            # Topic 2: 疼痛管理
            usa_pain = USA_TOPICS[2]
            st.info(f"""
            **{usa_pain['emoji']} {usa_pain['label_zh']}**

            {usa_pain['description']}

            **Keywords**: {', '.join(usa_pain['keywords'][:5])}

            **Cultural Significance**: Pain management 是美國醫療評論的顯著關注點（14.7%）
            """)

    # ============================================
    # 頁面 3: 關鍵詞深度比較
    # ============================================

    elif page == "🔍 關鍵詞比較":
        st.header("🔍 關鍵詞深度比較 (Keyword Analysis)")

        st.markdown("選擇對應的台美主題，查看關鍵詞權重對比")

        # 選擇器
        col1, col2 = st.columns(2)

        with col1:
            taiwan_topic_options = {f"Topic {i}: {TAIWAN_TOPICS[i]['emoji']} {TAIWAN_TOPICS[i]['label_zh']}": i
                                   for i in range(7)}
            selected_tw_label = st.selectbox("選擇台灣主題", list(taiwan_topic_options.keys()))
            selected_tw = taiwan_topic_options[selected_tw_label]

        with col2:
            usa_topic_options = {f"Topic {i}: {USA_TOPICS[i]['emoji']} {USA_TOPICS[i]['label_zh']}": i
                                for i in range(6)}
            selected_us_label = st.selectbox("選擇美國主題", list(usa_topic_options.keys()))
            selected_us = usa_topic_options[selected_us_label]

        st.markdown("---")

        # 顯示關鍵詞對比
        fig_keywords = plot_keyword_comparison(taiwan_model, usa_model, selected_tw, selected_us)
        st.pyplot(fig_keywords)

        st.markdown("---")

        # 顯示完整關鍵詞列表
        st.subheader("📝 完整關鍵詞列表（Top 30）")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown(f"### 🇹🇼 {TAIWAN_TOPICS[selected_tw]['label_zh']}")
            tw_words = taiwan_model.show_topic(selected_tw, topn=30)
            tw_df = pd.DataFrame(tw_words, columns=['關鍵詞', '權重'])
            tw_df['權重'] = tw_df['權重'].round(4)
            tw_df.index = tw_df.index + 1
            st.dataframe(tw_df, use_container_width=True, height=600)

        with col2:
            st.markdown(f"### 🇺🇸 {USA_TOPICS[selected_us]['label_zh']}")
            us_words = usa_model.show_topic(selected_us, topn=30)
            us_df = pd.DataFrame(us_words, columns=['Keyword', 'Weight'])
            us_df['Weight'] = us_df['Weight'].round(4)
            us_df.index = us_df.index + 1
            st.dataframe(us_df, use_container_width=True, height=600)

        st.markdown("---")

        # 關鍵詞分析
        st.subheader("🔬 關鍵詞特徵分析")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("#### 🇹🇼 台灣主題特徵")
            tw_info = TAIWAN_TOPICS[selected_tw]
            st.markdown(f"**主題名稱**: {tw_info['emoji']} {tw_info['label_zh']}")
            st.markdown(f"**英文名稱**: {tw_info['label_en']}")
            st.markdown(f"**情緒傾向**: {tw_info['sentiment']}")
            st.markdown(f"**主題說明**: {tw_info['description']}")

        with col2:
            st.markdown("#### 🇺🇸 美國主題特徵")
            us_info = USA_TOPICS[selected_us]
            st.markdown(f"**主題名稱**: {us_info['emoji']} {us_info['label_zh']}")
            st.markdown(f"**English Name**: {us_info['label_en']}")
            st.markdown(f"**Sentiment**: {us_info['sentiment']}")
            st.markdown(f"**Description**: {us_info['description']}")

    # ============================================
    # 頁面 4: 評分與情緒分析
    # ============================================

    elif page == "📊 評分與情緒分析":
        st.header("📊 評分與情緒對比分析 (Rating & Sentiment Analysis)")

        # 主題比例對比
        st.subheader("📈 主題比例對比")
        fig_proportion = plot_topic_proportion_comparison(usa_df)
        st.pyplot(fig_proportion)

        st.info("""
        **解讀**：
        - 🇹🇼 台灣最大主題是「醫療專業認可」（24.9%），反映正面評價
        - 🇺🇸 美國最大主題是「整體正面評價」（34.8%），比例更高
        - 🇹🇼 台灣「服務態度問題」主題顯著（17.3%），是文化特色
        - 🇺🇸 美國「急診等候時間」問題突出（16.4%）
        """)

        st.markdown("---")

        # 美國評分分佈箱型圖
        st.subheader("📊 美國各主題評分分佈")
        fig_ratings = plot_rating_comparison(usa_df)
        st.pyplot(fig_ratings)

        # 美國統計表
        st.subheader("📋 美國各主題統計數據")
        usa_stats = get_topic_statistics(usa_df)
        usa_stats_display = usa_stats.copy()
        usa_stats_display.index = [f"Topic {i}: {USA_TOPICS[i]['emoji']} {USA_TOPICS[i]['label_zh']}"
                                   for i in range(6)]
        st.dataframe(usa_stats_display, use_container_width=True)

        st.markdown("---")

        # 詳細評分分析
        st.subheader("🔍 各主題詳細評分分析")

        for topic_id in range(6):
            topic_info = USA_TOPICS[topic_id]
            topic_reviews = usa_df[usa_df['dominant_topic'] == topic_id]

            with st.expander(f"{topic_info['emoji']} Topic {topic_id}: {topic_info['label_zh']} ({len(topic_reviews)} reviews)"):
                col1, col2, col3, col4 = st.columns(4)

                with col1:
                    st.metric("平均評分", f"{topic_reviews['評分'].mean():.2f} ★")
                with col2:
                    st.metric("中位數", f"{topic_reviews['評分'].median():.1f} ★")
                with col3:
                    st.metric("標準差", f"{topic_reviews['評分'].std():.2f}")
                with col4:
                    st.metric("評論數", f"{len(topic_reviews):,}")

                # 評分分佈
                rating_counts = topic_reviews['評分'].value_counts().sort_index()
                fig, ax = plt.subplots(figsize=(8, 3))
                ax.bar(rating_counts.index, rating_counts.values,
                      color=COLORS['usa']['primary'], alpha=0.7)
                ax.set_xlabel('Rating (stars)')
                ax.set_ylabel('Count')
                ax.set_title(f'Rating Distribution for Topic {topic_id}')
                ax.grid(axis='y', alpha=0.3)
                st.pyplot(fig)

        st.markdown("---")

        # 跨文化比較重點
        st.subheader("🌍 跨文化評分比較重點")

        col1, col2 = st.columns(2)

        with col1:
            st.success("""
            ### ✅ 正面主題
            **🇹🇼 台灣**:
            - Topic 0: 醫療專業認可 (24.9%, 4.56★)
            - Topic 4: 手術治療成功 (9.6%, 4.38★)

            **🇺🇸 美國**:
            - Topic 4: 整體正面評價 (9.5%, 3.96★)

            **差異**: 台灣正面評價的評分更高
            """)

        with col2:
            st.error("""
            ### ❌ 負面主題
            **🇹🇼 台灣**:
            - Topic 2: 服務態度問題 (17.3%, 1.98★)
            - Topic 6: 急診與溝通 (10.3%, 2.34★)

            **🇺🇸 美國**:
            - Topic 5: 預約與帳單 (4.1%, 2.92★)
            - Topic 3: 護理照護品質 (14.7%, 3.08★)

            **差異**: 台灣負面評分更極端
            """)

if __name__ == "__main__":
    main()
