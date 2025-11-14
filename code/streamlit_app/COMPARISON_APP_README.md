# 🌏 台美醫院評論跨文化比較分析系統

## Taiwan-USA Hospital Review Cross-Cultural Comparison System

**作者**: Claude Code
**日期**: 2025-11-12
**版本**: 1.0.0

---

## 📖 系統簡介

本系統是一個互動式網頁應用程式，用於比較台灣與美國醫院評論的服務品質主題差異。透過 LDA 主題模型分析，揭示兩國醫療服務在文化、制度與病患期望上的差異。

### 核心功能

1. **🏠 跨文化概覽** - 資料集與模型品質比較
2. **🔗 主題對應映射** - 桑基圖視覺化主題關聯
3. **🔍 關鍵詞深度比較** - 雙語關鍵詞權重對比
4. **📊 評分與情緒分析** - 統計分析與評分分佈

---

## 📊 資料集資訊

### 台灣醫院評論
- **評論數**: 5,007 則
- **醫院數**: 26 家醫療中心
- **主題模型**: K=7 (7個主題)
- **Coherence Score**: 0.4175
- **語言**: 繁體中文

### 美國醫院評論
- **評論數**: 3,240 則
- **主題模型**: K=6 (6個主題)
- **Coherence Score**: 0.4029
- **語言**: English

---

## 🎯 主題標籤總覽

### 台灣 7 個主題

| Topic ID | 標籤 | English | 情緒 |
|----------|------|---------|------|
| 0 | 👨‍⚕️ 醫療專業認可 | Medical Professional Recognition | positive |
| 1 | ⏰ 就診流程與等候 | Process & Waiting Time | negative |
| 2 | 😠 服務態度問題 | Service Attitude Issues | negative |
| 3 | 🏥 設施與便利性 | Facility & Convenience | neutral |
| 4 | 🩺 手術治療成功 | Surgical Success | positive |
| 5 | 🛏️ 住院照護品質 | Inpatient Care | neutral |
| 6 | 🚨 急診與溝通 | Emergency & Communication | negative |

### 美國 6 個主題

| Topic ID | 標籤 | English | 情緒 |
|----------|------|---------|------|
| 0 | 💔 重症與生命照護 | Critical & Life Care | neutral |
| 1 | ⏰ 急診等候時間 | ER Waiting Time | negative |
| 2 | 😣 門診與疼痛管理 | Clinic & Pain Management | negative |
| 3 | 👩‍⚕️ 護理照護品質 | Nursing Care Quality | negative |
| 4 | ⭐ 整體正面評價 | Overall Positive Feedback | positive |
| 5 | 💰 預約與帳單問題 | Appointment & Billing | negative |

---

## 🔧 技術架構

### 核心技術棧

- **Frontend**: Streamlit 1.51.0
- **Data Processing**: Pandas, NumPy
- **LDA Model**: Gensim
- **Visualization**:
  - Matplotlib (靜態圖表)
  - Seaborn (統計圖表)
  - Plotly (互動式桑基圖)

### 檔案結構

```
code/streamlit_app/
├── taiwan_usa_comparison.py       # 主應用程式
├── comparison_config.py            # 配置檔案
├── run_comparison.sh               # 啟動腳本
├── analyze_models.py               # 模型分析工具
└── COMPARISON_APP_README.md        # 本說明文件
```

---

## 🚀 快速開始

### 方法 1: 使用啟動腳本（推薦）

```bash
cd code/streamlit_app
./run_comparison.sh
```

腳本會自動：
- ✅ 檢查 Python 版本
- ✅ 檢查必要套件
- ✅ 驗證資料檔案
- ✅ 啟動應用程式

### 方法 2: 手動啟動

```bash
cd code/streamlit_app
python3 -m streamlit run taiwan_usa_comparison.py --server.port 8503
```

---

## 📦 系統需求

### Python 版本
- Python 3.9 或以上

### 必要套件

```bash
pip3 install streamlit pandas numpy gensim matplotlib seaborn plotly scikit-learn scipy
```

或使用 requirements.txt:

```bash
pip3 install -r ../../requirements.txt
```

### 資料檔案

確保以下檔案存在：

```
results/
├── taiwan_lda_k7/
│   └── lda_k7_lda_model.pkl
└── usa_lda_k7/
    ├── usa_gensim_lda_k6_model.pkl
    └── usa_k6_topic_analysis_20251107_122236.csv
```

---

## 📱 使用指南

### 1. 啟動應用程式

執行 `./run_comparison.sh` 後，瀏覽器會自動開啟應用程式。

**本地網址**: http://localhost:8503

### 2. 導航頁面

使用左側邊欄選擇分析頁面：

#### 🏠 跨文化概覽
- 查看資料集基本統計
- 比較模型品質（Coherence, Perplexity）
- 檢視情緒分佈與文化差異重點

#### 🔗 主題對應映射
- 桑基圖視覺化主題關聯
- 查看詳細主題對應關係
- 了解文化獨特主題

#### 🔍 關鍵詞深度比較
- 選擇台美主題進行比較
- 查看關鍵詞權重對比圖
- 瀏覽完整關鍵詞列表（Top 30）

#### 📊 評分與情緒分析
- 主題比例對比圖
- 美國各主題評分箱型圖
- 詳細統計表格與評分分佈

### 3. 互動功能

- **下拉選單**: 選擇特定主題查看詳細資訊
- **展開卡片**: 點擊展開查看更多內容
- **圖表互動**: Plotly 圖表支援縮放、平移

---

## 🎨 視覺化特色

### 配色設計

- **🇹🇼 台灣**: 藍色系 (#1f77b4)
- **🇺🇸 美國**: 紅色系 (#d62728)
- **情緒**:
  - ✅ 正面: 綠色 (#2ecc71)
  - ⚖️ 中性: 橘色 (#f39c12)
  - ❌ 負面: 紅色 (#e74c3c)

### 圖表類型

1. **長條圖** (Bar Chart) - 模型品質、資料規模比較
2. **圓餅圖** (Pie Chart) - 情緒分佈
3. **桑基圖** (Sankey Diagram) - 主題對應關係
4. **水平長條圖** (Horizontal Bar) - 關鍵詞權重
5. **箱型圖** (Box Plot) - 評分分佈
6. **分組長條圖** (Grouped Bar) - 主題比例對比

---

## 🔍 文化差異發現

### 台灣獨特主題

#### 😠 服務態度問題 (17.3%)
台灣病患對醫護人員的「態度」特別敏感，形成獨立且比例顯著的主題。關鍵詞包括：態度、病人、護理師、服務等。

#### 🏥 設施與便利性 (10.2%)
停車場、動線、電梯等設施便利性在台灣醫療體驗中佔重要地位。

### 美國獨特主題

#### 💰 預約與帳單問題 (4.1%)
醫療帳單 (bill, billing) 和保險 (insurance) 問題是美國醫療系統的獨特痛點。

#### 😣 疼痛管理 (14.7%)
Pain management 是美國醫療評論的顯著關注點，關鍵詞包括：pain, clinic, help, never。

### 共同關注

1. **正面評價為主導**
   - 🇹🇼 醫療專業認可 (24.9%, 4.56★)
   - 🇺🇸 整體正面評價 (34.8%, 3.96★)

2. **等候時間普遍不滿**
   - 🇹🇼 就診流程與等候 (15.1%, 2.89★)
   - 🇺🇸 急診等候時間 (16.4%, 3.29★)

---

## 🐛 疑難排解

### 問題 1: 找不到 plotly 模組

**解決方案**:
```bash
pip3 install plotly --user
```

### 問題 2: Port 8503 already in use

**解決方案**:
```bash
# 方法 1: 更換端口
python3 -m streamlit run taiwan_usa_comparison.py --server.port 8504

# 方法 2: 終止現有進程
pkill -f "streamlit.*8503"
```

### 問題 3: 找不到資料檔案

**錯誤訊息**: `FileNotFoundError: [Errno 2] No such file or directory`

**解決方案**:
檢查檔案路徑是否正確，確保從 `code/streamlit_app/` 目錄啟動應用程式。

### 問題 4: 中文字體顯示為方框

這是已知限制，因為 matplotlib 預設沒有安裝中文字體。

**解決方案**（macOS）:
```python
# 在程式碼中添加
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False
```

---

## 📊 效能優化

### 快取機制

應用程式使用 Streamlit 的 `@st.cache_resource` 和 `@st.cache_data` 裝飾器，確保：
- 模型只載入一次
- 資料處理結果被快取
- 頁面切換更流暢

### 建議配置

- **RAM**: 至少 4GB
- **CPU**: 雙核心以上
- **瀏覽器**: Chrome, Firefox, Safari (最新版本)

---

## 🔄 更新與維護

### 更新資料

如果有新的評論資料或模型：

1. 更新模型檔案路徑於 `comparison_config.py`:
```python
TAIWAN_MODEL_PATH = BASE_DIR / "results/taiwan_lda_k7/新模型.pkl"
USA_MODEL_PATH = BASE_DIR / "results/usa_lda_k7/新模型.pkl"
```

2. 如有需要，更新主題標籤於 `comparison_config.py`

3. 重新啟動應用程式

### 擴展功能

可以在 `taiwan_usa_comparison.py` 中添加新的視覺化函數和頁面。

---

## 📞 聯絡與支援

### 問題回報

如遇到問題，請記錄：
1. 錯誤訊息
2. Python 版本
3. 作業系統
4. 重現步驟

### 功能建議

歡迎提出新功能建議！

---

## 📄 授權

本專案為學術研究使用。

---

## 🎉 致謝

- **LDA 模型**: Gensim
- **網頁框架**: Streamlit
- **視覺化**: Matplotlib, Seaborn, Plotly
- **開發工具**: Claude Code

---

**最後更新**: 2025-11-12
**文件版本**: 1.0.0
