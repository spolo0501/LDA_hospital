# 基於 Web of Science 的文獻增強工作流程

## 目標
使用 Web of Science 抓取的真實文獻來改寫和增強 Chapter 2.1-2.5

## 標準工作流程

### Step 1: 分析現有章節內容
- 讀取章節檔案
- 識別核心概念和理論框架
- 列出目前引用的文獻
- 找出需要補強的部分

### Step 2: 擬定 WOS 搜尋策略
根據章節主題，設計 3-5 組搜尋關鍵字：
- **主要關鍵字**（必須包含）
- **次要關鍵字**（可組合）
- **年份限制**（通常 2015-2024）
- **排除條件**（會議論文）

### Step 3: 執行 WOS 文獻抓取
```python
from wos_scraper_api import WOSScraperAPI

scraper = WOSScraperAPI(headless=False)

# 搜尋多組關鍵字
keyword_sets = [
    "healthcare service quality",
    "SERVQUAL AND healthcare",
    "patient satisfaction AND service quality"
]

for keywords in keyword_sets:
    papers = scraper.search_api(keywords, max_results=50)
    scraper.save_results(papers, f"Literature_Review/{keywords.replace(' ', '_')}")
```

### Step 4: 文獻分析與篩選
- 讀取抓取的文獻 CSV/JSON
- 根據摘要篩選相關文獻
- 識別高引用文獻（權威來源）
- 按主題分類文獻

### Step 5: 基於文獻改寫章節
- 用真實文獻替換目前的引用
- 補充最新研究（2020-2024）
- 加入實證證據支持論點
- 更新參考文獻列表

---

## Chapter 2.1 範例：Healthcare Service Quality Foundations

### 現有內容分析

**核心概念：**
1. SERVQUAL 五維度框架
2. 醫療特定服務品質模型（Brady & Cronin, Dagger et al.）
3. Technical vs. Functional Quality
4. 跨文化服務品質差異
5. 探索性方法的必要性

**目前引用的關鍵文獻：**
- Parasuraman et al. (1985, 1988) - SERVQUAL
- Brady & Cronin (2001) - 階層模型
- Dagger et al. (2007) - 醫療四維度模型
- Berry & Bendapudi (2007) - 醫療服務特性
- Andaleeb (2001) - 資訊不對稱

**需要補強的部分：**
1. 缺少 2020-2024 的最新研究
2. COVID-19 對服務品質的影響
3. 線上評論在服務品質研究中的應用
4. 跨文化醫療服務品質比較的實證研究
5. Topic modeling / LDA 在醫療品質研究中的應用

---

### 建議的 WOS 搜尋策略

#### 搜尋組 1: 醫療服務品質基礎
```
Query: "healthcare service quality" OR "hospital service quality"
Year: 2020-2024
Max Results: 100
Exclude: Conference papers
```

#### 搜尋組 2: SERVQUAL 在醫療的應用
```
Query: SERVQUAL AND (healthcare OR hospital OR medical)
Year: 2015-2024
Max Results: 50
Exclude: Conference papers
```

#### 搜尋組 3: 線上評論與醫療品質
```
Query: "online reviews" AND (healthcare OR hospital OR patient)
Year: 2018-2024
Max Results: 50
Exclude: Conference papers
```

#### 搜尋組 4: 跨文化醫療品質比較
```
Query: "cross-cultural" AND "service quality" AND healthcare
Year: 2015-2024
Max Results: 50
Exclude: Conference papers
```

#### 搜尋組 5: Topic modeling 在醫療研究
```
Query: ("topic modeling" OR "LDA" OR "text mining") AND (healthcare OR "patient feedback")
Year: 2018-2024
Max Results: 50
Exclude: Conference papers
```

---

## 實際執行範例

### 執行順序

1. **創建 Literature_Review 目錄**
```bash
mkdir -p Literature_Review/Chapter_2.1
cd Literature_Review/Chapter_2.1
```

2. **執行 WOS 搜尋**（一次搜尋一組）
```python
# 搜尋組 1
papers = scraper.search_api("healthcare service quality OR hospital service quality AND PY=(2020-2024)", max_results=100)
scraper.save_results(papers, "Literature_Review/Chapter_2.1/healthcare_service_quality_2020-2024")
```

3. **分析文獻**
- 開啟 CSV 檔案
- 按引用數排序
- 閱讀高引用文獻的摘要
- 標記相關文獻

4. **改寫章節**
- 在相關段落加入新文獻
- 更新論點和證據
- 補充最新研究趨勢
- 更新參考文獻列表

---

## 預期產出

### 改寫後的 Chapter 2.1 應包含：

1. **更新的理論框架**（基於 2020-2024 文獻）
2. **實證證據**（來自 WOS 高引用文獻）
3. **COVID-19 影響**（新興議題）
4. **線上評論研究**（方法論正當性）
5. **跨文化比較研究**（支持研究設計）

### 新增的參考文獻應包含：

- 至少 20-30 篇 2020-2024 的最新研究
- 高引用文獻（引用數 > 50）
- 實證研究（非純理論）
- 與研究問題直接相關

---

## 時間估計

- **Step 1**: 分析現有內容（30 分鐘）
- **Step 2**: 擬定搜尋策略（15 分鐘）
- **Step 3**: 執行 WOS 抓取（5 組 × 5 分鐘 = 25 分鐘）
- **Step 4**: 文獻分析與篩選（1-2 小時）
- **Step 5**: 改寫章節（2-3 小時）

**總計：約 4-6 小時 / 每章**

---

## 注意事項

1. **儲存位置**：統一儲存到 `Literature_Review/Chapter_X.X/` 子目錄
2. **檔案命名**：使用描述性名稱，包含搜尋關鍵字和日期
3. **去重**：不同搜尋組可能抓到重複文獻，需要手動去重
4. **引用格式**：保持 APA 格式一致性
5. **版本控制**：改寫前先備份原始檔案

---

## 下一步

準備好開始了嗎？我們可以：

1. **立即開始 Chapter 2.1**：我幫你執行上述 5 組 WOS 搜尋
2. **先看其他章節**：確認 2.2-2.5 的結構
3. **討論搜尋策略**：你想調整關鍵字嗎？

請告訴我你想如何進行！
