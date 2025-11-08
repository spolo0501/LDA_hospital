# 📁 專案檔案結構總覽

**專案**: 美國頂級醫院 Google Maps 評論分析
**完成日期**: 2025-10-28

---

## 🗂️ 完整檔案結構

```
GoogleReviews/
│
├── 📊 資料檔案
│   ├── cleaned_data_no_dedup/
│   │   ├── final_cleaned_sample_no_dedup.csv      ⭐ 最終清理資料 (3,363條)
│   │   ├── cleaning_report_no_dedup.txt           清理報告
│   │   ├── step1_merged_raw.csv                   中間步驟1
│   │   ├── step2_removed_blank.csv                中間步驟2
│   │   ├── step3_recent_year.csv                  中間步驟3
│   │   ├── step4_no_dedup.csv                     中間步驟4
│   │   └── step5_length_filtered.csv              中間步驟5
│   │
│   └── cleaned_data/                              (去重版本 - 參考用)
│       └── final_cleaned_sample.csv               2,932條 (已去重)
│
├── 📈 分析結果
│   ├── eda_results/                               探索性資料分析
│   │   ├── eda_visualizations.png                 ⭐ 12個視覺化圖表
│   │   ├── correlation_matrix.png                 ⭐ 相關性矩陣
│   │   └── EDA_REPORT.md                          ⭐ 完整 EDA 報告
│   │
│   ├── topic_modeling_results/                    主題建模分析
│   │   ├── lda_topics_analysis.png                ⭐ LDA 主題分析圖
│   │   └── TOPIC_MODELING_REPORT.md               ⭐ 完整主題建模報告
│   │
│   └── sentiment_analysis_results/                情感分析
│       ├── sentiment_analysis.png                 ⭐ 9個情感分析圖表
│       ├── SENTIMENT_ANALYSIS_REPORT.md           ⭐ 完整情感分析報告
│       └── reviews_with_sentiment.csv             ⭐ 包含情感分數的完整資料
│
├── 📝 總結報告
│   ├── ANALYSIS_SUMMARY.md                        ⭐⭐⭐ 綜合總結報告 (最重要)
│   ├── QUICK_REFERENCE.md                         ⭐⭐ 快速參考指南
│   ├── FILE_STRUCTURE.md                          ⭐ 本文檔 - 檔案結構
│   ├── VERSION_COMPARISON.md                      資料版本對比
│   └── DATA_CLEANING_SUMMARY.md                   資料清理總結
│
├── 🔧 分析腳本
│   ├── eda_analysis.py                            EDA 分析腳本
│   ├── topic_modeling.py                          主題建模腳本
│   └── sentiment_analysis.py                      情感分析腳本
│
└── 🏥 原始資料
    └── hospital_reviews/                          (28 家醫院原始評論)
        ├── AdventHealth_Orlando.csv
        ├── Johns_Hopkins_MD.csv
        ├── Mayo_Clinic.csv
        └── ... (共28個檔案)
```

---

## 🎯 必讀檔案（按重要性排序）

### 📌 第一優先級（必讀）

1. **QUICK_REFERENCE.md** (5分鐘)
   - 快速了解核心發現
   - 四大負面痛點
   - 立即可執行的改善措施

2. **ANALYSIS_SUMMARY.md** (15-20分鐘)
   - 最完整的綜合報告
   - 所有分析結果匯總
   - 詳細的管理建議

### 📌 第二優先級（深入了解）

3. **eda_results/EDA_REPORT.md**
   - 探索性資料分析詳細報告
   - 評分分布、醫院分析、時間趨勢

4. **topic_modeling_results/TOPIC_MODELING_REPORT.md**
   - 主題建模詳細分析
   - 正面/負面主題關鍵詞

5. **sentiment_analysis_results/SENTIMENT_ANALYSIS_REPORT.md**
   - 情感分析詳細報告
   - VADER 與 TextBlob 比較

### 📌 第三優先級（視覺化）

6. **eda_results/eda_visualizations.png**
   - 12 個 EDA 視覺化圖表

7. **topic_modeling_results/lda_topics_analysis.png**
   - 主題分析視覺化

8. **sentiment_analysis_results/sentiment_analysis.png**
   - 9 個情感分析圖表

---

## 📊 資料檔案說明

### 主要資料檔案

| 檔案 | 說明 | 樣本數 | 用途 |
|------|------|--------|------|
| `cleaned_data_no_dedup/final_cleaned_sample_no_dedup.csv` | 最終清理資料（未去重） | 3,363 | ⭐ 主要分析檔案 |
| `sentiment_analysis_results/reviews_with_sentiment.csv` | 包含情感分數的完整資料 | 3,240 | ⭐ 含 VADER 和 TextBlob 分數 |
| `cleaned_data/final_cleaned_sample.csv` | 已去重版本（參考） | 2,932 | 參考用 |

### 資料欄位說明

**final_cleaned_sample_no_dedup.csv** 包含欄位：
- 序號, 評論ID, 作者, 評分, 評論內容
- 評論日期, 實際日期, 照片數, 語言
- 醫院名稱, 來源檔案, 評論長度

**reviews_with_sentiment.csv** 額外包含：
- textblob_polarity (TextBlob 情感極性)
- textblob_subjectivity (TextBlob 主觀性)
- textblob_sentiment (TextBlob 情感分類)
- vader_compound (VADER 綜合分數)
- vader_neg, vader_neu, vader_pos (VADER 各維度)
- vader_sentiment (VADER 情感分類)

---

## 🎨 視覺化圖表說明

### EDA 視覺化 (eda_visualizations.png)
包含 12 個圖表：
1. 評分分布（柱狀圖）
2. 評分分布（餅圖）
3. 評論長度分布
4. 評論長度箱形圖
5. 評分vs評論長度
6. 評分vs評論長度（箱形圖）
7. Top 10 醫院評論數量
8. Top 10 醫院平均評分
9. 時間序列（月度評論數）
10. 時間序列（月度平均評分）
11. 語言分布
12. 語言vs平均評分

### 主題建模視覺化 (lda_topics_analysis.png)
包含 4 個圖表：
1. 正面評論主題分布
2. 負面評論主題分布
3. 正面評論 Top 3 主題關鍵詞
4. 負面評論 Top 3 主題關鍵詞

### 情感分析視覺化 (sentiment_analysis.png)
包含 9 個圖表：
1. TextBlob Polarity vs 評分
2. TextBlob Polarity 分布（箱形圖）
3. TextBlob Subjectivity vs 評分
4. TextBlob 情感分類分布
5. 評分類別 vs TextBlob 情感（熱圖）
6. VADER Compound vs 評分
7. VADER Compound 分布（箱形圖）
8. VADER 情感分類分布
9. 評分類別 vs VADER 情感（熱圖）

---

## 🔄 重新生成分析

### 完整分析流程

```bash
# 1. 確保環境正確
./fix_ide_env.sh

# 2. 執行資料清理（如果需要）
python3 clean_and_merge_hospitals_no_dedup.py

# 3. 執行三個分析（按順序）
python3 eda_analysis.py
python3 topic_modeling.py
python3 sentiment_analysis.py
```

### 單獨執行分析

```bash
# 只執行 EDA
python3 eda_analysis.py

# 只執行主題建模
python3 topic_modeling.py

# 只執行情感分析
python3 sentiment_analysis.py
```

---

## 📥 如何使用這些檔案

### 🎯 情境 1: 管理層快速了解
```bash
# 閱讀順序：
1. QUICK_REFERENCE.md          (5分鐘)
2. ANALYSIS_SUMMARY.md          (15分鐘)
3. 查看視覺化圖表                (5分鐘)
   - eda_results/eda_visualizations.png
   - topic_modeling_results/lda_topics_analysis.png
```

### 🎯 情境 2: 部門主管深入分析
```bash
# 醫療服務部門：
1. topic_modeling_results/TOPIC_MODELING_REPORT.md
2. 關注負面主題分析

# 客服部門：
1. sentiment_analysis_results/SENTIMENT_ANALYSIS_REPORT.md
2. 關注溝通相關主題

# IT 部門：
1. sentiment_analysis_results/SENTIMENT_ANALYSIS_REPORT.md
2. 了解 VADER 自動監控系統
```

### 🎯 情境 3: 數據分析師研究
```bash
# 使用包含情感分數的完整資料：
sentiment_analysis_results/reviews_with_sentiment.csv

# 進行進階分析：
- 按醫院分組分析
- 時間序列分析
- 預測模型開發
- Aspect-Based Sentiment Analysis
```

---

## 💾 檔案大小參考

```
cleaned_data_no_dedup/final_cleaned_sample_no_dedup.csv    ~1.8 MB
sentiment_analysis_results/reviews_with_sentiment.csv       ~2.2 MB
eda_results/eda_visualizations.png                          ~800 KB
topic_modeling_results/lda_topics_analysis.png              ~600 KB
sentiment_analysis_results/sentiment_analysis.png           ~900 KB
ANALYSIS_SUMMARY.md                                         ~50 KB
```

---

## 🔍 快速搜尋指南

### 找特定醫院的評論
```bash
# 在 CSV 中搜尋特定醫院
grep "AdventHealth_Orlando" cleaned_data_no_dedup/final_cleaned_sample_no_dedup.csv
```

### 找特定主題的分析
```bash
# 搜尋等待時間相關內容
grep -i "waiting" ANALYSIS_SUMMARY.md

# 搜尋帳單相關內容
grep -i "bill" ANALYSIS_SUMMARY.md
```

### 找特定評分的評論
```python
import pandas as pd
df = pd.read_csv('sentiment_analysis_results/reviews_with_sentiment.csv')

# 找出所有1星評論
negative_reviews = df[df['評分'] == 1]

# 找出情感分數與評分不一致的評論
inconsistent = df[
    ((df['評分'] >= 4) & (df['vader_sentiment'] == 'Negative')) |
    ((df['評分'] <= 2) & (df['vader_sentiment'] == 'Positive'))
]
```

---

## ✅ 檔案完整性檢查

### 必要檔案清單

- [ ] ANALYSIS_SUMMARY.md
- [ ] QUICK_REFERENCE.md
- [ ] FILE_STRUCTURE.md (本文檔)
- [ ] cleaned_data_no_dedup/final_cleaned_sample_no_dedup.csv
- [ ] eda_results/eda_visualizations.png
- [ ] eda_results/EDA_REPORT.md
- [ ] topic_modeling_results/lda_topics_analysis.png
- [ ] topic_modeling_results/TOPIC_MODELING_REPORT.md
- [ ] sentiment_analysis_results/sentiment_analysis.png
- [ ] sentiment_analysis_results/SENTIMENT_ANALYSIS_REPORT.md
- [ ] sentiment_analysis_results/reviews_with_sentiment.csv

---

## 📞 技術支援

### 檔案損壞或遺失
所有分析都可以重新生成：
```bash
python3 eda_analysis.py
python3 topic_modeling.py
python3 sentiment_analysis.py
```

### 需要不同格式的輸出
- PDF: 可使用 Markdown 轉 PDF 工具
- Excel: CSV 可直接在 Excel 中開啟
- PowerPoint: 圖片可直接插入 PPT

---

**最後更新**: 2025-10-28
**版本**: 1.0
**狀態**: ✅ 完整

**🎊 所有檔案已準備就緒，開始使用吧！**
