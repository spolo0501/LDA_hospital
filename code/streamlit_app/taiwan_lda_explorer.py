#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
台灣醫院 LDA 主題分析互動式應用程式
使用 Streamlit 建立互動式介面來探索和比較醫院評論的主題分佈
"""

import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import warnings
import jieba
import re
import os
warnings.filterwarnings('ignore')

# 設定 matplotlib 中文字體
# 在 Streamlit Cloud 上需要特殊處理
import matplotlib.font_manager as fm

def setup_chinese_font():
    """設定中文字型，支援本機和 Streamlit Cloud"""
    # 重新載入字型快取（重要！）
    fm._load_fontmanager(try_read_cache=False)

    # 嘗試使用系統字型
    available_fonts = [f.name for f in fm.fontManager.ttflist]

    # 優先順序列表
    chinese_fonts = [
        'Noto Sans CJK TC',  # Streamlit Cloud 透過 packages.txt 安裝
        'Noto Sans CJK SC',
        'Noto Sans TC',
        'Noto Sans SC',
        'Arial Unicode MS',  # macOS
        'Microsoft YaHei',   # Windows
        'SimHei',
        'STHeiti',
        'PingFang TC'
    ]

    # 找到第一個可用的字型
    selected_font = None
    for font in chinese_fonts:
        if font in available_fonts:
            selected_font = font
            plt.rcParams['font.sans-serif'] = [font]
            print(f"✅ 使用中文字型: {font}")
            break

    if selected_font is None:
        # 如果都找不到，嘗試使用路徑直接指定
        plt.rcParams['font.sans-serif'] = ['Noto Sans CJK TC', 'sans-serif']
        print("⚠️ 未找到預設中文字型，使用備用設定")
        # 顯示可用的字型（用於除錯）
        noto_fonts = [f for f in available_fonts if 'Noto' in f or 'CJK' in f]
        if noto_fonts:
            print(f"可用的 Noto/CJK 字型: {', '.join(noto_fonts[:5])}")

    plt.rcParams['axes.unicode_minus'] = False

setup_chinese_font()

# ============================================================================
# 頁面設定
# ============================================================================
st.set_page_config(
    page_title="台灣醫院 LDA 主題分析",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# 路徑設定
# ============================================================================
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# 支援展示模式（用於 Streamlit Cloud 部署）
# 本地開發：使用完整資料
# Streamlit Cloud：使用展示資料（透過環境變數或 secrets 設定）
# 自動偵測 Streamlit Cloud 環境
IS_STREAMLIT_CLOUD = os.getenv('STREAMLIT_SHARING_MODE') is not None or \
                      os.path.exists('/mount/src')

# 安全地檢查 secrets
USE_DEMO_FROM_SECRETS = False
try:
    USE_DEMO_FROM_SECRETS = st.secrets.get('USE_DEMO_DATA', False)
except Exception:
    pass

USE_DEMO = os.getenv('USE_DEMO_DATA', 'false').lower() == 'true' or \
           USE_DEMO_FROM_SECRETS or \
           IS_STREAMLIT_CLOUD

# 強制使用 demo 資料在 Streamlit Cloud
# 偵測 /mount/src 路徑（Streamlit Cloud 特徵）
if os.path.exists('/mount/src'):
    USE_DEMO = True

if USE_DEMO:
    DATA_DIR = BASE_DIR / "data_demo"
    RESULTS_DIR = BASE_DIR / "results_demo"
else:
    DATA_DIR = BASE_DIR / "data"
    RESULTS_DIR = BASE_DIR / "results"

RAW_DATA_DIR = DATA_DIR / "raw" / "taiwan"
PROCESSED_DATA_DIR = DATA_DIR / "processed" / "taiwan" if not USE_DEMO else DATA_DIR / "processed"

# ============================================================================
# 快取資料載入函數
# ============================================================================

@st.cache_data
def load_hospital_list():
    """載入醫院列表"""
    hospitals = []
    if RAW_DATA_DIR.exists():
        for file in sorted(RAW_DATA_DIR.glob("*.xlsx")):
            name_part = file.stem.split('_')
            if len(name_part) >= 2:
                hospital_name = name_part[1]
                hospitals.append(hospital_name)
    return hospitals

@st.cache_resource
def load_lda_model(k=7):
    """載入 LDA 模型"""
    model_dir = RESULTS_DIR / f"taiwan_lda_k{k}"
    model_path = model_dir / f"lda_k{k}_lda_model.pkl"

    if not model_path.exists():
        # 嘗試載入其他命名格式
        alt_paths = list(model_dir.glob("*lda_model.pkl"))
        if alt_paths:
            model_path = alt_paths[0]
        else:
            return None, None, None

    try:
        with open(model_path, 'rb') as f:
            loaded_data = pickle.load(f)

        # 檢查是否為字典格式（包含多個資訊）
        if isinstance(loaded_data, dict):
            if 'lda_model' in loaded_data:
                # 字典格式，提取 LDA 模型
                model = loaded_data['lda_model']
            else:
                st.error(f"模型檔案格式錯誤: 找不到 'lda_model' 鍵")
                st.error(f"可用的鍵: {list(loaded_data.keys())}")
                return None, None, None
        else:
            # 直接是模型物件
            model = loaded_data

        # 嘗試載入字典和語料庫
        dictionary = model.id2word if hasattr(model, 'id2word') else None

        return model, dictionary, model_path
    except Exception as e:
        st.error(f"載入模型時發生錯誤: {e}")
        return None, None, None

@st.cache_data
def load_analysis_results(k=7):
    """載入分析結果 Excel 檔案"""
    results_dir = RESULTS_DIR / f"taiwan_lda_k{k}" / "visualizations"
    results_path = results_dir / f"lda_k{k}_analysis_results.xlsx"

    if not results_path.exists():
        return None

    try:
        # 讀取所有 sheets
        excel_file = pd.ExcelFile(results_path)
        sheets = {}
        for sheet_name in excel_file.sheet_names:
            sheets[sheet_name] = pd.read_excel(excel_file, sheet_name=sheet_name)
        return sheets
    except Exception as e:
        st.error(f"載入分析結果時發生錯誤: {e}")
        return None

@st.cache_data
def load_reviews_data():
    """載入評論資料"""
    reviews_path = PROCESSED_DATA_DIR / "reviews_for_lda.txt"

    if not reviews_path.exists():
        return None

    try:
        reviews = []
        with open(reviews_path, 'r', encoding='utf-8') as f:
            for line in f:
                reviews.append(line.strip())
        return reviews
    except Exception as e:
        st.error(f"載入評論資料時發生錯誤: {e}")
        return None

@st.cache_data
def load_raw_hospital_data(hospital_name):
    """載入特定醫院的原始資料"""
    if RAW_DATA_DIR.exists():
        for file in RAW_DATA_DIR.glob("*.xlsx"):
            if hospital_name in file.stem:
                try:
                    df = pd.read_excel(file)
                    return df
                except Exception as e:
                    st.error(f"載入 {hospital_name} 資料時發生錯誤: {e}")
                    return None
    return None

@st.cache_data
def load_stopwords():
    """載入停用詞"""
    stopwords = set()
    stopwords_path = BASE_DIR / "stopwords_custom.txt"

    if stopwords_path.exists():
        with open(stopwords_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    stopwords.add(line)

    # 添加常見停用詞
    common_stopwords = ['的', '了', '在', '是', '我', '有', '和', '就', '不', '人', '都', '一', '一個', '上', '也', '很', '到', '說', '要', '去', '你', '會', '著', '沒有', '看', '好', '自己', '這']
    stopwords.update(common_stopwords)

    return stopwords

@st.cache_data
def load_all_reviews_with_ratings():
    """載入所有醫院的評論資料（包含評分）"""
    if not RAW_DATA_DIR.exists():
        return None

    all_reviews = []
    try:
        for file in sorted(RAW_DATA_DIR.glob("*.xlsx")):
            # 跳過分析結果檔案
            if 'analysis' in file.name or 'lda_k' in file.name:
                continue

            df = pd.read_excel(file)
            if 'review_text' in df.columns and 'rating' in df.columns:
                # 提取需要的欄位
                hospital_name = file.stem.split('_')[1] if '_' in file.stem else file.stem

                for _, row in df.iterrows():
                    # 確保 review_text 是字串且不為空
                    review_text = row['review_text']

                    # 處理各種資料類型
                    if pd.isna(review_text):
                        continue

                    # 轉換為字串
                    if not isinstance(review_text, str):
                        review_text = str(review_text)

                    # 去除空白並檢查是否為空
                    review_text = review_text.strip()
                    if not review_text:
                        continue

                    # 處理評分
                    rating = row['rating'] if pd.notna(row['rating']) else 0
                    if not isinstance(rating, (int, float)):
                        try:
                            rating = float(rating)
                        except:
                            rating = 0

                    # 處理評論者名稱
                    reviewer = row.get('reviewer_name', '匿名')
                    if pd.isna(reviewer):
                        reviewer = '匿名'
                    elif not isinstance(reviewer, str):
                        reviewer = str(reviewer)

                    # 處理日期
                    date = row.get('review_date', '')
                    if pd.isna(date):
                        date = ''
                    elif not isinstance(date, str):
                        date = str(date)

                    all_reviews.append({
                        'hospital': hospital_name,
                        'text': review_text,
                        'rating': rating,
                        'reviewer': reviewer,
                        'date': date
                    })

        return pd.DataFrame(all_reviews) if all_reviews else None
    except Exception as e:
        st.error(f"載入評論資料時發生錯誤: {e}")
        import traceback
        st.error(f"詳細錯誤: {traceback.format_exc()}")
        return None

def assign_topics_to_reviews(_model, dictionary, reviews_df):
    """將主題分配給評論（直接處理原始評論）"""
    if reviews_df is None or len(reviews_df) == 0:
        return None

    # 載入停用詞
    stopwords = load_stopwords()

    topic_assignments = []

    for _, row in reviews_df.iterrows():
        review_text = row['text']

        # 使用 jieba 進行分詞
        words = jieba.cut(review_text)

        # 過濾停用詞、單字符、數字
        filtered_words = [
            word for word in words
            if len(word) > 1 and
               word not in stopwords and
               not word.isdigit() and
               not re.match(r'^[a-zA-Z]+$', word)
        ]

        # 轉換為 bag-of-words
        bow = dictionary.doc2bow(filtered_words)

        if len(bow) == 0:
            # 如果沒有有效詞彙，分配到主題0，機率設為0
            topic_assignments.append({
                'topic_id': 0,
                'probability': 0.0
            })
            continue

        # 取得主題分佈
        topic_dist = _model.get_document_topics(bow, minimum_probability=0)

        # 找出主導主題
        if len(topic_dist) > 0:
            dominant_topic = max(topic_dist, key=lambda x: x[1])
            topic_assignments.append({
                'topic_id': dominant_topic[0],
                'probability': dominant_topic[1]
            })
        else:
            topic_assignments.append({
                'topic_id': 0,
                'probability': 0.0
            })

    # 加入主題資訊到 DataFrame
    reviews_df['topic_id'] = [t['topic_id'] for t in topic_assignments]
    reviews_df['topic_probability'] = [t['probability'] for t in topic_assignments]

    return reviews_df

# ============================================================================
# 分析函數
# ============================================================================

def get_topic_keywords(model, num_words=10):
    """取得每個主題的關鍵詞"""
    topics = []
    for topic_id in range(model.num_topics):
        topic_words = model.show_topic(topic_id, topn=num_words)
        topics.append({
            'topic_id': topic_id,
            'keywords': [word for word, _ in topic_words],
            'weights': [weight for _, weight in topic_words]
        })
    return topics

def calculate_hospital_topic_distribution(model, dictionary, hospital_reviews):
    """計算特定醫院的主題分佈"""
    if not hospital_reviews:
        return None

    topic_dist = np.zeros(model.num_topics)

    for review in hospital_reviews:
        # 將評論轉換為 bag-of-words
        bow = dictionary.doc2bow(review.split())
        # 取得主題分佈
        doc_topics = model.get_document_topics(bow)
        for topic_id, prob in doc_topics:
            topic_dist[topic_id] += prob

    # 正規化
    topic_dist = topic_dist / len(hospital_reviews)
    return topic_dist

# ============================================================================
# 視覺化函數
# ============================================================================

def plot_topic_keywords(topics, selected_topics=None, figsize=None):
    """繪製主題關鍵詞條狀圖"""
    if selected_topics is None:
        selected_topics = range(len(topics))

    n_topics = len(selected_topics)

    # 使用自定義尺寸或默認尺寸
    if figsize is None:
        figsize = (12, 3*n_topics)

    fig, axes = plt.subplots(n_topics, 1, figsize=figsize)

    if n_topics == 1:
        axes = [axes]

    for idx, topic_idx in enumerate(selected_topics):
        topic = topics[topic_idx]
        keywords = topic['keywords'][:10]
        weights = topic['weights'][:10]

        axes[idx].barh(keywords, weights, color='steelblue')
        axes[idx].set_xlabel('權重', fontsize=10)
        axes[idx].set_title(f'主題 {topic_idx}: {", ".join(keywords[:5])}...',
                           fontsize=12, fontweight='bold')
        axes[idx].invert_yaxis()

    plt.tight_layout()
    return fig

def plot_hospital_comparison(hospital_distributions, hospital_names, k=7):
    """繪製醫院主題分佈比較圖"""
    fig, ax = plt.subplots(figsize=(12, 6))

    x = np.arange(k)
    width = 0.8 / len(hospital_names)

    for idx, (hospital_name, dist) in enumerate(zip(hospital_names, hospital_distributions)):
        offset = (idx - len(hospital_names)/2) * width + width/2
        ax.bar(x + offset, dist, width, label=hospital_name, alpha=0.8)

    ax.set_xlabel('主題編號', fontsize=12)
    ax.set_ylabel('主題比例', fontsize=12)
    ax.set_title('醫院主題分佈比較', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels([f'主題{i}' for i in range(k)])
    ax.legend(loc='upper right')
    ax.grid(axis='y', alpha=0.3)

    plt.tight_layout()
    return fig

def plot_topic_heatmap(hospital_distributions, hospital_names, k=7):
    """繪製醫院-主題熱力圖"""
    fig, ax = plt.subplots(figsize=(10, len(hospital_names)*0.5 + 2))

    data = np.array(hospital_distributions)

    sns.heatmap(data,
                xticklabels=[f'主題{i}' for i in range(k)],
                yticklabels=hospital_names,
                cmap='YlOrRd',
                annot=True,
                fmt='.3f',
                cbar_kws={'label': '主題比例'},
                ax=ax)

    ax.set_title('醫院-主題分佈熱力圖', fontsize=14, fontweight='bold', pad=20)

    plt.tight_layout()
    return fig

# ============================================================================
# 主程式
# ============================================================================

def main():
    # 標題
    st.title("🏥 台灣醫院 LDA 主題分析系統")

    # 顯示展示模式提示
    if USE_DEMO:
        st.info("📊 展示模式：使用 5 家醫院資料進行展示 | 完整版本包含 26 家醫療中心")

    st.markdown("---")

    # 固定使用 K=7（已確定為最佳主題數）
    k_value = 7

    # 側邊欄
    with st.sidebar:
        st.header("⚙️ 導覽")

        # 功能選擇
        page = st.radio(
            "選擇分析模組",
            ["📊 主題總覽", "🔍 主題深入探索", "🏥 醫院評分比較", "📈 統計儀表板"],
            label_visibility="visible"
        )

        st.markdown("---")

        # 顯示模型資訊
        st.info(f"📌 使用模型：K=7 主題\n\n💡 首次載入需要幾秒鐘")

    # 載入模型
    with st.spinner(f"載入 K={k_value} 的 LDA 模型..."):
        model, dictionary, model_path = load_lda_model(k=k_value)

    if model is None:
        st.error(f"❌ 找不到 K={k_value} 的 LDA 模型！")
        st.info(f"請確認以下路徑存在模型檔案: {RESULTS_DIR / f'taiwan_lda_k{k_value}'}")
        return

    st.success(f"✅ 成功載入 K={k_value} 的 LDA 模型")

    # 根據選擇的頁面顯示不同內容
    if page == "📊 主題總覽":
        show_topic_overview(model, k_value)

    elif page == "🔍 主題深入探索":
        show_topic_exploration(model, k_value)

    elif page == "🏥 醫院評分比較":
        show_hospital_rating_comparison(model, dictionary, k_value)

    elif page == "📈 統計儀表板":
        show_statistics_dashboard(k_value)

# ============================================================================
# 各個頁面的顯示函數
# ============================================================================

def show_topic_overview(model, k_value):
    """顯示主題總覽頁面"""
    st.header("📊 主題總覽")

    # 取得主題關鍵詞（增加到 30 個）
    topics = get_topic_keywords(model, num_words=30)

    # 顯示選項
    col1, col2 = st.columns([1, 3])
    with col1:
        num_keywords = st.slider("顯示關鍵詞數量", 5, 30, 15)  # 預設15，最多30
    with col2:
        display_mode = st.radio(
            "顯示模式",
            ["表格", "視覺化"],
            horizontal=True
        )

    st.markdown("---")

    if display_mode == "表格":
        # 表格顯示
        for topic in topics:
            # 顯示更多關鍵詞在標題
            with st.expander(f"**主題 {topic['topic_id']}**: {', '.join(topic['keywords'][:8])}..."):
                topic_df = pd.DataFrame({
                    '關鍵詞': topic['keywords'][:num_keywords],
                    '權重': topic['weights'][:num_keywords]
                })
                st.dataframe(topic_df, use_container_width=True)
    else:
        # 視覺化顯示 - 縮小圖表
        col1, col2, col3 = st.columns([1, 1, 1])

        with col1:
            st.subheader("關鍵詞視覺化")
            fig = plot_topic_keywords(topics, figsize=(6, 12))
            st.pyplot(fig)
            plt.close()

        with col2:
            st.subheader("主題分佈")
            viz_dir = RESULTS_DIR / f"taiwan_lda_k{k_value}" / "visualizations"
            dist_path = viz_dir / f"lda_k{k_value}_distribution.png"
            if dist_path.exists():
                st.image(str(dist_path), use_container_width=True)
            else:
                st.info("暫無主題分佈圖")

        with col3:
            st.subheader("主題文字雲")
            viz_dir = RESULTS_DIR / f"taiwan_lda_k{k_value}" / "visualizations"
            wordcloud_path = viz_dir / f"lda_k{k_value}_wordclouds.png"
            if wordcloud_path.exists():
                st.image(str(wordcloud_path), use_container_width=True)
            else:
                st.info("暫無文字雲圖")

def show_hospital_rating_comparison(model, dictionary, k_value):
    """顯示醫院在各主題的評分比較"""
    st.header("🏥 醫院評分比較分析")

    st.markdown("""
    此頁面顯示不同醫院在各個主題的平均評分，幫助您了解：
    - 哪些醫院在特定服務面向（主題）表現較好
    - 各主題的整體評分趨勢
    - 醫院間的服務品質差異
    """)

    st.markdown("---")

    # 載入所有評論資料
    with st.spinner("載入評論資料並分析主題..."):
        reviews_df = load_all_reviews_with_ratings()

        if reviews_df is None or len(reviews_df) == 0:
            st.error("❌ 無法載入評論資料")
            return

        # 分配主題
        reviews_with_topics = assign_topics_to_reviews(model, model.id2word, reviews_df)

        if reviews_with_topics is None:
            st.error("❌ 無法進行主題分配")
            return

    st.success(f"✅ 成功分析 {len(reviews_with_topics)} 條評論")

    # 獲取所有醫院列表
    all_hospitals = sorted(reviews_with_topics['hospital'].unique())

    # 選擇要比較的醫院
    st.subheader("選擇要比較的醫院")
    selected_hospitals = st.multiselect(
        "選擇醫院（建議 3-8 家以便清楚比較）",
        all_hospitals,
        default=all_hospitals[:5] if len(all_hospitals) >= 5 else all_hospitals
    )

    if len(selected_hospitals) == 0:
        st.warning("⚠️ 請至少選擇 1 家醫院")
        return

    st.markdown("---")

    # 計算每家醫院在各主題的平均評分
    topic_ratings = []
    for hospital in selected_hospitals:
        hospital_data = reviews_with_topics[reviews_with_topics['hospital'] == hospital]
        hospital_ratings = []
        for topic_id in range(k_value):
            topic_data = hospital_data[hospital_data['topic_id'] == topic_id]
            if len(topic_data) > 0:
                avg_rating = topic_data['rating'].mean()
                count = len(topic_data)
            else:
                avg_rating = 0
                count = 0
            hospital_ratings.append({
                'hospital': hospital,
                'topic': topic_id,
                'avg_rating': avg_rating,
                'count': count
            })
        topic_ratings.extend(hospital_ratings)

    ratings_df = pd.DataFrame(topic_ratings)

    # 顯示選項
    viz_type = st.radio(
        "選擇視覺化類型",
        ["📊 分組長條圖", "🔥 熱力圖", "📈 折線圖"],
        horizontal=True
    )

    st.markdown("---")

    if viz_type == "📊 分組長條圖":
        # 分組長條圖：每個主題顯示各醫院評分
        st.subheader("各主題的醫院評分比較")

        fig, ax = plt.subplots(figsize=(14, 6))

        x = np.arange(k_value)
        width = 0.8 / len(selected_hospitals)

        for idx, hospital in enumerate(selected_hospitals):
            hospital_data = ratings_df[ratings_df['hospital'] == hospital]
            ratings = [hospital_data[hospital_data['topic'] == t]['avg_rating'].values[0] for t in range(k_value)]
            offset = (idx - len(selected_hospitals)/2) * width + width/2
            ax.bar(x + offset, ratings, width, label=hospital, alpha=0.8)

        ax.set_xlabel('主題編號', fontsize=12)
        ax.set_ylabel('平均評分（星級）', fontsize=12)
        ax.set_title('各主題的醫院平均評分比較', fontsize=14, fontweight='bold')
        ax.set_xticks(x)
        ax.set_xticklabels([f'主題 {i}' for i in range(k_value)])
        ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        ax.set_ylim(0, 5)
        ax.grid(axis='y', alpha=0.3)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    elif viz_type == "🔥 熱力圖":
        # 熱力圖：醫院 x 主題
        st.subheader("醫院-主題評分熱力圖")

        # 建立矩陣
        heatmap_data = []
        for hospital in selected_hospitals:
            hospital_data = ratings_df[ratings_df['hospital'] == hospital]
            ratings = [hospital_data[hospital_data['topic'] == t]['avg_rating'].values[0] for t in range(k_value)]
            heatmap_data.append(ratings)

        fig, ax = plt.subplots(figsize=(10, max(6, len(selected_hospitals)*0.5)))
        im = ax.imshow(heatmap_data, cmap='RdYlGn', aspect='auto', vmin=0, vmax=5)

        # 設定座標軸
        ax.set_xticks(np.arange(k_value))
        ax.set_yticks(np.arange(len(selected_hospitals)))
        ax.set_xticklabels([f'主題 {i}' for i in range(k_value)])
        ax.set_yticklabels(selected_hospitals)

        # 在格子中顯示數值
        for i in range(len(selected_hospitals)):
            for j in range(k_value):
                text = ax.text(j, i, f'{heatmap_data[i][j]:.2f}',
                             ha="center", va="center", color="black", fontsize=9)

        ax.set_title('醫院在各主題的平均評分', fontsize=14, fontweight='bold')
        fig.colorbar(im, ax=ax, label='平均評分（星級）')
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    else:  # 折線圖
        st.subheader("醫院評分趨勢比較")

        fig, ax = plt.subplots(figsize=(12, 6))

        for hospital in selected_hospitals:
            hospital_data = ratings_df[ratings_df['hospital'] == hospital]
            ratings = [hospital_data[hospital_data['topic'] == t]['avg_rating'].values[0] for t in range(k_value)]
            ax.plot(range(k_value), ratings, marker='o', label=hospital, linewidth=2)

        ax.set_xlabel('主題編號', fontsize=12)
        ax.set_ylabel('平均評分（星級）', fontsize=12)
        ax.set_title('各醫院在不同主題的評分趨勢', fontsize=14, fontweight='bold')
        ax.set_xticks(range(k_value))
        ax.set_xticklabels([f'主題 {i}' for i in range(k_value)])
        ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        ax.set_ylim(0, 5)
        ax.grid(True, alpha=0.3)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    # 顯示詳細數據表格
    st.markdown("---")
    with st.expander("📋 查看詳細評分數據", expanded=False):
        # 重新整理數據為表格格式
        pivot_df = ratings_df.pivot(index='hospital', columns='topic', values='avg_rating')
        pivot_df.columns = [f'主題 {i}' for i in range(k_value)]

        # 添加平均分列
        pivot_df['整體平均'] = pivot_df.mean(axis=1)

        # 只顯示選中的醫院
        pivot_df = pivot_df.loc[selected_hospitals]

        st.dataframe(pivot_df.style.format("{:.2f}").background_gradient(cmap='RdYlGn', vmin=0, vmax=5),
                    use_container_width=True)

        # 顯示評論數量
        st.markdown("#### 各主題的評論數量")
        count_pivot = ratings_df.pivot(index='hospital', columns='topic', values='count')
        count_pivot.columns = [f'主題 {i}' for i in range(k_value)]
        count_pivot = count_pivot.loc[selected_hospitals]
        st.dataframe(count_pivot, use_container_width=True)

def show_hospital_comparison(model, dictionary, k_value):
    """顯示醫院比較頁面（舊版，保留以防萬一）"""
    st.header("🏥 醫院比較分析")

    # 載入醫院列表
    hospitals = load_hospital_list()

    if not hospitals:
        st.error("❌ 找不到醫院資料！")
        return

    # 選擇要比較的醫院
    selected_hospitals = st.multiselect(
        "選擇要比較的醫院（建議選擇 2-5 家）",
        hospitals,
        default=hospitals[:3] if len(hospitals) >= 3 else hospitals
    )

    if len(selected_hospitals) < 2:
        st.warning("⚠️ 請至少選擇 2 家醫院進行比較")
        return

    st.markdown("---")

    # 載入評論資料
    with st.spinner("載入評論資料..."):
        all_reviews = load_reviews_data()

    if all_reviews is None:
        st.error("❌ 找不到評論資料！")
        return

    # 計算各醫院的主題分佈（這裡簡化處理，實際應該要有醫院標記）
    st.info("ℹ️ 注意：目前使用整體資料的主題分佈作為示範。完整版需要個別醫院的評論標記。")

    # 示範：使用模型的整體主題分佈
    topic_dist = np.zeros((len(selected_hospitals), model.num_topics))

    # 從分析結果載入（如果有的話）
    analysis_results = load_analysis_results(k=k_value)

    if analysis_results and 'topic_distribution' in analysis_results:
        st.success("✅ 已載入主題分佈資料")
        # 這裡可以進一步處理

    # 示範資料（隨機生成，實際應該從真實資料計算）
    for i in range(len(selected_hospitals)):
        # 生成隨機但合理的主題分佈
        np.random.seed(i * 42)  # 固定種子以保持一致性
        random_dist = np.random.dirichlet(np.ones(model.num_topics) * 5)
        topic_dist[i] = random_dist

    # 顯示視覺化選項
    viz_type = st.radio(
        "選擇視覺化類型",
        ["長條圖比較", "熱力圖"],
        horizontal=True
    )

    if viz_type == "長條圖比較":
        fig = plot_hospital_comparison(topic_dist, selected_hospitals, k=k_value)
        st.pyplot(fig)
        plt.close()
    else:
        fig = plot_topic_heatmap(topic_dist, selected_hospitals, k=k_value)
        st.pyplot(fig)
        plt.close()

    # 顯示數值表格
    with st.expander("📊 查看詳細數值"):
        dist_df = pd.DataFrame(
            topic_dist,
            columns=[f'主題{i}' for i in range(k_value)],
            index=selected_hospitals
        )
        st.dataframe(dist_df.style.format("{:.4f}"), use_container_width=True)

def show_topic_exploration(model, k_value):
    """顯示主題深入探索頁面"""
    st.header("🔍 主題深入探索")

    # 選擇要探索的主題
    topic_id = st.selectbox(
        "選擇主題",
        range(model.num_topics),
        format_func=lambda x: f"主題 {x}"
    )

    st.markdown("---")

    # 顯示主題關鍵詞（增加到30個）
    st.subheader(f"主題 {topic_id} - 關鍵詞與權重")
    topic_words = model.show_topic(topic_id, topn=30)
    topic_df = pd.DataFrame(topic_words, columns=['關鍵詞', '權重'])

    # 使用兩欄顯示表格，節省空間
    col1, col2 = st.columns(2)
    with col1:
        st.dataframe(topic_df.head(15), use_container_width=True, height=400)
    with col2:
        st.dataframe(topic_df.tail(15), use_container_width=True, height=400)

    # 新增：顯示該主題的評論
    st.markdown("---")
    st.subheader(f"📝 主題 {topic_id} 的代表性評論")

    with st.spinner("載入評論資料..."):
        # 載入評論資料
        reviews_df = load_all_reviews_with_ratings()

        if reviews_df is not None:
            # 分配主題（直接處理原始評論）
            reviews_with_topics = assign_topics_to_reviews(model, model.id2word, reviews_df)

            if reviews_with_topics is not None:
                # 篩選該主題的評論
                topic_reviews = reviews_with_topics[reviews_with_topics['topic_id'] == topic_id].copy()
                topic_reviews = topic_reviews.sort_values('topic_probability', ascending=False)

                # 顯示統計
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("評論數量", len(topic_reviews))
                with col2:
                    avg_rating = topic_reviews['rating'].mean()
                    st.metric("平均評分", f"{avg_rating:.2f} ⭐")
                with col3:
                    rating_dist = topic_reviews['rating'].value_counts().sort_index(ascending=False)
                    st.metric("最常見評分", f"{rating_dist.index[0]} 星")

                # 顯示評分分佈
                st.markdown("#### 評分分佈")
                rating_counts = topic_reviews['rating'].value_counts().sort_index(ascending=False)
                fig, ax = plt.subplots(figsize=(10, 4))
                ax.bar(rating_counts.index.astype(str), rating_counts.values, color='steelblue')
                ax.set_xlabel('評分（星級）')
                ax.set_ylabel('評論數量')
                ax.set_title(f'主題 {topic_id} 的評分分佈')
                plt.tight_layout()
                st.pyplot(fig)
                plt.close()

                # 顯示代表性評論
                st.markdown("#### 代表性評論（按主題相關度排序）")

                # 篩選條件
                col1, col2 = st.columns([1, 1])
                with col1:
                    selected_rating = st.selectbox(
                        "篩選評分",
                        ["全部"] + [f"{i} 星" for i in range(5, 0, -1)]
                    )
                with col2:
                    num_reviews = st.slider("顯示評論數量", 5, 50, 10)

                # 應用篩選
                filtered_reviews = topic_reviews.copy()
                if selected_rating != "全部":
                    rating_value = int(selected_rating.split()[0])
                    filtered_reviews = filtered_reviews[filtered_reviews['rating'] == rating_value]

                # 顯示評論（預設展開）
                if len(filtered_reviews) == 0:
                    st.info("🔍 此篩選條件下沒有評論")
                else:
                    for idx, (_, row) in enumerate(filtered_reviews.head(num_reviews).iterrows(), 1):
                        # 使用卡片式顯示，預設展開
                        with st.container():
                            st.markdown(f"#### 評論 {idx}")
                            col_meta1, col_meta2, col_meta3 = st.columns(3)
                            with col_meta1:
                                st.metric("評分", f"{row['rating']} ⭐")
                            with col_meta2:
                                st.metric("主題相關度", f"{row['topic_probability']:.1%}")
                            with col_meta3:
                                st.metric("醫院", "")
                                st.caption(row['hospital'])

                            st.markdown("**評論內容：**")
                            st.write(row['text'])

                            if row['date']:
                                st.caption(f"📅 日期: {row['date']}")

                            st.markdown("---")
            else:
                st.warning("無法分配主題到評論")
        else:
            st.info("💡 評論資料載入中或不可用。此功能需要原始評論資料。")

def show_statistics_dashboard(k_value):
    """顯示統計儀表板頁面"""
    st.header("📈 統計儀表板")

    # 載入預處理統計
    stats_path = PROCESSED_DATA_DIR / "preprocessing_stats.txt"

    if stats_path.exists():
        with open(stats_path, 'r', encoding='utf-8') as f:
            stats_content = f.read()

        # 解析統計資訊
        lines = stats_content.strip().split('\n')

        # 顯示總體統計
        st.subheader("📊 資料集統計")

        col1, col2, col3, col4 = st.columns(4)

        # 提取數字
        total_reviews = int(lines[2].split(': ')[1])
        num_hospitals = int(lines[3].split(': ')[1])
        avg_words = float(lines[4].split(': ')[1])

        col1.metric("總評論數", f"{total_reviews:,}")
        col2.metric("醫院數量", f"{num_hospitals}")
        col3.metric("平均詞數", f"{avg_words:.1f}")
        col4.metric("LDA 主題數", k_value)

        st.markdown("---")

        # 各醫院評論數量
        st.subheader("🏥 各醫院評論數量")

        # 找到醫院列表開始的行
        hospital_start_idx = None
        for i, line in enumerate(lines):
            if "=== 各醫院評論數量 ===" in line:
                hospital_start_idx = i + 2
                break

        if hospital_start_idx:
            hospital_data = []
            for line in lines[hospital_start_idx:]:
                if line.strip() and ':' in line:
                    parts = line.split(': ')
                    if len(parts) == 2:
                        hospital_data.append({
                            '醫院名稱': parts[0].strip(),
                            '評論數': int(parts[1].strip())
                        })

            if hospital_data:
                hospital_df = pd.DataFrame(hospital_data)
                hospital_df = hospital_df.sort_values('評論數', ascending=False)

                # 長條圖
                fig, ax = plt.subplots(figsize=(12, 8))
                ax.barh(hospital_df['醫院名稱'], hospital_df['評論數'], color='steelblue')
                ax.set_xlabel('評論數', fontsize=12)
                ax.set_title('各醫院評論數量分佈', fontsize=14, fontweight='bold')
                ax.invert_yaxis()
                ax.grid(axis='x', alpha=0.3)
                plt.tight_layout()
                st.pyplot(fig)
                plt.close()

                # 顯示表格
                with st.expander("📋 查看詳細數據"):
                    st.dataframe(hospital_df, use_container_width=True, height=400)

    # 載入現有的視覺化圖表
    st.markdown("---")
    st.subheader("📊 LDA 分析結果視覺化")

    viz_dir = RESULTS_DIR / f"taiwan_lda_k{k_value}" / "visualizations"
    if viz_dir.exists():
        col1, col2 = st.columns(2)

        with col1:
            dist_path = viz_dir / f"lda_k{k_value}_distribution.png"
            if dist_path.exists():
                st.image(str(dist_path), caption="主題分佈圖", use_container_width=True)

        with col2:
            heatmap_path = viz_dir / f"lda_k{k_value}_rating_heatmap.png"
            if heatmap_path.exists():
                st.image(str(heatmap_path), caption="評分熱力圖", use_container_width=True)

# ============================================================================
# 執行主程式
# ============================================================================

if __name__ == "__main__":
    main()
