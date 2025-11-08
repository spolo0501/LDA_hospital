請先閱讀並理解專案的目錄架構規範：

1. **閱讀 CLAUDE.md**：這是專案的目錄架構規範文件，定義了所有檔案的存放位置
2. **閱讀 README.md**：了解專案的研究目標、主要成果和方法論

**專案概況**：
- 研究主題：台美醫院服務品質跨文化比較
- 方法：LDA 主題模型分析線上評論
- 現況：台灣和美國的 7-topic LDA 分析已完成

**核心規範**：
- 台灣原始資料 → `data/raw/taiwan/`
- 台灣LDA k7結果 → `results/taiwan_lda_k7/`
- 美國LDA k7結果 → `results/usa_lda_k7/`
- 比較結果 → `results/comparison/`
- 期刊論文 → `manuscripts/`
- 程式碼 → `code/[preprocessing|lda_analysis|comparison]/`

**接下來，請告訴我您想進行什麼任務，我將依照規範執行。**
