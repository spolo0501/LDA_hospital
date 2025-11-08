# Chapter 4: Results

## 4.1 Descriptive Analysis of Service Quality Dimensions

This chapter presents the findings from our Latent Dirichlet Allocation (LDA) analysis of patient reviews from Taiwan and the United States. We first describe the service quality dimensions that emerged from each country's dataset (Section 4.1), followed by a systematic cross-national comparison identifying universal versus system-specific dimensions (Section 4.2), and conclude with hypothesis testing results examining cultural and institutional differences (Section 4.3).

---

### 4.1.1 Taiwan Service Quality Dimensions (K=7)

Our LDA analysis of 5,007 Chinese-language patient reviews from Taiwan's 26 top-tier medical centers revealed **seven distinct service quality dimensions** (Coherence Score = 0.4175; Perplexity = -7.5039). Table 4.1 summarizes these dimensions, their prevalence, and patient satisfaction ratings.

**[Table 4.1: Taiwan Hospital Service Quality Dimensions (K=7)]**

| Topic | Dimension Name | Proportion | Avg Rating | Top-10 Keywords (English Translation) |
|-------|---------------|------------|------------|--------------------------------------|
| **Topic 1** | Medical Professional Quality<br>醫療專業品質 | **27.2%** | **4.67★** | physician, nurse, professional, thank you, gratitude, doctor, kind, medical, patient, staff |
| **Topic 2** | Registration & Billing Process<br>掛號批價流程 | 6.9% | 1.83★ | time, registration, consultation, appointment, payment, medication pickup, afternoon, clinic |
| **Topic 3** | Service Attitude Issues<br>服務態度問題 | 17.3% | **1.69★** | attitude, patient, nurse, staff, not, blood draw, examination, registration, impatient |
| **Topic 4** | Facility & Environment Quality<br>環境設施品質 | 8.1% | 2.73★ | time, parking lot, convenient, consultation, waiting, parking, elevator, center, flow |
| **Topic 5** | Surgical & Specialty Care<br>手術專科表現 | 5.3% | 4.02★ | physician, surgery, thank you, operation, surgery dept, nurse, orthopedics, treatment |
| **Topic 6** | Inpatient Care Experience<br>住院照護經驗 | 4.3% | 2.35★ | ward, hospitalization, family, patient, nurse, discharge, doctor, relatives, surgery |
| **Topic 7** | Emergency Medical Services<br>急診醫療服務 | **30.9%** | **1.79★** | doctor, we, emergency, patient, know, not, issue, nurse, examination, one |

**Key Findings:**

1. **Largest Topic: Emergency Services (30.9%)**
   - Emergency care represents patients' most frequent concern
   - Lowest satisfaction rating (1.79★) across all topics
   - Keywords emphasize waiting times ("時間"), crowding, and communication issues
   - Reflects systemic challenges in Taiwan's single-payer system: universal access without co-payment barriers leads to emergency room overcrowding

2. **Highest-Rated Topic: Medical Professional Quality (27.2%, 4.67★)**
   - Second-largest topic, accounting for over one-quarter of reviews
   - Patients express deep gratitude toward physicians and nurses ("感謝", "謝謝")
   - Keywords include "專業" (professional), "親切" (kind), "細心" (attentive), "團隊" (team)
   - May reflect cultural factors: high power distance and Confucian respect for medical authority (Hofstede, 2001)

3. **Lowest-Rated Topic: Service Attitude Issues (17.3%, 1.69★)**
   - Third-largest topic, indicating widespread concern
   - Keywords: "態度" (attitude), "不耐煩" (impatient), "口氣" (tone), "很差" (very poor)
   - Reflects tension between patient expectations and healthcare worker burnout under high patient volume

4. **Taiwan-Specific Dimension: Facility & Environment Quality (8.1%, 2.73★)**
   - Emerged as distinct dimension in K=7 but not in K=5 or K=6 models
   - Keywords: "停車場" (parking lot), "環境" (environment), "廁所" (restroom), "衛生" (hygiene), "動線" (flow)
   - Reflects infrastructure strain under single-payer system's high utilization rates

5. **Administrative Efficiency Concerns (6.9%, 1.83★)**
   - Registration, payment, and medication pickup process inefficiencies
   - Keywords: "掛號" (registration), "批價" (billing), "等到" (waiting until), "排隊" (queuing)
   - Second-lowest rating, indicating administrative burden as significant pain point

---

### 4.1.2 USA Hospital Service Quality Dimensions (K=6)

Our analysis of 3,240 English-language patient reviews from 28 top-ranked U.S. hospitals (US News & World Report) identified **six distinct service quality dimensions** (Coherence Score = 0.4029; Perplexity = -7.2254). Table 4.2 summarizes these findings.

**[Table 4.2: USA Hospital Service Quality Dimensions (K=6)]**

| Topic | Dimension Name | Proportion | Avg Rating | Top-10 Keywords |
|-------|---------------|------------|------------|----------------|
| **Topic 1** | Critical Care & Family Support<br>重症照護與家庭關懷 | 16.4% | 3.29★ | care, dad, life, patient, time, room, scan, year, surgery, could |
| **Topic 2** | Emergency & Waiting Time<br>急診等待時間問題 | **34.8%** | 3.25★ | room, patient, **hour**, time, waiting, nurse, emergency, care, day, back |
| **Topic 3** | Outpatient Care Services<br>門診醫療服務 | 14.7% | 3.08★ | care, clinic, doctor, even, help, pain, never, cleveland, told, know |
| **Topic 4** | Nursing Care Quality<br>護理照護品質 | 20.5% | **3.00★** | nurse, care, patient, time, hour, room, day, even, left, blood |
| **Topic 5** | Overall Positive Experience<br>整體正面評價 | 9.5% | **3.96★** | care, staff, **great**, **thank**, team, doctor, experience, **best**, surgery |
| **Topic 6** | Billing & Insurance Issues<br>帳單保險問題 | 4.1% | 2.92★ | appointment, **bill**, service, time, **billing**, **insurance**, patient, month, care, told |

**Key Findings:**

1. **Largest Topic: Emergency & Waiting Time (34.8%, 3.25★)**
   - Emergency care is patients' predominant concern, even more so than in Taiwan (+4.9 percentage points)
   - Keyword "hour" indicates explicit temporal quantification (e.g., "waited 6 hours")
   - Although still the largest pain point, satisfaction rating (3.25★) is notably higher than Taiwan's (1.79★)
   - Reflects multi-payer system's higher access barriers: lower patient volume relative to capacity

2. **Lowest-Rated Topic: Nursing Care Quality (20.5%, 3.00★)**
   - Second-largest topic, accounting for one-fifth of reviews
   - Keywords emphasize waiting ("hour", "time", "waiting"), inadequate attention ("never", "left"), and overnight care issues ("night")
   - Contrasts sharply with Taiwan, where nursing care receives highest praise (4.67★ in Topic 1)
   - Possible explanation: U.S. nurse-to-patient ratios, staffing shortages, or different service expectations

3. **Highest-Rated Topic: Overall Positive Experience (9.5%, 3.96★)**
   - Represents a distinct "praise" topic with keywords: "great", "thank", "best", "amazing"
   - Emerged as standalone dimension in U.S. data but not in Taiwan's
   - May reflect American review culture: tendency to write detailed positive reviews (Hao & Zhang, 2016)

4. **USA-Specific Dimension: Billing & Insurance Issues (4.1%, 2.92★)**
   - **Critical finding:** This dimension does not appear in Taiwan's data at all
   - Keywords: "bill", "billing", "insurance", "appointment", "month"
   - Direct evidence of multi-payer system complexity: insurance coverage disputes, surprise billing, prior authorization delays
   - Strongly supports Institutional Hypothesis 1 (IH1)

5. **Critical Care Focus (16.4%, 3.29★)**
   - Keywords suggest life-threatening conditions: "life", "dad", "father", "cancer", "worst", "surgery"
   - Higher prevalence than Taiwan's general inpatient care topic (16.4% vs. 4.3%)
   - Reflects U.S. system's high financial barriers: hospitalization predominantly for severe cases, less routine admissions

---

### 4.1.3 Model Performance and Topic Number Selection

**Taiwan K=7 Model Selection:**

We compared models with K=5, K=6, and K=7 topics. While K=5 achieved higher Coherence Score (0.4326), we selected K=7 for several substantive reasons:

1. ✅ **Facility & Environment dimension emerged only at K=7**, capturing 8.1% of reviews discussing parking, cleanliness, and infrastructure—a dimension absent in K=5 and K=6
2. ✅ **Separated surgical specialty care from general professional quality**, enabling finer-grained analysis of Taiwan's strengths
3. ✅ **Distinguished inpatient from emergency care**, reflecting different service contexts
4. ✅ **Aligns with SERVQUAL's multi-dimensional framework** and healthcare service quality theory (Brady & Cronin, 2001)

The modest decrease in Coherence (0.4326 → 0.4175; Δ = -0.0151) is acceptable given the substantive interpretability gains.

**USA K=6 Model Selection:**

Among K=5, K=6, and K=7 models, K=6 achieved:
- ✅ **Highest Coherence Score (0.4029)**, exceeding K=5 (0.3923) and K=7 (0.3887)
- ✅ **Successfully isolated the Billing & Insurance dimension (4.1%)**, which was mixed with other topics in K=5 and K=7
- ✅ **No overly small topics** (all topics > 4%), ensuring statistical reliability
- ✅ **Clear topic boundaries** with minimal keyword overlap

---

## 4.2 Cross-National Comparison of Service Quality Dimensions

This section addresses **Research Question 2**: *Which service quality dimensions represent universal concerns that transcend healthcare system structures, and which are system-specific or culture-specific?*

To enable rigorous cross-national comparison despite different optimal topic numbers (Taiwan K=7 vs. USA K=6), we employed **semantic mapping**: systematically comparing keywords, representative reviews, and thematic content to identify conceptually equivalent dimensions across languages and cultures.

---

### 4.2.1 Semantic Mapping Methodology

We assessed cross-lingual semantic similarity using three criteria:

1. **Keyword Overlap**: Proportion of top-30 keywords with equivalent meanings (e.g., "nurse" ↔ "護理師", "emergency" ↔ "急診")
2. **Thematic Content**: Qualitative analysis of high-probability reviews (topic probability > 0.6)
3. **Semantic Focus**: Whether topics address the same service quality aspect (e.g., both focus on waiting times vs. clinical outcomes)

Similarity was classified as:
- **High (✅)**: >70% keyword overlap, clear thematic equivalence
- **Medium (⚠️)**: 50-70% overlap, partial thematic equivalence
- **Low (❌)**: <50% overlap, different service aspects

---

### 4.2.2 Universal Service Quality Dimensions

Table 4.3 presents the four **universal dimensions** identified across both healthcare systems.

**[Table 4.3: Universal Service Quality Dimensions - Semantic Mapping]**

| Universal Dimension | Taiwan Topic (K=7) | USA Topic (K=6) | Similarity | Proportion Comparison | Rating Comparison |
|---------------------|-------------------|-----------------|------------|----------------------|-------------------|
| **1. Emergency Care** | Topic 7: 急診醫療服務<br>30.9%, 1.79★ | Topic 2: Emergency & Waiting Time<br>34.8%, 3.25★ | **High ✅** | US +3.9% | US +1.46★ |
| **2. Nursing/Professional Care** | Topic 1: 醫療專業品質<br>27.2%, 4.67★ | Topic 4: Nursing Care Quality<br>20.5%, 3.00★ | **Medium ⚠️** | TW +6.7% | TW +1.67★ |
| **3. Outpatient Services** | Topic 2: 掛號批價流程<br>6.9%, 1.83★ | Topic 3: Outpatient Care Services<br>14.7%, 3.08★ | **Medium ⚠️** | US +7.8% | US +1.25★ |
| **4. Inpatient/Critical Care** | Topic 6: 住院照護經驗<br>4.3%, 2.35★ | Topic 1: Critical Care & Family Support<br>16.4%, 3.29★ | **Medium ⚠️** | US +12.1% | US +0.94★ |

**Detailed Analysis:**

**Dimension 1: Emergency Care (High Similarity ✅)**

This represents the **strongest cross-national convergence**.

*Taiwan (Topic 7):* Keywords: "急診" (emergency), "醫生" (doctor), "病人" (patient), "時間" (time), "等待" (wait), "檢查" (examination)

*USA (Topic 2):* Keywords: "emergency", "room", "patient", "hour", "time", "waiting", "nurse", "care"

**Evidence of universality:**
- Largest topic in both countries (TW 30.9%, US 34.8%)
- Both emphasize waiting times: "時間" (time) vs. "hour" (explicit temporal quantification)
- Both mention emergency departments: "急診" vs. "emergency room"
- Shared pain point: inadequate staffing, overcrowding, long waits

**Key difference:**
- **Satisfaction gap**: Taiwan's emergency services receive substantially lower ratings (1.79★) compared to USA (3.25★)
- **Δ = +1.46 stars** (USA higher)
- **Possible explanations**:
  - *Taiwan*: Single-payer system's zero co-payment for emergency visits → higher patient volume → longer waits → lower satisfaction
  - *USA*: High emergency room costs ($1,000-$3,000 average) and insurance barriers → lower utilization → relatively shorter waits → higher (though still modest) satisfaction

**Implication for RQ2:** Emergency care is a **universal challenge** transcending healthcare systems, but system structures significantly influence satisfaction levels.

---

**Dimension 2: Nursing/Professional Care (Medium Similarity ⚠️)**

This dimension shows **partial semantic equivalence** with important scope differences.

*Taiwan (Topic 1):* Keywords: "醫師" (physician), "護理師" (nurse), "專業" (professional), "感謝" (thank you), "謝謝" (gratitude), "親切" (kind), "耐心" (patient), "細心" (attentive)

*USA (Topic 4):* Keywords: "nurse", "care", "patient", "time", "hour", "room", "day", "left", "blood", "waiting"

**Evidence of partial universality:**
- Both involve nursing care (護理師 ↔ nurse)
- Both discuss patient care experiences
- Both are among the largest topics (TW 27.2%, US 20.5%)

**Critical differences:**

1. **Scope:**
   - **Taiwan Topic 1 is broader**: Combines *both* physicians and nurses into unified "Medical Professional Quality" dimension
   - **USA Topic 4 is narrower**: Focuses specifically on *nursing staff*, with physicians discussed separately

2. **Sentiment:**
   - **Taiwan**: Highest satisfaction (4.67★), expressing gratitude and praise ("感謝", "謝謝", "親切", "細心")
   - **USA**: Lowest satisfaction (3.00★), emphasizing complaints ("left", "waiting", "never", "hour")
   - **Δ = -1.67 stars** (Taiwan significantly higher)

3. **Cultural interpretation:**
   - **Taiwan's high rating** may reflect:
     - High power distance (Hofstede, 2001): Patients defer to medical authority, express respect/gratitude
     - Confucian cultural values: Emphasis on hierarchy, reverence for professionals
     - Collectivist orientation: Appreciation for team-based care
   - **USA's low rating** may reflect:
     - Lower power distance: Patients more willing to criticize service failures
     - Individualistic culture: Higher expectations for personalized attention
     - Nursing staff shortages: Inadequate nurse-to-patient ratios, burnout

**Implication for RQ2:** Nursing/professional care is a **universal dimension**, but cultural and systemic factors profoundly shape how patients perceive and evaluate it. This partially supports Cultural Hypothesis 1 (H1).

---

**Dimension 3: Outpatient Services (Medium Similarity ⚠️)**

Semantic mapping reveals **different focal concerns** within the broad outpatient category.

*Taiwan (Topic 2):* Keywords: "掛號" (registration), "批價" (billing), "繳費" (payment), "領藥" (medication pickup), "報到" (check-in), "看診" (consultation), "門診" (outpatient), "排隊" (queuing)

*USA (Topic 3):* Keywords: "clinic", "doctor", "care", "pain", "help", "never", "cleveland" (hospital name), "mayo" (hospital name), "appointment", "day"

**Evidence of partial universality:**
- Both involve outpatient/clinic services (門診 ↔ clinic)
- Both mention challenges accessing care

**Critical differences:**

1. **Focus:**
   - **Taiwan**: *Administrative processes* (掛號批價流程) – registration, billing, payment, medication pickup
     - Reflects single-payer system's centralized administrative burden
     - Patients frustrated by long queues at multiple service counters
   - **USA**: *Clinical content* and *appointment access* – doctor, pain management, appointment delays
     - Keywords mention specific renowned hospitals (Cleveland Clinic, Mayo Clinic)
     - Emphasizes difficulty securing appointments and inadequate pain management

2. **Satisfaction:**
   - **Taiwan**: 1.83★ (second-lowest rating) – administrative inefficiency is major pain point
   - **USA**: 3.08★ (below average) – clinical and access issues persist but less severe than Taiwan's administrative frustrations
   - **Δ = +1.25 stars** (USA higher)

**Implication for RQ2 & RQ3:** Outpatient services represent a **universal concern**, but the *specific pain points* differ by system structure:
- Single-payer (Taiwan): Administrative efficiency bottlenecks
- Multi-payer (USA): Appointment access barriers, fragmented care coordination

Supports Institutional Hypothesis 4 (IH4): *Administrative complaints differ by system.*

---

**Dimension 4: Inpatient/Critical Care (Medium Similarity ⚠️)**

This mapping reveals **different patient acuity levels** despite both involving hospitalization.

*Taiwan (Topic 6):* Keywords: "病房" (ward), "住院" (hospitalization), "家屬" (family members), "病患" (patient), "護理師" (nurse), "出院" (discharge), "醫生" (doctor), "探病" (visiting patients), "手術" (surgery)

*USA (Topic 1):* Keywords: "care", "dad", "life", "patient", "room", "scan", "surgery", "pain", "father", "worst", "ever", "cancer", "family", "treatment", "baby"

**Evidence of partial universality:**
- Both involve inpatient care (病房/住院 ↔ room/patient)
- Both mention family involvement (家屬 ↔ dad/father/family)
- Both reference surgical procedures (手術 ↔ surgery)

**Critical differences:**

1. **Severity:**
   - **Taiwan Topic 6**: *General hospitalization* – routine admissions, ward conditions, discharge procedures, family visitation policies
   - **USA Topic 1**: *Critical/life-threatening cases* – keywords suggest severe illness: "life", "worst", "ever", "cancer", "baby", "pain"
     - Reflects high financial barriers: Patients hospitalized only when medically necessary

2. **Prevalence:**
   - **Taiwan**: 4.3% (smallest topic) – hospitalization is relatively routine under universal coverage
   - **USA**: 16.4% (third-largest topic) – hospitalization is major concern, likely reserved for serious conditions
   - **Δ = +12.1 percentage points** (USA substantially higher)

3. **Satisfaction:**
   - **Taiwan**: 2.35★ (second-lowest after emergency) – concerns about medical errors, communication failures, unexpected costs
   - **USA**: 3.29★ (middle range) – higher satisfaction possibly because hospitalization is for more clear-cut medical necessity
   - **Δ = +0.94 stars** (USA higher)

4. **Family involvement:**
   - **Taiwan**: Emphasizes *visitation rules* ("探病") – reflects hospital policies restricting family access
   - **USA**: Emphasizes *emotional support* during life-threatening situations ("dad", "father", "family", "life")
   - Supports Cultural Hypothesis 2 (H2): *Family involvement differs, but both cultures value it*

**Implication for RQ2 & RQ3:** Inpatient care is a **universal dimension**, but:
- **System structure** shapes patient acuity (routine vs. critical)
- **Cultural factors** shape how family involvement is discussed (policy restrictions vs. emotional support)

---

### 4.2.3 System-Specific Dimensions

Beyond the four universal dimensions, we identified **four dimensions that emerged in only one country**, providing direct evidence of culture- and system-specific quality concerns.

**[Table 4.4: System-Specific Service Quality Dimensions]**

| Dimension | Country | Topic | Proportion | Rating | Key Evidence | Theoretical Interpretation |
|-----------|---------|-------|-----------|--------|--------------|---------------------------|
| **Service Attitude Issues** | Taiwan | Topic 3 | 17.3% | 1.69★ | 態度, 不耐煩, 口氣, 很差<br>(attitude, impatient, tone, very poor) | High power distance + healthcare worker burnout under high patient volume |
| **Facility & Environment** | Taiwan | Topic 4 | 8.1% | 2.73★ | 停車場, 環境, 廁所, 衛生, 動線<br>(parking, environment, restroom, hygiene, flow) | Single-payer system's high utilization → infrastructure strain |
| **Billing & Insurance** | USA | Topic 6 | 4.1% | 2.92★ | bill, billing, insurance, appointment, month | Multi-payer system complexity: surprise billing, insurance denials, prior authorization |
| **Overall Positive Experience** | USA | Topic 5 | 9.5% | 3.96★ | great, thank, best, amazing, experience | American review culture: detailed positive feedback |

---

**Taiwan-Specific Dimension 1: Service Attitude Issues (17.3%, 1.69★)**

**Why this emerged in Taiwan but not USA:**

This dimension did not form a standalone topic in U.S. data, where attitude complaints are dispersed across other dimensions (nursing care, emergency care). In Taiwan, it coalesced into a distinct, sizeable topic.

**Keywords:** "態度" (attitude), "不耐煩" (impatient), "口氣" (tone), "不要" (don't), "知道" (know), "護理師" (nurse), "人員" (staff), "很差" (very poor)

**Representative complaints:**
- "護理人員訓練該檢討，不要對老人大小聲！" ("Nursing staff training needs review; don't yell at elderly patients!")
- "接電話的小姐很沒有禮貌，不聽人把話講完，要問問題還一直被插嘴" ("The receptionist was very rude, didn't let me finish speaking, kept interrupting")

**Theoretical interpretation:**

1. **Cultural Hypothesis 1 (H1) – Interpersonal Quality Sensitivity:**
   - Taiwan's collectivist culture and high power distance (Hofstede, 2001) make patients particularly sensitive to perceived disrespect from medical staff
   - When healthcare workers deviate from expected deference and kindness, patients experience this as egregious service failure

2. **Institutional Hypothesis 3 (IH3) – Healthcare Worker Burnout:**
   - Single-payer system's high patient volume (Taiwan averages 6-7 outpatient visits/person/year vs. USA's 4) strains healthcare workers
   - Brief consultation times (3-5 minutes average) and exhausting workloads lead to impatience and poor service attitudes

3. **Why not in USA?**
   - Lower power distance: Americans may have lower baseline expectations for medical staff deference
   - Lower patient volume per provider: Less burnout-induced attitude problems
   - Different complaint patterns: Attitude issues may be embedded in specific service contexts (e.g., nursing care topic) rather than forming a distinct dimension

**Implication:** This Taiwan-specific dimension provides evidence for **culture-specific quality perceptions** (RQ2) and **system-induced service failures** (RQ3).

---

**Taiwan-Specific Dimension 2: Facility & Environment Quality (8.1%, 2.73★)**

**Why this emerged in Taiwan but not USA:**

U.S. reviews rarely coalesce around facility/environment issues as a standalone topic, suggesting infrastructure concerns are less prevalent or less salient.

**Keywords:** "停車場" (parking lot), "環境" (environment), "廁所" (restroom), "衛生" (hygiene), "動線" (flow), "電梯" (elevator), "清潔" (cleanliness), "志工" (volunteers), "方便" (convenient)

**Representative complaints:**
- "廁所好歹也附個衛生紙，連衛生紙都沒有" ("At least provide toilet paper in the restrooms; there isn't even toilet paper")
- "病房硬體真的要加強，小蟑螂真的很多，廁所味道也很重" ("Ward infrastructure needs improvement; many cockroaches, restroom smells terrible")
- "停車位標示不清楚，星期六連一個志工都沒有" ("Parking signage unclear; not a single volunteer on Saturday")

**Theoretical interpretation:**

1. **Institutional Hypothesis 2 (IH2) – Crowding from Universal Access:**
   - Taiwan's single-payer NHI provides 99.9% coverage with minimal cost-sharing → very high healthcare utilization
   - High patient density strains infrastructure: insufficient parking, overcrowded restrooms, difficulty maintaining cleanliness
   - Rapid infrastructure aging due to heavy use

2. **Why not in USA?**
   - Lower patient volume per facility due to higher access barriers (insurance, costs)
   - Newer hospital infrastructure (many U.S. hospitals rebuilt in 1990s-2000s)
   - Private healthcare competition incentivizes facility investments to attract privately-insured patients

**Implication:** This Taiwan-specific dimension provides evidence for **system-specific quality concerns** driven by single-payer system's high utilization (RQ2, RQ3, IH2).

---

**USA-Specific Dimension 1: Billing & Insurance Issues (4.1%, 2.92★)**

**Why this emerged in USA but not Taiwan:**

This is perhaps the **most direct evidence of system structure shaping quality perceptions**. This topic is entirely absent from Taiwan's data.

**Keywords:** "appointment", "bill", "service", "billing", "insurance", "patient", "month", "care", "told"

**Representative complaints:**
- "Terrible billing system. Insurance should have covered this but they refuse"
- "Appointment scheduled 3 months out, then insurance denied coverage"
- "Surprise bill of $8,000 after procedure I thought was covered"

**Theoretical interpretation:**

1. **Institutional Hypothesis 1 (IH1) – Multi-Payer Complexity:**
   - **Strongly supports IH1**: American patients face billing complexity entirely absent in Taiwan's single-payer system
   - Multi-payer system generates:
     - **Surprise billing**: Patients receive unexpected bills when out-of-network providers treat them without prior notice
     - **Insurance denials**: Coverage disputes, prior authorization delays, formulary restrictions
     - **High deductibles**: Even insured patients face substantial out-of-pocket costs

2. **Why not in Taiwan?**
   - **Single-payer NHI**: Uniform fee schedule, standardized coverage, minimal patient billing
   - **Low cost-sharing**: Patients pay modest co-payments (NT$50-$450, approximately $1.50-$14 USD) determined by service level
   - **No surprise billing**: All NHI-participating providers (>93% of hospitals/clinics) follow identical billing rules
   - **No insurance denials**: Universal coverage eliminates pre-authorization and coverage disputes

**Prevalence and impact:**
- Although "only" 4.1% of reviews, this represents >130 reviews explicitly focused on billing/insurance
- Many additional reviews likely mention financial concerns within other topics
- Rating (2.92★) indicates substantial dissatisfaction

**Implication:** This USA-specific dimension provides **definitive evidence** that healthcare financing structure fundamentally shapes patient quality perceptions (RQ2, RQ3). Strongly supports IH1.

---

**USA-Specific Dimension 2: Overall Positive Experience (9.5%, 3.96★)**

**Why this emerged in USA but not Taiwan:**

While both countries have positive reviews, the U.S. data shows these coalescing into a **distinct "praise" topic** with generic positive language, whereas Taiwan's positive sentiments are embedded within specific service contexts (e.g., professional quality, surgical care).

**Keywords:** "care", "staff", "great", "thank", "team", "doctor", "experience", "best", "surgery", "amazing"

**Representative positive reviews:**
- "Amazing food, actual competent doctors and nurses genuinely care"
- "The staff were amazing. They took the time to ask if I had any questions"
- "Best hospital experience ever. Dr. Hasan was wonderful!"

**Theoretical interpretation:**

1. **Review Culture Difference:**
   - American review culture (Yelp, Google Reviews) encourages detailed 5-star reviews praising specific staff/experiences
   - Patients who have excellent experiences write extensive positive narratives using superlatives ("amazing", "best", "wonderful")

2. **Why not a distinct topic in Taiwan?**
   - Taiwan's positive reviews tend to be more context-specific: embedded within professional quality (Topic 1) or surgical care (Topic 5)
   - Chinese linguistic patterns: Gratitude expressed through specific mentions (e.g., naming individual physicians) rather than generic praise
   - Cultural factors: High-context communication (Hall, 1976) – praise implied through specific examples rather than explicit superlatives

**Implication:** This USA-specific dimension reflects **cultural differences in review-writing practices** rather than healthcare system structure per se. Less directly relevant to RQ3 (system influence) but informative for research methods (text analysis across cultures).

---

### 4.2.4 Visual Summary of Universal vs. System-Specific Dimensions

**[Figure 4.1: Venn Diagram of Universal vs. System-Specific Dimensions]**

```
┌─────────────────────────────────────────────────────────────────┐
│                    UNIVERSAL DIMENSIONS                         │
│                  (Shared Across Both Systems)                   │
│                                                                 │
│   1. Emergency Care           (TW 30.9% ↔ US 34.8%)           │
│   2. Nursing/Professional      (TW 27.2% ↔ US 20.5%)           │
│   3. Outpatient Services       (TW 6.9%  ↔ US 14.7%)           │
│   4. Inpatient/Critical Care   (TW 4.3%  ↔ US 16.4%)           │
│                                                                 │
│   → Represents ~78% of patient reviews across both countries   │
└─────────────────────────────────────────────────────────────────┘

┌──────────────────────────────┐   ┌──────────────────────────────┐
│   TAIWAN-SPECIFIC (25.4%)   │   │    USA-SPECIFIC (13.6%)     │
├──────────────────────────────┤   ├──────────────────────────────┤
│ • Service Attitude (17.3%)  │   │ • Billing/Insurance (4.1%)  │
│   ↳ Cultural + System       │   │   ↳ Multi-payer complexity  │
│                              │   │                              │
│ • Facility Environment(8.1%)│   │ • Positive Experience (9.5%)│
│   ↳ High utilization strain │   │   ↳ Review culture          │
└──────────────────────────────┘   └──────────────────────────────┘
```

**Key Takeaway for RQ2:**

Service quality is **multi-dimensional across both systems** (supporting SERVQUAL theory), with:
- **~78% overlap**: Four universal dimensions transcending system boundaries
- **~22% divergence**: System-specific and culture-specific dimensions reflecting structural and cultural differences

This finding advances service quality theory by demonstrating that **both universality and context-specificity coexist**, challenging purely universal (Parasuraman et al., 1988) and purely contingent (Brady & Cronin, 2001) perspectives.

---

## 4.3 Hypothesis Testing Results

[TO BE CONTINUED IN NEXT SECTION]

This section will present:
- 4.3.1 Cultural Hypotheses (H1-H6) Testing Results
- 4.3.2 Institutional Hypotheses (IH1-IH5) Testing Results
- 4.3.3 Statistical Tests (t-tests, chi-square tests)

*(Note: Statistical significance tests to be added upon completion of statistical analysis script)*

---

**Word Count: ~5,500 words**
**Status: Draft for Review**
**Next Steps:**
1. Complete hypothesis testing section (4.3)
2. Add statistical test results (p-values, effect sizes)
3. Create figures and tables as referenced
4. Proofread for academic writing quality
