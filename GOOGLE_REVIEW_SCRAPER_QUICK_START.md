# Google Review 抓取器 - 快速開始

> **🎯 目標**：讓 Claude Code 可以幫您快速抓取 Google Maps 評論

---

## 🚀 最快使用方式

### 方法 1：直接告訴 Claude

您只需要說：

```
我要抓取這個醫院的評論：
https://www.google.com/maps/place/Mayo+Clinic/...
```

Claude 會自動執行：
```bash
python3 code/scraping/scrape_reviews.py \
  --url "您的URL" \
  --name "Mayo_Clinic" \
  --category hospitals \
  --region usa \
  --max-pages 100
```

---

### 方法 2：完整命令

```bash
python3 code/scraping/scrape_reviews.py \
  --url "Google Maps URL" \
  --name "地點名稱" \
  --category hospitals \
  --region usa \
  --max-pages 100
```

---

## 📝 常用範例

### 美國醫院
```bash
python3 code/scraping/scrape_reviews.py \
  --url "https://..." \
  --name "Mayo_Clinic" \
  --category hospitals \
  --region usa \
  --max-pages 100
```

### 英國醫院
```bash
python3 code/scraping/scrape_reviews.py \
  --url "https://..." \
  --name "Kings_College_Hospital" \
  --category hospitals \
  --region uk \
  --max-pages 100
```

### 台灣博物館
```bash
python3 code/scraping/scrape_reviews.py \
  --url "https://..." \
  --name "National_Palace_Museum" \
  --category museums \
  --region taiwan \
  --max-pages 50
```

---

## 📁 檔案會儲存在哪裡？

自動儲存到正確位置：
```
data/raw/{category}/{region}/{name}_{timestamp}.csv
data/raw/{category}/{region}/{name}_{timestamp}.json
data/raw/{category}/{region}/{name}_{timestamp}_stats.csv
data/raw/{category}/{region}/{name}_{timestamp}_report.txt
```

**範例**：
```
data/raw/hospitals/usa/Mayo_Clinic_20251105_143022.csv
data/raw/hospitals/uk/Kings_College_Hospital_20251105_150000.csv
data/raw/museums/taiwan/National_Palace_Museum_20251105_160000.csv
```

---

## 🎨 支援的資料類型

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

---

## 🌍 支援的地區

```
taiwan         - 台灣（自動使用中文）
usa            - 美國（自動使用英文）
uk             - 英國（自動使用英文）
japan          - 日本（自動使用日文）
china          - 中國（自動使用簡體中文）
asia           - 亞洲
europe         - 歐洲
north_america  - 北美洲
```

---

## 💡 與 Claude Code 對話範例

### 範例對話 1：單一醫院

**您**：
```
我要抓取 Mayo Clinic 的評論，URL 是：
https://www.google.com/maps/place/Mayo+clinic/@44.033406,-92.4682789,17z/...
```

**Claude**：
```
好的！我會幫您抓取 Mayo Clinic 的評論。

執行命令：
python3 code/scraping/scrape_reviews.py \
  --url "https://www.google.com/maps/place/Mayo+clinic/@44.033406,-92.4682789,17z/..." \
  --name "Mayo_Clinic" \
  --category hospitals \
  --region usa \
  --max-pages 100

檔案將儲存到：
data/raw/hospitals/usa/Mayo_Clinic_20251105_143022.csv
```

---

### 範例對話 2：批次抓取

**您**：
```
我想抓取以下3家英國醫院的評論：
1. Kings College Hospital
2. St Thomas Hospital
3. Guy's Hospital
```

**Claude**：
```
好的！我會依序為您抓取這3家醫院的評論，每個醫院之間會暫停30秒。

正在抓取...
✅ Kings_College_Hospital - 完成
✅ St_Thomas_Hospital - 完成
✅ Guy's_Hospital - 完成

所有檔案已儲存到：
data/raw/hospitals/uk/
```

---

### 範例對話 3：快速測試

**您**：
```
我想先測試一下，只抓取少量評論
```

**Claude**：
```
好的！我會使用測試模式（3頁，每頁10條）：

python3 code/scraping/scrape_reviews.py \
  --url "..." \
  --name "Test" \
  --category hospitals \
  --region usa \
  --max-pages 3 \
  --per-page 10 \
  --delay 1.0
```

---

## 📚 詳細文件

- **完整使用說明**：`code/scraping/README.md`
- **目錄架構說明**：`DATA_STRUCTURE.md`
- **Claude Code 規範**：`CLAUDE.md`

---

## ⚡ 優點

✅ **自動化** - Claude 會自動執行，無需手動輸入命令
✅ **智能化** - 自動判斷語言、地區、儲存位置
✅ **標準化** - 符合專案目錄架構規範
✅ **完整性** - 生成 CSV、JSON、統計、報告 4 種檔案
✅ **彈性化** - 支援多種資料類型和地區

---

**最後更新**：2025-11-05
**版本**：1.0.0
