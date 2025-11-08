開始新的 LDA 分析前，請確認以下事項（依據 CLAUDE.md 規範）：

## 1. 資料位置確認
- 台灣原始資料：`data/raw/taiwan/*.xlsx`（26家醫院）
- 台灣處理後資料：`data/processed/taiwan/reviews_for_lda.txt`
- 美國原始資料：`data/raw/usa/`
- 美國處理後資料：`data/processed/usa/`

## 2. 程式碼存放
新的分析程式碼應存放於：
- 資料前處理：`code/preprocessing/`
- LDA 訓練分析：`code/lda_analysis/`
- 台美比較：`code/comparison/`

## 3. 結果儲存位置
- 台灣 k7 結果：`results/taiwan_lda_k7/`
- 美國 k7 結果：`results/usa_lda_k7/`
- 比較結果：`results/comparison/`

## 4. 主題數量選擇框架
依據本專案的方法論，選擇主題數量時應考慮：
1. 統計指標（Coherence, Perplexity）
2. 肘部法則
3. 可解釋性
4. 理論驗證（SERVQUAL等）
5. 分布平衡

**目前狀態**：台灣和美國都採用 K=7

## 5. 視覺化標準
- 主題分布圖
- 詞雲圖（每個主題）
- 評分熱力圖
- 醫院-主題分布圖

請告訴我：
1. 要分析哪個國家的資料？
2. 要進行什麼類型的分析？
3. 是否需要調整主題數量？

我將依照規範執行分析並儲存結果。
