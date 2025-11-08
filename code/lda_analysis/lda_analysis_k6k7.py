#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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

# 設定中文字體
plt.rcParams['font.sans-serif'] = ['Hiragino Sans GB', 'Arial Unicode MS', 'STHeiti']
plt.rcParams['axes.unicode_minus'] = False

def train_and_analyze_lda(num_topics, output_prefix, df=None, dictionary=None, corpus=None, texts=None):
    """訓練指定主題數的LDA模型並生成分析報告"""

    print(f"\n{'='*60}")
    print(f"訓練 {num_topics} 個主題的 LDA 模型")
    print(f"{'='*60}\n")

    print(f"✓ 已載入 {len(df)} 筆評論")

    # 訓練LDA模型
    print(f"\n訓練 {num_topics} 個主題的模型...")
    lda_model = LdaModel(
        corpus=corpus,
        id2word=dictionary,
        num_topics=num_topics,
        alpha='symmetric',
        eta='auto',
        iterations=100,
        passes=10,
        random_state=42
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

    print(f"  Coherence Score: {coherence_score:.4f}")
    print(f"  Perplexity: {perplexity_score:.4f}")

    # 顯示主題關鍵詞
    print(f"\n主題關鍵詞:")
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
        print(f"\n主題 {idx+1}:")
        print(f"  {keywords}")

    # 為每篇評論分配主題
    print("\n為評論分配主題...")
    topic_assignments = []
    for doc_bow in corpus:
        topic_dist = lda_model.get_document_topics(doc_bow, minimum_probability=0)
        topic_probs = [prob for _, prob in topic_dist]
        dominant_topic = topic_probs.index(max(topic_probs)) + 1
        topic_assignments.append({
            'dominant_topic': dominant_topic,
            'topic_probability': max(topic_probs)
        })

    df_result = pd.concat([df, pd.DataFrame(topic_assignments)], axis=1)

    # 統計每個主題的評論數量和平均評分
    print("\n主題統計:")
    print("-" * 60)
    topic_stats = df_result.groupby('dominant_topic').agg({
        'hospital_name': 'count',
        'rating': 'mean'
    }).rename(columns={'hospital_name': 'review_count'})

    for topic_id in range(1, num_topics + 1):
        if topic_id in topic_stats.index:
            count = topic_stats.loc[topic_id, 'review_count']
            rating = topic_stats.loc[topic_id, 'rating']
            percentage = (count / len(df_result)) * 100
            print(f"\n主題 {topic_id}:")
            print(f"  評論數: {count} ({percentage:.1f}%)")
            print(f"  平均評分: {rating:.2f}")
            print(f"  關鍵詞: {topics_keywords[topic_id-1]['keywords']}")

    # 生成文字雲
    print("\n生成文字雲...")
    fig, axes = plt.subplots(2, (num_topics + 1) // 2, figsize=(20, 10))
    axes = axes.flatten()

    for idx in range(num_topics):
        topic_words = dict(lda_model.show_topic(idx, topn=30))
        wordcloud = WordCloud(
            font_path='/System/Library/Fonts/Hiragino Sans GB.ttc',
            width=800,
            height=400,
            background_color='white'
        ).generate_from_frequencies(topic_words)

        axes[idx].imshow(wordcloud, interpolation='bilinear')
        axes[idx].set_title(f'主題 {idx+1}', fontsize=14, fontweight='bold')
        axes[idx].axis('off')

    # 隱藏多餘的子圖
    for idx in range(num_topics, len(axes)):
        axes[idx].axis('off')

    plt.tight_layout()
    plt.savefig(f'{output_prefix}_wordclouds.png', dpi=300, bbox_inches='tight')
    print(f"✓ 文字雲已儲存: {output_prefix}_wordclouds.png")
    plt.close()

    # 主題分布圖
    print("生成主題分布圖...")
    topic_counts = df_result['dominant_topic'].value_counts().sort_index()

    plt.figure(figsize=(12, 6))
    bars = plt.bar(range(1, num_topics + 1), topic_counts.values)

    # 為每個柱子添加不同顏色
    colors = plt.cm.Set3(np.linspace(0, 1, num_topics))
    for bar, color in zip(bars, colors):
        bar.set_color(color)

    plt.xlabel('主題編號', fontsize=12)
    plt.ylabel('評論數量', fontsize=12)
    plt.title(f'{num_topics}個主題的評論分布', fontsize=14, fontweight='bold')
    plt.xticks(range(1, num_topics + 1))

    # 在柱子上添加百分比
    for i, (topic_id, count) in enumerate(topic_counts.items()):
        percentage = (count / len(df_result)) * 100
        plt.text(topic_id, count, f'{percentage:.1f}%',
                ha='center', va='bottom', fontsize=10)

    plt.tight_layout()
    plt.savefig(f'{output_prefix}_distribution.png', dpi=300, bbox_inches='tight')
    print(f"✓ 分布圖已儲存: {output_prefix}_distribution.png")
    plt.close()

    # 主題-評分熱力圖
    print("生成主題-評分關係圖...")
    plt.figure(figsize=(10, 6))

    topic_rating_data = []
    for topic_id in range(1, num_topics + 1):
        topic_df = df_result[df_result['dominant_topic'] == topic_id]
        rating_dist = topic_df['rating'].value_counts().sort_index()
        for rating in range(1, 6):
            count = rating_dist.get(rating, 0)
            topic_rating_data.append({
                'topic': f'主題{topic_id}',
                'rating': f'{rating}星',
                'count': count
            })

    heatmap_df = pd.DataFrame(topic_rating_data).pivot(
        index='topic', columns='rating', values='count'
    ).fillna(0)

    sns.heatmap(heatmap_df, annot=True, fmt='g', cmap='YlOrRd', cbar_kws={'label': '評論數量'})
    plt.title(f'{num_topics}個主題的評分分布熱力圖', fontsize=14, fontweight='bold')
    plt.xlabel('評分', fontsize=12)
    plt.ylabel('主題', fontsize=12)
    plt.tight_layout()
    plt.savefig(f'{output_prefix}_rating_heatmap.png', dpi=300, bbox_inches='tight')
    print(f"✓ 熱力圖已儲存: {output_prefix}_rating_heatmap.png")
    plt.close()

    # 儲存結果到Excel
    print("\n儲存結果到Excel...")

    # 準備主題摘要
    topic_summary = []
    for topic_id in range(1, num_topics + 1):
        if topic_id in topic_stats.index:
            topic_summary.append({
                '主題編號': topic_id,
                '關鍵詞': topics_keywords[topic_id-1]['keywords'],
                '評論數量': int(topic_stats.loc[topic_id, 'review_count']),
                '佔比': f"{(topic_stats.loc[topic_id, 'review_count'] / len(df_result) * 100):.1f}%",
                '平均評分': f"{topic_stats.loc[topic_id, 'rating']:.2f}"
            })

    topic_summary_df = pd.DataFrame(topic_summary)

    # 選擇代表性評論
    representative_reviews = []
    for topic_id in range(1, num_topics + 1):
        topic_reviews = df_result[
            (df_result['dominant_topic'] == topic_id) &
            (df_result['topic_probability'] > 0.8)
        ].nlargest(5, 'topic_probability')

        for _, review in topic_reviews.iterrows():
            representative_reviews.append({
                '主題': topic_id,
                '醫院': review['hospital_name'],
                '評分': review['rating'],
                '主題機率': f"{review['topic_probability']:.3f}",
                '評論內容': review['review_text']
            })

    representative_df = pd.DataFrame(representative_reviews)

    # 準備醫院分析
    hospital_topic = df_result.groupby(['hospital_name', 'dominant_topic']).size().unstack(fill_value=0)
    hospital_topic.columns = [f'主題{i}' for i in hospital_topic.columns]

    # 寫入Excel
    excel_file = f'{output_prefix}_analysis_results.xlsx'
    with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
        topic_summary_df.to_excel(writer, sheet_name='主題摘要', index=False)
        representative_df.to_excel(writer, sheet_name='代表性評論', index=False)
        hospital_topic.to_excel(writer, sheet_name='醫院主題分布')

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
                adjusted_width = min((max_length + 2) * 1.2, 50)
                worksheet.column_dimensions[column[0].column_letter].width = adjusted_width

    print(f"✓ Excel結果已儲存: {excel_file}")

    # 儲存模型
    model_file = f'{output_prefix}_lda_model.pkl'
    with open(model_file, 'wb') as f:
        pickle.dump({
            'lda_model': lda_model,
            'coherence_score': coherence_score,
            'perplexity_score': perplexity_score,
            'topics_keywords': topics_keywords,
            'topic_stats': topic_stats
        }, f)
    print(f"✓ 模型已儲存: {model_file}")

    print(f"\n{'='*60}")
    print(f"K={num_topics} 分析完成!")
    print(f"{'='*60}\n")

    return {
        'num_topics': num_topics,
        'coherence': coherence_score,
        'perplexity': perplexity_score,
        'topics': topics_keywords
    }

if __name__ == "__main__":
    print("\n" + "="*60)
    print("7 個构面的 LDA 主題分析")
    print("="*60)

    # 載入資料
    print("\n載入前處理資料...")
    df = pd.read_csv('../processed_data/combined_reviews.csv')

    # 將tokens_str轉換回list
    texts = [text.split() for text in df['tokens_str']]

    print(f"✓ 已載入 {len(texts)} 筆評論")
    print(f"  平均詞數: {np.mean([len(t) for t in texts]):.2f}")

    # 建立字典和語料庫
    print("\n建立字典和語料庫...")
    dictionary = corpora.Dictionary(texts)
    original_size = len(dictionary)

    # 過濾極端詞彙
    dictionary.filter_extremes(
        no_below=3,  # 至少出現在3個文檔中
        no_above=0.5,  # 最多出現在50%的文檔中
        keep_n=None
    )
    dictionary.compactify()

    print(f"  原始詞彙數: {original_size}")
    print(f"  過濾後詞彙數: {len(dictionary)}")

    # 建立語料庫（Bag of Words）
    corpus = [dictionary.doc2bow(text) for text in texts]
    print(f"✓ 語料庫建立完成，共 {len(corpus)} 筆文檔")

    # 訓練K=7的模型
    result = train_and_analyze_lda(7, 'lda_k7', df=df, dictionary=dictionary, corpus=corpus, texts=texts)

    # 顯示最終結果摘要
    print("\n" + "="*60)
    print("最終結果摘要")
    print("="*60)

    print(f"\n主題數: {result['num_topics']}")
    print(f"Coherence Score: {result['coherence']:.4f}")
    print(f"Perplexity: {result['perplexity']:.4f}")

    print("\n7個构面的關鍵詞:")
    print("-" * 60)
    for topic in result['topics']:
        print(f"  构面 {topic['topic_id']}: {', '.join(topic['top_words'])}")

    print("\n" + "="*60)
    print("已生成以下研究成果檔案:")
    print("="*60)
    print("✓ lda_k7_wordclouds.png - 7個构面的文字雲視覺化")
    print("✓ lda_k7_distribution.png - 构面評論數量分布圖")
    print("✓ lda_k7_rating_heatmap.png - 构面與評分關係熱力圖")
    print("✓ lda_k7_analysis_results.xlsx - 完整分析結果Excel檔案")
    print("    └─ 工作表1: 主題摘要（包含關鍵詞、評論數、佔比、平均評分）")
    print("    └─ 工作表2: 代表性評論（每個构面的高機率代表性評論）")
    print("    └─ 工作表3: 醫院主題分布（各醫院在不同构面的評論分布）")
    print("✓ lda_k7_lda_model.pkl - 訓練完成的LDA模型檔案")
    print("="*60)
    print("\n分析完成！所有研究成果檔案已準備就緒。")
