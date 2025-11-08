#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
主題內涵驗證工具
自動化執行多種驗證分析
"""

import pandas as pd
import numpy as np
import pickle
from collections import Counter
from pathlib import Path


class TopicValidator:
    """主題驗證器"""

    def __init__(self, model_file, data_file, num_topics=5):
        """
        初始化驗證器

        Args:
            model_file: LDA模型檔案路徑
            data_file: 含主題分配的資料檔案
            num_topics: 主題數量
        """
        self.num_topics = num_topics

        # 載入模型
        with open(model_file, 'rb') as f:
            model_data = pickle.load(f)
            self.model = model_data if not isinstance(model_data, dict) else model_data['model']

        # 載入資料
        self.df = pd.read_csv(data_file)

        print(f"✓ 已載入模型（{num_topics}個主題）和資料（{len(self.df)}筆）\n")

    def extract_representative_reviews(self, top_n=10, min_prob=0.90):
        """
        提取各主題的代表性評論

        Args:
            top_n: 每個主題提取幾筆
            min_prob: 最小主題概率閾值

        Returns:
            dict: {topic_id: [reviews]}
        """
        print("=" * 80)
        print("驗證方法1：代表性文本分析")
        print("=" * 80)

        results = {}

        for topic_id in range(1, self.num_topics + 1):
            print(f"\n【主題 {topic_id}】")
            print("-" * 80)

            # 篩選該主題且概率高的評論
            topic_reviews = self.df[
                (self.df['dominant_topic'] == topic_id) &
                (self.df['topic_probability'] >= min_prob)
            ]

            if len(topic_reviews) == 0:
                print(f"  [警告] 無概率 ≥ {min_prob} 的評論，降低閾值至0.80")
                topic_reviews = self.df[
                    (self.df['dominant_topic'] == topic_id) &
                    (self.df['topic_probability'] >= 0.80)
                ]

            # 按概率排序取top_n
            top_reviews = topic_reviews.nlargest(top_n, 'topic_probability')

            results[topic_id] = []

            for idx, (_, row) in enumerate(top_reviews.iterrows(), 1):
                review_text = row['review_text']
                prob = row['topic_probability']
                rating = row['rating']

                results[topic_id].append({
                    'text': review_text,
                    'probability': prob,
                    'rating': rating
                })

                # 顯示前3筆
                if idx <= 3:
                    print(f"{idx}. 概率={prob:.3f} | 評分={rating}")
                    print(f"   {review_text[:120]}...")
                    print()

            print(f"  總計: {len(top_reviews)} 筆高概率評論（概率 ≥ {min_prob if len(topic_reviews) > 0 else 0.80}）")

        return results

    def analyze_keyword_overlap(self, top_k=10):
        """
        分析主題間關鍵詞重疊率

        Args:
            top_k: 比較前k個關鍵詞

        Returns:
            DataFrame: 重疊率矩陣
        """
        print("\n" + "=" * 80)
        print("驗證方法2：關鍵詞重疊分析（區分效度）")
        print("=" * 80)

        # 取得各主題的top-k關鍵詞
        topic_keywords = {}
        for topic_id in range(self.num_topics):
            words = self.model.show_topic(topic_id, topn=top_k)
            topic_keywords[topic_id + 1] = set([w for w, p in words])

        # 計算兩兩重疊
        overlap_matrix = pd.DataFrame(0,
                                      index=range(1, self.num_topics + 1),
                                      columns=range(1, self.num_topics + 1))

        overlaps = []

        for i in range(1, self.num_topics + 1):
            for j in range(i + 1, self.num_topics + 1):
                overlap = topic_keywords[i].intersection(topic_keywords[j])
                overlap_rate = len(overlap) / top_k
                overlap_matrix.loc[i, j] = overlap_rate
                overlap_matrix.loc[j, i] = overlap_rate

                overlaps.append({
                    'Topic_Pair': f'T{i}-T{j}',
                    'Overlap_Keywords': ', '.join(overlap) if overlap else '(無)',
                    'Overlap_Rate': f'{overlap_rate:.0%}'
                })

        # 顯示結果
        print(f"\n重疊率矩陣（Top-{top_k}關鍵詞）：\n")
        print(overlap_matrix.to_string())

        print("\n\n詳細重疊詞彙：\n")
        overlap_df = pd.DataFrame(overlaps)
        print(overlap_df.to_string(index=False))

        # 統計
        avg_overlap = overlap_df['Overlap_Rate'].apply(lambda x: float(x.strip('%')) / 100).mean()
        print(f"\n平均重疊率: {avg_overlap:.1%}")

        if avg_overlap < 0.15:
            print("✅ 結論：平均重疊率 < 15%，主題區分效度良好")
        elif avg_overlap < 0.25:
            print("⚠️  結論：平均重疊率介於15-25%，主題區分尚可")
        else:
            print("❌ 結論：平均重疊率 > 25%，主題可能有重疊問題")

        return overlap_df

    def analyze_topic_consistency(self):
        """
        分析主題內部一致性（透過評分變異數）
        """
        print("\n" + "=" * 80)
        print("驗證方法3：主題內部一致性分析")
        print("=" * 80)

        consistency_results = []

        for topic_id in range(1, self.num_topics + 1):
            topic_reviews = self.df[self.df['dominant_topic'] == topic_id]

            # 評分統計
            ratings = topic_reviews['rating'].dropna()
            mean_rating = ratings.mean()
            std_rating = ratings.std()

            # 主題概率統計
            probs = topic_reviews['topic_probability']
            mean_prob = probs.mean()

            consistency_results.append({
                'Topic': topic_id,
                'N_Reviews': len(topic_reviews),
                'Mean_Rating': f'{mean_rating:.2f}',
                'Std_Rating': f'{std_rating:.2f}',
                'Mean_Topic_Prob': f'{mean_prob:.3f}'
            })

        consistency_df = pd.DataFrame(consistency_results)
        print("\n主題內部統計：\n")
        print(consistency_df.to_string(index=False))

        print("\n✅ 解讀：")
        print("  - Mean_Topic_Prob 越高 → 主題分配越明確")
        print("  - Std_Rating 低 → 主題內評價一致（但正負向主題std自然會高）")

        return consistency_df

    def validate_topic_labels_with_keywords(self, custom_labels=None):
        """
        驗證主題標籤與關鍵詞的語義一致性

        Args:
            custom_labels: 自訂的主題標籤字典 {1: "標籤1", ...}
        """
        print("\n" + "=" * 80)
        print("驗證方法4：主題標籤與關鍵詞的語義一致性")
        print("=" * 80)

        if custom_labels is None:
            custom_labels = {
                1: "醫療診斷與檢查",
                2: "掛號流程與等候",
                3: "服務態度與溝通",
                4: "急診與特殊醫療",
                5: "專業品質與肯定"
            }

        for topic_id in range(1, self.num_topics + 1):
            print(f"\n主題 {topic_id}: {custom_labels[topic_id]}")
            print("-" * 60)

            # Top 15關鍵詞
            words = self.model.show_topic(topic_id - 1, topn=15)
            keywords_str = ', '.join([w for w, p in words])
            print(f"關鍵詞: {keywords_str}")

            # 人工判斷提示
            print(f"\n❓ 這些關鍵詞是否支持標籤「{custom_labels[topic_id]}」？")
            print("   （研究者需自行判斷並記錄於論文中）")

    def generate_validation_report(self, output_file='./final_results/topic_validation_report.txt'):
        """
        生成完整驗證報告
        """
        output_path = Path(output_file)
        output_path.parent.mkdir(exist_ok=True)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("=" * 80 + "\n")
            f.write("LDA主題內涵驗證報告\n")
            f.write("=" * 80 + "\n\n")

            # 方法1: 代表性評論
            f.write("## 驗證方法1：代表性文本分析\n\n")
            rep_reviews = self.extract_representative_reviews(top_n=5, min_prob=0.90)

            for topic_id, reviews in rep_reviews.items():
                f.write(f"### 主題 {topic_id}\n\n")
                for idx, review in enumerate(reviews[:3], 1):
                    f.write(f"{idx}. 概率={review['probability']:.3f}, 評分={review['rating']}\n")
                    f.write(f"   {review['text'][:200]}...\n\n")

            # 方法2: 關鍵詞重疊
            f.write("\n## 驗證方法2：關鍵詞重疊分析\n\n")
            overlap_df = self.analyze_keyword_overlap(top_k=10)
            f.write(overlap_df.to_string(index=False))
            f.write("\n\n")

            # 方法3: 內部一致性
            f.write("\n## 驗證方法3：主題內部一致性\n\n")
            consistency_df = self.analyze_topic_consistency()
            f.write(consistency_df.to_string(index=False))
            f.write("\n\n")

            f.write("=" * 80 + "\n")
            f.write("報告結束\n")

        print(f"\n\n✓ 完整驗證報告已儲存至: {output_path}")

    def run_all_validations(self):
        """執行所有驗證分析"""
        print("\n開始執行主題內涵驗證...\n")

        # 驗證1: 代表性評論
        self.extract_representative_reviews(top_n=5, min_prob=0.90)

        # 驗證2: 關鍵詞重疊
        self.analyze_keyword_overlap(top_k=10)

        # 驗證3: 內部一致性
        self.analyze_topic_consistency()

        # 驗證4: 標籤驗證
        self.validate_topic_labels_with_keywords()

        # 生成報告
        self.generate_validation_report()

        print("\n" + "=" * 80)
        print("所有驗證分析完成！")
        print("=" * 80)


def main():
    """主程式"""
    print("=" * 80)
    print("主題內涵驗證工具")
    print("=" * 80)

    validator = TopicValidator(
        model_file='./lda_results/models/lda_model_5topics.pkl',
        data_file='./lda_results/documents_with_topics_5topics.csv',
        num_topics=5
    )

    validator.run_all_validations()


if __name__ == '__main__':
    main()
