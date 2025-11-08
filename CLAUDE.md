# Claude Code 目錄架構規範

> **重要提醒**：此檔案定義了本專案的標準目錄結構。當 Claude Code 生成新檔案時，請遵循此架構將檔案存放在正確位置。

---

## 專案目標

本專案旨在比較台灣與美國醫院評論的服務品質構面，使用 LDA (Latent Dirichlet Allocation) 主題模型進行分析。目前研究進度：
- 台灣：7-topic LDA 分析完成
- 美國：7-topic LDA 分析完成
- 台美比較：初步比較完成

---

## 目錄結構規範

### 💡 新版架構（2025-11-05 更新）

支援多種資料類型（醫院、博物館、機場等）和多個國家/地區。

```
LDA_hospital/
├── data/                           # 所有資料檔案
│   ├── raw/                        # 原始資料（不可修改）
│   │   ├── hospitals/              # 醫院評論 ⭐ 新架構
│   │   │   ├── taiwan/             # 台灣醫院
│   │   │   ├── usa/                # 美國醫院
│   │   │   └── uk/                 # 英國醫院
│   │   ├── museums/                # 博物館評論 ⭐ 新架構
│   │   │   ├── taiwan/
│   │   │   ├── usa/
│   │   │   └── uk/
│   │   ├── airports/               # 機場評論 ⭐ 新架構
│   │   │   ├── asia/
│   │   │   ├── europe/
│   │   │   └── north_america/
│   │   ├── taiwan/                 # 🔄 舊架構（保留相容）
│   │   └── usa/                    # 🔄 舊架構（保留相容）
│   │
│   ├── processed/                  # 處理後的資料
│   │   ├── hospitals/              # ⭐ 新架構
│   │   │   ├── taiwan/
│   │   │   └── usa/
│   │   ├── museums/                # ⭐ 新架構
│   │   ├── taiwan/                 # 🔄 舊架構（保留相容）
│   │   └── usa/                    # 🔄 舊架構（保留相容）
│   │
│   └── cleaned/                    # 資料清理過程的中間檔案
│       ├── hospitals/              # ⭐ 新架構
│       └── taiwan/                 # 🔄 舊架構（保留相容）
│
├── results/                        # 所有分析結果
│   ├── taiwan_lda_k7/             # 台灣 7-topic LDA 結果 ✅ 主要成果
│   │   ├── *.pkl                  # LDA 模型檔案
│   │   ├── *.xlsx                 # 分析結果表格
│   │   └── visualizations/        # 所有圖表（.png）
│   ├── usa_lda_k7/                # 美國 7-topic LDA 結果 ✅ 主要成果
│   │   ├── *.pkl                  # LDA 模型檔案
│   │   ├── *.py                   # 分析程式碼
│   │   └── visualizations/        # 所有圖表
│   └── comparison/                 # 台美比較結果 ✅ 主要成果
│       ├── Taiwan_USA_*.png       # 比較視覺化
│       ├── Taiwan_USA_*.md        # 比較報告
│       └── *.py                   # 比較分析程式碼
│
├── manuscripts/                    # 期刊論文與學術寫作 📝
│   ├── Journal_Paper_Draft.md     # 期刊論文完整草稿（Introduction-Conclusion）
│   ├── 台美醫院服務品質跨文化比較_期刊論文.md
│   └── reports/                   # 其他研究報告
│       ├── FINAL_SUMMARY.md
│       ├── LITERATURE_AND_THEORIES.md
│       └── *.md
│
├── code/                          # 程式碼
│   ├── scraping/                  # Google Review 資料抓取 ⭐ 新增
│   │   ├── google_review_scraper.py     # 核心爬蟲
│   │   └── scrape_reviews.py            # 智能包裝器
│   ├── preprocessing/             # 資料前處理
│   │   └── data_preprocessing.py
│   ├── lda_analysis/              # LDA 分析
│   │   ├── lda_analysis.py
│   │   ├── lda_analysis_k6k7.py
│   │   ├── optimize_lda.py
│   │   └── topic_validation_tool.py
│   └── comparison/                # 比較分析（目前為空，未來使用）
│
├── archive/                       # 舊版本/已廢棄檔案 🗄️
│   ├── old_k6_results/           # K=6 的舊結果（已被 K=7 取代）
│   ├── troubleshooting_docs/     # 問題排除文件
│   ├── deprecated_code/          # 舊程式碼
│   └── old_reports/              # 舊版分析報告
│
├── CLAUDE.md                      # 📌 本檔案（Claude Code 使用指南）
├── README.md                      # 專案說明
├── requirements.txt               # Python 套件需求
├── medical_dict_custom.txt        # 醫療詞典
└── stopwords_custom.txt           # 停用詞表
```

---

## Claude Code 檔案生成規則

### 🟢 規則 0：Google Review 資料抓取（⭐ 新增）

使用智能抓取器 `code/scraping/scrape_reviews.py` 抓取 Google Maps 評論。

**使用方式**：
```bash
python3 code/scraping/scrape_reviews.py \
  --url "Google Maps URL" \
  --name "Place_Name" \
  --category {hospitals|museums|airports|restaurants|...} \
  --region {taiwan|usa|uk|japan|...} \
  --max-pages 100
```

**自動儲存位置**：
- 原始資料 → `data/raw/{category}/{region}/{Place_Name}_{timestamp}.csv`
- JSON 資料 → `data/raw/{category}/{region}/{Place_Name}_{timestamp}.json`
- 統計資料 → `data/raw/{category}/{region}/{Place_Name}_{timestamp}_stats.csv`
- 抓取報告 → `data/raw/{category}/{region}/{Place_Name}_{timestamp}_report.txt`

**範例**：
```bash
# ✅ 抓取英國醫院評論
python3 code/scraping/scrape_reviews.py \
  --url "https://www.google.com/maps/place/..." \
  --name "Kings_College_Hospital" \
  --category hospitals \
  --region uk \
  --max-pages 100

# ✅ 抓取台灣博物館評論
python3 code/scraping/scrape_reviews.py \
  --url "https://www.google.com/maps/place/..." \
  --name "National_Palace_Museum" \
  --category museums \
  --region taiwan \
  --max-pages 50
```

**支援的資料類型（category）**：
- `hospitals` - 醫院
- `museums` - 博物館
- `airports` - 機場
- `restaurants` - 餐廳
- `hotels` - 飯店
- `universities` - 大學
- `shopping_malls` - 購物中心
- `tourist_attractions` - 旅遊景點

**支援的地區（region）**：
- `taiwan`, `usa`, `uk`, `japan`, `china`
- `asia`, `europe`, `north_america`

---

### 🔴 規則 1：新資料檔案

**新架構（推薦）**：
- **原始資料**（.xlsx, .csv）→ `data/raw/{category}/{region}/`
- **處理後資料**（.txt, .csv）→ `data/processed/{category}/{region}/`
- **清理過程檔案**（.csv）→ `data/cleaned/{category}/{region}/`

**舊架構（相容）**：
- **原始資料**（.xlsx, .csv）→ `data/raw/[taiwan|usa]/`
- **處理後資料**（.txt, .csv）→ `data/processed/[taiwan|usa]/`
- **清理過程檔案**（.csv）→ `data/cleaned/[taiwan|usa]/`

**範例**：
```python
# ❌ 錯誤
output_file = "cleaned_reviews.csv"

# ✅ 正確
output_file = "data/processed/taiwan/cleaned_reviews.csv"
```

---

### 🔴 規則 2：LDA 分析結果
- **台灣 7-topic 結果** → `results/taiwan_lda_k7/`
  - 模型檔案（.pkl）、分析表格（.xlsx）放在根目錄
  - 圖表（.png）放在 `visualizations/` 子目錄
- **美國 7-topic 結果** → `results/usa_lda_k7/`
- **比較結果** → `results/comparison/`

**範例**：
```python
# ❌ 錯誤
model.save("lda_model_new.pkl")
plt.savefig("topic_distribution.png")

# ✅ 正確
model.save("results/taiwan_lda_k7/lda_model_k7_v2.pkl")
plt.savefig("results/taiwan_lda_k7/visualizations/topic_distribution_v2.png")
```

---

### 🔴 規則 3：期刊論文與報告
- **期刊論文主要稿件** → `manuscripts/`（根目錄）
- **其他研究報告** → `manuscripts/reports/`

**命名規範**：
- 英文論文：`[Topic]_[JournalName]_Draft.md`
- 中文論文：`[主題]_期刊論文.md`
- 比較報告：`Taiwan_USA_[Topic]_Report.md`

**範例**：
```python
# ❌ 錯誤
with open("new_chapter.md", "w") as f:
    f.write(content)

# ✅ 正確
with open("manuscripts/Chapter2_Literature_Review.md", "w") as f:
    f.write(content)
```

---

### 🔴 規則 4：程式碼
- **資料前處理程式** → `code/preprocessing/`
- **LDA 分析程式** → `code/lda_analysis/`
- **比較分析程式** → `code/comparison/`

**範例**：
```python
# ❌ 錯誤
new_script = "compare_topics.py"

# ✅ 正確
new_script = "code/comparison/compare_topics_taiwan_usa.py"
```

---

### 🔴 規則 5：舊檔案與測試
- **不再使用的檔案** → `archive/deprecated_code/`
- **舊版本結果**（如 K=6）→ `archive/old_k6_results/`
- **臨時測試檔案** → 完成後應刪除或移至 `archive/`

---

## 檔案命名規範

### 資料檔案
- 原始資料：`[醫院編號]_[醫院名稱]_[評論數].xlsx`
- 處理資料：`reviews_for_lda_[date].txt`
- 清理資料：`step[N]_[description].csv`

### 分析結果
- 模型：`[country]_lda_k[N]_model.pkl`
- 圖表：`[country]_lda_k[N]_[chart_type].png`
- 報告：`[Country]_LDA_k[N]_Analysis_Report.md`

### 程式碼
- 功能描述：`[action]_[object]_[details].py`
- 範例：`compare_topics_taiwan_usa.py`, `preprocess_reviews_usa.py`

---

## 使用範例

### 情境 1：新增美國醫院原始資料
```python
import pandas as pd

# 載入資料
df = pd.read_csv("hospitals_usa_raw.csv")

# ✅ 儲存到正確位置
df.to_csv("data/raw/usa/hospitals_usa_2025.csv", index=False)
```

### 情境 2：生成新的台灣 LDA 視覺化
```python
import matplotlib.pyplot as plt

# 繪製主題分布
plt.figure(figsize=(10, 6))
# ... plotting code ...

# ✅ 儲存到正確位置
plt.savefig("results/taiwan_lda_k7/visualizations/topic_distribution_updated_2025.png")
```

### 情境 3：撰寫比較分析報告
```markdown
# ✅ 檔案位置
manuscripts/Taiwan_USA_Service_Quality_Comparison_2025.md

# 內容
## Abstract
This study compares service quality dimensions...
```

### 情境 4：新增比較分析程式碼
```python
# ✅ 檔案位置
code/comparison/cross_country_topic_alignment.py

# 內容
def align_topics(taiwan_topics, usa_topics):
    """
    Compare and align topics between Taiwan and USA LDA models.
    """
    pass
```

---

## 如何引導 Claude Code 使用此架構

### 方法 1：在對話開始時提及
```
請遵循 CLAUDE.md 中的目錄架構規範來存放檔案。
```

### 方法 2：在具體任務中指定
```
請生成台美比較的視覺化圖表，並按照 CLAUDE.md 的規範，
將圖片儲存到 results/comparison/ 目錄。
```

### 方法 3：使用 .claude/commands/ 自定義命令
在 `.claude/commands/` 目錄下建立自訂命令，例如：

```bash
# .claude/commands/save-result.md
請將分析結果依照 CLAUDE.md 規範儲存：
- 台灣LDA結果 → results/taiwan_lda_k7/
- 美國LDA結果 → results/usa_lda_k7/
- 比較結果 → results/comparison/
- 論文 → manuscripts/
```

然後使用：
```
/save-result
```

---

## 常見問題 FAQ

### Q1：如果檔案類型不在規範中怎麼辦？
**A**：根據檔案性質判斷：
- 資料相關 → `data/`
- 分析結果 → `results/`
- 文字報告 → `manuscripts/reports/`
- 程式碼 → `code/`
- 不確定 → 詢問使用者

### Q2：臨時測試檔案該放哪裡？
**A**：建議在根目錄建立 `temp_test_[description].py`，完成後移至 `archive/deprecated_code/` 或刪除。

### Q3：如何處理跨國家的比較程式碼？
**A**：放在 `code/comparison/`，並在檔名中註明比較對象，例如：
```
code/comparison/compare_taiwan_usa_k7.py
```

### Q4：舊版本的分析結果要保留嗎？
**A**：
- 已被取代的舊版本（如 K=6）→ `archive/old_k6_results/`
- 目前版本（K=7）→ `results/[country]_lda_k7/`

---

## 版本記錄

- **2025-11-05**：初始版本，建立標準目錄架構
  - 整理台灣26家醫院原始資料到 `data/raw/taiwan/`
  - 移動台美 K=7 LDA 結果到 `results/`
  - 整理期刊論文到 `manuscripts/`
  - 封存舊版本結果到 `archive/`

---

## 聯絡資訊

如有架構調整需求，請通知專案負責人 Simon。

**最後更新**：2025-11-05
