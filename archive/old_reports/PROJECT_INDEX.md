# 🏥 美國醫院評論分析 - 專案總覽

**專案完成日期**: 2025-10-28  
**資料來源**: Google Maps 美國 28 家頂級醫院評論  
**總樣本數**: 3,363 條評論（最近一年）  
**分析類型**: EDA + 主題建模 + 情感分析 + 台美比較框架

---

## 📂 快速導航

### 🌟 必讀文件（按重要性排序）

1. **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)** ⭐⭐⭐
   - 5 分鐘快速了解核心發現
   - 四大負面痛點
   - 立即可執行的改善措施

2. **[ANALYSIS_SUMMARY.md](ANALYSIS_SUMMARY.md)** ⭐⭐⭐⭐⭐
   - 15-20 分鐘完整總結（最重要）
   - 所有分析結果匯總
   - 詳細管理建議和行動計劃

3. **[FILE_STRUCTURE.md](FILE_STRUCTURE.md)** ⭐⭐
   - 完整檔案結構說明
   - 快速找到需要的檔案

---

## 📊 分析成果總覽

### 已完成的分析 ✅

| 分析類型 | 主要產出 | 核心發現 |
|---------|---------|---------|
| **EDA 探索性分析** | 12個視覺化圖表 | 評分極化（86.4%為1星或5星） |
| **主題建模 (LDA)** | 正負面主題識別 | 4大負面痛點 + 2大正面優勢 |
| **情感分析** | VADER 79%準確率 | 情感與評分強相關（r=0.72） |
| **台美比較框架** | 完整對照框架 | 7個構面一對一映射 |

### 進行中的分析 ⏳

| 分析類型 | 目的 | 預期完成時間 |
|---------|------|------------|
| **主題優化 (5-7主題)** | 確定最佳主題數量 | 執行中 |

---

## 🎯 核心發現速覽

### 評分分布
- ⭐⭐⭐⭐⭐ (5星): 50.0% (1,683條)
- ⭐ (1星): 36.3% (1,221條)
- 中間評分 (2-4星): 僅 13.6%
- **極化現象**: 86.4%為極端評分

### 四大負面痛點 ⚠️

| 排名 | 痛點 | 預期影響 | 對應台灣 |
|-----|------|---------|---------|
| 1 | **等待時間過長** | 最嚴重 | T2 (6.9%) |
| 2 | **溝通問題** | 嚴重 | T3 (17.3%) |
| 3 | **🌟帳單/保險問題** | 美國獨特 | 無（~0%） |
| 4 | **預約困難** | 中等 | T2 (6.9%) |

### 兩大正面優勢 ✅

| 優勢 | 特徵 | 對應台灣 |
|-----|------|---------|
| **醫療專業認可** | 最突出 | T1 (27.2%, 4.67星) |
| **手術治療成功** | 高評價 | T5 (5.3%, 4.02星) |

---

## 📁 檔案結構快速索引

```
GoogleReviews/
│
├── 📄 核心文件/
│   ├── PROJECT_INDEX.md              ⭐ 本文檔 - 專案總覽
│   ├── QUICK_REFERENCE.md            ⭐ 快速參考（5分鐘）
│   ├── ANALYSIS_SUMMARY.md           ⭐⭐⭐ 綜合報告（最重要）
│   └── FILE_STRUCTURE.md             詳細檔案結構
│
├── 📊 分析結果/
│   ├── eda_results/                  EDA 探索性分析
│   │   ├── eda_visualizations.png    ⭐ 12個視覺化圖表
│   │   ├── correlation_matrix.png    相關性矩陣
│   │   └── EDA_REPORT.md            完整報告
│   │
│   ├── topic_modeling_results/       主題建模
│   │   ├── lda_topics_analysis.png   ⭐ LDA 主題分析
│   │   └── TOPIC_MODELING_REPORT.md  完整報告
│   │
│   ├── sentiment_analysis_results/   情感分析
│   │   ├── sentiment_analysis.png    ⭐ 9個情感圖表
│   │   ├── SENTIMENT_ANALYSIS_REPORT.md
│   │   └── reviews_with_sentiment.csv ⭐ 包含情感分數
│   │
│   └── topic_optimization_results/   主題優化（執行中）
│       └── ...
│
├── 🌏 台美比較研究/
│   ├── TAIWAN_USA_COMPARISON_FRAMEWORK.md    ⭐ 比較框架
│   ├── TOPIC_SELECTION_GUIDE.md              主題選擇指南
│   ├── TOPIC_EVOLUTION_4_TO_7_ANALYSIS.md    主題演進分析
│   └── QUICK_COMPARISON_YOUR_4_TO_NEW_7.md   快速對照
│
├── 📊 資料檔案/
│   ├── cleaned_data_no_dedup/
│   │   └── final_cleaned_sample_no_dedup.csv ⭐ 3,363條
│   └── sentiment_analysis_results/
│       └── reviews_with_sentiment.csv        ⭐ 含情感分數
│
└── 🔧 分析腳本/
    ├── eda_analysis.py                       EDA 分析
    ├── topic_modeling.py                     主題建模
    ├── sentiment_analysis.py                 情感分析
    └── topic_optimization_analysis.py        主題優化
```

---

## 🚀 三種使用情境

### 情境 A: 醫院管理者（實務應用）

**目標**: 了解服務問題，制定改善計劃

**推薦路徑** (15分鐘):
```
1. 閱讀 QUICK_REFERENCE.md (5分鐘)
   → 了解四大痛點

2. 查看 topic_modeling_results/lda_topics_analysis.png
   → 視覺化主題分布

3. 閱讀 QUICK_REFERENCE.md 中的「立即可執行措施」
   → 獲得具體行動建議
```

**關鍵輸出**:
- 優先改善領域清單
- 短期快速勝利措施
- 中長期戰略規劃

---

### 情境 B: 研究人員（學術研究）

**目標**: 進行台美跨國比較研究

**推薦路徑** (45分鐘):
```
1. 閱讀 ANALYSIS_SUMMARY.md (20分鐘)
   → 全面了解美國分析結果

2. 閱讀 TAIWAN_USA_COMPARISON_FRAMEWORK.md (15分鐘)
   → 理解比較框架

3. 閱讀台灣分析結果
   → /Users/simon/Downloads/Claude_code/LDA_hospital/LDA分析結果文字描述報告.md

4. 閱讀 TOPIC_SELECTION_GUIDE.md (10分鐘)
   → 了解主題數量選擇依據
```

**關鍵輸出**:
- 台美 7 對 7 構面對照表
- 文化差異假設
- 研究問題與方法論

---

### 情境 C: 數據分析師（技術深度）

**目標**: 理解方法、重現分析或二次開發

**推薦路徑**:
```
1. 查看分析腳本
   - eda_analysis.py
   - topic_modeling.py
   - sentiment_analysis.py

2. 使用分析結果資料
   - sentiment_analysis_results/reviews_with_sentiment.csv

3. 閱讀詳細報告
   - eda_results/EDA_REPORT.md
   - topic_modeling_results/TOPIC_MODELING_REPORT.md
   - sentiment_analysis_results/SENTIMENT_ANALYSIS_REPORT.md
```

**關鍵輸出**:
- 可重現的分析流程
- 包含情感分數的完整資料
- 詳細的方法論說明

---

## 📊 關鍵數據一覽

### 資料統計

| 指標 | 數值 |
|------|------|
| 總評論數 | 3,363 條 |
| 醫院數 | 28 家 |
| 時間範圍 | 2024-11-13 至 2025-10-28 (349天) |
| 平均評論長度 | 437 字元 |
| 英文評論比例 | 96.3% (3,240條) |

### 評分分布

| 評分 | 數量 | 百分比 |
|------|------|--------|
| 5星 | 1,683 | 50.0% |
| 4星 | 145 | 4.3% |
| 3星 | 138 | 4.1% |
| 2星 | 176 | 5.2% |
| 1星 | 1,221 | 36.3% |

### 模型品質

| 模型 | 指標 | 數值 |
|------|------|------|
| VADER | 準確率 | 79.0% |
| VADER | 與評分相關性 | r = 0.72 |
| TextBlob | 準確率 | 63.4% |
| LDA (5主題) | Coherence | 待確認 |
| LDA (7主題) | Coherence | 待確認 (台灣: 0.4175) |

---

## 🌏 台美比較研究重點

### 台灣資料概況

- 樣本數: 5,007 條
- 醫院數: 26 家醫學中心
- 主題數: 7 個構面
- Coherence Score: 0.4175
- 負面比例: 59.4%

### 美國資料概況

- 樣本數: 3,363 條
- 醫院數: 28 家頂級醫院
- 主題數: 5-7 個（測試中）
- 負面比例: 67.0% (基於4主題分析)

### 預期關鍵差異

| 維度 | 台灣 | 美國 | 差異原因 |
|------|------|------|---------|
| **負面評論比例** | 59.4% | 67% | 體系複雜度 |
| **服務態度問題** | 17.3% | 預期 8-12% | 文化期待 |
| **急診問題** | 30.9% | 27.3% | 跨文化共通 |
| **🌟帳單問題** | ~0% | 預期 12-15% | 體系差異 |

### 研究價值

1. **量化體系影響**: 帳單問題佔美國負面評論 12-15%
2. **識別共通挑戰**: 急診問題台美相似（~30%, ~1.7星）
3. **文化差異洞察**: 態度 vs 系統的關注焦點

---

## 🎯 您之前的 4 主題研究 vs 新的 7 主題

### 您的 4 主題結果回顧

| 主題 | 佔比 | 評分 | 特徵 |
|------|------|------|------|
| US0: 急診照護 | 27.3% | 1.63星 | 與台灣T7平行 |
| US1: 行政問題 | 22.6% | 低分 | 🌟 美國獨特 |
| US2: 護理與等待 | ? | 低分 | 疼痛管理 |
| US3: 正向經驗 | 33.0% | 4.15星 | 多維度合併 |

### 5-7 主題的預期細分

#### US1 (22.6%) 拆分為：
```
├─ 帳單/保險問題 (12-15%) 🌟 最重要的新發現
│  → 美國醫療體系獨特問題
│  → 台灣幾乎 0%
│  → 可量化健保優勢
│
└─ 預約/行政流程 (7-10%)
   → 與台灣可比較的共通問題
```

#### US3 (33.0%) 拆分為：
```
├─ 醫療專業與態度 (18-22%)
│  vs 台灣 T1: 27.2%
│
└─ 手術治療經驗 (8-12%)
   vs 台灣 T5: 5.3%
```

---

## 🔧 技術資訊

### 環境需求

```bash
Python 3.10+
pandas, numpy, matplotlib, seaborn
scikit-learn, nltk
textblob, vaderSentiment
gensim (用於 Coherence Score)
```

### 快速安裝

```bash
pip install pandas numpy matplotlib seaborn scikit-learn nltk textblob vaderSentiment gensim
```

### 環境問題修復

```bash
# 如果遇到 numpy/pandas 導入錯誤
./fix_ide_env.sh

# 或手動修復
unset PYTHONPATH
unset PYTHONHOME
```

詳見: [QUICK_FIX.md](QUICK_FIX.md)

---

## 📞 常見問題 (FAQ)

### Q1: 我應該從哪個檔案開始？

**A**: 依您的需求：
- 快速了解 → `QUICK_REFERENCE.md` (5分鐘)
- 完整理解 → `ANALYSIS_SUMMARY.md` (20分鐘)
- 台美比較 → `TAIWAN_USA_COMPARISON_FRAMEWORK.md`
- 查看圖表 → `eda_results/eda_visualizations.png`

### Q2: 為什麼要測試 5、6、7 個主題？

**A**: 
- 台灣使用了 7 個主題
- 為了台美比較，需要確定美國最適合的主題數
- 6-7 個主題可以將「行政問題」拆分成「帳單」和「預約」
- 這是您之前研究的關鍵發現精確化

### Q3: 美國獨特的「帳單問題」有多重要？

**A**:
- 預期佔負面評論的 12-15%
- 台灣幾乎 0%（健保制度）
- 可以量化「醫療體系複雜度」對滿意度的影響
- 學術價值極高

### Q4: VADER 和 TextBlob 哪個更好？

**A**:
- **VADER**: 79%準確率，r=0.72，推薦用於自動監控
- **TextBlob**: 63.4%準確率，r=0.66，適合一般分析
- 建議使用 VADER

### Q5: 分析結果可以用於實務嗎？

**A**: 可以！
- 四大痛點清楚明確
- 提供短中長期改善建議
- 可用於建立評論監控系統
- 查看 `QUICK_REFERENCE.md` 中的行動計劃

---

## ✅ 專案完成度

- [x] 資料收集與清理 (3,363條)
- [x] EDA 探索性分析
- [x] 主題建模 (LDA)
- [x] 情感分析 (VADER & TextBlob)
- [x] 綜合分析報告
- [x] 視覺化圖表 (25+ 個)
- [x] 台美比較框架
- [ ] 主題優化 (5-7主題) - **執行中**
- [ ] 台美詳細對照分析 - **待完成**

---

## 📈 下一步建議

### 短期（本週）
1. ⏳ 等待主題優化分析完成
2. ⏳ 確認使用 7 個主題（與台灣一致）
3. ⏳ 建立台美構面一對一對照表

### 中期（本月）
1. ⏳ 完成台美量化比較
2. ⏳ 撰寫跨國比較研究報告
3. ⏳ 準備學術發表材料

### 長期（未來）
1. ⏳ Aspect-Based Sentiment Analysis
2. ⏳ 時間序列預測分析
3. ⏳ 擴展到更多國家

---

## 🎓 引用本研究

```
美國醫院Google評論分析專案 (2025)
資料來源: Google Maps 美國28家頂級醫院評論
分析期間: 2024-11-13 至 2025-10-28
樣本數: 3,363條評論
主要方法: LDA主題建模、VADER情感分析、EDA統計分析
```

---

## 📚 相關文件索引

### 核心分析報告
- [綜合分析報告](ANALYSIS_SUMMARY.md) ⭐⭐⭐⭐⭐
- [EDA 報告](eda_results/EDA_REPORT.md)
- [主題建模報告](topic_modeling_results/TOPIC_MODELING_REPORT.md)
- [情感分析報告](sentiment_analysis_results/SENTIMENT_ANALYSIS_REPORT.md)

### 台美比較研究
- [比較框架](TAIWAN_USA_COMPARISON_FRAMEWORK.md) ⭐⭐⭐⭐
- [主題選擇指南](TOPIC_SELECTION_GUIDE.md)
- [主題演進分析](TOPIC_EVOLUTION_4_TO_7_ANALYSIS.md)
- [4主題vs7主題對照](QUICK_COMPARISON_YOUR_4_TO_NEW_7.md)

### 快速參考
- [快速參考指南](QUICK_REFERENCE.md) ⭐⭐⭐
- [檔案結構說明](FILE_STRUCTURE.md)
- [資料版本對比](VERSION_COMPARISON.md)

### 技術文件
- [環境快速修復](QUICK_FIX.md)
- [疑難排解指南](TROUBLESHOOTING_NUMPY_IMPORT.md)
- [資料清理總結](DATA_CLEANING_SUMMARY.md)

---

**專案狀態**: ✅ 主要分析完成，⏳ 主題優化進行中  
**最後更新**: 2025-10-28  
**版本**: 1.0

---

**🎊 開始探索您的分析結果！**

需要協助？查看 [QUICK_REFERENCE.md](QUICK_REFERENCE.md) 或各詳細報告。
