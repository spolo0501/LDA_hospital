#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
結果分析與報告產生程式
功能：深度分析主題、產生Excel報告、醫院比較分析
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import pickle
from collections import Counter
import warnings
warnings.filterwarnings('ignore')

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'Microsoft JhengHei', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False


class ResultAnalyzer:
    """結果分析器"""

    def __init__(self, model_file, data_file='./processed_data/combined_reviews.csv',
                 output_dir='./final_results'):
        """
        初始化分析器

        Args:
            model_file: 訓練好的LDA模型檔案
            data_file: 前處理後的資料檔案
            output_dir: 結果輸出目錄
        """
        self.model_file = Path(model_file)
        self.data_file = Path(data_file)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

        # 載入模型和資料
        self.load_model()
        self.load_data()

    def load_model(self):
        """載入LDA模型"""
        print(f"\n載入模型: {self.model_file}")

        with open(self.model_file, 'rb') as f:
            model_data = pickle.load(f)

        # 處理不同格式的模型檔案
        if isinstance(model_data, dict):
            self.model = model_data.get('model')
            self.dictionary = model_data.get('dictionary')
            self.corpus = model_data.get('corpus')
        else:
            # 假設直接是模型物件
            self.model = model_data
            self.dictionary = None
            self.corpus = None

        self.num_topics = self.model.num_topics
        print(f"✓ 已載入 {self.num_topics} 個主題的模型")

    def load_data(self):
        """載入資料"""
        print(f"載入資料: {self.data_file}")
        self.df = pd.read_csv(self.data_file)
        self.texts = [text.split() for text in self.df['tokens_str']]

        # 如果模型沒有dictionary，重建
        if self.dictionary is None:
            from gensim import corpora
            self.dictionary = corpora.Dictionary(self.texts)
            self.dictionary.filter_extremes(no_below=3, no_above=0.5)
            self.dictionary.compactify()

        # 如果模型沒有corpus，重建
        if self.corpus is None:
            self.corpus = [self.dictionary.doc2bow(text) for text in self.texts]

        print(f"✓ 已載入 {len(self.df)} 筆評論\n")

    def assign_topics_to_documents(self):
        """為每個文檔分配主題"""
        print("為每筆評論分配主題...")

        doc_topics = []

        for idx, doc_bow in enumerate(self.corpus):
            # 取得該文檔的主題分布
            topic_dist = self.model.get_document_topics(doc_bow)

            if topic_dist:
                # 找到主要主題（概率最高）
                dominant_topic = max(topic_dist, key=lambda x: x[1])
                topic_id, topic_prob = dominant_topic

                # 取得所有主題的概率（用於完整分析）
                all_topics = {f'topic_{i+1}_prob': 0.0 for i in range(self.num_topics)}
                for tid, prob in topic_dist:
                    all_topics[f'topic_{tid+1}_prob'] = prob

            else:
                topic_id, topic_prob = -1, 0.0
                all_topics = {f'topic_{i+1}_prob': 0.0 for i in range(self.num_topics)}

            doc_topics.append({
                'dominant_topic': topic_id + 1,
                'dominant_topic_prob': topic_prob,
                **all_topics
            })

        # 加入原始DataFrame
        topic_df = pd.DataFrame(doc_topics)
        self.result_df = pd.concat([self.df.reset_index(drop=True), topic_df], axis=1)

        print(f"✓ 完成主題分配\n")
        return self.result_df

    def name_topics(self, custom_names=None):
        """
        為主題命名

        Args:
            custom_names: 自訂主題名稱字典，例如 {1: "服務態度", 2: "等候時間", ...}

        Returns:
            主題名稱映射字典
        """
        print("分析各主題關鍵詞並建議命名...\n")

        topic_names = {}

        for topic_id in range(self.num_topics):
            # 取得該主題的top關鍵詞
            words = self.model.show_topic(topic_id, topn=10)
            top_words = [w for w, p in words[:5]]

            # 如果有自訂名稱就使用，否則用關鍵詞
            if custom_names and (topic_id + 1) in custom_names:
                topic_name = custom_names[topic_id + 1]
            else:
                topic_name = f"主題{topic_id+1}"

            topic_names[topic_id + 1] = topic_name

            # 顯示建議
            print(f"主題 {topic_id+1}: {topic_name}")
            print(f"  關鍵詞: {', '.join(top_words)}")
            print()

        # 儲存主題名稱
        self.topic_names = topic_names

        # 加入主題名稱到結果DataFrame
        self.result_df['dominant_topic_name'] = self.result_df['dominant_topic'].map(topic_names)

        return topic_names

    def generate_topic_summary(self):
        """生成主題摘要統計"""
        print("生成主題摘要統計...\n")

        summary_data = []

        for topic_id in range(1, self.num_topics + 1):
            topic_docs = self.result_df[self.result_df['dominant_topic'] == topic_id]

            # 統計
            doc_count = len(topic_docs)
            doc_percentage = doc_count / len(self.result_df) * 100
            avg_prob = topic_docs['dominant_topic_prob'].mean()

            # 關鍵詞
            words = self.model.show_topic(topic_id - 1, topn=10)
            top_keywords = ', '.join([w for w, p in words[:10]])

            # 主題名稱
            topic_name = self.topic_names.get(topic_id, f"主題{topic_id}")

            summary_data.append({
                '主題ID': topic_id,
                '主題名稱': topic_name,
                '評論數量': doc_count,
                '佔比(%)': f"{doc_percentage:.2f}",
                '平均主題概率': f"{avg_prob:.3f}",
                '關鍵詞': top_keywords
            })

        summary_df = pd.DataFrame(summary_data)

        # 儲存摘要
        summary_file = self.output_dir / 'topic_summary.csv'
        summary_df.to_csv(summary_file, index=False, encoding='utf-8-sig')
        print(f"✓ 主題摘要已儲存至: {summary_file}\n")

        return summary_df

    def analyze_by_hospital(self):
        """各醫院的主題分布分析"""
        print("分析各醫院的主題分布...\n")

        hospital_topic_analysis = []

        for hospital in self.result_df['hospital_name'].unique():
            hospital_data = self.result_df[self.result_df['hospital_name'] == hospital]

            # 該醫院的主要主題
            topic_counts = hospital_data['dominant_topic'].value_counts()
            main_topic = topic_counts.idxmax() if len(topic_counts) > 0 else -1
            main_topic_name = self.topic_names.get(main_topic, "未知")
            main_topic_percentage = topic_counts.max() / len(hospital_data) * 100

            # 各主題分布
            topic_dist = {}
            for topic_id in range(1, self.num_topics + 1):
                count = len(hospital_data[hospital_data['dominant_topic'] == topic_id])
                percentage = count / len(hospital_data) * 100
                topic_dist[f'主題{topic_id}(%)'] = f"{percentage:.1f}"

            hospital_topic_analysis.append({
                '醫院名稱': hospital,
                '評論總數': len(hospital_data),
                '主要主題ID': main_topic,
                '主要主題名稱': main_topic_name,
                '主要主題佔比(%)': f"{main_topic_percentage:.1f}",
                **topic_dist
            })

        analysis_df = pd.DataFrame(hospital_topic_analysis)

        # 儲存分析結果
        hospital_file = self.output_dir / 'hospital_topic_analysis.csv'
        analysis_df.to_csv(hospital_file, index=False, encoding='utf-8-sig')
        print(f"✓ 醫院主題分析已儲存至: {hospital_file}\n")

        # 視覺化
        self._plot_hospital_topic_heatmap(analysis_df)

        return analysis_df

    def _plot_hospital_topic_heatmap(self, analysis_df):
        """繪製醫院-主題熱力圖"""
        # 準備數據
        topic_cols = [col for col in analysis_df.columns if col.startswith('主題') and col.endswith('(%)')]

        # 轉換為數值
        heatmap_data = analysis_df[['醫院名稱'] + topic_cols].copy()
        for col in topic_cols:
            heatmap_data[col] = heatmap_data[col].astype(float)

        heatmap_data = heatmap_data.set_index('醫院名稱')

        # 繪製熱力圖
        plt.figure(figsize=(12, max(8, len(analysis_df) * 0.5)))

        sns.heatmap(
            heatmap_data,
            annot=True,
            fmt='.1f',
            cmap='YlOrRd',
            cbar_kws={'label': '百分比(%)'},
            linewidths=0.5
        )

        plt.title('各醫院主題分布熱力圖', fontsize=16, fontweight='bold', pad=20)
        plt.xlabel('主題', fontsize=12)
        plt.ylabel('醫院', fontsize=12)
        plt.tight_layout()

        heatmap_file = self.output_dir / 'hospital_topic_heatmap.png'
        plt.savefig(heatmap_file, dpi=300, bbox_inches='tight')
        print(f"✓ 熱力圖已儲存至: {heatmap_file}\n")

        plt.close()

    def extract_representative_reviews(self, top_n=5):
        """
        提取各主題的代表性評論

        Args:
            top_n: 每個主題提取的評論數量
        """
        print(f"提取各主題的代表性評論 (每主題{top_n}筆)...\n")

        representative_reviews = []

        for topic_id in range(1, self.num_topics + 1):
            topic_name = self.topic_names.get(topic_id, f"主題{topic_id}")
            topic_docs = self.result_df[self.result_df['dominant_topic'] == topic_id]

            # 按主題概率排序，取前N筆
            top_docs = topic_docs.nlargest(top_n, 'dominant_topic_prob')

            for idx, row in top_docs.iterrows():
                representative_reviews.append({
                    '主題ID': topic_id,
                    '主題名稱': topic_name,
                    '主題概率': f"{row['dominant_topic_prob']:.3f}",
                    '醫院名稱': row['hospital_name'],
                    '評論內容': row['review_text'],
                    '評分': row.get('rating', 'N/A')
                })

        rep_df = pd.DataFrame(representative_reviews)

        # 儲存
        rep_file = self.output_dir / 'representative_reviews.csv'
        rep_df.to_csv(rep_file, index=False, encoding='utf-8-sig')
        print(f"✓ 代表性評論已儲存至: {rep_file}\n")

        return rep_df

    def generate_excel_report(self):
        """生成完整的Excel報告"""
        print("生成完整Excel報告...\n")

        excel_file = self.output_dir / 'LDA_analysis_report.xlsx'

        with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
            # Sheet 1: 主題摘要
            summary_df = self.generate_topic_summary()
            summary_df.to_excel(writer, sheet_name='主題摘要', index=False)

            # Sheet 2: 所有評論及其主題
            self.result_df.to_excel(writer, sheet_name='評論主題分配', index=False)

            # Sheet 3: 醫院主題分析
            hospital_df = self.analyze_by_hospital()
            hospital_df.to_excel(writer, sheet_name='醫院主題分析', index=False)

            # Sheet 4: 代表性評論
            rep_df = self.extract_representative_reviews(top_n=5)
            rep_df.to_excel(writer, sheet_name='代表性評論', index=False)

            # Sheet 5: 各主題關鍵詞詳細
            keywords_data = []
            for topic_id in range(self.num_topics):
                words = self.model.show_topic(topic_id, topn=20)
                topic_name = self.topic_names.get(topic_id + 1, f"主題{topic_id+1}")

                for rank, (word, prob) in enumerate(words, 1):
                    keywords_data.append({
                        '主題ID': topic_id + 1,
                        '主題名稱': topic_name,
                        '排名': rank,
                        '關鍵詞': word,
                        '權重': f"{prob:.4f}"
                    })

            keywords_df = pd.DataFrame(keywords_data)
            keywords_df.to_excel(writer, sheet_name='主題關鍵詞', index=False)

        print(f"✓ Excel報告已生成: {excel_file}\n")
        print("=" * 60)
        print("報告包含以下工作表:")
        print("  1. 主題摘要 - 各主題統計概覽")
        print("  2. 評論主題分配 - 每筆評論的主題")
        print("  3. 醫院主題分析 - 各醫院主題分布")
        print("  4. 代表性評論 - 各主題的典型評論")
        print("  5. 主題關鍵詞 - 各主題詳細關鍵詞")
        print("=" * 60)

    def visualize_all(self):
        """生成所有視覺化圖表"""
        print("\n生成視覺化圖表...\n")

        # 1. 主題分布圓餅圖
        self._plot_topic_pie_chart()

        # 2. 各主題平均評分（如果有rating欄位）
        if 'rating' in self.result_df.columns:
            self._plot_topic_ratings()

        # 3. 主題詞雲（已在lda_analysis.py生成）

        print("✓ 所有視覺化圖表已生成\n")

    def _plot_topic_pie_chart(self):
        """繪製主題分布圓餅圖"""
        topic_counts = self.result_df['dominant_topic'].value_counts().sort_index()

        labels = [self.topic_names.get(tid, f"主題{tid}") for tid in topic_counts.index]
        sizes = topic_counts.values

        fig, ax = plt.subplots(figsize=(10, 8))
        colors = plt.cm.Set3(range(len(labels)))

        wedges, texts, autotexts = ax.pie(
            sizes,
            labels=labels,
            autopct='%1.1f%%',
            colors=colors,
            startangle=90,
            textprops={'fontsize': 11}
        )

        # 美化百分比文字
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
            autotext.set_fontsize(10)

        ax.set_title('主題分布圓餅圖', fontsize=16, fontweight='bold', pad=20)

        plt.tight_layout()

        pie_file = self.output_dir / 'topic_distribution_pie.png'
        plt.savefig(pie_file, dpi=300, bbox_inches='tight')
        print(f"  ✓ 圓餅圖: {pie_file}")

        plt.close()

    def _plot_topic_ratings(self):
        """繪製各主題的平均評分"""
        # 移除無效評分
        valid_data = self.result_df[self.result_df['rating'].notna()].copy()

        if len(valid_data) == 0:
            print("  [跳過] 無有效評分資料")
            return

        # 計算各主題平均評分
        topic_ratings = valid_data.groupby('dominant_topic')['rating'].agg(['mean', 'count']).reset_index()
        topic_ratings['topic_name'] = topic_ratings['dominant_topic'].map(self.topic_names)

        # 繪圖
        fig, ax = plt.subplots(figsize=(12, 6))

        bars = ax.bar(
            topic_ratings['topic_name'],
            topic_ratings['mean'],
            color='steelblue',
            edgecolor='black',
            alpha=0.7
        )

        # 加上數值標籤
        for i, (bar, mean_val, count) in enumerate(zip(bars, topic_ratings['mean'], topic_ratings['count'])):
            height = bar.get_height()
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                height,
                f'{mean_val:.2f}\n(n={count})',
                ha='center',
                va='bottom',
                fontsize=9
            )

        ax.set_xlabel('主題', fontsize=12)
        ax.set_ylabel('平均評分', fontsize=12)
        ax.set_title('各主題平均評分', fontsize=16, fontweight='bold')
        ax.set_ylim(0, 5.5)
        ax.grid(axis='y', alpha=0.3)

        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        rating_file = self.output_dir / 'topic_average_ratings.png'
        plt.savefig(rating_file, dpi=300, bbox_inches='tight')
        print(f"  ✓ 評分圖: {rating_file}")

        plt.close()


def main():
    """主程式"""
    print("=" * 60)
    print("LDA分析結果報告產生")
    print("=" * 60)

    # 請使用者指定模型檔案
    print("\n請提供LDA模型檔案路徑:")
    print("範例: ./lda_results/models/lda_model_8topics.pkl")
    print("或: ./optimization_results/models/exp_1_model.pkl")

    model_path = input("\n模型檔案路徑: ").strip()

    if not model_path:
        print("未提供模型路徑，使用預設路徑...")
        model_path = './lda_results/models/lda_model_8topics.pkl'

    if not Path(model_path).exists():
        print(f"錯誤：找不到模型檔案 {model_path}")
        return

    # 建立分析器
    analyzer = ResultAnalyzer(
        model_file=model_path,
        data_file='./processed_data/combined_reviews.csv',
        output_dir='./final_results'
    )

    # 分配主題
    analyzer.assign_topics_to_documents()

    # 主題命名（可自訂）
    print("\n您可以為主題自訂名稱，或直接按Enter使用預設名稱")
    print("格式: 1:服務態度,2:等候時間,3:醫療品質")

    custom_input = input("\n自訂名稱 (可選): ").strip()

    custom_names = None
    if custom_input:
        try:
            custom_names = {}
            for pair in custom_input.split(','):
                tid, name = pair.split(':')
                custom_names[int(tid)] = name
        except:
            print("格式錯誤，使用預設名稱")
            custom_names = None

    analyzer.name_topics(custom_names)

    # 生成報告
    analyzer.generate_excel_report()

    # 視覺化
    analyzer.visualize_all()

    print("\n" + "=" * 60)
    print("分析完成！")
    print("=" * 60)
    print(f"\n所有結果已儲存至: {analyzer.output_dir}")


if __name__ == '__main__':
    main()
