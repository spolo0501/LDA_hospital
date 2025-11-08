#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
資料前處理程式
功能：合併25個醫院的Google評論資料，進行中文斷詞與清理
"""

import pandas as pd
import numpy as np
import jieba
import jieba.analyse
import re
import os
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')


class ReviewPreprocessor:
    """醫院評論資料前處理器"""

    def __init__(self, data_dir='.', output_dir='./processed_data'):
        """
        初始化前處理器

        Args:
            data_dir: Excel檔案所在目錄
            output_dir: 處理後資料輸出目錄
        """
        self.data_dir = Path(data_dir)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

        # 載入停用詞
        self.stopwords = self._load_stopwords()

        # 載入醫療專用詞典
        self._load_medical_dict()

    def _load_stopwords(self):
        """載入停用詞表"""
        stopwords = set()

        # 基本中文停用詞
        basic_stopwords = [
            '的', '了', '在', '是', '我', '有', '和', '就', '不', '人', '都', '一',
            '個', '上', '也', '很', '到', '說', '要', '去', '你', '會', '著', '沒',
            '看', '好', '自己', '這', '那', '裡', '什麼', '他', '她', '們', '為',
            '能', '他們', '以', '來', '被', '得', '可以', '這個', '已', '並', '等',
            '而', '還', '與', '對', '但', '或', '因為', '所以', '如果', '這樣',
            '那麼', '中', '後', '裡', '時', '把', '給', '讓', '當', '然', '種',
            '及', '與其', '再', '則', '向', '只', '由', '從', '將', '便', '其'
        ]
        stopwords.update(basic_stopwords)

        # 醫療領域特定停用詞（一些太常見但無意義的詞）
        medical_stopwords = [
            '醫院', '看病', '就醫', '真的', '覺得', '感覺', '非常', '十分',
            '蠻', '還是', '比較', '應該', '可能', '好像', '似乎', '大概',
            '已經', '還有', '而且', '不過', '但是', '所以', '因為', '如果',
            '雖然', '因此', '然後', '接著', '之後', '後來', '最後', '結果'
        ]
        stopwords.update(medical_stopwords)

        # 嘗試載入自訂停用詞檔案
        custom_stopwords_file = self.data_dir / 'stopwords_custom.txt'
        if custom_stopwords_file.exists():
            with open(custom_stopwords_file, 'r', encoding='utf-8') as f:
                custom_words = [line.strip() for line in f if line.strip()]
                stopwords.update(custom_words)
                print(f"✓ 已載入自訂停用詞：{len(custom_words)} 個")

        return stopwords

    def _load_medical_dict(self):
        """載入醫療專用詞典"""
        medical_terms = [
            # 科別
            '內科', '外科', '婦產科', '小兒科', '骨科', '眼科', '耳鼻喉科',
            '泌尿科', '皮膚科', '神經科', '精神科', '復健科', '家醫科', '急診',
            '牙科', '中醫科', '放射科', '病理科', '麻醉科', '整形外科',

            # 醫療人員
            '醫師', '醫生', '護理師', '護士', '藥師', '醫護人員', '櫃檯人員',
            '志工', '行政人員', '醫事人員',

            # 服務流程
            '掛號', '批價', '領藥', '繳費', '報到', '看診', '檢查', '治療',
            '住院', '出院', '複診', '初診', '轉診', '會診', '手術', '開刀',
            '急診', '門診', '預約', '候診', '叫號',

            # 設施設備
            '診間', '候診室', '急診室', '病房', '加護病房', '檢驗室', '藥局',
            '停車場', '電梯', '洗手間', '掛號處', '批價櫃檯',

            # 服務品質相關
            '態度', '專業', '效率', '等候時間', '服務品質', '醫療品質',
            '看診品質', '環境', '衛生', '清潔', '動線', '流程',

            # 檢查治療
            '抽血', '打針', '吃藥', '拿藥', '點滴', '超音波', '斷層掃描',
            'X光', 'CT', 'MRI', '內視鏡', '心電圖', '血壓', '體溫',

            # 疾病症狀
            '疼痛', '發燒', '咳嗽', '頭痛', '腹痛', '不舒服', '症狀', '病情',

            # 時間相關
            '等待', '久候', '排隊', '等很久', '等候', '時間', '快速', '迅速', '緩慢'
        ]

        # 將專業詞彙加入jieba詞典
        for term in medical_terms:
            jieba.add_word(term)

        # 嘗試載入自訂醫療詞典
        custom_dict_file = self.data_dir / 'medical_dict_custom.txt'
        if custom_dict_file.exists():
            jieba.load_userdict(str(custom_dict_file))
            print(f"✓ 已載入自訂醫療詞典")

    def clean_text(self, text):
        """
        清理文本

        Args:
            text: 原始文本

        Returns:
            清理後的文本
        """
        if pd.isna(text) or not isinstance(text, str):
            return ""

        # 移除網址
        text = re.sub(r'http\S+|www\S+', '', text)

        # 移除email
        text = re.sub(r'\S+@\S+', '', text)

        # 移除表情符號和特殊字元（保留中文、英文、數字、基本標點）
        text = re.sub(r'[^\u4e00-\u9fff\u3000-\u303fa-zA-Z0-9\s，。！？、；：「」『』（）\(\)\.。,]', '', text)

        # 移除多餘空白
        text = re.sub(r'\s+', ' ', text)

        # 移除過短的文本（少於5個字）
        if len(text.strip()) < 5:
            return ""

        return text.strip()

    def tokenize(self, text):
        """
        中文斷詞

        Args:
            text: 清理後的文本

        Returns:
            詞彙列表
        """
        if not text:
            return []

        # 使用jieba進行分詞
        words = jieba.cut(text)

        # 過濾停用詞、單字、數字
        filtered_words = [
            word.strip() for word in words
            if word.strip()
            and len(word.strip()) > 1  # 至少2個字元
            and word.strip() not in self.stopwords
            and not word.strip().isdigit()  # 排除純數字
            and not re.match(r'^[a-zA-Z]+$', word.strip())  # 排除純英文（可選）
        ]

        return filtered_words

    def load_all_reviews(self):
        """
        載入所有Excel檔案的評論資料

        Returns:
            合併後的DataFrame
        """
        all_reviews = []
        excel_files = sorted(self.data_dir.glob('*.xlsx'))

        print(f"\n開始載入 {len(excel_files)} 個Excel檔案...")

        for idx, file_path in enumerate(excel_files, 1):
            try:
                df = pd.read_excel(file_path)

                # 提取醫院名稱（從檔名）
                hospital_name = df['hospital_name'].iloc[0] if 'hospital_name' in df.columns else file_path.stem

                # 保留需要的欄位
                if 'review_text' in df.columns:
                    reviews_df = df[['review_text']].copy()
                    reviews_df['hospital_name'] = hospital_name
                    reviews_df['file_name'] = file_path.name

                    # 添加其他有用的欄位（如果存在）
                    for col in ['rating', 'review_date', 'reviewer_name']:
                        if col in df.columns:
                            reviews_df[col] = df[col]

                    all_reviews.append(reviews_df)
                    print(f"  [{idx}/{len(excel_files)}] {hospital_name}: {len(reviews_df)} 筆評論")

            except Exception as e:
                print(f"  [錯誤] 無法讀取 {file_path.name}: {str(e)}")

        # 合併所有資料
        combined_df = pd.concat(all_reviews, ignore_index=True)
        print(f"\n✓ 總共載入 {len(combined_df)} 筆評論")

        return combined_df

    def preprocess_reviews(self, df):
        """
        前處理所有評論

        Args:
            df: 包含評論的DataFrame

        Returns:
            處理後的DataFrame
        """
        print("\n開始前處理評論文字...")

        # 清理文本
        print("  1. 清理文本...")
        df['cleaned_text'] = df['review_text'].apply(self.clean_text)

        # 移除空白評論
        original_count = len(df)
        df = df[df['cleaned_text'] != ''].copy()
        removed_count = original_count - len(df)
        print(f"  2. 移除 {removed_count} 筆空白或過短評論，剩餘 {len(df)} 筆")

        # 斷詞
        print("  3. 進行中文斷詞...")
        df['tokens'] = df['cleaned_text'].apply(self.tokenize)

        # 計算詞數
        df['token_count'] = df['tokens'].apply(len)

        # 移除詞數過少的評論（少於3個詞）
        df = df[df['token_count'] >= 3].copy()
        print(f"  4. 移除詞數過少評論，最終保留 {len(df)} 筆有效評論")

        # 將tokens轉換為空格分隔的字串（方便後續LDA使用）
        df['tokens_str'] = df['tokens'].apply(lambda x: ' '.join(x))

        return df

    def save_processed_data(self, df):
        """
        儲存處理後的資料

        Args:
            df: 處理後的DataFrame
        """
        # 儲存完整資料（包含所有欄位）
        output_file = self.output_dir / 'combined_reviews.csv'
        df.to_csv(output_file, index=False, encoding='utf-8-sig')
        print(f"\n✓ 完整資料已儲存至: {output_file}")

        # 儲存僅用於LDA的文本資料
        lda_file = self.output_dir / 'reviews_for_lda.txt'
        with open(lda_file, 'w', encoding='utf-8') as f:
            for tokens_str in df['tokens_str']:
                f.write(tokens_str + '\n')
        print(f"✓ LDA訓練資料已儲存至: {lda_file}")

        # 儲存統計資訊
        stats_file = self.output_dir / 'preprocessing_stats.txt'
        with open(stats_file, 'w', encoding='utf-8') as f:
            f.write("=== 資料前處理統計 ===\n\n")
            f.write(f"總評論數: {len(df)}\n")
            f.write(f"醫院數量: {df['hospital_name'].nunique()}\n")
            f.write(f"平均詞數: {df['token_count'].mean():.2f}\n")
            f.write(f"詞數中位數: {df['token_count'].median():.2f}\n")
            f.write(f"最少詞數: {df['token_count'].min()}\n")
            f.write(f"最多詞數: {df['token_count'].max()}\n\n")
            f.write("=== 各醫院評論數量 ===\n\n")
            hospital_counts = df['hospital_name'].value_counts()
            for hospital, count in hospital_counts.items():
                f.write(f"{hospital}: {count}\n")
        print(f"✓ 統計資訊已儲存至: {stats_file}")

        # 產生詞頻統計
        self._generate_word_frequency(df)

    def _generate_word_frequency(self, df):
        """生成詞頻統計"""
        from collections import Counter

        # 統計所有詞彙
        all_words = []
        for tokens in df['tokens']:
            all_words.extend(tokens)

        word_freq = Counter(all_words)

        # 儲存top 200高頻詞
        freq_file = self.output_dir / 'word_frequency_top200.txt'
        with open(freq_file, 'w', encoding='utf-8') as f:
            f.write("排名\t詞彙\t出現次數\n")
            for idx, (word, count) in enumerate(word_freq.most_common(200), 1):
                f.write(f"{idx}\t{word}\t{count}\n")
        print(f"✓ 詞頻統計已儲存至: {freq_file}")

        print(f"\n=== Top 20 高頻詞 ===")
        for word, count in word_freq.most_common(20):
            print(f"  {word}: {count}")

    def run(self):
        """執行完整的前處理流程"""
        print("=" * 60)
        print("醫院評論資料前處理")
        print("=" * 60)

        # 載入資料
        df = self.load_all_reviews()

        # 前處理
        df = self.preprocess_reviews(df)

        # 儲存結果
        self.save_processed_data(df)

        print("\n" + "=" * 60)
        print("前處理完成！")
        print("=" * 60)

        return df


def main():
    """主程式"""
    # 建立前處理器並執行
    preprocessor = ReviewPreprocessor(
        data_dir='.',
        output_dir='./processed_data'
    )

    df = preprocessor.run()

    print("\n下一步：執行 python lda_analysis.py 進行主題模型分析")


if __name__ == '__main__':
    main()
