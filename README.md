# 台美醫院服務品質跨文化比較研究

> **Hospital Service Quality Cross-Cultural Comparison: Taiwan vs. USA**
> Using Latent Dirichlet Allocation (LDA) Topic Modeling on Online Reviews

---

## 專案簡介

本研究透過 **Latent Dirichlet Allocation (LDA)** 主題模型分析台灣與美國醫院的線上評論，識別兩國醫院服務品質的關鍵構面，並進行跨文化比較。

### 研究問題
1. 台灣和美國醫院服務品質各有哪些主要構面？
2. 兩國患者關注的服務品質面向有何異同？
3. 如何透過資料驅動方法（LDA）補充傳統問卷調查的不足？

### 主要發現
- **台灣（K=7）**：識別出 7 個服務品質構面
- **美國（K=7）**：識別出 7 個服務品質構面
- **跨文化差異**：兩國患者在服務態度、等待時間、專業品質等面向的重視程度有所不同

---

## 目錄結構

```
LDA_hospital/
├── data/                      # 資料檔案
│   ├── raw/                   # 原始資料
│   ├── processed/             # 處理後資料
│   └── cleaned/               # 清理過程資料
├── results/                   # 分析結果 ⭐
│   ├── taiwan_lda_k7/        # 台灣 7-topic LDA 結果
│   ├── usa_lda_k7/           # 美國 7-topic LDA 結果
│   └── comparison/           # 台美比較結果
├── manuscripts/               # 期刊論文 📝
├── code/                      # 程式碼
├── archive/                   # 舊版本檔案
├── CLAUDE.md                  # Claude Code 使用指南
└── README.md                  # 本檔案
```

詳細目錄架構請參考 **[CLAUDE.md](CLAUDE.md)**。

---

## 快速開始

### 1. 環境設定

```bash
# 安裝 Python 套件
pip install -r requirements.txt
```

**主要套件**：
- `jieba==0.42.1`：中文斷詞
- `gensim==4.3.3`：LDA 模型
- `pandas`, `numpy`：資料處理
- `matplotlib`, `wordcloud`：視覺化

### 2. 資料位置

- **台灣原始資料**：`data/raw/taiwan/`（26 家醫院，.xlsx 格式）
- **美國原始資料**：`data/raw/usa/`
- **處理後資料**：`data/processed/[taiwan|usa]/`

### 3. 執行分析

#### 台灣資料前處理
```bash
python code/preprocessing/data_preprocessing.py
```

#### LDA 主題模型訓練（K=7）
```bash
python code/lda_analysis/lda_analysis_k6k7.py
```

#### 視覺化結果
分析結果會自動儲存至 `results/taiwan_lda_k7/visualizations/`。

---

## 主要成果

### 1. 台灣醫院服務品質 7 構面（K=7）

| 構面編號 | 構面名稱 | 代表性關鍵詞 | 占比 |
|---------|---------|-------------|------|
| Topic 1 | 醫療診斷與檢查 | 醫生、檢查、問題、治療 | 14.9% |
| Topic 2 | 掛號與等待時間 | 時間、掛號、等待、批價 | 17.8% |
| Topic 3 | 服務態度與溝通 | 態度、護士、病人、急診 | 25.7% |
| Topic 4 | 急診與特殊照護 | 急診、開刀、小孩 | 12.9% |
| Topic 5 | 專業品質與滿意度 | 醫師、專業、感謝、親切 | 28.7% |

**關鍵洞察**：
- **服務態度**是最大關注點（25.7%），但評分最低（2.95/5）
- **專業品質**獲得最高評價（4.52/5）
- **等待時間**是系統性問題，橫跨多家醫院

詳細分析請參考：`manuscripts/Journal_Paper_Draft.md`

### 2. 美國醫院服務品質 7 構面（K=7）

（結果儲存於 `results/usa_lda_k7/`）

### 3. 台美比較

比較視覺化與報告：
- `results/comparison/Taiwan_USA_Comparison_Visualization.png`
- `results/comparison/Taiwan_USA_Hospital_Reviews_Comparison_Report.md`

---

## 方法論亮點

### 主題數量選擇框架

本研究提出 **多準則決策框架** 來選擇最佳主題數量（K），而非僅依賴 coherence 指標：

| 準則 | 說明 |
|-----|------|
| 1. 統計指標 | Coherence Score、Perplexity |
| 2. 肘部法則 | Coherence 曲線的轉折點 |
| 3. 可解釋性 | 主題是否具有明確語意 |
| 4. 理論驗證 | 與 SERVQUAL 等理論框架的一致性 |
| 5. 分布平衡 | 避免主題過度集中或碎片化 |

**為何選擇 K=7 而非 K=2？**
- K=2 雖有最高 coherence (0.464)，但僅區分正負評，缺乏診斷價值
- K=7 coherence 仍高 (0.433)，且能識別出 7 個可操作的管理構面

詳見：`manuscripts/Journal_Paper_Draft.md` 第 3.3.2 節

---

## 檔案清單

### 重要資料檔案
- `data/raw/taiwan/*.xlsx`：台灣 26 家醫院原始評論
- `data/processed/taiwan/reviews_for_lda.txt`：處理後的台灣評論

### 重要結果檔案
- `results/taiwan_lda_k7/lda_k7_lda_model.pkl`：台灣 LDA 模型
- `results/taiwan_lda_k7/lda_k7_analysis_results.xlsx`：台灣分析結果表格
- `results/taiwan_lda_k7/visualizations/lda_k7_wordclouds.png`：台灣詞雲圖

### 重要論文檔案
- `manuscripts/Journal_Paper_Draft.md`：完整期刊論文草稿（12,000 字）
- `manuscripts/台美醫院服務品質跨文化比較_期刊論文.md`：中文版期刊論文

### 重要程式碼
- `code/preprocessing/data_preprocessing.py`：資料前處理
- `code/lda_analysis/lda_analysis_k6k7.py`：LDA 訓練與分析
- `code/lda_analysis/optimize_lda.py`：主題數量優化

---

## 使用 Claude Code

本專案支援 **Claude Code** 輔助開發。請遵循 **[CLAUDE.md](CLAUDE.md)** 中的目錄架構規範。

### 如何引導 Claude Code
```
請遵循 CLAUDE.md 的目錄架構規範來生成和儲存檔案。
```

### 常用指令示例
- 生成新的視覺化：
  ```
  請生成台灣 LDA k7 的主題分布圖，並儲存到 results/taiwan_lda_k7/visualizations/
  ```
- 撰寫比較報告：
  ```
  請撰寫台美服務品質比較報告，並儲存到 manuscripts/
  ```

---

## 研究貢獻

### 理論貢獻
1. **實證驗證**服務品質的多維度性質（與 SERVQUAL 一致）
2. 發現**急診照護**是醫療服務特有構面（非一般服務品質框架所涵蓋）

### 方法論貢獻
1. 提出 **LDA 主題數量選擇的多準則框架**
2. 證明 **coherence 最大化並非充分條件**（K=2 vs. K=7 的案例）

### 實務貢獻
1. 識別**服務態度**為台灣醫院的首要改善領域
2. 提供**低成本、可持續的品質監測方法**（線上評論分析）
3. 支援**醫院間標竿比較**（topic profile 分析）

---

## 下一步研究方向

1. **時序分析**：追蹤主題演變，評估品質改善措施成效
2. **多平台資料**：整合 Facebook、PTT 等平台評論
3. **情感分析**：結合 LDA 與 sentiment analysis
4. **跨國比較**：擴展至更多國家（日本、韓國、新加坡等）
5. **階層式 LDA**：探索子主題（如服務態度細分為醫師態度 vs. 護理師態度）

---

## 引用本研究

```bibtex
@article{hospital_lda_2025,
  title={Uncovering Service Quality Dimensions in Taiwan's Hospitals:
         A Latent Dirichlet Allocation Approach Using Online Reviews},
  author={[Your Name]},
  journal={[Target Journal]},
  year={2025},
  note={Working Paper}
}
```

---

## 授權與聯絡

**專案負責人**：Simon
**更新日期**：2025-11-05
**授權**：本專案僅供學術研究使用

---

## 附錄

### A. 台灣醫院清單（26 家）
1. 國立臺灣大學醫學院附設醫院
2. 臺北榮民總醫院
3. 三軍總醫院
4. 國泰綜合醫院
5. 亞東紀念醫院
... （完整清單見 `data/raw/taiwan/`）

### B. 主題關鍵詞完整列表
見 `manuscripts/Journal_Paper_Draft.md` Appendix A

### C. 代表性評論範例
見 `manuscripts/Journal_Paper_Draft.md` Appendix B

---

**最後更新**：2025-11-05
