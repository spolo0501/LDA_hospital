#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LDA模型迭代優化程式
功能：參數網格搜尋、停用詞調整、多次實驗比較
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import pickle
import json
from datetime import datetime
from itertools import product
import warnings
warnings.filterwarnings('ignore')

from gensim import corpora
from gensim.models import LdaModel, CoherenceModel

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'Microsoft JhengHei', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False


class LDAOptimizer:
    """LDA模型優化器"""

    def __init__(self, data_file='./processed_data/combined_reviews.csv',
                 output_dir='./optimization_results'):
        """
        初始化優化器

        Args:
            data_file: 前處理後的資料檔案
            output_dir: 優化結果輸出目錄
        """
        self.data_file = Path(data_file)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

        # 建立子目錄
        (self.output_dir / 'models').mkdir(exist_ok=True)
        (self.output_dir / 'experiments').mkdir(exist_ok=True)

        self.df = None
        self.texts = None

    def load_data(self):
        """載入資料"""
        print("\n載入資料...")
        self.df = pd.read_csv(self.data_file)
        self.texts = [text.split() for text in self.df['tokens_str']]
        print(f"✓ 已載入 {len(self.texts)} 筆評論")
        return self

    def grid_search(self, num_topics_list, alpha_list, eta_list,
                    min_freq_list=[3], max_freq_ratio_list=[0.5],
                    iterations=100, passes=10):
        """
        參數網格搜尋

        Args:
            num_topics_list: 主題數量列表，例如 [5, 8, 10, 12]
            alpha_list: alpha參數列表，例如 ['symmetric', 'asymmetric', 0.01, 0.1]
            eta_list: eta參數列表，例如 ['auto', 'symmetric', 0.01, 0.1]
            min_freq_list: 最小詞頻列表
            max_freq_ratio_list: 最大詞頻比例列表
            iterations: 訓練迭代次數
            passes: 訓練輪數

        Returns:
            實驗結果DataFrame
        """
        print("\n" + "=" * 60)
        print("開始參數網格搜尋")
        print("=" * 60)

        # 產生所有參數組合
        param_combinations = list(product(
            num_topics_list, alpha_list, eta_list,
            min_freq_list, max_freq_ratio_list
        ))

        total_experiments = len(param_combinations)
        print(f"\n總共 {total_experiments} 組參數組合\n")

        results = []
        experiment_id = 0

        for num_topics, alpha, eta, min_freq, max_freq_ratio in param_combinations:
            experiment_id += 1

            print(f"[{experiment_id}/{total_experiments}] 訓練模型:")
            print(f"  主題數={num_topics}, alpha={alpha}, eta={eta}, "
                  f"min_freq={min_freq}, max_freq_ratio={max_freq_ratio}")

            try:
                # 建立字典和語料庫
                dictionary = corpora.Dictionary(self.texts)
                dictionary.filter_extremes(
                    no_below=min_freq,
                    no_above=max_freq_ratio
                )
                dictionary.compactify()
                corpus = [dictionary.doc2bow(text) for text in self.texts]

                # 訓練模型
                model = LdaModel(
                    corpus=corpus,
                    id2word=dictionary,
                    num_topics=num_topics,
                    alpha=alpha,
                    eta=eta,
                    iterations=iterations,
                    passes=passes,
                    random_state=42,
                    per_word_topics=True
                )

                # 計算評估指標
                coherence_model = CoherenceModel(
                    model=model,
                    texts=self.texts,
                    dictionary=dictionary,
                    coherence='c_v'
                )
                coherence = coherence_model.get_coherence()
                perplexity = model.log_perplexity(corpus)

                # 記錄結果
                result = {
                    'experiment_id': experiment_id,
                    'num_topics': num_topics,
                    'alpha': str(alpha),
                    'eta': str(eta),
                    'min_freq': min_freq,
                    'max_freq_ratio': max_freq_ratio,
                    'vocab_size': len(dictionary),
                    'coherence': coherence,
                    'perplexity': perplexity,
                    'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                }
                results.append(result)

                print(f"  ✓ Coherence={coherence:.4f}, Perplexity={perplexity:.4f}, "
                      f"詞彙數={len(dictionary)}\n")

                # 儲存模型
                model_file = self.output_dir / 'models' / f'exp_{experiment_id}_model.pkl'
                with open(model_file, 'wb') as f:
                    pickle.dump({
                        'model': model,
                        'dictionary': dictionary,
                        'corpus': corpus,
                        'params': result
                    }, f)

            except Exception as e:
                print(f"  ✗ 訓練失敗: {str(e)}\n")
                continue

        # 轉換為DataFrame並排序
        results_df = pd.DataFrame(results)
        results_df = results_df.sort_values('coherence', ascending=False)

        # 儲存結果
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        results_file = self.output_dir / f'grid_search_results_{timestamp}.csv'
        results_df.to_csv(results_file, index=False, encoding='utf-8-sig')

        print("=" * 60)
        print(f"✓ 網格搜尋完成！結果已儲存至: {results_file}")
        print("=" * 60)

        # 顯示最佳結果
        self._print_best_results(results_df)

        # 視覺化比較
        self._visualize_grid_search(results_df, timestamp)

        return results_df

    def _print_best_results(self, results_df, top_n=5):
        """顯示最佳結果"""
        print(f"\n=== Top {top_n} 最佳模型 (依據Coherence Score) ===\n")

        for idx, row in results_df.head(top_n).iterrows():
            print(f"第 {row['experiment_id']} 組實驗:")
            print(f"  主題數: {row['num_topics']}")
            print(f"  alpha: {row['alpha']}, eta: {row['eta']}")
            print(f"  min_freq: {row['min_freq']}, max_freq_ratio: {row['max_freq_ratio']}")
            print(f"  詞彙數: {row['vocab_size']}")
            print(f"  Coherence: {row['coherence']:.4f}")
            print(f"  Perplexity: {row['perplexity']:.4f}")
            print()

    def _visualize_grid_search(self, results_df, timestamp):
        """視覺化網格搜尋結果"""
        # 1. 不同主題數的coherence比較
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))

        # 按主題數分組
        topics_groups = results_df.groupby('num_topics')

        # 圖1: 各主題數的Coherence分布
        topics_coherence = topics_groups['coherence'].mean().sort_index()
        axes[0, 0].bar(topics_coherence.index, topics_coherence.values,
                       color='steelblue', edgecolor='black')
        axes[0, 0].set_xlabel('主題數量', fontsize=12)
        axes[0, 0].set_ylabel('平均 Coherence Score', fontsize=12)
        axes[0, 0].set_title('不同主題數的平均Coherence比較', fontsize=14)
        axes[0, 0].grid(axis='y', alpha=0.3)

        # 圖2: alpha參數影響
        if len(results_df['alpha'].unique()) > 1:
            alpha_coherence = results_df.groupby('alpha')['coherence'].mean().sort_values(ascending=False)
            axes[0, 1].barh(range(len(alpha_coherence)), alpha_coherence.values, color='coral')
            axes[0, 1].set_yticks(range(len(alpha_coherence)))
            axes[0, 1].set_yticklabels(alpha_coherence.index)
            axes[0, 1].set_xlabel('平均 Coherence Score', fontsize=12)
            axes[0, 1].set_title('不同alpha參數的平均Coherence比較', fontsize=14)
            axes[0, 1].grid(axis='x', alpha=0.3)
        else:
            axes[0, 1].text(0.5, 0.5, 'alpha參數無變化', ha='center', va='center', fontsize=14)
            axes[0, 1].axis('off')

        # 圖3: eta參數影響
        if len(results_df['eta'].unique()) > 1:
            eta_coherence = results_df.groupby('eta')['coherence'].mean().sort_values(ascending=False)
            axes[1, 0].barh(range(len(eta_coherence)), eta_coherence.values, color='lightgreen')
            axes[1, 0].set_yticks(range(len(eta_coherence)))
            axes[1, 0].set_yticklabels(eta_coherence.index)
            axes[1, 0].set_xlabel('平均 Coherence Score', fontsize=12)
            axes[1, 0].set_title('不同eta參數的平均Coherence比較', fontsize=14)
            axes[1, 0].grid(axis='x', alpha=0.3)
        else:
            axes[1, 0].text(0.5, 0.5, 'eta參數無變化', ha='center', va='center', fontsize=14)
            axes[1, 0].axis('off')

        # 圖4: Coherence vs Perplexity散點圖
        scatter = axes[1, 1].scatter(
            results_df['perplexity'],
            results_df['coherence'],
            c=results_df['num_topics'],
            cmap='viridis',
            s=100,
            alpha=0.6,
            edgecolors='black'
        )
        axes[1, 1].set_xlabel('Perplexity', fontsize=12)
        axes[1, 1].set_ylabel('Coherence Score', fontsize=12)
        axes[1, 1].set_title('Coherence vs Perplexity (顏色表示主題數)', fontsize=14)
        axes[1, 1].grid(True, alpha=0.3)

        # 加上顏色條
        cbar = plt.colorbar(scatter, ax=axes[1, 1])
        cbar.set_label('主題數量', fontsize=10)

        plt.tight_layout()

        plot_file = self.output_dir / f'grid_search_comparison_{timestamp}.png'
        plt.savefig(plot_file, dpi=300, bbox_inches='tight')
        print(f"✓ 視覺化圖表已儲存至: {plot_file}")

        plt.close()

    def test_custom_stopwords(self, additional_stopwords, num_topics=8,
                               alpha='symmetric', eta='auto'):
        """
        測試添加自訂停用詞的效果

        Args:
            additional_stopwords: 額外的停用詞列表
            num_topics: 主題數量
            alpha: alpha參數
            eta: eta參數

        Returns:
            (原始coherence, 新coherence, 改善幅度)
        """
        print(f"\n測試添加 {len(additional_stopwords)} 個停用詞的效果...")

        # 1. 原始模型（不加停用詞）
        print("\n訓練原始模型...")
        dictionary_orig = corpora.Dictionary(self.texts)
        dictionary_orig.filter_extremes(no_below=3, no_above=0.5)
        dictionary_orig.compactify()
        corpus_orig = [dictionary_orig.doc2bow(text) for text in self.texts]

        model_orig = LdaModel(
            corpus=corpus_orig,
            id2word=dictionary_orig,
            num_topics=num_topics,
            alpha=alpha,
            eta=eta,
            iterations=100,
            passes=10,
            random_state=42
        )

        coherence_orig = CoherenceModel(
            model=model_orig,
            texts=self.texts,
            dictionary=dictionary_orig,
            coherence='c_v'
        ).get_coherence()

        print(f"  原始Coherence: {coherence_orig:.4f}")
        print(f"  原始詞彙數: {len(dictionary_orig)}")

        # 2. 過濾停用詞後的模型
        print(f"\n過濾停用詞後訓練新模型...")

        texts_filtered = []
        for text in self.texts:
            filtered = [word for word in text if word not in additional_stopwords]
            texts_filtered.append(filtered)

        dictionary_new = corpora.Dictionary(texts_filtered)
        dictionary_new.filter_extremes(no_below=3, no_above=0.5)
        dictionary_new.compactify()
        corpus_new = [dictionary_new.doc2bow(text) for text in texts_filtered]

        model_new = LdaModel(
            corpus=corpus_new,
            id2word=dictionary_new,
            num_topics=num_topics,
            alpha=alpha,
            eta=eta,
            iterations=100,
            passes=10,
            random_state=42
        )

        coherence_new = CoherenceModel(
            model=model_new,
            texts=texts_filtered,
            dictionary=dictionary_new,
            coherence='c_v'
        ).get_coherence()

        print(f"  新Coherence: {coherence_new:.4f}")
        print(f"  新詞彙數: {len(dictionary_new)}")

        # 計算改善幅度
        improvement = (coherence_new - coherence_orig) / coherence_orig * 100

        print(f"\n改善幅度: {improvement:+.2f}%")

        if improvement > 0:
            print("✓ 添加停用詞有助於提升模型品質")
        else:
            print("✗ 添加停用詞反而降低模型品質，建議不要使用")

        return coherence_orig, coherence_new, improvement

    def interactive_stopword_tuning(self):
        """
        互動式停用詞調整

        允許使用者查看高頻詞、添加停用詞、重新訓練並比較結果
        """
        print("\n" + "=" * 60)
        print("互動式停用詞調整")
        print("=" * 60)

        # 顯示當前高頻詞
        from collections import Counter

        all_words = []
        for text in self.texts:
            all_words.extend(text)

        word_freq = Counter(all_words)

        print("\n=== 目前 Top 50 高頻詞 ===\n")
        for idx, (word, count) in enumerate(word_freq.most_common(50), 1):
            print(f"{idx:2d}. {word:10s} ({count:4d}次)")

        print("\n" + "=" * 60)
        print("建議檢查這些高頻詞，找出可能無意義的詞彙")
        print("然後將它們加入 stopwords_custom.txt 檔案")
        print("再重新執行 data_preprocessing.py")
        print("=" * 60)

        # 儲存高頻詞到檔案方便編輯
        freq_file = self.output_dir / 'high_frequency_words_for_review.txt'
        with open(freq_file, 'w', encoding='utf-8') as f:
            f.write("# 請檢查以下高頻詞，找出可能無意義的詞彙\n")
            f.write("# 將它們複製到 stopwords_custom.txt 中\n\n")
            for word, count in word_freq.most_common(100):
                f.write(f"{word}\t{count}\n")

        print(f"\n✓ 高頻詞列表已儲存至: {freq_file}")
        print("  您可以編輯此檔案，挑選要加入停用詞的詞彙")

    def compare_experiments(self, experiment_ids):
        """
        比較多個實驗結果

        Args:
            experiment_ids: 實驗ID列表
        """
        print(f"\n比較實驗: {experiment_ids}")

        models_data = []

        for exp_id in experiment_ids:
            model_file = self.output_dir / 'models' / f'exp_{exp_id}_model.pkl'

            if not model_file.exists():
                print(f"  [警告] 找不到實驗 {exp_id} 的模型")
                continue

            with open(model_file, 'rb') as f:
                data = pickle.load(f)
                models_data.append({
                    'exp_id': exp_id,
                    'model': data['model'],
                    'params': data['params']
                })

        if len(models_data) < 2:
            print("需要至少2個有效的實驗進行比較")
            return

        # 並排顯示各實驗的主題關鍵詞
        print("\n" + "=" * 80)
        print("各實驗的主題關鍵詞比較")
        print("=" * 80)

        for data in models_data:
            exp_id = data['exp_id']
            model = data['model']
            params = data['params']

            print(f"\n實驗 {exp_id}:")
            print(f"  參數: {params['num_topics']}主題, alpha={params['alpha']}, eta={params['eta']}")
            print(f"  Coherence: {params['coherence']:.4f}\n")

            for topic_id in range(params['num_topics']):
                words = model.show_topic(topic_id, topn=10)
                keywords = ', '.join([w for w, p in words])
                print(f"  主題{topic_id+1}: {keywords}")

            print()


def main():
    """主程式"""
    print("=" * 60)
    print("LDA模型優化")
    print("=" * 60)

    optimizer = LDAOptimizer(
        data_file='./processed_data/combined_reviews.csv',
        output_dir='./optimization_results'
    )

    optimizer.load_data()

    # 選項1: 參數網格搜尋
    print("\n請選擇優化方式:")
    print("1. 參數網格搜尋（推薦）")
    print("2. 互動式停用詞調整")
    print("3. 測試自訂停用詞效果")

    choice = input("\n請輸入選項 (1-3)，直接按Enter執行選項1: ").strip()

    if choice == '' or choice == '1':
        # 執行網格搜尋
        print("\n執行參數網格搜尋...")

        results_df = optimizer.grid_search(
            num_topics_list=[5, 6, 7, 8, 9, 10, 11, 12],  # 主題數範圍
            alpha_list=['symmetric', 'asymmetric'],  # alpha參數
            eta_list=['auto', 'symmetric'],  # eta參數
            min_freq_list=[3, 5],  # 最小詞頻
            max_freq_ratio_list=[0.4, 0.5, 0.6],  # 最大詞頻比例
            iterations=100,
            passes=10
        )

    elif choice == '2':
        # 互動式停用詞調整
        optimizer.interactive_stopword_tuning()

    elif choice == '3':
        # 測試自訂停用詞
        print("\n請輸入要測試的停用詞（以空格分隔）:")
        stopwords_input = input().strip()

        if stopwords_input:
            additional_stopwords = set(stopwords_input.split())
            optimizer.test_custom_stopwords(additional_stopwords)
        else:
            print("未輸入停用詞")

    else:
        print("無效選項")

    print("\n" + "=" * 60)
    print("優化完成！")
    print("=" * 60)


if __name__ == '__main__':
    main()
