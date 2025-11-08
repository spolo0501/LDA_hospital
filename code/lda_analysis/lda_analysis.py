#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LDA主題模型分析程式
功能：自動探索最佳主題數量、訓練LDA模型、視覺化結果
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import pickle
import warnings
warnings.filterwarnings('ignore')

# Gensim相關
from gensim import corpora
from gensim.models import LdaModel, CoherenceModel
import gensim

# 視覺化
import pyLDAvis
import pyLDAvis.gensim_models as gensimvis

# 中文字型設定（matplotlib）
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'Microsoft JhengHei', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False


class LDAAnalyzer:
    """LDA主題模型分析器"""

    def __init__(self, data_file='./processed_data/combined_reviews.csv',
                 output_dir='./lda_results'):
        """
        初始化LDA分析器

        Args:
            data_file: 前處理後的資料檔案
            output_dir: 結果輸出目錄
        """
        self.data_file = Path(data_file)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

        # 建立子目錄
        (self.output_dir / 'models').mkdir(exist_ok=True)
        (self.output_dir / 'visualizations').mkdir(exist_ok=True)

        self.df = None
        self.texts = None
        self.dictionary = None
        self.corpus = None

    def load_data(self):
        """載入前處理後的資料"""
        print("\n載入前處理資料...")
        self.df = pd.read_csv(self.data_file)

        # 將tokens_str轉換回list
        self.texts = [text.split() for text in self.df['tokens_str']]

        print(f"✓ 已載入 {len(self.texts)} 筆評論")
        print(f"  平均詞數: {np.mean([len(t) for t in self.texts]):.2f}")

        return self

    def build_dictionary_corpus(self, min_freq=3, max_freq_ratio=0.5):
        """
        建立字典和語料庫

        Args:
            min_freq: 詞彙最小出現次數
            max_freq_ratio: 詞彙最大出現比例（文檔比例）
        """
        print("\n建立字典和語料庫...")

        # 建立字典
        self.dictionary = corpora.Dictionary(self.texts)

        # 原始字典大小
        original_size = len(self.dictionary)

        # 過濾極端詞彙
        self.dictionary.filter_extremes(
            no_below=min_freq,  # 至少出現在n個文檔中
            no_above=max_freq_ratio,  # 最多出現在x%的文檔中
            keep_n=None  # 保留所有通過過濾的詞
        )

        # 壓縮字典ID
        self.dictionary.compactify()

        print(f"  原始詞彙數: {original_size}")
        print(f"  過濾後詞彙數: {len(self.dictionary)}")
        print(f"  過濾參數: min_freq={min_freq}, max_freq_ratio={max_freq_ratio}")

        # 建立語料庫（Bag of Words）
        self.corpus = [self.dictionary.doc2bow(text) for text in self.texts]

        print(f"✓ 語料庫建立完成，共 {len(self.corpus)} 筆文檔")

        # 儲存字典
        dict_file = self.output_dir / 'models' / 'dictionary.pkl'
        with open(dict_file, 'wb') as f:
            pickle.dump(self.dictionary, f)

        return self

    def compute_coherence_perplexity(self, model):
        """
        計算模型評估指標

        Args:
            model: 訓練好的LDA模型

        Returns:
            (coherence_score, perplexity)
        """
        # Coherence Score (C_v) - 越高越好
        coherence_model = CoherenceModel(
            model=model,
            texts=self.texts,
            dictionary=self.dictionary,
            coherence='c_v'
        )
        coherence_score = coherence_model.get_coherence()

        # Perplexity - 越低越好
        perplexity = model.log_perplexity(self.corpus)

        return coherence_score, perplexity

    def find_optimal_topics(self, min_topics=2, max_topics=20, step=1,
                            alpha='symmetric', eta='auto', iterations=100):
        """
        自動尋找最佳主題數量

        Args:
            min_topics: 最小主題數
            max_topics: 最大主題數
            step: 步進
            alpha: 文檔-主題分布超參數
            eta: 主題-詞彙分布超參數
            iterations: 訓練迭代次數

        Returns:
            結果DataFrame
        """
        print(f"\n開始探索最佳主題數量 (從 {min_topics} 到 {max_topics})...")
        print("這可能需要一些時間，請耐心等候...")

        results = []
        topic_range = range(min_topics, max_topics + 1, step)

        for num_topics in topic_range:
            print(f"\n  訓練 {num_topics} 個主題的模型...")

            # 訓練模型
            lda_model = LdaModel(
                corpus=self.corpus,
                id2word=self.dictionary,
                num_topics=num_topics,
                alpha=alpha,
                eta=eta,
                iterations=iterations,
                passes=10,
                random_state=42,
                per_word_topics=True
            )

            # 計算評估指標
            coherence, perplexity = self.compute_coherence_perplexity(lda_model)

            results.append({
                'num_topics': num_topics,
                'coherence': coherence,
                'perplexity': perplexity
            })

            print(f"    Coherence: {coherence:.4f}, Perplexity: {perplexity:.4f}")

            # 儲存模型
            model_file = self.output_dir / 'models' / f'lda_model_{num_topics}topics.pkl'
            with open(model_file, 'wb') as f:
                pickle.dump(lda_model, f)

        # 轉換為DataFrame
        results_df = pd.DataFrame(results)

        # 儲存結果
        results_file = self.output_dir / 'topic_optimization_results.csv'
        results_df.to_csv(results_file, index=False, encoding='utf-8-sig')
        print(f"\n✓ 優化結果已儲存至: {results_file}")

        # 視覺化
        self._plot_optimization_results(results_df)

        # 推薦最佳主題數
        self._recommend_optimal_topics(results_df)

        return results_df

    def _plot_optimization_results(self, results_df):
        """繪製優化結果圖表"""
        fig, axes = plt.subplots(1, 2, figsize=(15, 5))

        # Coherence Score
        axes[0].plot(results_df['num_topics'], results_df['coherence'],
                     marker='o', linewidth=2, markersize=8)
        axes[0].set_xlabel('主題數量', fontsize=12)
        axes[0].set_ylabel('Coherence Score', fontsize=12)
        axes[0].set_title('Coherence Score vs 主題數量\n(越高越好)', fontsize=14)
        axes[0].grid(True, alpha=0.3)

        # 標註最大值
        max_idx = results_df['coherence'].idxmax()
        max_topics = results_df.loc[max_idx, 'num_topics']
        max_coherence = results_df.loc[max_idx, 'coherence']
        axes[0].scatter([max_topics], [max_coherence], color='red', s=200, zorder=5)
        axes[0].annotate(f'最大值: {max_topics}個主題',
                         xy=(max_topics, max_coherence),
                         xytext=(10, 10), textcoords='offset points',
                         fontsize=10, color='red',
                         bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.7))

        # Perplexity
        axes[1].plot(results_df['num_topics'], results_df['perplexity'],
                     marker='s', linewidth=2, markersize=8, color='orange')
        axes[1].set_xlabel('主題數量', fontsize=12)
        axes[1].set_ylabel('Perplexity', fontsize=12)
        axes[1].set_title('Perplexity vs 主題數量\n(越低越好)', fontsize=14)
        axes[1].grid(True, alpha=0.3)

        # 標註最小值
        min_idx = results_df['perplexity'].idxmin()
        min_topics = results_df.loc[min_idx, 'num_topics']
        min_perplexity = results_df.loc[min_idx, 'perplexity']
        axes[1].scatter([min_topics], [min_perplexity], color='red', s=200, zorder=5)
        axes[1].annotate(f'最小值: {min_topics}個主題',
                         xy=(min_topics, min_perplexity),
                         xytext=(10, -20), textcoords='offset points',
                         fontsize=10, color='red',
                         bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.7))

        plt.tight_layout()

        # 儲存圖表
        plot_file = self.output_dir / 'visualizations' / 'topic_optimization.png'
        plt.savefig(plot_file, dpi=300, bbox_inches='tight')
        print(f"✓ 優化圖表已儲存至: {plot_file}")

        plt.close()

    def _recommend_optimal_topics(self, results_df):
        """推薦最佳主題數"""
        print("\n" + "=" * 60)
        print("最佳主題數量推薦")
        print("=" * 60)

        # 根據Coherence Score最大值
        max_coherence_idx = results_df['coherence'].idxmax()
        best_by_coherence = results_df.loc[max_coherence_idx, 'num_topics']
        coherence_value = results_df.loc[max_coherence_idx, 'coherence']

        print(f"\n依據 Coherence Score: {int(best_by_coherence)} 個主題")
        print(f"  (Coherence Score = {coherence_value:.4f})")

        # 根據Perplexity最小值
        min_perplexity_idx = results_df['perplexity'].idxmin()
        best_by_perplexity = results_df.loc[min_perplexity_idx, 'num_topics']
        perplexity_value = results_df.loc[min_perplexity_idx, 'perplexity']

        print(f"\n依據 Perplexity: {int(best_by_perplexity)} 個主題")
        print(f"  (Perplexity = {perplexity_value:.4f})")

        # 尋找elbow point（coherence增長放緩的點）
        coherence_diff = results_df['coherence'].diff()
        if len(coherence_diff) > 2:
            # 找到增長率變化最大的點
            coherence_diff2 = coherence_diff.diff()
            elbow_idx = coherence_diff2.idxmax()
            if pd.notna(elbow_idx) and elbow_idx > 0:
                elbow_topics = results_df.loc[elbow_idx, 'num_topics']
                print(f"\n依據 Elbow Point: {int(elbow_topics)} 個主題")

        print("\n建議：")
        print(f"  推薦使用 {int(best_by_coherence)} 個主題進行後續分析")
        print(f"  您也可以嘗試 {int(best_by_coherence)-1} 到 {int(best_by_coherence)+1} 個主題之間的模型")
        print("=" * 60)

    def visualize_topics(self, num_topics, model=None):
        """
        視覺化特定主題數的LDA模型

        Args:
            num_topics: 主題數量
            model: 已訓練的模型（可選，若無則載入）
        """
        print(f"\n視覺化 {num_topics} 個主題的模型...")

        # 載入模型（如果沒有提供）
        if model is None:
            model_file = self.output_dir / 'models' / f'lda_model_{num_topics}topics.pkl'
            if not model_file.exists():
                print(f"錯誤：找不到模型檔案 {model_file}")
                return

            with open(model_file, 'rb') as f:
                model = pickle.load(f)

        # 1. 使用pyLDAvis產生互動式視覺化
        print("  生成互動式視覺化...")
        vis_data = gensimvis.prepare(model, self.corpus, self.dictionary, mds='mmds')

        html_file = self.output_dir / 'visualizations' / f'lda_vis_{num_topics}topics.html'
        pyLDAvis.save_html(vis_data, str(html_file))
        print(f"  ✓ 互動式視覺化已儲存至: {html_file}")

        # 2. 顯示各主題的top關鍵詞
        self._print_topic_keywords(model, num_topics)

        # 3. 生成詞雲
        self._generate_topic_wordclouds(model, num_topics)

    def _print_topic_keywords(self, model, num_topics, top_words=15):
        """顯示各主題的關鍵詞"""
        print(f"\n=== {num_topics} 個主題的關鍵詞 ===\n")

        topics_keywords = []

        for topic_id in range(num_topics):
            print(f"主題 {topic_id + 1}:")

            # 取得該主題的top詞彙
            words = model.show_topic(topic_id, topn=top_words)

            keywords = []
            for word, prob in words:
                keywords.append(f"{word}({prob:.3f})")
                print(f"  {word}: {prob:.4f}")

            topics_keywords.append({
                'topic_id': topic_id + 1,
                'keywords': ', '.join([w for w, p in words])
            })

            print()

        # 儲存關鍵詞到檔案
        keywords_df = pd.DataFrame(topics_keywords)
        keywords_file = self.output_dir / f'topic_keywords_{num_topics}topics.csv'
        keywords_df.to_csv(keywords_file, index=False, encoding='utf-8-sig')
        print(f"✓ 主題關鍵詞已儲存至: {keywords_file}")

    def _generate_topic_wordclouds(self, model, num_topics):
        """生成各主題的詞雲"""
        try:
            from wordcloud import WordCloud
        except ImportError:
            print("  [警告] 未安裝wordcloud套件，跳過詞雲生成")
            return

        print("\n生成主題詞雲...")

        # 計算合適的子圖佈局
        n_cols = min(3, num_topics)
        n_rows = (num_topics + n_cols - 1) // n_cols

        fig, axes = plt.subplots(n_rows, n_cols, figsize=(6 * n_cols, 5 * n_rows))

        if num_topics == 1:
            axes = [axes]
        else:
            axes = axes.flatten()

        for topic_id in range(num_topics):
            # 取得主題詞彙及權重
            words = dict(model.show_topic(topic_id, topn=50))

            # 生成詞雲
            wc = WordCloud(
                font_path='/System/Library/Fonts/Hiragino Sans GB.ttc',  # macOS中文字型
                width=800,
                height=600,
                background_color='white',
                max_words=50,
                relative_scaling=0.5,
                colormap='viridis'
            ).generate_from_frequencies(words)

            # 繪製
            axes[topic_id].imshow(wc, interpolation='bilinear')
            axes[topic_id].set_title(f'主題 {topic_id + 1}', fontsize=14, fontweight='bold')
            axes[topic_id].axis('off')

        # 隱藏多餘的子圖
        for idx in range(num_topics, len(axes)):
            axes[idx].axis('off')

        plt.tight_layout()

        # 儲存
        wordcloud_file = self.output_dir / 'visualizations' / f'topic_wordclouds_{num_topics}topics.png'
        plt.savefig(wordcloud_file, dpi=300, bbox_inches='tight')
        print(f"✓ 詞雲圖已儲存至: {wordcloud_file}")

        plt.close()

    def analyze_topic_distribution(self, num_topics, model=None):
        """
        分析主題分布

        Args:
            num_topics: 主題數量
            model: 已訓練的模型
        """
        print(f"\n分析主題分布...")

        # 載入模型
        if model is None:
            model_file = self.output_dir / 'models' / f'lda_model_{num_topics}topics.pkl'
            with open(model_file, 'rb') as f:
                model = pickle.load(f)

        # 為每個文檔分配主要主題
        doc_topics = []

        for doc_bow in self.corpus:
            topic_dist = model.get_document_topics(doc_bow)

            # 找到概率最高的主題
            if topic_dist:
                dominant_topic = max(topic_dist, key=lambda x: x[1])
                topic_id, topic_prob = dominant_topic
            else:
                topic_id, topic_prob = -1, 0.0

            doc_topics.append({
                'dominant_topic': topic_id + 1,  # 從1開始編號
                'topic_probability': topic_prob
            })

        # 加入原始資料
        topic_df = self.df.copy()
        topic_df['dominant_topic'] = [d['dominant_topic'] for d in doc_topics]
        topic_df['topic_probability'] = [d['topic_probability'] for d in doc_topics]

        # 儲存結果
        result_file = self.output_dir / f'documents_with_topics_{num_topics}topics.csv'
        topic_df.to_csv(result_file, index=False, encoding='utf-8-sig')
        print(f"✓ 文檔主題分配已儲存至: {result_file}")

        # 統計分析
        self._analyze_topic_statistics(topic_df, num_topics)

        return topic_df

    def _analyze_topic_statistics(self, topic_df, num_topics):
        """統計分析主題分布"""
        print("\n=== 主題分布統計 ===\n")

        # 各主題文檔數量
        topic_counts = topic_df['dominant_topic'].value_counts().sort_index()

        print("各主題評論數量:")
        for topic_id, count in topic_counts.items():
            percentage = count / len(topic_df) * 100
            print(f"  主題 {topic_id}: {count} 筆 ({percentage:.1f}%)")

        # 各醫院的主題分布
        print("\n各醫院主要主題:")
        hospital_topic = topic_df.groupby('hospital_name')['dominant_topic'].agg(
            lambda x: x.mode()[0] if len(x.mode()) > 0 else -1
        )

        for hospital, main_topic in hospital_topic.items():
            print(f"  {hospital}: 主題 {main_topic}")

        # 繪製主題分布圖
        self._plot_topic_distribution(topic_df, num_topics)

    def _plot_topic_distribution(self, topic_df, num_topics):
        """繪製主題分布圖"""
        fig, axes = plt.subplots(1, 2, figsize=(15, 5))

        # 1. 整體主題分布
        topic_counts = topic_df['dominant_topic'].value_counts().sort_index()
        axes[0].bar(topic_counts.index, topic_counts.values, color='skyblue', edgecolor='black')
        axes[0].set_xlabel('主題', fontsize=12)
        axes[0].set_ylabel('評論數量', fontsize=12)
        axes[0].set_title('各主題評論數量分布', fontsize=14)
        axes[0].grid(axis='y', alpha=0.3)

        # 加上數值標籤
        for i, v in enumerate(topic_counts.values):
            axes[0].text(topic_counts.index[i], v, str(v),
                        ha='center', va='bottom', fontsize=10)

        # 2. 主題概率分布（箱型圖）
        topic_probs = [topic_df[topic_df['dominant_topic'] == i]['topic_probability'].values
                       for i in range(1, num_topics + 1)]

        axes[1].boxplot(topic_probs, labels=range(1, num_topics + 1))
        axes[1].set_xlabel('主題', fontsize=12)
        axes[1].set_ylabel('主題概率', fontsize=12)
        axes[1].set_title('各主題的分配概率分布', fontsize=14)
        axes[1].grid(axis='y', alpha=0.3)

        plt.tight_layout()

        plot_file = self.output_dir / 'visualizations' / f'topic_distribution_{num_topics}topics.png'
        plt.savefig(plot_file, dpi=300, bbox_inches='tight')
        print(f"\n✓ 主題分布圖已儲存至: {plot_file}")

        plt.close()


def main():
    """主程式"""
    print("=" * 60)
    print("LDA主題模型分析")
    print("=" * 60)

    # 建立分析器
    analyzer = LDAAnalyzer(
        data_file='./processed_data/combined_reviews.csv',
        output_dir='./lda_results'
    )

    # 載入資料
    analyzer.load_data()

    # 建立字典和語料庫
    analyzer.build_dictionary_corpus(min_freq=3, max_freq_ratio=0.5)

    # 自動尋找最佳主題數（這會花較長時間）
    print("\n" + "=" * 60)
    print("開始探索最佳主題數量")
    print("=" * 60)

    results_df = analyzer.find_optimal_topics(
        min_topics=2,
        max_topics=15,  # 可調整範圍
        step=1,
        iterations=100
    )

    # 根據結果，選擇最佳主題數進行詳細分析
    best_num_topics = int(results_df.loc[results_df['coherence'].idxmax(), 'num_topics'])

    print(f"\n使用 {best_num_topics} 個主題進行詳細分析...")

    # 視覺化
    analyzer.visualize_topics(best_num_topics)

    # 分析主題分布
    analyzer.analyze_topic_distribution(best_num_topics)

    print("\n" + "=" * 60)
    print("LDA分析完成！")
    print("=" * 60)
    print("\n下一步：")
    print(f"1. 查看 ./lda_results/visualizations/lda_vis_{best_num_topics}topics.html 互動式視覺化")
    print(f"2. 檢視 ./lda_results/topic_keywords_{best_num_topics}topics.csv 為主題命名")
    print("3. 如需調整參數，執行 python optimize_lda.py")


if __name__ == '__main__':
    main()
