# 文獻搜尋策略快速總結

## 📊 整體規劃一覽

### 總覽
- **總章節數**：5 章（2.1-2.5）
- **總搜尋組數**：25 組
- **預計文獻數**：600-700 篇（去重後）
- **預計時間**：3-5 個工作天

---

## 📚 各章節概況

| 章節 | 主題 | 搜尋組數 | 目標文獻 | 優先度 |
|------|------|---------|---------|--------|
| **2.1** | 醫療服務品質理論基礎 | 6 | 200 篇 | ⭐⭐⭐ 最高 |
| **2.2** | 跨文化服務品質差異 | 5 | 150 篇 | ⭐⭐ 中等 |
| **2.3** | 台美醫療體系比較 | 5 | 150 篇 | ⭐⭐ 中等 |
| **2.4** | 線上評論作為資料來源 | 5 | 150 篇 | ⭐⭐⭐ 高 |
| **2.5** | 文本挖掘與主題模型 | 4 | 150 篇 | ⭐⭐⭐ 高 |

---

## 🎯 建議執行順序

### 第 1 週：核心基礎
1. **Chapter 2.1** - Healthcare Service Quality Foundations
   - 最重要的理論章節
   - 6 組搜尋，約 200 篇文獻
   - 時間：6-8 小時

2. **Chapter 2.4** - Online Reviews as Data Source
   - 方法論正當性
   - 5 組搜尋，約 150 篇文獻
   - 時間：5-6 小時

### 第 2 週：脈絡分析
3. **Chapter 2.2** - Cross-Cultural Differences
   - 文化脈絡
   - 5 組搜尋，約 150 篇文獻
   - 時間：5-6 小時

4. **Chapter 2.3** - Healthcare Systems Comparison
   - 制度脈絡
   - 5 組搜尋，約 150 篇文獻
   - 時間：5-6 小時

### 第 3 週：方法論
5. **Chapter 2.5** - Text Mining and Topic Modeling
   - 分析方法
   - 4 組搜尋，約 150 篇文獻
   - 時間：5-6 小時

---

## ⚡ 快速開始：Chapter 2.1

### 為什麼從 2.1 開始？
1. ✅ 理論基礎章節，影響其他章節
2. ✅ 最需要更新（很多舊文獻）
3. ✅ 內容最豐富，可作為示範

### Chapter 2.1 的 6 組搜尋

```python
# 搜尋組 1：醫療服務品質基礎（50 篇）
query_1 = "healthcare service quality OR hospital service quality AND PY=(2020-2024)"

# 搜尋組 2：SERVQUAL 應用（40 篇）
query_2 = "SERVQUAL AND (healthcare OR hospital) AND PY=(2018-2024)"

# 搜尋組 3：患者體驗（40 篇）
query_3 = "patient experience AND service quality AND hospital AND PY=(2020-2024)"

# 搜尋組 4：雙重品質維度（30 篇）
query_4 = "technical quality AND functional quality AND healthcare AND PY=(2015-2024)"

# 搜尋組 5：COVID-19 影響（30 篇）
query_5 = "COVID-19 AND hospital AND service quality AND PY=(2020-2024)"

# 搜尋組 6：滿意度維度（30 篇）
query_6 = "patient satisfaction AND quality dimensions AND hospital AND PY=(2018-2024)"
```

**總計：220 篇文獻，預計 30-40 分鐘**

---

## 💾 儲存架構

```
Literature_Review/
├── Chapter_2.1_Healthcare_Service_Quality/
│   ├── 2.1-1_healthcare_service_quality_2020-2024.csv
│   ├── 2.1-1_healthcare_service_quality_2020-2024.json
│   ├── 2.1-2_SERVQUAL_healthcare_2018-2024.csv
│   ├── 2.1-2_SERVQUAL_healthcare_2018-2024.json
│   ├── ... (共 6 組)
│   └── ANALYSIS_2.1.md
│
├── Chapter_2.2_Cross_Cultural/
├── Chapter_2.3_Healthcare_Systems/
├── Chapter_2.4_Online_Reviews/
├── Chapter_2.5_Text_Mining/
│
├── MASTER_SEARCH_STRATEGY.md (完整策略)
└── QUICK_SUMMARY.md (本檔案)
```

---

## 📋 標準工作流程（每章）

### Step 1: 執行 WOS 搜尋 (30-40 分鐘)
```bash
# 創建目錄
mkdir -p Literature_Review/Chapter_2.1_Healthcare_Service_Quality

# 執行搜尋（使用 Python 腳本）
python3 search_chapter_2_1.py
```

### Step 2: 合併與去重 (15 分鐘)
- 合併所有 CSV 檔案
- 按 DOI 或 UID 去重
- 按引用數排序

### Step 3: 文獻分析 (2-3 小時)
- 閱讀 Top 20 高引用文獻摘要
- 標記相關主題
- 創建 ANALYSIS.md 筆記

### Step 4: 改寫章節 (3-4 小時)
- 整合新文獻到現有內容
- 補充最新研究（2020-2024）
- 更新參考文獻列表

**每章總時間：6-8 小時**

---

## 🎯 關鍵成功因素

### 1. 分批執行
- ❌ 不要一次執行 25 組搜尋
- ✅ 每次專注 1 章（5-6 組）
- ✅ 搜尋完立即分析，避免資料過載

### 2. 優先高引用文獻
- **引用數 > 100**：必讀核心文獻
- **引用數 50-100**：重點閱讀
- **引用數 < 50**：選擇性閱讀

### 3. 關注年份
- **2022-2024**：最新研究，優先考慮
- **2020-2021**：COVID-19 相關，重要
- **2015-2019**：經典研究，選擇性引用

### 4. 平衡理論與實證
- 理論文章：建立框架
- 實證研究：提供證據
- 方法論文章：支持研究設計

---

## 🚀 立即開始 Chapter 2.1？

我可以現在幫你：

1. **創建 Chapter 2.1 目錄**
2. **執行 6 組 WOS 搜尋**（約 220 篇文獻）
3. **生成 CSV/JSON 檔案**
4. **顯示初步統計**（引用數分布、年份分布）

只需要約 **30-40 分鐘**。

---

## 📞 需要討論的問題

1. **搜尋策略合適嗎？**
   - 關鍵字需要調整？
   - 數量太多或太少？

2. **執行順序同意嗎？**
   - 從 2.1 開始？
   - 還是其他章節優先？

3. **時間安排可行嗎？**
   - 一次做一章？
   - 還是先全部抓取？

請告訴我你的想法！
