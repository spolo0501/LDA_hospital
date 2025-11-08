# 台灣醫院線上評論LDA主題分析系統

基於25家台灣醫院的Google評論，使用LDA（Latent Dirichlet Allocation）主題模型進行醫療服務品質構面研究。

## 📁 專案結構

```
LDA_hospital/
├── data_preprocessing.py      # 資料前處理程式
├── lda_analysis.py           # LDA主題模型分析
├── optimize_lda.py           # 模型參數優化
├── result_analysis.py        # 結果分析與報告產生
├── requirements.txt          # Python依賴套件
├── stopwords_custom.txt      # 自訂停用詞表（可編輯）
├── medical_dict_custom.txt   # 自訂醫療詞典（可編輯）
│
├── *.xlsx                    # 25個醫院評論資料檔案
│
├── processed_data/           # 前處理後的資料
│   ├── combined_reviews.csv
│   ├── reviews_for_lda.txt
│   └── word_frequency_top200.txt
│
├── lda_results/              # LDA分析結果
│   ├── models/               # 訓練好的模型
│   ├── visualizations/       # 視覺化圖表
│   └── topic_keywords_*.csv
│
├── optimization_results/     # 參數優化結果
│   ├── models/
│   ├── experiments/
│   └── grid_search_results_*.csv
│
└── final_results/            # 最終分析報告
    ├── LDA_analysis_report.xlsx
    ├── hospital_topic_heatmap.png
    └── topic_distribution_pie.png
```

## 🚀 快速開始

### 1. 安裝依賴套件

```bash
pip install -r requirements.txt
```

### 2. 執行完整分析流程

#### 步驟1：資料前處理

```bash
python data_preprocessing.py
```

**功能：**
- 合併25個醫院的Excel評論資料
- 中文斷詞（jieba）
- 清理文本、去除停用詞
- 生成詞頻統計

**輸出：**
- `processed_data/combined_reviews.csv` - 合併後的資料
- `processed_data/word_frequency_top200.txt` - 高頻詞列表

**💡 提示：** 檢查 `word_frequency_top200.txt`，將無意義的高頻詞加入 `stopwords_custom.txt`，然後重新執行此步驟。

---

#### 步驟2：LDA主題模型分析

```bash
python lda_analysis.py
```

**功能：**
- 自動探索最佳主題數量（2-15個主題）
- 計算Coherence Score和Perplexity
- 訓練LDA模型並視覺化
- 為每筆評論分配主題

**輸出：**
- `lda_results/topic_optimization_results.csv` - 各主題數的評估指標
- `lda_results/visualizations/topic_optimization.png` - 優化曲線圖
- `lda_results/visualizations/lda_vis_Ntopics.html` - **互動式主題視覺化**
- `lda_results/visualizations/topic_wordclouds_Ntopics.png` - 主題詞雲
- `lda_results/models/lda_model_Ntopics.pkl` - 訓練好的模型

**重要：** 執行完成後，程式會推薦最佳主題數量。請查看互動式視覺化HTML檔案，確認主題是否清晰可辨。

---

#### 步驟3（選用）：參數優化

```bash
python optimize_lda.py
```

**功能：**
- 參數網格搜尋（主題數、alpha、eta、詞頻閾值）
- 測試自訂停用詞的效果
- 互動式停用詞調整
- 比較多個實驗結果

**使用場景：**
- 當預設LDA結果不理想時
- 想要微調模型參數時
- 需要測試不同停用詞組合時

**輸出：**
- `optimization_results/grid_search_results_*.csv` - 所有實驗結果
- `optimization_results/grid_search_comparison_*.png` - 參數比較圖

---

#### 步驟4：產生最終報告

```bash
python result_analysis.py
```

**執行後會要求：**
1. 輸入模型檔案路徑（例如：`./lda_results/models/lda_model_8topics.pkl`）
2. （可選）為主題自訂名稱

**功能：**
- 為每筆評論分配主題
- 分析各醫院主題分布
- 提取代表性評論
- 產生完整Excel報告

**輸出：**
- `final_results/LDA_analysis_report.xlsx` - **完整Excel報告**，包含：
  - 主題摘要
  - 評論主題分配
  - 醫院主題分析
  - 代表性評論
  - 主題關鍵詞
- `final_results/hospital_topic_heatmap.png` - 醫院-主題熱力圖
- `final_results/topic_distribution_pie.png` - 主題分布圓餅圖

---

## 📊 主要分析指標

### 1. Coherence Score (C_v)
- **意義：** 衡量主題內詞彙的語義一致性
- **範圍：** -1 到 1（越高越好）
- **用途：** 選擇最佳主題數量的主要指標

### 2. Perplexity
- **意義：** 衡量模型的預測能力
- **特性：** 越低越好
- **注意：** 不一定與主題可解釋性正相關

### 3. 主題概率
- 每筆評論對各主題的歸屬概率
- 主導主題（Dominant Topic）：概率最高的主題

---

## 🔧 進階調整

### 調整停用詞

1. 執行 `data_preprocessing.py` 後查看 `processed_data/word_frequency_top200.txt`
2. 將無意義的高頻詞加入 `stopwords_custom.txt`
3. 重新執行 `data_preprocessing.py`

**範例停用詞：**
```
真的
覺得
感覺
非常
蠻
```

### 調整醫療詞典

編輯 `medical_dict_custom.txt`，添加專業術語以改善斷詞效果：

```
台大醫院
長庚醫院
榮民總醫院
慢性病處方箋
```

### 調整LDA參數

在 `optimize_lda.py` 中修改網格搜尋參數：

```python
results_df = optimizer.grid_search(
    num_topics_list=[5, 6, 7, 8, 9, 10],  # 主題數範圍
    alpha_list=['symmetric', 'asymmetric', 0.01, 0.1],  # 文檔-主題分布
    eta_list=['auto', 'symmetric', 0.01],  # 主題-詞彙分布
    min_freq_list=[3, 5],  # 最小詞頻
    max_freq_ratio_list=[0.4, 0.5, 0.6]  # 最大詞頻比例
)
```

**參數說明：**
- `alpha`: 控制每個文檔包含多少主題（值越小，主題越集中）
- `eta`: 控制每個主題包含多少詞彙（值越小，詞彙越集中）
- `min_freq`: 詞彙至少要出現在幾個文檔中
- `max_freq_ratio`: 詞彙最多出現在多少比例的文檔中

---

## 📈 使用技巧

### 1. 如何判斷主題數量是否合適？

**好的指標：**
- ✅ Coherence Score相對較高
- ✅ 各主題關鍵詞明確且不重疊
- ✅ 主題有清晰的語義意義
- ✅ 評論分配到主題的概率較高（>0.3）

**不好的指標：**
- ❌ 多個主題的關鍵詞相似
- ❌ 某些主題的關鍵詞雜亂無意義
- ❌ 主題分布極度不平衡（某主題佔90%）

### 2. 如何命名主題？

1. 查看 `lda_results/topic_keywords_*.csv` 中的關鍵詞
2. 閱讀 `final_results/LDA_analysis_report.xlsx` 中的代表性評論
3. 根據關鍵詞和評論內容命名

**範例主題名稱：**
- 醫療專業品質
- 服務態度
- 等候時間與流程
- 環境設施
- 掛號批價效率
- 醫病溝通

### 3. 迭代優化流程

```
1. 執行基礎分析 → 2. 檢視高頻詞 → 3. 調整停用詞
                                    ↓
        6. 產生最終報告 ← 5. 選擇最佳模型 ← 4. 參數優化
```

---

## 🎯 研究應用

### 可能的醫療服務品質構面

根據LDA分析結果，可能發現的品質構面包括：

1. **醫療專業品質** - 診斷準確性、治療效果、醫師專業
2. **服務態度** - 醫護人員態度、同理心、溝通品質
3. **就醫流程效率** - 等候時間、掛號便利性、批價速度
4. **環境與設施** - 醫院環境、清潔度、設備新穎度
5. **行政服務** - 櫃檯服務、預約系統、電話諮詢
6. **醫病溝通** - 病情解釋、用藥說明、諮詢回應

### 分析建議

- **醫院間比較：** 查看 `hospital_topic_heatmap.png` 了解各醫院在不同構面的表現
- **改善重點：** 分析評論數量多的負面主題，找出服務弱點
- **優勢特色：** 分析高評分主題，突顯醫院優勢

---

## ⚠️ 注意事項

1. **中文字型問題：** macOS預設使用 `PingFang.ttc`，Windows需調整為 `Microsoft JhengHei` 或 `SimHei`
2. **記憶體需求：** 處理大量文本時，建議至少8GB RAM
3. **執行時間：** 網格搜尋可能需要數小時，請耐心等候
4. **資料隱私：** 注意評論可能包含個人資訊，使用時請遵守資料保護規範

---

## 🛠️ 疑難排解

### 問題：jieba斷詞不正確

**解決：** 將專業詞彙加入 `medical_dict_custom.txt`

### 問題：主題關鍵詞不清晰

**解決：**
1. 增加停用詞（編輯 `stopwords_custom.txt`）
2. 調整 `min_freq` 和 `max_freq_ratio` 參數
3. 嘗試不同的主題數量

### 問題：某個主題佔比過高

**解決：**
1. 檢查是否有過多無意義詞彙
2. 增加主題數量
3. 調整 `alpha` 參數（設為較小值，如0.01）

### 問題：視覺化圖表中文顯示為方塊

**解決：** 修改程式中的字型設定
```python
plt.rcParams['font.sans-serif'] = ['您的中文字型名稱']
```

---

## 📚 參考資源

- [Gensim LDA文檔](https://radimrehurek.com/gensim/models/ldamodel.html)
- [pyLDAvis使用指南](https://github.com/bmabey/pyLDAvis)
- [jieba中文分詞](https://github.com/fxsjy/jieba)

---

## 💬 聯絡與支援

如有問題或建議，請聯繫專案負責人。

---

**祝您研究順利！🎉**
