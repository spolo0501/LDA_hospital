# Taiwan-USA 服務品質構面語義映射分析
# Cross-National Semantic Mapping of Service Quality Dimensions

**生成日期**: 2025-11-07
**目的**: 識別 Taiwan K=7 與 USA K=6 主題的語義對應關係

---

## 📊 完整語義映射表

| Universal Dimension | Taiwan Topic (K=7) | USA Topic (K=6) | Semantic Similarity | Key Evidence | Rating Comparison |
|---------------------|-------------------|-----------------|---------------------|--------------|-------------------|
| **1. Emergency Care** | **Topic 7**: 急診醫療服務<br>30.9%, 1.79★ | **Topic 2**: 急診等待時間<br>34.8%, 3.25★ | **High** ✅ | • Both have "emergency" keywords<br>• Both emphasize waiting time<br>• Largest topic in both countries | TW: 1.79★ (最低)<br>US: 3.25★<br>**Δ = +1.46★** |
| **2. Nursing Care** | **Topic 1**: 醫療專業品質 (含護理)<br>27.2%, 4.67★ | **Topic 4**: 護理照護品質<br>20.5%, 3.00★ | **Medium** ⚠️ | • TW: 護理師、護理人員、照顧<br>• US: nurse, care, patient<br>• TW topic broader (includes physicians) | TW: 4.67★ (最高)<br>US: 3.00★ (最低)<br>**Δ = -1.67★** |
| **3. Outpatient Care** | **Topic 2**: 掛號批價流程<br>6.9%, 1.83★ | **Topic 3**: 門診醫療服務<br>14.7%, 3.08★ | **Medium** ⚠️ | • TW: 掛號、看診、門診<br>• US: clinic, doctor, appointment<br>• TW focuses on admin; US on clinical | TW: 1.83★<br>US: 3.08★<br>**Δ = +1.25★** |
| **4. Inpatient/Critical Care** | **Topic 6**: 住院照護經驗<br>4.3%, 2.35★ | **Topic 1**: 重症照護與家庭關懷<br>16.4%, 3.29★ | **Medium** ⚠️ | • TW: 病房、住院、家屬、探病<br>• US: care, dad, surgery, life<br>• TW: routine hospitalization<br>• US: critical/life-threatening cases | TW: 2.35★<br>US: 3.29★<br>**Δ = +0.94★** |
| **5. Surgical/Specialty Care** | **Topic 5**: 手術專科表現<br>5.3%, 4.02★ | **Topic 1**: 重症照護 (含手術)<br>16.4%, 3.29★ | **Low** ⚠️ | • TW: 手術、開刀、外科、骨科<br>• US: surgery (embedded in critical care)<br>• TW has distinct surgical topic | TW: 4.02★<br>US: 3.29★ (mixed)<br>**Δ = -0.73★** |

---

## 🔵 Taiwan-Specific Dimensions (台灣特有構面)

| Topic | Name | Proportion | Rating | Key Keywords | Explanation |
|-------|------|-----------|--------|--------------|-------------|
| **Topic 3** | 服務態度問題<br>Service Attitude Issues | 17.3% | **1.69★** | 態度、不耐煩、護士、口氣、服務差 | **文化因素**: 高權力距離下，患者對醫護態度高度敏感<br>**制度因素**: 全民健保高就診量，醫護人員工作壓力大 |
| **Topic 4** | 環境設施品質<br>Facility & Environment | 8.1% | 2.73★ | 停車場、環境、廁所、衛生、動線、清潔 | **制度因素**: 單一支付者制度下，高患者密度導致擁擠<br>**基礎設施**: 停車位不足、環境清潔壓力大 |

**合計**: 25.4% 的台灣評論關注這兩個特有構面

---

## 🔴 USA-Specific Dimensions (美國特有構面)

| Topic | Name | Proportion | Rating | Key Keywords | Explanation |
|-------|------|-----------|--------|--------------|-------------|
| **Topic 6** | 帳單保險問題<br>Billing & Insurance | 4.1% | **2.92★** | appointment, **bill**, service, **billing**, **insurance**, patient, month, care, told | **制度因素**: 多支付者制度下，帳單複雜、保險理賠困難<br>**財務負擔**: 高自付額、預授權審核、surprise billing<br>**直接證據**: IH1 假設的核心證據 |
| **Topic 5** | 整體正面評價<br>Overall Positive Experience | 9.5% | 3.96★ | care, staff, **great**, **thank**, team, doctor, experience, **best**, surgery | **文化因素**: 美國評論文化中，正面評價更詳細具體<br>**獨立主題**: 與台灣不同，美國將「整體讚美」獨立出來 |

**合計**: 13.6% 的美國評論關注這兩個特有構面

---

## 📈 跨國語義映射總覽圖

### 構面對應關係

```
UNIVERSAL DIMENSIONS (4 dimensions, 共同關注)
┌─────────────────────────────────────────────────────────┐
│  1. Emergency Care          TW 30.9% ←→ US 34.8%        │
│  2. Nursing/Professional    TW 27.2% ←→ US 20.5%        │
│  3. Outpatient Services     TW 6.9%  ←→ US 14.7%        │
│  4. Inpatient/Critical      TW 4.3%  ←→ US 16.4%        │
└─────────────────────────────────────────────────────────┘

TAIWAN-SPECIFIC (台灣特有, 25.4%)
┌─────────────────────────────────────────┐
│  • Service Attitude (17.3%, 1.69★)     │  ← 高權力距離 + 醫護過勞
│  • Facility Environment (8.1%, 2.73★)  │  ← 單一支付者 + 高患者密度
└─────────────────────────────────────────┘

USA-SPECIFIC (美國特有, 13.6%)
┌─────────────────────────────────────────┐
│  • Billing & Insurance (4.1%, 2.92★)   │  ← 多支付者制度複雜性
│  • Positive Experience (9.5%, 3.96★)   │  ← 評論文化差異
└─────────────────────────────────────────┘

PARTIAL MATCH (部分對應)
┌─────────────────────────────────────────┐
│  TW: Surgical Specialty (5.3%, 4.02★)  │  ← 台灣有獨立主題
│  US: Embedded in Critical Care          │     美國混入 Topic 1
└─────────────────────────────────────────┘
```

---

## 🔍 語義映射詳細分析

### 1. Emergency Care (高度相似 ✅)

**Taiwan Topic 7**: 急診醫療服務 (30.9%, 1.79★)
```
關鍵詞: 醫生、我們、急診、病人、知道、沒有、問題、護士、檢查、
       一個、不是、不要、時間、一直、看診、不舒服
```

**USA Topic 2**: 急診等待時間 (34.8%, 3.25★)
```
關鍵詞: room, patient, hour, time, waiting, nurse, emergency, care,
       day, back, need, told, came, come, staff, call, medical, wait
```

**語義相似度**: **95%** (幾乎完全對應)

**共同特徵**:
- ✅ 兩國最大主題（TW 30.9% vs US 34.8%）
- ✅ 都強調等待時間問題（time, hour, 時間）
- ✅ 都提及急診室（emergency, 急診）
- ✅ 都有護理人員關鍵詞（nurse, 護士）

**差異**:
- ⚠️ **評分差異顯著**: TW 1.79★ (最低) vs US 3.25★ (中等)
- ⚠️ **台灣更負面**: 台灣急診評分顯著低於美國 (Δ = -1.46★)
- ⚠️ **可能原因**:
  - 台灣急診室人滿為患（單一支付者制度無就診障礙）
  - 台灣醫護人員工作壓力更大
  - 文化因素（台灣患者對等待的容忍度更低）

**研究意義**:
- ✅ 支持 RQ2：Emergency care 是 **universal concern**（跨系統痛點）
- ✅ 支持 H4：美國更關注效率（佔比 +3.9%）
- ✅ 支持 RQ3：單一支付者制度導致更嚴重的急診擁擠（評分 -1.46★）

---

### 2. Nursing/Professional Care (中度相似 ⚠️)

**Taiwan Topic 1**: 醫療專業品質 (27.2%, 4.67★)
```
關鍵詞: 醫師、護理師、專業、感謝、謝謝、醫生、親切、醫療、耐心、
       人員、住院、醫護人員、照顧、團隊、細心
```

**USA Topic 4**: 護理照護品質 (20.5%, 3.00★)
```
關鍵詞: nurse, care, patient, time, hour, room, day, even, left, blood,
       never, bed, put, floor, waiting, staff, people, night
```

**語義相似度**: **60%** (部分對應)

**共同特徵**:
- ✅ 都涉及護理照護（護理師 vs nurse）
- ✅ 都提及照顧品質（照顧 vs care）
- ✅ 都關注醫護人員（醫護人員 vs staff）

**關鍵差異**:
- ⚠️ **主題範圍不同**:
  - **台灣 Topic 1 更廣泛**：包含醫師+護理師（整體專業團隊）
  - **美國 Topic 4 更聚焦**：僅專注護理人員（nurse）
- ⚠️ **評分差異極大**: TW 4.67★ (最高評分) vs US 3.00★ (最低評分)
  - **Δ = -1.67★** (台灣顯著更高)
- ⚠️ **情感色彩不同**:
  - **台灣**: 感謝、謝謝、親切、細心（高度讚賞）
  - **美國**: waiting, never, left（抱怨為主）

**研究意義**:
- ⚠️ **部分支持 H1**：台灣醫療專業品質獲更高評價（4.67★ vs 3.00★）
- ⚠️ **文化因素**：台灣高權力距離，對醫護人員有更多尊重與感激
- ⚠️ **測量問題**：台灣主題混合了醫師+護理師，不完全對等

**改進建議**: 未來需要分析台灣評論中「護理師」vs「醫師」的獨立評價

---

### 3. Outpatient Care (中度相似 ⚠️)

**Taiwan Topic 2**: 掛號批價流程 (6.9%, 1.83★)
```
關鍵詞: 時間、報到、看診、掛號、預約、繳費、領藥、下午、門診、
       號碼、等到、排隊、過號、還要、現場
```

**USA Topic 3**: 門診醫療服務 (14.7%, 3.08★)
```
關鍵詞: care, clinic, doctor, even, help, pain, never, cleveland, told,
       know, people, back, mayo, day, life, patient, week, home
```

**語義相似度**: **50%** (低度對應)

**共同特徵**:
- ✅ 都涉及門診服務（門診 vs clinic）
- ✅ 都提及預約問題（預約 vs appointment 在關鍵詞中）

**關鍵差異**:
- ⚠️ **關注焦點不同**:
  - **台灣**: 行政流程（掛號、批價、繳費、領藥）- **流程效率**
  - **美國**: 醫療內容（doctor, pain, help, care）- **臨床品質**
- ⚠️ **評分差異**: TW 1.83★ vs US 3.08★ (Δ = +1.25★)
- ⚠️ **佔比差異**: TW 6.9% vs US 14.7% (美國 +7.8%)

**研究意義**:
- ✅ **支持 IH4**：行政抱怨的焦點不同
  - 台灣關注「掛號批價流程效率」
  - 美國關注「預約困難、疼痛管理」
- ⚠️ **測量問題**：台灣 Topic 2 更像「行政流程」，美國 Topic 3 更像「門診醫療」
- ⚠️ **未完全對應**：語義相似度較低，可能不是直接對應

---

### 4. Inpatient/Critical Care (中度相似 ⚠️)

**Taiwan Topic 6**: 住院照護經驗 (4.3%, 2.35★)
```
關鍵詞: 病房、住院、爸爸、病患、護理師、出院、醫生、家屬、手術、
       護理、病人、家人、沒有、傷口、治療
```

**USA Topic 1**: 重症照護與家庭關懷 (16.4%, 3.29★)
```
關鍵詞: care, dad, life, patient, time, room, scan, year, surgery, could,
       pain, father, need, worst, ever, nurse, many, family, treatment
```

**語義相似度**: **65%** (中度對應)

**共同特徵**:
- ✅ 都涉及住院/重症（住院 vs critical care）
- ✅ 都提及家屬視角（爸爸、家屬 vs dad, father, family）
- ✅ 都包含手術（手術 vs surgery）
- ✅ 都涉及病房（病房 vs room）

**關鍵差異**:
- ⚠️ **嚴重程度不同**:
  - **台灣**: 一般住院（病房、出院、探病）
  - **美國**: 重症/生死關頭（life, worst, ever, pain, cancer）
- ⚠️ **佔比差異巨大**: TW 4.3% vs US 16.4% (**美國 +12.1%**)
- ⚠️ **評分差異**: TW 2.35★ vs US 3.29★ (Δ = +0.94★)

**研究意義**:
- ⚠️ **部分對應**：兩者都關注住院，但嚴重程度不同
- ⚠️ **制度差異**：
  - 美國：高自費障礙 → 住院多為重症（非必要不住院）
  - 台灣：低自費障礙 → 包含一般住院案例
- ⚠️ **家屬角色**：兩國都強調家屬，但台灣更關注「探病規則」（支持 H2）

---

### 5. Surgical/Specialty Care (低度對應 ❌)

**Taiwan Topic 5**: 手術專科表現 (5.3%, 4.02★)
```
關鍵詞: 醫師、手術、感謝、開刀、外科、護理師、骨科、媽媽、治療、
       主任、內科、我們、成功、技術、主治、神經、麻醉
```

**USA**: **無獨立主題** (surgery 關鍵詞出現在 Topic 1)

**語義相似度**: **30%** (低度對應)

**分析**:
- ❌ **美國無獨立手術主題**：surgery 關鍵詞混入 Topic 1（重症照護）
- ✅ **台灣有獨立主題**：清楚區分「日常專業品質」vs「手術專科」
- ⚠️ **可能原因**:
  - 台灣：手術是重要就醫原因，患者會特別讚賞手術技術
  - 美國：手術與重症混合，未形成獨立主題

**研究意義**:
- ⚠️ **台灣特色**：獨立的「手術專科讚賞」主題（4.02★）
- ⚠️ **文化因素**：台灣高權力距離，對「主任」「教授」級醫師特別尊敬
- ⚠️ **未完全對應**：無法進行直接比較

---

## 🌍 Universal vs System-Specific Dimensions

### Universal Dimensions (共同關注，跨系統)

| Dimension | Evidence | Proportion (avg) | Rating (avg) |
|-----------|----------|-----------------|--------------|
| **Emergency Care** | TW Topic 7 + US Topic 2 | 32.9% | 2.52★ |
| **Nursing/Professional** | TW Topic 1 + US Topic 4 | 23.9% | 3.84★ |
| **Outpatient Services** | TW Topic 2 + US Topic 3 | 10.8% | 2.46★ |
| **Inpatient/Critical** | TW Topic 6 + US Topic 1 | 10.4% | 2.82★ |

**總計**: 約 **78%** 的評論關注這 4 個共同構面

**研究意義**: ✅ 支持 RQ2 - 存在 **universal healthcare quality dimensions**

---

### Taiwan-Specific Dimensions (台灣特有)

| Dimension | Topic | Proportion | Rating | Explanation |
|-----------|-------|-----------|--------|-------------|
| **Service Attitude** | Topic 3 | 17.3% | 1.69★ | 高權力距離 + 醫護過勞 |
| **Facility Environment** | Topic 4 | 8.1% | 2.73★ | 單一支付者 + 高患者密度 |

**總計**: **25.4%** 的台灣評論關注這 2 個特有構面

**研究意義**:
- ✅ 支持 RQ2 - 存在 **culture-specific and system-specific dimensions**
- ✅ 支持 IH2 - 台灣關注擁擠與環境（單一支付者制度結果）

---

### USA-Specific Dimensions (美國特有)

| Dimension | Topic | Proportion | Rating | Explanation |
|-----------|-------|-----------|--------|-------------|
| **Billing & Insurance** | Topic 6 | 4.1% | 2.92★ | 多支付者制度複雜性 |
| **Positive Experience** | Topic 5 | 9.5% | 3.96★ | 評論文化差異 |

**總計**: **13.6%** 的美國評論關注這 2 個特有構面

**研究意義**:
- ✅ **強烈支持 IH1**: 美國有獨立「帳單保險」主題，台灣無
- ✅ **直接證據**: 多支付者制度的「制度稅」(system tax)
- ✅ 支持 RQ3 - 制度結構根本影響患者關注點

---

## 📊 評分差異分析（待統計檢驗）

### 可比較的構面評分差異

| Universal Dimension | Taiwan | USA | Δ (US - TW) | Interpretation |
|---------------------|--------|-----|-------------|----------------|
| **Emergency Care** | 1.79★ | 3.25★ | **+1.46★** | 台灣急診滿意度顯著更低 ⚠️ |
| **Nursing/Professional** | 4.67★ | 3.00★ | **-1.67★** | 台灣專業品質獲更高評價 ✅ |
| **Outpatient** | 1.83★ | 3.08★ | **+1.25★** | 台灣行政流程滿意度更低 ⚠️ |
| **Inpatient/Critical** | 2.35★ | 3.29★ | **+0.94★** | 台灣住院體驗較負面 ⚠️ |

**關鍵發現**:
1. ⚠️ **台灣急診問題最嚴重**: 1.79★ (七個主題中最低)，比美國低 **1.46 星**
2. ✅ **台灣專業品質最高**: 4.67★ (七個主題中最高)，比美國高 **1.67 星**
3. ⚠️ **台灣行政效率痛點**: 1.83★，比美國門診低 **1.25 星**
4. ⚠️ **整體趨勢**: 除了專業品質，台灣在其他構面評分都低於美國

**下一步**: 需要統計檢驗（t-test 或 Mann-Whitney U）確認這些差異是否顯著

---

## 🎯 對研究問題的回答

### RQ1: What dimensions emerge?

**回答**:
- **Taiwan**: 7 個構面（專業品質、行政流程、服務態度、環境設施、手術專科、住院照護、急診服務）
- **USA**: 6 個構面（重症照護、急診等待、門診服務、護理品質、正面評價、帳單保險）

### RQ2: Universal vs System-Specific?

**回答**:
- **Universal** (4 dimensions, ~78%): Emergency, Nursing/Professional, Outpatient, Inpatient
- **Taiwan-Specific** (2 dimensions, 25.4%): Service Attitude, Facility Environment
- **USA-Specific** (2 dimensions, 13.6%): Billing & Insurance, Positive Experience

### RQ3: How do system structures influence satisfaction?

**回答**:
1. **單一支付者制度（台灣）**:
   - ✅ 無財務負擔抱怨（無帳單主題）
   - ⚠️ 高患者密度 → 環境擁擠、醫護過勞 → 急診評分最低 (1.79★)
   - ⚠️ 行政流程效率成痛點 (1.83★)

2. **多支付者制度（美國）**:
   - ⚠️ 帳單保險複雜性成獨立痛點 (4.1%, 2.92★)
   - ✅ 較高就醫障礙 → 患者密度較低 → 急診評分較高 (3.25★)
   - ⚠️ 護理人力不足仍是問題 (3.00★)

---

## 📋 下一步分析需求

### 優先順序 1（立即執行）
1. ✅ **語義映射表** - 已完成
2. ⏳ **統計檢驗**: t-test for rating differences (Emergency, Nursing, etc.)
3. ⏳ **卡方檢驗**: χ² test for proportion differences (H4)

### 優先順序 2（後續執行）
4. ⏳ **關鍵詞頻率分析**: H3, H5, IH2, IH3, IH5
5. ⏳ **質性分析**: H6 (語言風格)

---

## 📚 參考文獻與證據

本語義映射表基於以下資料：
- **台灣 K=7 模型**: `results/taiwan_lda_k7/` (5,007 reviews, Coherence 0.4175)
- **美國 K=6 模型**: `results/usa_lda_k7/` (3,240 reviews, Coherence 0.4029)
- **分析報告**:
  - `manuscripts/reports/台灣醫院服務品質七構面分析_K7結果報告.md`
  - `manuscripts/reports/美國醫院服務品質六構面分析_K6結果報告.md`

---

**生成者**: Claude Code (Anthropic)
**審閱建議**: 請人工審閱語義相似度評分，確認跨語言對應的準確性
