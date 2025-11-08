# Google Review 智能抓取器

整合到 LDA_hospital 專案的 Google Maps 評論抓取工具。

---

## 📋 目錄

1. [快速開始](#快速開始)
2. [功能特色](#功能特色)
3. [使用方式](#使用方式)
4. [進階用法](#進階用法)
5. [常見問題](#常見問題)

---

## 🚀 快速開始

### 最簡單的使用方式

```bash
# 在 LDA_hospital 專案根目錄執行
cd /Users/simon/Library/CloudStorage/Dropbox/paper/Working\ paper/Hospitals/LDA_hospital

# 抓取美國醫院評論
python3 code/scraping/scrape_reviews.py \
  --url "https://www.google.com/maps/place/Mayo+Clinic/..." \
  --name "Mayo_Clinic" \
  --category hospitals \
  --region usa \
  --max-pages 100
```

執行後，檔案會自動儲存到：
- `data/raw/hospitals/usa/Mayo_Clinic_20251105_143022.csv`
- `data/raw/hospitals/usa/Mayo_Clinic_20251105_143022.json`
- `data/raw/hospitals/usa/Mayo_Clinic_20251105_143022_stats.csv`
- `data/raw/hospitals/usa/Mayo_Clinic_20251105_143022_report.txt`

---

## ✨ 功能特色

### 🎯 智能目錄管理
- ✅ 自動根據 `category` 和 `region` 創建目錄
- ✅ 符合 CLAUDE.md 規範的目錄架構
- ✅ 自動生成帶時間戳的檔案名稱

### 🌍 多語言支援
- ✅ 自動根據地區設定語言
  - Taiwan → 中文 (zh-TW)
  - USA/UK → 英文 (en)
  - Japan → 日文 (ja)

### 📊 完整的輸出格式
- ✅ CSV - 易於分析的表格格式
- ✅ JSON - 完整的原始資料
- ✅ Stats - 統計摘要（評分分布、評論數等）
- ✅ Report - 詳細的抓取報告

### 🔄 穩定性
- ✅ 錯誤處理和重試機制
- ✅ 分頁自動管理
- ✅ API 請求延遲控制

---

## 📖 使用方式

### 基本參數

| 參數 | 說明 | 必填 | 範例 |
|------|------|------|------|
| `--url` | Google Maps URL 或 Place ID | ✅ | "https://..." |
| `--name` | 地點名稱（用於檔名） | ✅ | "Mayo_Clinic" |
| `--category` | 資料類型 | ✅ | "hospitals" |
| `--region` | 地區 | ✅ | "usa" |
| `--max-pages` | 最大抓取頁數 | ❌ | 100 |
| `--per-page` | 每頁評論數 | ❌ | 20 |
| `--delay` | 每頁間延遲（秒） | ❌ | 2.0 |

### 支援的資料類型（category）

```
hospitals          - 醫院
museums            - 博物館
airports           - 機場
restaurants        - 餐廳
hotels             - 飯店
universities       - 大學
shopping_malls     - 購物中心
tourist_attractions - 旅遊景點
```

### 支援的地區（region）

```
taiwan         - 台灣
usa            - 美國
uk             - 英國
japan          - 日本
china          - 中國
asia           - 亞洲（跨國）
europe         - 歐洲（跨國）
north_america  - 北美洲（跨國）
```

---

## 🎓 進階用法

### 範例 1：抓取英國醫院評論

```bash
python3 code/scraping/scrape_reviews.py \
  --url "https://www.google.com/maps/place/Kings+College+Hospital/..." \
  --name "Kings_College_Hospital" \
  --category hospitals \
  --region uk \
  --max-pages 100 \
  --per-page 20 \
  --delay 2.0
```

**輸出位置**：`data/raw/hospitals/uk/Kings_College_Hospital_*.csv`

---

### 範例 2：抓取台灣博物館評論

```bash
python3 code/scraping/scrape_reviews.py \
  --url "https://www.google.com/maps/place/National+Palace+Museum/..." \
  --name "National_Palace_Museum" \
  --category museums \
  --region taiwan \
  --max-pages 50
```

**輸出位置**：`data/raw/museums/taiwan/National_Palace_Museum_*.csv`

---

### 範例 3：批次抓取多個地點

創建一個批次腳本 `batch_scrape.sh`：

```bash
#!/bin/bash

HOSPITALS=(
  "Mayo_Clinic|https://www.google.com/maps/place/..."
  "Cleveland_Clinic|https://www.google.com/maps/place/..."
  "Johns_Hopkins|https://www.google.com/maps/place/..."
)

for hospital in "${HOSPITALS[@]}"; do
  IFS='|' read -r name url <<< "$hospital"

  echo "抓取: $name"
  python3 code/scraping/scrape_reviews.py \
    --url "$url" \
    --name "$name" \
    --category hospitals \
    --region usa \
    --max-pages 100

  echo "等待 30 秒..."
  sleep 30
done

echo "批次抓取完成！"
```

執行：
```bash
chmod +x batch_scrape.sh
./batch_scrape.sh
```

---

### 範例 4：快速測試（少量評論）

```bash
# 只抓取 3 頁，每頁 10 條評論，用於測試
python3 code/scraping/scrape_reviews.py \
  --url "Google Maps URL" \
  --name "Test_Hospital" \
  --category hospitals \
  --region usa \
  --max-pages 3 \
  --per-page 10 \
  --delay 1.0
```

---

## 🔍 輸出檔案說明

### CSV 檔案

包含以下欄位：
- 序號
- 評論ID
- 作者姓名
- 評分 (1-5 星)
- 評論內容
- 評論日期
- 照片數量
- 按讚數

### JSON 檔案

完整的原始資料，包含：
- `place_id` - 地點 ID
- `total_reviews` - 總評論數
- `pages_fetched` - 成功抓取的頁數
- `reviews` - 評論陣列
- `scraping_duration` - 抓取耗時
- `timestamp` - 抓取時間

### Stats 檔案

統計摘要：
- 總評論數
- 平均評分
- 有文字評論數
- 有照片評論數
- 抓取頁數
- 抓取時間

### Report 檔案

詳細報告：
- 基本資訊
- 抓取統計
- 評分分布（1-5星）
- 評論內容統計
- 檔案位置

---

## ❓ 常見問題

### Q1: 如何獲取 Google Maps URL？

1. 在 Google Maps 搜尋地點
2. 點擊「分享」
3. 複製連結
4. 或直接複製瀏覽器網址列的 URL

### Q2: 為什麼抓取失敗？

可能原因：
- ❌ URL 格式錯誤 → 確認是完整的 Google Maps URL
- ❌ 地點沒有評論 → 檢查 Google Maps 是否有評論
- ❌ 網路問題 → 檢查網路連線
- ❌ API 速率限制 → 增加 `--delay` 參數

### Q3: 如何抓取更多評論？

增加 `--max-pages` 參數：
```bash
--max-pages 200  # 抓取 200 頁（約 4000 條評論）
```

### Q4: 可以抓取中文評論嗎？

可以！設定 `--region taiwan` 會自動使用中文：
```bash
--region taiwan  # 自動設定為 zh-TW
```

### Q5: 如何避免被 Google 封鎖？

建議：
- ✅ 增加延遲時間：`--delay 3.0`
- ✅ 降低每頁評論數：`--per-page 10`
- ✅ 批次抓取時加入暫停時間
- ✅ 避免在短時間內大量請求

### Q6: 檔案儲存在哪裡？

自動儲存到：
```
data/raw/{category}/{region}/{name}_{timestamp}.csv
```

例如：
```
data/raw/hospitals/usa/Mayo_Clinic_20251105_143022.csv
```

### Q7: 如何查看抓取進度？

程式會即時顯示進度：
```
📄 正在抓取第 1 頁...
✅ 第 1 頁完成，獲得 20 條評論
📄 正在抓取第 2 頁...
✅ 第 2 頁完成，獲得 20 條評論
...
```

---

## 🛠️ 技術架構

### 核心模組

1. **google_review_scraper.py** - 核心爬蟲
   - 處理 Google Maps API 請求
   - 解析評論數據
   - 儲存 CSV/JSON

2. **scrape_reviews.py** - 智能包裝器
   - 目錄管理
   - 參數處理
   - 報告生成

### 資料流程

```
Google Maps URL
    ↓
提取 Place ID
    ↓
API 請求（分頁）
    ↓
解析評論數據
    ↓
儲存到正確目錄
    ↓
生成報告
```

---

## 📞 支援

遇到問題？

1. 檢查 CLAUDE.md 規範
2. 查看 DATA_STRUCTURE.md
3. 檢視生成的 `*_report.txt` 檔案

---

## 📝 更新日誌

**2025-11-05**
- ✅ 初始版本
- ✅ 支援多類型資料（hospitals, museums, airports 等）
- ✅ 支援多地區（taiwan, usa, uk 等）
- ✅ 自動目錄管理
- ✅ 完整的錯誤處理
- ✅ 詳細的抓取報告

---

**最後更新**：2025-11-05
**版本**：1.0.0
