#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
美國醫院評論 Gensim LDA 分析（7個主題）
與台灣分析使用相同方法與參數，確保可比較性
"""

import pickle
import pandas as pd
import numpy as np
from gensim.models import LdaModel
from gensim.models.coherencemodel import CoherenceModel
from gensim import corpora
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import warnings
warnings.filterwarnings('ignore')

# 英文文本處理
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# 下載必要的NLTK資源
print("下載NLTK資源...")
try:
    nltk.download('stopwords', quiet=True)
    nltk.download('punkt', quiet=True)
    nltk.download('wordnet', quiet=True)
    nltk.download('omw-1.4', quiet=True)
    nltk.download('punkt_tab', quiet=True)
    print("✓ NLTK資源準備完成")
except Exception as e:
    print(f"⚠️  NLTK下載警告: {e}")

# 設定英文字體
plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

def preprocess_english_text(text):
    """英文文本前處理"""
    # 轉小寫
    text = text.lower()

    # 移除URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)

    # 移除email
    text = re.sub(r'\S+@\S+', '', text)

    # 只保留字母和空格
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)

    # 移除多餘空格
    text = ' '.join(text.split())

    return text

def tokenize_and_lemmatize(text, stop_words):
    """分詞與詞形還原"""
    lemmatizer = WordNetLemmatizer()

    # 分詞
    tokens = word_tokenize(text)

    # 詞形還原並移除停用詞
    tokens = [lemmatizer.lemmatize(token) for token in tokens
              if token not in stop_words and len(token) > 2]

    return tokens

def train_and_analyze_lda(num_topics, output_prefix, df=None, dictionary=None, corpus=None, texts=None):
    """訓練指定主題數的LDA模型並生成分析報告"""

    print(f"\n{'='*60}")
    print(f"Training LDA Model with {num_topics} Topics")
    print(f"訓練 {num_topics} 個主題的 LDA 模型")
    print(f"{'='*60}\n")

    print(f"✓ Loaded {len(df)} reviews")
    print(f"✓ 已載入 {len(df)} 筆評論")

    # 訓練LDA模型（使用與台灣相同的參數）
    print(f"\nTraining {num_topics}-topic model...")
    print(f"訓練 {num_topics} 個主題的模型...")
    lda_model = LdaModel(
        corpus=corpus,
        id2word=dictionary,
        num_topics=num_topics,
        alpha='symmetric',      # 與台灣一致
        eta='auto',             # 與台灣一致
        iterations=100,         # 與台灣一致
        passes=10,              # 與台灣一致
        random_state=42         # 與台灣一致
    )

    # 計算coherence和perplexity
    coherence_model = CoherenceModel(
        model=lda_model,
        texts=texts,
        dictionary=dictionary,
        coherence='c_v'
    )
    coherence_score = coherence_model.get_coherence()
    perplexity_score = lda_model.log_perplexity(corpus)

    print(f"\nModel Quality Metrics:")
    print(f"  Coherence Score: {coherence_score:.4f}")
    print(f"  Perplexity: {perplexity_score:.4f}")

    # 顯示主題關鍵詞
    print(f"\nTopic Keywords:")
    print(f"主題關鍵詞:")
    print("-" * 60)
    topics_keywords = []
    for idx in range(num_topics):
        topic_words = lda_model.show_topic(idx, topn=10)
        keywords = ', '.join([word for word, prob in topic_words])
        topics_keywords.append({
            'topic_id': idx + 1,
            'keywords': keywords,
            'top_words': [word for word, prob in topic_words[:5]]
        })
        print(f"\nTopic {idx+1} | 主題 {idx+1}:")
        print(f"  {keywords}")

    # 為每篇評論分配主題
    print("\nAssigning topics to reviews...")
    print("為評論分配主題...")
    topic_assignments = []
    for doc_bow in corpus:
        topic_dist = lda_model.get_document_topics(doc_bow, minimum_probability=0)
        topic_probs = [prob for _, prob in topic_dist]
        dominant_topic = topic_probs.index(max(topic_probs)) + 1
        topic_assignments.append({
            'dominant_topic': dominant_topic,
            'topic_probability': max(topic_probs)
        })

    df_result = pd.concat([df.reset_index(drop=True), pd.DataFrame(topic_assignments)], axis=1)

    # 統計每個主題的評論數量和平均評分
    print("\nTopic Statistics:")
    print("主題統計:")
    print("-" * 60)
    topic_stats = df_result.groupby('dominant_topic').agg({
        '評分': ['count', 'mean']
    })
    topic_stats.columns = ['review_count', 'avg_rating']

    topic_summary = []
    for topic_id in range(1, num_topics + 1):
        if topic_id in topic_stats.index:
            count = topic_stats.loc[topic_id, 'review_count']
            rating = topic_stats.loc[topic_id, 'avg_rating']
            percentage = (count / len(df_result)) * 100

            topic_summary.append({
                'Topic_ID': topic_id,
                'Keywords': topics_keywords[topic_id-1]['keywords'],
                'Review_Count': int(count),
                'Percentage': f"{percentage:.1f}%",
                'Avg_Rating': f"{rating:.2f}"
            })

            print(f"\nTopic {topic_id} | 主題 {topic_id}:")
            print(f"  Reviews: {int(count)} ({percentage:.1f}%)")
            print(f"  評論數: {int(count)} ({percentage:.1f}%)")
            print(f"  Avg Rating: {rating:.2f} stars")
            print(f"  平均評分: {rating:.2f} 星")
            print(f"  Keywords: {topics_keywords[topic_id-1]['keywords']}")

    # 生成視覺化
    print("\nGenerating visualizations...")
    print("生成視覺化圖表...")

    # 1. 文字雲
    fig, axes = plt.subplots(3, 3, figsize=(20, 20))
    axes = axes.flatten()

    for idx in range(num_topics):
        topic_words = dict(lda_model.show_topic(idx, topn=50))
        wordcloud = WordCloud(
            width=400,
            height=400,
            background_color='white',
            colormap='viridis',
            relative_scaling=0.5,
            min_font_size=10
        ).generate_from_frequencies(topic_words)

        axes[idx].imshow(wordcloud, interpolation='bilinear')
        axes[idx].set_title(f'Topic {idx+1}\n主題 {idx+1}', fontsize=14, fontweight='bold')
        axes[idx].axis('off')

    # 隱藏多餘的子圖
    for idx in range(num_topics, len(axes)):
        axes[idx].axis('off')

    plt.tight_layout()
    plt.savefig(f'{output_prefix}_wordclouds.png', dpi=300, bbox_inches='tight')
    print(f"✓ Saved: {output_prefix}_wordclouds.png")
    plt.close()

    # 2. 主題分布圖
    fig, ax = plt.subplots(figsize=(12, 6))
    topic_counts = df_result['dominant_topic'].value_counts().sort_index()
    colors = plt.cm.Set3(np.linspace(0, 1, num_topics))

    bars = ax.bar(topic_counts.index, topic_counts.values, color=colors, edgecolor='black', linewidth=1.5)
    ax.set_xlabel('Topic ID | 主題編號', fontsize=12, fontweight='bold')
    ax.set_ylabel('Number of Reviews | 評論數量', fontsize=12, fontweight='bold')
    ax.set_title('Topic Distribution (USA Hospitals)\n主題分布（美國醫院）', fontsize=14, fontweight='bold')
    ax.set_xticks(range(1, num_topics + 1))
    ax.grid(axis='y', alpha=0.3, linestyle='--')

    # 添加數值標籤
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}\n({height/len(df_result)*100:.1f}%)',
                ha='center', va='bottom', fontsize=10)

    plt.tight_layout()
    plt.savefig(f'{output_prefix}_distribution.png', dpi=300, bbox_inches='tight')
    print(f"✓ Saved: {output_prefix}_distribution.png")
    plt.close()

    # 3. 評分熱力圖
    fig, ax = plt.subplots(figsize=(10, 6))
    rating_topic_matrix = pd.crosstab(
        df_result['dominant_topic'],
        df_result['評分'],
        normalize='index'
    ) * 100

    sns.heatmap(rating_topic_matrix, annot=True, fmt='.1f', cmap='RdYlGn',
                cbar_kws={'label': 'Percentage | 百分比 (%)'}, ax=ax)
    ax.set_xlabel('Rating (Stars) | 評分（星）', fontsize=12, fontweight='bold')
    ax.set_ylabel('Topic ID | 主題編號', fontsize=12, fontweight='bold')
    ax.set_title('Topic-Rating Heatmap (USA Hospitals)\n主題-評分熱力圖（美國醫院）',
                 fontsize=14, fontweight='bold')

    plt.tight_layout()
    plt.savefig(f'{output_prefix}_rating_heatmap.png', dpi=300, bbox_inches='tight')
    print(f"✓ Saved: {output_prefix}_rating_heatmap.png")
    plt.close()

    # 準備Excel輸出
    topic_summary_df = pd.DataFrame(topic_summary)

    # 選擇代表性評論
    representative_reviews = []
    for topic_id in range(1, num_topics + 1):
        topic_reviews = df_result[
            (df_result['dominant_topic'] == topic_id) &
            (df_result['topic_probability'] > 0.6)
        ].nlargest(5, 'topic_probability')

        for _, review in topic_reviews.iterrows():
            representative_reviews.append({
                'Topic': topic_id,
                'Hospital': review['醫院名稱'],
                'Rating': review['評分'],
                'Topic_Probability': f"{review['topic_probability']:.3f}",
                'Review_Content': review['評論內容'][:500]  # 限制長度
            })

    representative_df = pd.DataFrame(representative_reviews)

    # 醫院分析
    hospital_topic = df_result.groupby(['醫院名稱', 'dominant_topic']).size().unstack(fill_value=0)
    hospital_topic.columns = [f'Topic_{i}' for i in hospital_topic.columns]

    # 寫入Excel
    excel_file = f'{output_prefix}_analysis_results.xlsx'
    with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
        topic_summary_df.to_excel(writer, sheet_name='Topic_Summary', index=False)
        representative_df.to_excel(writer, sheet_name='Representative_Reviews', index=False)
        hospital_topic.to_excel(writer, sheet_name='Hospital_Topic_Distribution')

        # 調整列寬
        for sheet_name in writer.sheets:
            worksheet = writer.sheets[sheet_name]
            for column in worksheet.columns:
                max_length = 0
                column = [cell for cell in column]
                for cell in column:
                    try:
                        if len(str(cell.value)) > max_length:
                            max_length = len(str(cell.value))
                    except:
                        pass
                adjusted_width = min((max_length + 2) * 1.2, 80)
                worksheet.column_dimensions[column[0].column_letter].width = adjusted_width

    print(f"✓ Excel results saved: {excel_file}")
    print(f"✓ Excel結果已儲存: {excel_file}")

    # 儲存模型
    model_file = f'{output_prefix}_lda_model.pkl'
    with open(model_file, 'wb') as f:
        pickle.dump({
            'lda_model': lda_model,
            'dictionary': dictionary,
            'coherence_score': coherence_score,
            'perplexity_score': perplexity_score,
            'topics_keywords': topics_keywords,
            'topic_stats': topic_stats
        }, f)
    print(f"✓ Model saved: {model_file}")
    print(f"✓ 模型已儲存: {model_file}")

    print(f"\n{'='*60}")
    print(f"K={num_topics} Analysis Complete!")
    print(f"K={num_topics} 分析完成!")
    print(f"{'='*60}\n")

    return {
        'num_topics': num_topics,
        'coherence': coherence_score,
        'perplexity': perplexity_score,
        'topics': topics_keywords,
        'topic_summary': topic_summary
    }

if __name__ == "__main__":
    print("\n" + "="*60)
    print("USA Hospital Reviews - Gensim LDA Analysis (7 Topics)")
    print("美國醫院評論 - Gensim LDA 分析（7個主題）")
    print("="*60)

    # 載入資料
    print("\nLoading data...")
    print("載入資料...")
    df = pd.read_csv('cleaned_data_no_dedup/final_cleaned_sample_no_dedup.csv', encoding='utf-8-sig')
    print(f"✓ Loaded {len(df):,} reviews")
    print(f"✓ 已載入 {len(df):,} 筆評論")

    # 篩選英文評論
    df_en = df[df['語言'] == 'en'].copy()
    print(f"✓ English reviews: {len(df_en):,} ({len(df_en)/len(df)*100:.1f}%)")
    print(f"✓ 英文評論: {len(df_en):,} ({len(df_en)/len(df)*100:.1f}%)")

    # 文本前處理
    print("\nPreprocessing text...")
    print("文本前處理中...")

    # 英文停用詞
    stop_words = set(stopwords.words('english'))
    # 添加醫院相關常見詞（這些詞太通用，不具區分性）
    custom_stop_words = {'hospital', 'doctor', 'went', 'like', 'would', 'one', 'get', 'go'}
    stop_words.update(custom_stop_words)

    # 處理文本
    print("Processing reviews...")
    df_en['cleaned_text'] = df_en['評論內容'].apply(preprocess_english_text)
    df_en['tokens'] = df_en['cleaned_text'].apply(lambda x: tokenize_and_lemmatize(x, stop_words))

    # 移除空評論
    df_en = df_en[df_en['tokens'].str.len() > 0].copy()
    print(f"✓ Valid reviews after preprocessing: {len(df_en):,}")
    print(f"✓ 前處理後有效評論: {len(df_en):,}")

    texts = df_en['tokens'].tolist()
    print(f"  Average tokens per review: {np.mean([len(t) for t in texts]):.2f}")
    print(f"  平均每篇詞數: {np.mean([len(t) for t in texts]):.2f}")

    # 建立字典和語料庫
    print("\nBuilding dictionary and corpus...")
    print("建立字典和語料庫...")
    dictionary = corpora.Dictionary(texts)
    original_size = len(dictionary)

    # 過濾極端詞彙（與台灣使用相同參數）
    dictionary.filter_extremes(
        no_below=3,      # 至少出現在3個文檔中（與台灣一致）
        no_above=0.5,    # 最多出現在50%的文檔中（與台灣一致）
        keep_n=None
    )
    dictionary.compactify()

    print(f"  Original vocabulary size: {original_size}")
    print(f"  原始詞彙數: {original_size}")
    print(f"  Filtered vocabulary size: {len(dictionary)}")
    print(f"  過濾後詞彙數: {len(dictionary)}")

    # 建立語料庫（Bag of Words）
    corpus = [dictionary.doc2bow(text) for text in texts]
    print(f"✓ Corpus created with {len(corpus)} documents")
    print(f"✓ 語料庫建立完成，共 {len(corpus)} 筆文檔")

    # 訓練K=7的模型
    result = train_and_analyze_lda(7, 'usa_gensim_lda_k7', df=df_en,
                                   dictionary=dictionary, corpus=corpus, texts=texts)

    # 顯示最終結果摘要
    print("\n" + "="*60)
    print("Final Results Summary")
    print("最終結果摘要")
    print("="*60)

    print(f"\nNumber of Topics: {result['num_topics']}")
    print(f"主題數: {result['num_topics']}")
    print(f"Coherence Score: {result['coherence']:.4f}")
    print(f"Perplexity: {result['perplexity']:.4f}")

    print("\n7 Topics Keywords:")
    print("7個主題的關鍵詞:")
    print("-" * 60)
    for topic in result['topics']:
        print(f"  Topic {topic['topic_id']}: {', '.join(topic['top_words'])}")

    print("\nTopic Distribution:")
    print("主題分布:")
    print("-" * 60)
    for item in result['topic_summary']:
        print(f"  Topic {item['Topic_ID']}: {item['Review_Count']} reviews ({item['Percentage']}), "
              f"Avg Rating: {item['Avg_Rating']} stars")

    print("\n" + "="*60)
    print("Generated Files:")
    print("已生成以下研究成果檔案:")
    print("="*60)
    print("✓ usa_gensim_lda_k7_wordclouds.png - Word clouds for 7 topics")
    print("✓ usa_gensim_lda_k7_distribution.png - Topic distribution chart")
    print("✓ usa_gensim_lda_k7_rating_heatmap.png - Topic-rating heatmap")
    print("✓ usa_gensim_lda_k7_analysis_results.xlsx - Complete analysis results Excel file")
    print("    └─ Sheet 1: Topic Summary")
    print("    └─ Sheet 2: Representative Reviews")
    print("    └─ Sheet 3: Hospital Topic Distribution")
    print("✓ usa_gensim_lda_k7_lda_model.pkl - Trained LDA model file")
    print("="*60)
    print("\nAnalysis complete! All research outputs are ready.")
    print("分析完成！所有研究成果檔案已準備就緒。")
    print("\n🎊 Now Taiwan and USA analyses use the same methodology (Gensim LDA)!")
    print("🎊 現在台灣與美國分析使用相同方法（Gensim LDA）！")
