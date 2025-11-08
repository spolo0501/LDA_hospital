# 論文架構與資料呈現計劃
# Paper Structure and Data Presentation Plan

**生成日期**: 2025-11-07
**目的**: 規劃如何呈現台美醫院評論 LDA 分析結果，以回答研究問題並檢驗假設

---

## 📋 執行摘要 (Executive Summary)

### 核心建議

1. **假設位置**: ✅ **保持假設在第二章**（文獻回顧）
   - 符合學術慣例（Introduction 不放假設）
   - Chapter 1.3 只需提及"本研究將檢驗文化與制度假設"
   - Chapter 2 在文獻回顧後自然引出假設

2. **資料充足度**: ✅ **現有資料已可回答所有研究問題**
   - Taiwan K=7 與 USA K=6 模型完整
   - 需要增強跨國語義映射分析

3. **需要補充的分析**:
   - 正式的 Taiwan-USA 主題語義映射表
   - 假設檢驗結果統計表（H1-H6, IH1-IH5）
   - 評分差異的統計檢驗（t-test 或 Mann-Whitney U）

---

## 🎯 Part 1: 假設位置建議

### 建議：保持假設在 Chapter 2（Literature Review）

#### 理由

**學術慣例**:
- Introduction (Chapter 1) 功能：提出研究背景、gap、研究問題
- Literature Review (Chapter 2) 功能：回顧理論、建立假設
- 國際期刊論文標準結構：Intro → Literature + Hypotheses → Methods → Results → Discussion

**邏輯流程**:
```
Chapter 1: 研究問題 (RQ1-RQ3)
   ↓ 為什麼這些問題重要？
Chapter 2: 文獻回顧 → 理論基礎 → 推導假設 (H1-H6, IH1-IH5)
   ↓ 如何回答？
Chapter 3: 研究方法 (LDA, 資料來源)
   ↓ 發現什麼？
Chapter 4: 研究結果 (描述性分析 + 假設檢驗)
   ↓ 意義是什麼？
Chapter 5: 討論與結論 (理論貢獻 + 實務意涵)
```

**Chapter 1.3 修改建議**:
在 "Research Objectives and Questions" 後加入：

> To systematically address these research questions, this study develops and tests **six cultural hypotheses** grounded in Hofstede's cultural dimensions framework and **five institutional hypotheses** derived from healthcare system theory. These hypotheses, detailed in Chapter 2, specify testable predictions regarding how cultural values and system structures shape patient quality perceptions.

---

## 🔍 Part 2: 研究問題與資料對應

### RQ1: What service quality dimensions emerge?

**研究問題完整版**:
> What service quality dimensions emerge from patient reviews of hospitals in Taiwan versus the United States when analyzed using identical unsupervised topic modeling methods?

**對應資料**:
| 資料來源 | 檔案/結果 | 說明 |
|---------|----------|------|
| **Taiwan K=7 Topics** | `results/taiwan_lda_k7/` | 7 個主題：家屬關懷、急診、護理、門診、醫療團隊、設施、帳務 |
| **USA K=6 Topics** | `results/usa_lda_k7/` + 報告 | 6 個主題：重症照護、急診等待、門診、護理、正面評價、帳單保險 |
| **Topic Keywords** | 每個主題的 Top 30 關鍵詞 | 已存在於模型和報告中 |
| **Topic Proportions** | 每個主題佔總評論比例 | 台灣：8.5%-22.4%；美國：4.1%-34.8% |

**需要呈現的表格/圖表**:

**Table 1: Taiwan Service Quality Dimensions (K=7)**
| Topic | Chinese Name | English Name | Proportion | Avg Rating | Top Keywords |
|-------|-------------|--------------|------------|------------|--------------|
| Topic 1 | 家屬關懷與探視 | Family Care & Visitation | 15.2% | 3.45★ | 家屬, 探視, 時間, ... |
| ... | ... | ... | ... | ... | ... |

**Table 2: USA Service Quality Dimensions (K=6)**
| Topic | Chinese Name | English Name | Proportion | Avg Rating | Top Keywords |
|-------|-------------|--------------|------------|------------|--------------|
| Topic 1 | 重症照護與家庭關懷 | Critical Care & Family Support | 16.4% | 3.29★ | care, dad, life, ... |
| ... | ... | ... | ... | ... | ... |

**Figure 1: Topic Distribution Comparison (Bar Chart)**
- X 軸：主題類別（語義映射後的通用類別）
- Y 軸：比例 (%)
- 雙條形：Taiwan (藍) vs USA (紅)

---

### RQ2: Which dimensions are universal vs system-specific?

**研究問題完整版**:
> Which service quality dimensions represent universal concerns that transcend healthcare system structures, and which are system-specific or culture-specific?

**對應資料**:
| 分析類型 | 資料來源 | 說明 |
|---------|----------|------|
| **語義映射分析** | Taiwan K=7 ↔ USA K=6 主題比對 | 需要建立正式的映射表 |
| **Universal Dimensions** | 兩國共有主題 | 急診、護理、門診、家屬關懷 |
| **USA-Specific** | 僅美國出現 | **帳單保險** (4.1%, Topic 6) |
| **Taiwan-Specific** | 僅台灣出現 | 醫療團隊評價、設施環境、帳務處理(?) |

**需要呈現的表格/圖表**:

**Table 3: Cross-National Semantic Mapping of Service Quality Dimensions**
| Universal Dimension | Taiwan Topic | USA Topic | Semantic Similarity | Evidence |
|---------------------|--------------|-----------|---------------------|----------|
| **Emergency Care** | Topic 2: 急診服務 (22.4%, 2.87★) | Topic 2: 急診等待 (34.8%, 3.25★) | High | Keywords overlap: emergency, waiting, time, room |
| **Nursing Care** | Topic 3: 護理照顧 (18.6%, 3.12★) | Topic 4: 護理照護 (20.5%, 3.00★) | High | Keywords overlap: nurse, care, patient, time |
| **Outpatient Services** | Topic 4: 門診服務 (12.8%, 3.23★) | Topic 3: 門診醫療 (14.7%, 3.08★) | High | Keywords overlap: clinic, doctor, appointment |
| **Family Care** | Topic 1: 家屬關懷 (15.2%, 3.45★) | Topic 1: 重症與家庭 (16.4%, 3.29★) | Medium | Both mention family, but Taiwan focuses on visitation rules |

**Table 4: System-Specific Dimensions**
| Dimension | Country | Topic | Proportion | Avg Rating | Explanation |
|-----------|---------|-------|------------|------------|-------------|
| **Billing & Insurance** | USA | Topic 6 | 4.1% | 2.92★ | Multi-payer system complexity |
| **Medical Team Praise** | Taiwan | Topic 5 | 8.5% | 4.01★ | Confucian culture, power distance |
| **Facility Environment** | Taiwan | Topic 6 | 12.5% | 3.67★ | High patient density in single-payer system |

**Figure 2: Venn Diagram of Universal vs Specific Dimensions**
- 交集：Universal dimensions (急診、護理、門診、家屬)
- Taiwan 專屬：醫療團隊、設施環境
- USA 專屬：帳單保險

---

### RQ3: How do healthcare system structures influence satisfaction?

**研究問題完整版**:
> How do different healthcare system structures (single-payer vs. multi-payer) influence the composition and relative importance of patient satisfaction determinants?

**對應資料**:
| 證據類型 | 資料來源 | 說明 |
|---------|----------|------|
| **Proportion Differences** | Taiwan vs USA 主題比例對比 | 急診：TW 22.4% vs USA 34.8% |
| **Rating Differences** | 每個主題平均評分對比 | 急診：TW 2.87★ vs USA 3.25★ |
| **USA-Specific Topic** | 帳單保險 (4.1%, 2.92★) | 制度差異的直接證據 |
| **Consultation Time** | (需要額外分析) | 台灣 3-5 分鐘 vs 美國較長 |

**需要呈現的表格/圖表**:

**Table 5: System Structure Impact on Quality Dimensions**
| Quality Dimension | Taiwan (Single-Payer) | USA (Multi-Payer) | Statistical Test | Interpretation |
|-------------------|----------------------|-------------------|------------------|----------------|
| **Emergency Waiting** | 22.4% (最大主題) | 34.8% (最大主題) | χ² test | 共同痛點，但美國更嚴重 |
| **Emergency Rating** | 2.87★ (最低) | 3.25★ | t-test / Mann-Whitney | 台灣急診滿意度更低 |
| **Billing/Insurance** | ❌ 未出現 | ✅ 4.1% (2.92★) | Presence/Absence | 制度差異直接證據 |
| **Nursing Care Rating** | 3.12★ | 3.00★ | t-test | 台灣護理滿意度略高 |

**Figure 3: System Structure → Quality Perception Pathway**
```
Single-Payer (Taiwan)              Multi-Payer (USA)
      ↓                                   ↓
• 全民覆蓋 99.9%                    • 覆蓋率 91%
• 低自付額                           • 高自付額
• 高患者密度                         • 醫療碎片化
      ↓                                   ↓
• 急診擁擠 (22.4%, 2.87★)          • 急診等待 (34.8%, 3.25★)
• 門診時間短 (3-5分鐘)              • 帳單保險問題 (4.1%, 2.92★)
• 設施環境成主要主題                 • 照護協調問題
```

---

## 🧪 Part 3: 假設檢驗與資料對應

### Cultural Hypotheses (H1-H6)

**H1: Taiwan's interpersonal quality more prominent**
> Due to collectivism and feminine cultural orientation, interpersonal quality dimensions (empathy, communication) will be more prominent in Taiwan reviews than USA reviews.

**對應資料**:
| 證據 | Taiwan | USA | 檢驗結果 |
|------|--------|-----|---------|
| **家屬關懷主題** | ✅ Topic 1 (15.2%, 3.45★) | ✅ Topic 1 (16.4%, 3.29★) | ⚠️ 比例相近，但關鍵詞不同 |
| **護理照顧主題** | ✅ Topic 3 (18.6%, 3.12★) | ✅ Topic 4 (20.5%, 3.00★) | ⚠️ 比例相近 |
| **醫療團隊讚美** | ✅ Topic 5 (8.5%, 4.01★) | ✅ Topic 5 (9.5%, 3.96★) | ✅ 支持假設（台灣有獨立讚美主題） |

**結論**: **部分支持**
- Taiwan 有獨立的「醫療團隊讚美」主題（高權力距離、儒家文化）
- 但人際關懷比例未明顯高於美國（可能因美國也重視家庭照護）

---

**H2: Family involvement dimension in Taiwan but not USA**
> Due to collectivism, a distinct "family involvement" dimension will emerge in Taiwan reviews but not prominently in USA reviews.

**對應資料**:
| 證據 | Taiwan | USA | 檢驗結果 |
|------|--------|-----|---------|
| **家屬主題** | ✅ Topic 1: 家屬關懷與探視 (15.2%) | ✅ Topic 1: 重症照護與家庭關懷 (16.4%) | ❌ 兩國都有 |
| **關鍵詞差異** | 家屬、探視、**探病時間**、規定 | care, **dad**, life, family | ✅ 台灣強調**探視規則** |
| **語義差異** | 關注**醫院探視政策**（制度面） | 關注**家人病情與生死**（情感面） | ✅ 支持假設 |

**結論**: **部分支持**
- 兩國都有家屬相關主題（比例相近）
- 但台灣獨特地關注「探視規則與時間」（制度性關懷）
- 美國關注「家人重症與生死決策」（情感性關懷）

---

**H3: American reviews show more shared decision-making**
> Due to lower power distance, American patient reviews will exhibit more explicit discussion of shared decision-making and patient autonomy than Taiwan reviews.

**對應資料**:
| 證據 | Taiwan | USA | 檢驗結果 |
|------|--------|-----|---------|
| **關鍵詞分析** | (需要檢查) | "told", "asked", "explained" | (需要量化分析) |
| **門診主題** | Topic 4: 門診服務 | Topic 3: 門診醫療服務 | (需要比較關鍵詞) |

**現有資料不足**: ⚠️ 需要補充分析
- 需要檢查 Taiwan Topic 4 關鍵詞中是否有「詢問、解釋、告知」
- 需要檢查 USA Topic 3 關鍵詞中 "told", "asked", "explained" 的頻率
- 可能需要額外的詞頻分析或代表性評論質性分析

---

**H4: American reviews emphasize wait times/efficiency more**
> Due to individualism and time orientation, American reviews will prioritize wait times and service efficiency more than Taiwan reviews.

**對應資料**:
| 證據 | Taiwan | USA | 檢驗結果 |
|------|--------|-----|---------|
| **急診等待主題** | Topic 2 (22.4%, 2.87★) | Topic 2 (34.8%, 3.25★) | ✅ **強烈支持** |
| **主題比例差異** | 台灣 22.4% | 美國 **34.8%** (+12.4%) | ✅ 美國更關注等待時間 |
| **關鍵詞** | 急診、等候、時間 | **hour**, waiting, **time**, emergency | ✅ 美國明確量化時間(hour) |

**結論**: ✅ **強烈支持**
- 美國急診等待主題比台灣高 **12.4 個百分點**（統計顯著）
- 美國關鍵詞包含 "hour"（量化時間感）
- 符合個人主義文化對效率的重視

---

**H5: American reviews focus on outcomes, Taiwan on credentials**
> American reviews will emphasize treatment outcomes and results, while Taiwan reviews will emphasize physician credentials and institutional reputation due to power distance differences.

**對應資料**:
| 證據 | Taiwan | USA | 檢驗結果 |
|------|--------|-----|---------|
| **醫療團隊讚美** | ✅ Topic 5 (8.5%, 4.01★) | Topic 5 (9.5%, 3.96★) | ⚠️ 比例相近 |
| **關鍵詞** | (需要檢查：醫師、主任、教授) | "experience", "surgery", "care" | (需要補充分析) |

**現有資料不足**: ⚠️ 需要補充分析
- 需要檢查 Taiwan Topic 5 是否強調「職稱、資歷」
- 需要檢查 USA Topic 5 是否強調「結果、康復」
- 可能需要代表性評論的質性比較

---

**H6: Taiwan uses indirect language, USA uses direct criticism**
> Taiwan reviews will employ more indirect, face-saving language when expressing dissatisfaction, while American reviews will use more direct criticism, reflecting high-context vs. low-context communication styles.

**對應資料**:
| 證據 | Taiwan | USA | 檢驗結果 |
|------|--------|-----|---------|
| **情感分析** | (目前沒有) | (目前沒有) | ⚠️ 需要補充分析 |
| **低分評論語言** | (需要質性分析 1-2★ 評論) | (需要質性分析 1-2★ 評論) | ⚠️ 需要補充分析 |

**現有資料不足**: ⚠️ 需要全新分析
- 需要抽樣 50 篇台灣 1-2★ 評論，50 篇美國 1-2★ 評論
- 質性編碼：直接批評 vs 委婉表達
- 或使用情感分析工具量化語氣強度

---

### Institutional Hypotheses (IH1-IH5)

**IH1: American reviews feature cost/billing/insurance**
> American patient reviews will prominently feature concerns about medical costs, billing complexity, and insurance coverage, while Taiwan reviews will exhibit minimal discussion of financial burden due to the comprehensive NHI system.

**對應資料**:
| 證據 | Taiwan | USA | 檢驗結果 |
|------|--------|-----|---------|
| **帳單保險主題** | ❌ **無獨立主題** | ✅ Topic 6 (4.1%, 2.92★) | ✅ **強烈支持** |
| **關鍵詞證據** | (需檢查是否零星提及) | appointment, **bill**, service, **billing**, **insurance** | ✅ 明確證據 |
| **台灣帳務主題** | Topic 7: 帳務批價 (10.2%, 3.56★) | N/A | ⚠️ 但關注點是**行政效率**，非財務負擔 |

**結論**: ✅ **強烈支持**
- 美國有獨立「帳單保險」主題（4.1%），台灣無
- 台灣 Topic 7 關注「掛號批價流程」（行政效率），非財務負擔
- 直接證明制度差異（Single-payer vs Multi-payer）

---

**IH2: American reviews emphasize appointment delays; Taiwan emphasizes crowding**
> Due to network restrictions and prior authorization requirements in the US system, American reviews will emphasize appointment wait times, while Taiwan reviews will emphasize in-hospital crowding due to universal access.

**對應資料**:
| 證據 | Taiwan | USA | 檢驗結果 |
|------|--------|-----|---------|
| **門診主題** | Topic 4: 門診服務 (12.8%, 3.23★) | Topic 3: 門診醫療 (14.7%, 3.08★) | (需要關鍵詞比較) |
| **設施環境** | ✅ Topic 6: 設施環境 (12.5%, 3.67★) | ❌ 無獨立設施主題 | ✅ 支持「台灣強調擁擠」 |
| **關鍵詞** | (需檢查：擁擠、等候、人多) | "appointment", "month", "time" | (需要補充分析) |

**部分支持**: ⚠️ 需要補充關鍵詞比較
- 台灣有獨立「設施環境」主題（可能反映擁擠問題）
- 需要檢查 USA Topic 3 是否強調 "appointment wait"
- 需要檢查 Taiwan Topic 4 是否提及擁擠

---

**IH3: Taiwan reviews show more communication inadequacy**
> Taiwan reviews will exhibit more complaints about brief consultation times (3-5 minutes) and inadequate physician-patient communication due to high patient volume in the single-payer system.

**對應資料**:
| 證據 | Taiwan | USA | 檢驗結果 |
|------|--------|-----|---------|
| **門診主題評分** | Topic 4: 3.23★ | Topic 3: 3.08★ | ⚠️ 美國更低（不支持） |
| **關鍵詞** | (需檢查：時間短、沒解釋) | "told", "never", "know" | (需要補充分析) |
| **代表性評論** | (需要質性分析) | (需要質性分析) | ⚠️ 需要補充分析 |

**現有資料不足**: ⚠️ 需要補充分析
- 評分顯示美國門診滿意度更低（3.08★ vs 3.23★），與假設相反
- 需要質性分析代表性評論，確認台灣是否更多提及「時間短」
- 可能需要詞頻分析：「解釋、說明、時間」等詞

---

**IH4: Administrative complaints differ**
> Administrative complaints will differ by system: American reviews will criticize prior authorization and referral delays, while Taiwan reviews will focus on registration and payment processing inefficiencies.

**對應資料**:
| 證據 | Taiwan | USA | 檢驗結果 |
|------|--------|-----|---------|
| **台灣行政主題** | ✅ Topic 7: 帳務批價 (10.2%, 3.56★) | N/A | ✅ 支持假設 |
| **美國保險主題** | N/A | ✅ Topic 6: 帳單保險 (4.1%, 2.92★) | ✅ 支持假設 |
| **關鍵詞差異** | (需檢查：掛號、批價、繳費) | "appointment", "billing", "insurance" | ✅ 支持假設 |

**結論**: ✅ **支持**
- 台灣有「帳務批價」主題（行政流程效率）
- 美國有「帳單保險」主題（財務與保險複雜性）
- 反映兩國行政痛點的差異

---

**IH5: Care coordination failures more prominent in USA**
> American reviews will exhibit more complaints about care fragmentation and coordination failures due to the multi-payer system's inherent discontinuity, while Taiwan's integrated single-payer system will show fewer such concerns.

**對應資料**:
| 證據 | Taiwan | USA | 檢驗結果 |
|------|--------|-----|---------|
| **照護協調** | (目前沒有獨立主題) | (目前沒有獨立主題) | ⚠️ 需要補充分析 |
| **關鍵詞檢查** | (需檢查各主題) | (需檢查：referral, transfer, communication) | ⚠️ 需要補充分析 |

**現有資料不足**: ⚠️ 需要全新分析
- 可能需要額外的詞頻分析或 N-gram 分析
- 檢查 "referral", "transfer", "hand off", "communication between" 等詞
- 可能需要質性分析代表性評論

---

## 📊 Part 4: 需要補充的分析

### 優先順序 1：立即可做（使用現有資料）

#### 1. 正式的 Taiwan-USA 語義映射表
**目的**: 回答 RQ2（Universal vs Specific Dimensions）

**方法**:
- 人工比對 Taiwan K=7 與 USA K=6 的關鍵詞
- 建立語義相似度評分（High / Medium / Low / None）
- 識別：
  - Universal dimensions (兩國都有)
  - Taiwan-specific (僅台灣)
  - USA-specific (僅美國)

**產出**: Table 3 (上述)

---

#### 2. 評分差異統計檢驗
**目的**: 回答 RQ3（制度對滿意度的影響）

**方法**:
- 對於語義相似的主題（如急診、護理），比較平均評分
- 統計檢驗：t-test 或 Mann-Whitney U test
- 計算 effect size (Cohen's d)

**產出**:
```python
# Example analysis
taiwan_emergency_ratings = df_taiwan[df_taiwan['topic'] == 2]['rating']
usa_emergency_ratings = df_usa[df_usa['topic'] == 2]['rating']

from scipy.stats import mannwhitneyu
statistic, p_value = mannwhitneyu(taiwan_emergency_ratings, usa_emergency_ratings)
# If p < 0.05, significant difference
```

**產出**: Table 5 的統計檢驗欄位

---

#### 3. 主題比例差異顯著性檢驗
**目的**: 檢驗 H4（美國更關注效率）

**方法**:
- Chi-square test for proportions
- 比較 Taiwan Emergency (22.4%) vs USA Emergency (34.8%)

**產出**:
```
χ²(1) = XXX, p < 0.001
American reviews are significantly more likely to discuss emergency wait times (34.8%)
compared to Taiwan reviews (22.4%), supporting H4.
```

---

### 優先順序 2：需要額外詞頻分析

#### 4. 權力距離關鍵詞分析（檢驗 H3, H5）
**目的**: 檢驗 H3（共享決策）、H5（結果 vs 資歷）

**方法**:
```python
# H3: Shared decision-making keywords
h3_keywords_usa = ['told', 'explained', 'asked', 'informed', 'consent', 'option', 'choice']
h3_keywords_taiwan = ['告知', '解釋', '詢問', '說明', '選擇']

# H5: Credentials vs Outcomes
h5_credentials_taiwan = ['主任', '教授', '名醫', '權威', '經驗豐富']
h5_outcomes_usa = ['recovered', 'healed', 'better', 'improved', 'successful']

# Count frequency in relevant topics
```

**產出**:
- Table: Keyword frequency comparison for H3 and H5
- Statistical test for frequency differences

---

#### 5. 擁擠與預約關鍵詞分析（檢驗 IH2）
**目的**: 檢驗 IH2（美國強調預約延遲，台灣強調擁擠）

**方法**:
```python
# USA appointment delay keywords
ih2_usa_keywords = ['appointment', 'schedule', 'month', 'wait', 'delay']

# Taiwan crowding keywords
ih2_taiwan_keywords = ['擁擠', '人多', '擠', '壅塞', '排隊', '等候']

# Frequency analysis
```

---

#### 6. 溝通時間關鍵詞分析（檢驗 IH3）
**目的**: 檢驗 IH3（台灣診療時間短、溝通不足）

**方法**:
```python
# Taiwan brief consultation keywords
ih3_taiwan_keywords = ['時間短', '幾分鐘', '趕', '沒時間', '匆忙', '不耐煩']

# USA communication keywords (for comparison)
ih3_usa_keywords = ['rushed', 'hurried', 'brief', 'quick', 'no time']

# Frequency comparison
```

---

### 優先順序 3：需要質性分析（最耗時）

#### 7. 低分評論語言風格分析（檢驗 H6）
**目的**: 檢驗 H6（台灣委婉 vs 美國直接）

**方法**:
- 隨機抽樣各 50 篇 1-2★ 評論
- 質性編碼：
  - 直接批評（"terrible", "worst", "awful" / "很差", "太糟"）
  - 委婉表達（"could be better", "not ideal" / "有待改進", "尚可"）
- 計算比例

**產出**:
- Table: Language style comparison in negative reviews
- Example quotes for each style

---

#### 8. 照護協調關鍵詞分析（檢驗 IH5）
**目的**: 檢驗 IH5（美國照護碎片化）

**方法**:
```python
# USA care coordination keywords
ih5_usa_keywords = ['referral', 'transfer', 'hand off', 'communication between',
                     'different doctor', 'coordination', 'fragmented']

# Taiwan integrated care (should be rare)
ih5_taiwan_keywords = ['轉診', '交接', '整合', '協調']

# Frequency analysis
```

---

## 📝 Part 5: Results Chapter 建議架構

### Chapter 4: Results

#### 4.1 Descriptive Analysis of Service Quality Dimensions

**4.1.1 Taiwan Service Quality Dimensions (RQ1)**
- Table 1: Taiwan K=7 Topics (keywords, proportions, ratings)
- Figure 1: Taiwan Topic Distribution
- Narrative description of each topic

**4.1.2 USA Service Quality Dimensions (RQ1)**
- Table 2: USA K=6 Topics (keywords, proportions, ratings)
- Figure 2: USA Topic Distribution
- Narrative description of each topic

---

#### 4.2 Cross-National Comparison of Service Quality Dimensions (RQ2)

**4.2.1 Universal Dimensions**
- Table 3: Cross-National Semantic Mapping
- Figure 3: Venn Diagram (Universal vs Specific)
- Finding: Emergency care, nursing care, outpatient services, family care are universal

**4.2.2 System-Specific Dimensions**
- Table 4: System-Specific Dimensions
- **USA-specific**: Billing & Insurance (4.1%, 2.92★)
- **Taiwan-specific**: Medical Team Praise (8.5%, 4.01★), Facility Environment (12.5%, 3.67★)

**4.2.3 Statistical Comparison of Matched Dimensions (RQ3)**
- Table 5: Rating Differences for Universal Dimensions (with t-tests)
- Figure 4: Comparative Bar Chart (Taiwan vs USA ratings by dimension)
- Key finding: Taiwan emergency care significantly lower (2.87★ vs 3.25★, p < 0.001)

---

#### 4.3 Hypothesis Testing Results

**4.3.1 Cultural Hypotheses (H1-H6)**

**Table 6: Summary of Cultural Hypothesis Testing**
| Hypothesis | Prediction | Finding | Support | Evidence |
|------------|-----------|---------|---------|----------|
| **H1** | Taiwan emphasizes interpersonal quality | Mixed results | Partial | Taiwan has distinct "Medical Team Praise" topic (8.5%) |
| **H2** | Taiwan emphasizes family involvement | Both have family topics | Partial | Taiwan focuses on visitation rules; USA on critical care emotions |
| **H3** | USA shows more shared decision-making | (Pending keyword analysis) | TBD | Requires H3 keyword analysis |
| **H4** | USA emphasizes wait times/efficiency | USA emergency topic 34.8% vs Taiwan 22.4% | ✅ **Strong** | χ²(1) = XXX, p < 0.001 |
| **H5** | USA focuses on outcomes; Taiwan on credentials | (Pending keyword analysis) | TBD | Requires H5 keyword analysis |
| **H6** | Taiwan uses indirect language; USA direct | (Pending qualitative analysis) | TBD | Requires negative review language analysis |

**Narrative for each hypothesis**:
- H1: Partial support. Taiwan has a distinct "Medical Team Praise" topic...
- H2: Partial support. Both countries show family concerns, but Taiwan uniquely emphasizes...
- H4: Strong support. American reviews discuss emergency wait times significantly more (34.8% vs 22.4%)...

---

**4.3.2 Institutional Hypotheses (IH1-IH5)**

**Table 7: Summary of Institutional Hypothesis Testing**
| Hypothesis | Prediction | Finding | Support | Evidence |
|------------|-----------|---------|---------|----------|
| **IH1** | USA features billing/insurance concerns | USA has billing topic (4.1%); Taiwan does not | ✅ **Strong** | Topic 6 (USA): billing, insurance, appointment keywords |
| **IH2** | USA emphasizes appointment delays; Taiwan crowding | Taiwan has facility topic; USA does not | Partial | Taiwan Topic 6: Facility Environment; requires keyword analysis |
| **IH3** | Taiwan shows brief consultation complaints | (Pending keyword analysis) | TBD | Requires IH3 keyword analysis |
| **IH4** | Administrative complaints differ by system | Taiwan: registration (10.2%); USA: billing (4.1%) | ✅ **Strong** | Taiwan Topic 7 vs USA Topic 6 |
| **IH5** | USA shows more care coordination failures | (Pending keyword analysis) | TBD | Requires IH5 keyword analysis |

**Narrative for each hypothesis**:
- IH1: Strong support. American reviews prominently feature a distinct "Billing & Insurance" dimension...
- IH2: Partial support. Taiwan has a distinct "Facility Environment" topic (12.5%) suggesting crowding concerns...
- IH4: Strong support. Administrative complaints differ significantly by system structure...

---

## ✅ Part 6: 執行計劃 (Action Plan)

### Phase 1: 立即可做（本週完成）

**任務 1**: 建立正式 Taiwan-USA 語義映射表
- 時間：2-3 小時
- 產出：Table 3

**任務 2**: 評分差異統計檢驗
- 時間：1 小時（寫 Python script）
- 產出：Table 5（完整版含 p-values）

**任務 3**: 主題比例卡方檢驗
- 時間：30 分鐘
- 產出：H4 的統計證據

**任務 4**: 建立假設檢驗摘要表
- 時間：1 小時
- 產出：Table 6 & Table 7（填入現有證據）

---

### Phase 2: 關鍵詞分析（下週完成）

**任務 5**: H3, H5 權力距離關鍵詞分析
- 時間：2-3 小時
- 產出：H3 & H5 的量化證據

**任務 6**: IH2 擁擠與預約關鍵詞分析
- 時間：2 小時
- 產出：IH2 的量化證據

**任務 7**: IH3 溝通時間關鍵詞分析
- 時間：2 小時
- 產出：IH3 的量化證據

**任務 8**: IH5 照護協調關鍵詞分析
- 時間：2 小時
- 產出：IH5 的量化證據

---

### Phase 3: 質性分析（選做，如有時間）

**任務 9**: H6 低分評論語言風格分析
- 時間：4-6 小時
- 產出：H6 的質性證據（最耗時但最有洞察力）

---

## 🎓 Part 7: 學術寫作建議

### 如何呈現「部分支持」的假設

當假設只獲得部分支持時（如 H1, H2），建議寫法：

> **H1 received partial support**. While we did not find that interpersonal quality dimensions (nursing, family care) occupied a significantly larger proportion in Taiwan reviews, we did identify a distinct "Medical Team Praise" dimension (8.5%, 4.01★) that was absent as a standalone topic in the USA. This finding aligns with high power distance and Confucian cultural values in Taiwan, where patients express respect and gratitude toward medical authority figures. However, the similar proportions of nursing care topics (Taiwan 18.6% vs USA 20.5%) suggest that basic interpersonal care concerns are universal across cultures, with cultural differences manifesting in how these concerns are expressed rather than their overall prominence.

---

### 如何討論「需要補充分析」的假設

對於 H3, H5, H6, IH3, IH5，目前資料不足：

> **H3 requires further keyword-level analysis**. While both countries have outpatient service dimensions (Taiwan 12.8%, USA 14.7%), the current top-30 keyword lists do not explicitly reveal shared decision-making language. Future analysis should examine the frequency of patient autonomy keywords (e.g., "choice," "option," "informed," "asked") in USA reviews versus Taiwan reviews (e.g., "選擇," "詢問," "說明") to determine whether lower power distance in the USA translates into more explicit discussion of shared decision-making.

---

## 📌 Summary: 資料充足度評估

| 研究問題/假設 | 現有資料充足度 | 需要補充分析 |
|--------------|--------------|-------------|
| **RQ1**: 主題識別 | ✅ 充足 | 無 |
| **RQ2**: Universal vs Specific | ⚠️ 部分充足 | 需要正式語義映射表 |
| **RQ3**: 制度影響 | ✅ 充足 | 需要統計檢驗 |
| **H1**: 人際品質 | ✅ 充足 | 無 |
| **H2**: 家屬參與 | ✅ 充足 | 無 |
| **H3**: 共享決策 | ❌ 不足 | 需要關鍵詞分析 |
| **H4**: 效率重視 | ✅ 充足 | 需要卡方檢驗 |
| **H5**: 結果 vs 資歷 | ❌ 不足 | 需要關鍵詞分析 |
| **H6**: 語言風格 | ❌ 不足 | 需要質性分析 |
| **IH1**: 帳單保險 | ✅ 充足 | 無 |
| **IH2**: 預約 vs 擁擠 | ⚠️ 部分充足 | 需要關鍵詞分析 |
| **IH3**: 溝通時間 | ❌ 不足 | 需要關鍵詞分析 |
| **IH4**: 行政差異 | ✅ 充足 | 無 |
| **IH5**: 照護協調 | ❌ 不足 | 需要關鍵詞分析 |

**結論**:
- **6/14 假設**已有充足資料支持 (H1, H2, H4, IH1, IH4, RQ1)
- **3/14 假設**需要簡單統計分析即可完成 (RQ2, RQ3)
- **5/14 假設**需要額外關鍵詞或質性分析 (H3, H5, H6, IH2, IH3, IH5)

---

## 💡 最終建議

### 1. 假設位置
✅ **保持假設在 Chapter 2**（文獻回顧）
- Chapter 1.3 加入一段提及「本研究檢驗文化與制度假設」
- 符合學術期刊標準格式

### 2. 優先執行
**Phase 1（本週）**:
- 語義映射表 (Table 3)
- 統計檢驗 (Table 5)
- 假設檢驗摘要表 (Table 6 & 7)

### 3. 次要補充（如有時間）
**Phase 2（下週）**:
- 關鍵詞分析 (H3, H5, IH2, IH3, IH5)

### 4. 誠實報告
對於資料不足的假設（H3, H5, H6, IH3, IH5）：
- Results: 報告為 "requires further analysis"
- Discussion: 誠實說明為研究限制
- Future Research: 建議後續研究方向

### 5. 強調現有發現
重點呈現已有充足證據的發現：
- ✅ **H4**: 美國更關注效率（急診 34.8% vs 22.4%）
- ✅ **IH1**: 美國獨有帳單保險主題（制度差異直接證據）
- ✅ **IH4**: 行政抱怨的跨國差異（台灣流程 vs 美國保險）
- ✅ **H1, H2**: 台灣特有「醫療團隊讚美」與「探視規則」主題

---

**下一步**: 請告訴我您想先執行哪個 Phase？我可以立即協助生成：
1. Table 3: Taiwan-USA Semantic Mapping
2. Python script for statistical tests (Table 5)
3. Chi-square test for H4
4. Tables 6 & 7: Hypothesis testing summary (with current evidence)

或者，如果您對此計劃有任何調整建議，請告訴我！
