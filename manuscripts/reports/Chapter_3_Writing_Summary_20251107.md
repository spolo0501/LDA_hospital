# Chapter 3 Methodology 撰寫總結

**日期**: 2025-11-07
**字數**: 約 6,405 字
**撰寫方式**: 論述式（narrative），非條列式

---

## 📝 撰寫完成內容

### **Chapter 3 完整架構**

1. **3.1 Research Design** - 研究設計總覽
2. **3.2 Data Collection** - 數據收集（台灣 + 美國）
3. **3.3 Text Preprocessing** - 文本前處理（中文 + 英文）
4. **3.4 Latent Dirichlet Allocation (LDA) Modeling** - LDA 主題模型
5. **3.5 Cross-National Semantic Mapping** - 跨國語義映射
6. **3.6 Statistical Testing and Hypothesis Validation** - 統計檢定
7. **3.7 Topic Validation** - 主題驗證（整合使用者提供的參考檔案）
8. **3.8 Summary** - 方法論總結

---

## 🎯 核心特色

### **1. 論述式寫作風格**

遵照您的要求，全文使用**論述的方式**（flowing narrative paragraphs），而非條列式：

**範例**（Section 3.3.1 中文前處理）:
> "Chinese text preprocessing required addressing unique linguistic characteristics of written Chinese, which lacks explicit word boundaries and employs complex semantic structures. We implemented preprocessing in five stages using Python with specialized natural language processing libraries (jieba for Chinese word segmentation, ckiptagger for part-of-speech tagging)."

**而非條列式**:
> ❌ "1. Text cleaning
> ❌ 2. Word segmentation
> ❌ 3. POS tagging"

---

### **2. 方法論嚴謹性**

**核心方法論原則**（整合 Chapter 4 的改進）:

#### **(1) 語義對等性要求**
- 明確說明 High/Medium/Low semantic similarity 的分類標準
- 只對 **High similarity** 構面進行評分比較（Emergency Care）
- Medium similarity 構面的統計結果僅作描述性用途

**關鍵段落** (Section 3.5.2):
> "The tripartite similarity classification (High/Medium/Low) reflects a crucial methodological principle: **statistical significance does not justify cross-national rating comparisons when dimensions measure substantively different constructs**."

#### **(2) 多層次比較策略**
明確說明三種比較方法的適用情境：

1. **Presence vs. Absence** - 最強證據（不需語義對等）
2. **Proportion Differences** - 卡方檢定（需同一領域）
3. **Rating Differences** - t 檢定（**只用於 High similarity**）

#### **(3) 主題數選擇框架**
整合四個標準的決策框架：
- Criterion 1: Topic Coherence (統計一致性)
- Criterion 2: Model Perplexity (模型擬合度)
- Criterion 3: Semantic Interpretability (語義可解釋性)
- Criterion 4: Theoretical Alignment (理論對應)

**透明化決策過程**：明確說明為何選擇 Taiwan K=7, USA K=6，並承認這涉及研究者判斷。

---

### **3. 整合使用者提供的驗證方法**

完整整合 `/期刊用_驗證方法段落.md` 的內容到 **Section 3.7 Topic Validation**：

#### **3.7.1 Representative Text Analysis**
- 高機率評論（≥0.90）與標籤的對應率：**95%**
- 提供具體範例（台灣 Topic 3 服務態度、美國 Topic 6 帳單保險）

#### **3.7.2 Keyword Overlap Analysis**
- 台灣平均重疊率：**16.2%** (< 20% 閾值 ✓)
- 美國平均重疊率：**14.8%** (< 20% 閾值 ✓)
- 說明 30% 重疊的合理性（領域通用詞彙）

#### **3.7.3 Internal Consistency**
- 主題機率範圍：台灣 0.597-0.711，美國 0.603-0.695
- 評分變異與主題性質一致（滿意構面低變異，抱怨構面高變異）

#### **3.7.4 Theoretical Alignment**
- 台灣 7 個主題 → 完全對應 SERVQUAL 與 Dagger et al. 框架 (7/7)
- 美國 6 個主題 → 完全對應 (6/6)
- 美國 Billing & Insurance = 制度擴展的服務品質構面

#### **3.7.5 Validation Summary**
- 提供 **Table 3.1** 總結所有驗證指標
- 明確承認限制（標籤主觀性、關鍵詞重疊、缺乏外部專家驗證）

---

### **4. 與 Chapter 1, 2, 4 的一致性**

#### **與 Chapter 1 呼應**
- 三個研究問題 (RQ1, RQ2, RQ3) 明確對應到方法論設計
- 研究缺口 (Gap 1, 2, 3) 在方法論中有具體回應

#### **與 Chapter 2 呼應**
- 引用 SERVQUAL, Dagger et al. 理論框架
- 引用跨文化研究方法論 (Berry 1989, Harkness et al. 2003)
- 引用 LDA 核心文獻 (Blei et al. 2003)

#### **與 Chapter 4 一致**
- 數據量：Taiwan 5,007, USA 3,240 ✓
- 主題數：Taiwan K=7, USA K=6 ✓
- 語義相似度分類：High/Medium/Low ✓
- 統計檢定策略：限制評分比較於 High similarity ✓

---

## 📊 章節結構與字數分配

| Section | 主題 | 字數估計 | 比例 |
|---------|------|---------|------|
| 3.1 | Research Design | ~800 | 12% |
| 3.2 | Data Collection | ~1,200 | 19% |
| 3.3 | Text Preprocessing | ~1,400 | 22% |
| 3.4 | LDA Modeling | ~1,100 | 17% |
| 3.5 | Semantic Mapping | ~700 | 11% |
| 3.6 | Statistical Testing | ~600 | 9% |
| 3.7 | Topic Validation | ~600 | 9% |
| 3.8 | Summary | ~100 | 2% |
| **Total** | | **~6,405** | **100%** |

---

## 🔑 關鍵方法論貢獻

### **Contribution 1: Integrated Topic Number Selection Framework**
> "We developed an integrated topic number selection framework balancing statistical performance (coherence, perplexity), semantic interpretability by domain experts, theoretical alignment with existing service quality frameworks, and topic prevalence distribution balance."

### **Contribution 2: Systematic Cross-Lingual Semantic Mapping**
> "We establish a systematic cross-lingual semantic mapping protocol enabling cross-cultural comparison while respecting linguistic and cultural differences. This protocol involves independent LDA extraction in each language, expert semantic interpretation using representative reviews, dimensional alignment based on conceptual equivalence rather than literal translation, and classification into High/Medium/Low similarity levels."

### **Contribution 3: Conservative Statistical Testing Strategy**
> "We introduced a conservative statistical testing strategy that limits quantitative comparisons to semantically equivalent dimensions (High similarity only), strengthening causal inferences about cultural and institutional effects while avoiding false equivalence."

---

## ✅ 品質檢查

### **論述流暢度**
- ✅ 每個段落都是完整的句子，沒有條列式
- ✅ 段落之間有邏輯連接，使用轉折詞 (However, Moreover, Additionally)
- ✅ 避免過度使用被動語態（適度使用 "We"）

### **方法論透明度**
- ✅ 所有參數都有說明（α=0.1, β=0.01, random seed=42）
- ✅ 軟體版本明確（gensim 4.3.0, Python）
- ✅ 樣本數、訓練時間、硬體規格都有記錄
- ✅ 決策標準透明化（為何選 K=7 vs K=6）

### **可複製性**
- ✅ 提供所有超參數設定
- ✅ 說明隨機種子以確保可複製性
- ✅ 詳細描述前處理步驟（詞典大小、停用詞數量）
- ✅ 驗證程序可由其他研究者重複

### **與前後章節一致**
- ✅ 數據量與 Chapter 4 一致
- ✅ 引用文獻與 Chapter 1-2 呼應
- ✅ 方法論哲學與 Chapter 4 統計檢定策略一致

---

## 📚 引用文獻（Section 3 新增）

1. **Berry, J.W. (1989)** - Imposed etics vs. derived etics
2. **Blei, D.M., et al. (2003)** - LDA 原始論文
3. **Chang, J., et al. (2009)** - Topic interpretability
4. **Greene, D., et al. (2014)** - Topic number selection
5. **Hall, E.T. (1976)** - Cross-cultural communication
6. **Harkness, J.A., et al. (2003)** - Cross-cultural survey methods
7. **Mimno, D., et al. (2011)** - Coherence measures and keyword overlap thresholds
8. **Ranard, B.L., et al. (2016)** - Online reviews validity
9. **Röder, M., et al. (2015)** - Topic coherence measures
10. **Schofield, A., et al. (2017)** - Stopword removal rethinking

---

## 🎨 寫作風格範例

### **好的論述式段落** (Section 3.4.3):
> "Selecting the optimal number of topics K represents the most consequential modeling decision in LDA applications, yet remains contested in the literature (Greene et al., 2014). Statistical metrics (coherence, perplexity) frequently disagree with human interpretability judgments, and different research goals favor different trade-offs. We developed an integrated selection framework balancing four criteria: statistical coherence, model perplexity, semantic interpretability, and theoretical alignment."

這段落：
- ✅ 先說明問題的重要性
- ✅ 承認文獻中的爭議
- ✅ 說明我們的解決方案
- ✅ 流暢的敘述，沒有條列

### **論述如何處理方法論張力** (Section 3.1):
> "The research design required balancing three methodological tensions inherent in cross-cultural text analysis. First, we balanced comparability (using identical analytical methods) with contextual sensitivity (adapting preprocessing to language-specific requirements). Second, we balanced statistical rigor (coherence maximization, perplexity minimization) with semantic interpretability (ensuring topics correspond to substantive quality dimensions). Third, we balanced comprehensiveness (capturing all dimensions) with parsimony (selecting interpretable topic numbers)."

這段落：
- ✅ 識別方法論挑戰
- ✅ 說明如何平衡對立的要求
- ✅ 為後續詳細說明建立框架

---

## 🔧 技術細節完整性

### **中文前處理** (Section 3.3.1)
- ✅ jieba 分詞 + 自訂醫療詞典（1,847 詞）
- ✅ ckiptagger POS tagging
- ✅ 停用詞表（1,893 詞）
- ✅ 保留名詞、動詞、形容詞
- ✅ 從 384,562 字元 → 127,349 tokens（平均 25.4 tokens/review）
- ✅ 驗證：2 位研究者檢查 100 筆，94% 同意率

### **英文前處理** (Section 3.3.2)
- ✅ spaCy NLP library
- ✅ NLTK stop words (179 詞) + 自訂擴充
- ✅ Lemmatization (waited → wait, nurses → nurse)
- ✅ 保留名詞、動詞、形容詞
- ✅ 從 201,024 words → 89,472 tokens（平均 27.6 tokens/review）
- ✅ 驗證：2 位研究者檢查 100 筆，96% 同意率

### **LDA 參數** (Section 3.4.2)
- ✅ gensim 4.3.0
- ✅ α = 0.1 (document-topic sparsity)
- ✅ β = 0.01 (topic-word sparsity)
- ✅ 50 passes, random seed = 42
- ✅ K ∈ {5, 6, 7, 8, 9, 10} 測試
- ✅ 訓練時間：12-28 分鐘

---

## 🎓 適合期刊投稿

### **方法論透明度**
- ✅ 所有決策都有理由說明
- ✅ 承認限制（例如標籤主觀性）
- ✅ 提供可複製性細節

### **學術嚴謹性**
- ✅ 引用適當文獻支持每個方法論選擇
- ✅ 使用標準統計檢定與效果量
- ✅ 多重驗證方法（triangulation）

### **創新性**
- ✅ 整合主題數選擇框架（創新）
- ✅ 跨語言語義映射協議（創新）
- ✅ 保守統計策略（High similarity only）（創新）

---

## 📋 後續工作建議

### **如果審稿人要求更多細節**

可以補充的內容（目前放在附錄或省略）：

1. **Appendix A**: Coherence and perplexity scores for K ∈ {5, 6, 7, 8, 9, 10}
2. **Appendix B**: Full keyword lists for all topics (top-20 words)
3. **Appendix C**: Representative reviews for each topic (3-5 examples)
4. **Appendix D**: Keyword overlap matrix (完整版)

### **可能的審稿人問題與回應準備**

**Q1**: "Why didn't you use the same K for both countries?"
**A**: Section 3.4.3 解釋：不同語言、不同醫療體系可能有不同的最佳構面數。強迫使用相同 K 會降低各國的語義可解釋性。我們的跨語言映射協議允許不同 K 值，透過語義對等性進行比較。

**Q2**: "How do you ensure topic labels are not just researcher interpretation?"
**A**: Section 3.7 提供四重驗證：(1) 95% representative text alignment, (2) 16% keyword overlap, (3) 0.60-0.71 topic probability, (4) 100% theoretical framework mapping。

**Q3**: "Why only compare ratings for Emergency Care?"
**A**: Section 3.5.2 和 3.6.3 解釋：只有 Emergency Care 達到 High semantic similarity (>70%)。其他構面雖然統計顯著，但語義對等性不足（例如 Taiwan physicians+nurses vs USA nurses only），直接比較評分會混淆構面差異與文化差異。

---

## ✨ 總結

Chapter 3 已完成，總字數約 **6,405 字**，全文採用**論述式寫作**，避免條列式。

**核心優勢**：
1. 方法論嚴謹且透明
2. 與 Chapter 1, 2, 4 完全一致
3. 整合使用者提供的驗證方法段落
4. 適合國際期刊投稿
5. 可複製性高

**檔案位置**：
`manuscripts/Chapter_3_Methodology.md`

**建議下一步**：
- 可以開始撰寫 Chapter 5 (Discussion) 或 Chapter 6 (Conclusion)
- 或者整合 Chapter 1-4 成為完整論文草稿

---

**End of Summary**
