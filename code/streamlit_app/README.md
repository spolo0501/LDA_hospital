# 台灣醫院 LDA 主題分析互動式應用程式

這是一個使用 Streamlit 建立的互動式應用程式，用於探索和分析台灣醫院評論的 LDA 主題模型結果。

## 功能特色

### 📊 主題總覽
- 顯示所有主題的關鍵詞和權重
- 支援表格和視覺化兩種顯示模式
- 可調整顯示的關鍵詞數量

### 🏥 醫院比較
- 選擇多家醫院進行主題分佈比較
- 提供長條圖和熱力圖兩種視覺化方式
- 詳細數值表格查看

### 🔍 主題深入探索
- 查看特定主題的詳細關鍵詞
- 視覺化呈現詞彙權重
- 顯示主題詞雲圖

### 📈 統計儀表板
- 資料集總體統計資訊
- 各醫院評論數量分佈
- LDA 分析結果視覺化

## 安裝需求

### 必要套件

```bash
pip install streamlit pandas numpy matplotlib seaborn gensim openpyxl
```

或使用專案的 requirements.txt：

```bash
pip install -r ../../requirements.txt
```

### Python 版本
- Python 3.8 或更高版本

## 使用方式

### 方法 1：使用啟動腳本（推薦）

```bash
# 給予執行權限（首次使用）
chmod +x run_app.sh

# 啟動應用程式
./run_app.sh
```

### 方法 2：直接使用 Streamlit

```bash
streamlit run taiwan_lda_explorer.py
```

### 方法 3：從專案根目錄啟動

```bash
cd /path/to/LDA_hospital
streamlit run code/streamlit_app/taiwan_lda_explorer.py
```

## 應用程式介面說明

### 側邊欄設定
- **主題數 (K) 選擇**：可選擇 3-10 個主題（預設為 7）
- **分析模組選擇**：切換不同的分析頁面

### 主要功能區
根據選擇的模組顯示不同的分析內容和互動元件

## 資料結構需求

應用程式需要以下資料檔案：

```
LDA_hospital/
├── data/
│   ├── raw/taiwan/              # 原始醫院評論資料 (*.xlsx)
│   └── processed/taiwan/
│       ├── reviews_for_lda.txt  # 處理後的評論文本
│       └── preprocessing_stats.txt  # 預處理統計
└── results/
    └── taiwan_lda_k[N]/         # K=N 的 LDA 分析結果
        ├── lda_k[N]_lda_model.pkl  # LDA 模型檔案
        └── visualizations/
            ├── lda_k[N]_analysis_results.xlsx
            ├── lda_k[N]_distribution.png
            ├── lda_k[N]_rating_heatmap.png
            └── lda_k[N]_wordclouds.png
```

## 功能擴充計畫

### 短期目標
- [ ] 加入個別醫院的主題分佈計算（需要評論-醫院對應資料）
- [ ] 新增評論搜尋和瀏覽功能
- [ ] 支援自訂主題標籤

### 中期目標
- [ ] 支援多個 K 值模型的比較
- [ ] 加入時間序列分析（如果有時間戳記資料）
- [ ] 新增評論情感分析整合

### 長期目標
- [ ] 整合台美醫院比較功能
- [ ] 支援模型參數調整和即時訓練
- [ ] 加入匯出報告功能

## 常見問題

### Q1: 找不到 LDA 模型檔案
**A**: 請確認 `results/taiwan_lda_k7/` 目錄下存在 `lda_k7_lda_model.pkl` 檔案。如果使用其他 K 值，請確認對應目錄存在。

### Q2: 中文字體顯示問題
**A**: 應用程式已設定使用 'Arial Unicode MS', 'Microsoft YaHei', 'SimHei' 等中文字體。如果仍有問題，請安裝對應的字體。

### Q3: 醫院比較功能顯示示範資料
**A**: 目前版本需要個別醫院的評論標記資料。完整版需要在評論資料中加入醫院 ID 欄位。

### Q4: 應用程式載入很慢
**A**: 首次載入會快取資料，後續會更快。如果持續緩慢，可能是模型檔案過大或資料量太多。

## 技術細節

### 快取機制
- 使用 `@st.cache_data` 快取資料載入
- 使用 `@st.cache_resource` 快取模型載入
- 大幅提升重複操作的速度

### 路徑管理
- 自動偵測專案根目錄
- 支援相對路徑和絕對路徑
- 相容不同的執行方式

## 授權與貢獻

本專案為學術研究用途。如有問題或建議，請聯繫專案負責人。

## 更新記錄

### v1.0.0 (2025-11-11)
- 初始版本發布
- 實作四大核心功能模組
- 支援 K=3-10 的主題數選擇
- 基礎的醫院比較功能

---

**最後更新**: 2025-11-11
**版本**: 1.0.0
**作者**: Simon
