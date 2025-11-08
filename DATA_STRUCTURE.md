# 資料目錄架構設計

## 🎯 設計原則

支援多種資料類型（醫院、博物館、機場等）和多個國家/地區的彈性架構。

---

## 📁 目錄結構

```
LDA_hospital/
├── data/
│   ├── raw/                        # 原始資料（不可修改）
│   │   ├── hospitals/             # 醫院評論
│   │   │   ├── taiwan/            # 台灣醫院
│   │   │   ├── usa/               # 美國醫院
│   │   │   ├── uk/                # 英國醫院
│   │   │   └── ...                # 其他國家
│   │   ├── museums/               # 博物館評論
│   │   │   ├── taiwan/
│   │   │   ├── usa/
│   │   │   └── uk/
│   │   ├── airports/              # 機場評論
│   │   │   ├── asia/
│   │   │   ├── europe/
│   │   │   └── north_america/
│   │   └── restaurants/           # 餐廳評論（範例）
│   │
│   ├── processed/                 # 處理後的資料
│   │   ├── hospitals/
│   │   │   ├── taiwan/
│   │   │   └── usa/
│   │   ├── museums/
│   │   └── ...
│   │
│   └── cleaned/                   # 清理過程的中間檔案
│       ├── hospitals/
│       └── museums/
```

---

## 🏷️ 命名規範

### 原始資料檔案
```
{Place_Name}_{Timestamp}.csv
{Place_Name}_{Timestamp}.json
{Place_Name}_{Timestamp}_stats.csv

範例：
- National_Taiwan_University_Hospital_20251105_143022.csv
- British_Museum_20251105_150000.json
```

### 合併後的資料
```
{category}_{region}_merged_{date}.csv

範例：
- hospitals_taiwan_merged_20251105.csv
- museums_uk_merged_20251105.csv
```

---

## 🔧 資料類型（Category）

支援的資料類型：
- `hospitals` - 醫院
- `museums` - 博物館
- `airports` - 機場
- `restaurants` - 餐廳
- `hotels` - 飯店
- `universities` - 大學
- `shopping_malls` - 購物中心
- `tourist_attractions` - 旅遊景點

可根據研究需求擴充。

---

## 🌍 地區（Region）

支援的地區：
- `taiwan` - 台灣
- `usa` - 美國
- `uk` - 英國
- `japan` - 日本
- `china` - 中國
- `asia` - 亞洲（跨國資料）
- `europe` - 歐洲（跨國資料）
- `north_america` - 北美洲

可根據研究需求擴充。

---

## 📊 使用範例

### 情境 1：抓取英國醫院評論
```python
# 儲存位置
data/raw/hospitals/uk/Kings_College_Hospital_20251105.csv

# 處理後
data/processed/hospitals/uk/reviews_for_lda.txt
```

### 情境 2：抓取台灣博物館評論
```python
# 儲存位置
data/raw/museums/taiwan/National_Palace_Museum_20251105.csv

# 處理後
data/processed/museums/taiwan/reviews_cleaned.csv
```

### 情境 3：跨國機場比較研究
```python
# 儲存位置
data/raw/airports/asia/Singapore_Changi_20251105.csv
data/raw/airports/europe/London_Heathrow_20251105.csv
data/raw/airports/north_america/JFK_20251105.csv

# 合併後
data/processed/airports/cross_regional_comparison.csv
```

---

## 🎯 與現有專案的整合

### 現有的台灣26家醫院資料
保持在原位置：
```
data/raw/taiwan/
```

新資料使用新架構：
```
data/raw/hospitals/taiwan/
```

兩者可共存，逐步遷移。

---

## 📝 元資料（Metadata）

每個 category/region 組合應包含一個 `README.md`：

```markdown
# {Category} - {Region}

## 資料來源
- Google Maps Reviews

## 抓取日期
- 2025-11-05

## 地點列表
1. {Place Name} - {Place ID} - {Review Count}
2. ...

## 備註
- 語言：English/中文
- 評論數量：{Total}
```

---

**建立日期**：2025-11-05  
**最後更新**：2025-11-05
