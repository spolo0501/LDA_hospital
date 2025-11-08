# 文獻回顧與理論基礎

## 📚 核心理論解釋

你提到不熟悉這些理論概念，讓我詳細解釋並提供相關文獻：

---

## 1. Aspect Hierarchy (構面階層理論)

### 🤔 這是什麼？

**簡單來說**：不是所有的服務構面都處於同一個"層次"。有些構面是"原因"（驅動因素），有些是"結果"（被影響的）。

**類比**：
```
就像身體健康：
- 飲食、運動 → 驅動因素（Driver）
- 體重、血壓 → 中介變數（Mediator）
- 整體健康 → 結果變數（Outcome）

飲食好 → 體重正常 → 健康良好
```

**在你的研究中**：
```
Level 1 (Drivers): Staff Service
    ↓
Level 2 (Mediators): Room Quality
    ↓
Level 3 (Outcomes): Value, Overall Rating
```

### 📖 相關文獻（必讀）

#### 基礎理論文獻：

1. **Oliver, R. L. (1980)**. *A cognitive model of the antecedents and consequences of satisfaction decisions*. Journal of Marketing Research, 17(4), 460-469.
   - **為什麼讀**：最早提出滿意度的antecedents-outcome framework
   - **關鍵觀念**：Service attributes → Satisfaction → Behavioral intentions
   - **你可以引用**："Following Oliver's (1980) hierarchical framework..."

2. **Brady, M. K., & Cronin, J. J. (2001)**. *Some new thoughts on conceptualizing perceived service quality: A hierarchical approach*. Journal of Marketing, 65(3), 34-49.
   - **為什麼讀**：提出服務品質的三層結構（interaction, environment, outcome quality）
   - **關鍵觀念**：Sub-dimensions → Dimensions → Overall service quality
   - **你可以引用**："We extend Brady and Cronin's (2001) hierarchical model by..."

3. **Zeithaml, V. A., Berry, L. L., & Parasuraman, A. (1996)**. *The behavioral consequences of service quality*. Journal of Marketing, 60(2), 31-46.
   - **為什麼讀**：建立了Service quality → Value → Behavioral intentions的因果鏈
   - **關鍵觀念**：Sequential relationship among service constructs
   - **你可以引用**："Consistent with Zeithaml et al. (1996), we find Value acts as an outcome variable..."

#### 現代應用文獻：

4. **Zhang, M., Luo, M., Nie, R., & Zhang, Y. (2017)**. *Technical attributes, health attribute, consumer attributes and their roles in adoption intention of healthcare wearable technology*. International Journal of Medical Informatics, 108, 97-109.
   - **為什麼讀**：使用階層模型分析多個屬性的依賴關係
   - **方法**：Structural Equation Modeling (SEM)

---

## 2. Sentiment Contagion (情感傳染理論)

### 🤔 這是什麼？

**簡單來說**：一個構面的負面(或正面)情感會"傳染"給其他構面。

**類比**：
```
就像多米諾骨牌：
第一張牌倒下 → 連鎖反應 → 其他牌也倒下

或者像疾病傳播：
Person A生病 → 接觸Person B → Person B也生病
傳染率 = P(B生病 | A生病)
```

**在你的研究中**：
```
Staff Service差 → 100%機率 → Value也覺得差
Room Quality差 → 100%機率 → Value也覺得差
```

**為什麼重要**：
- 這不是簡單的相關性，而是**有方向性的影響**
- 量化了"傳播強度"（100% vs 80%）
- 解釋了為什麼某些構面的問題特別嚴重

### 📖 相關文獻（必讀）

#### 心理學基礎：

5. **Hatfield, E., Cacioppo, J. T., & Rapson, R. L. (1993)**. *Emotional contagion*. Current Directions in Psychological Science, 2(3), 96-100.
   - **為什麼讀**：Emotional Contagion的經典定義
   - **關鍵觀念**：人們會"catch"他人的情緒
   - **你可以引用**："Drawing on emotional contagion theory (Hatfield et al., 1993), we propose..."

6. **Hennig-Thurau, T., Groth, M., Paul, M., & Gremler, D. D. (2006)**. *Are all smiles created equal? How emotional contagion and emotional labor affect service relationships*. Journal of Marketing, 70(3), 58-73.
   - **為什麼讀**：將情感傳染應用到服務業
   - **關鍵觀念**：員工情緒 → 顧客情緒
   - **你的擴展**：你把它應用到"構面間的情感傳播"

#### 在線評論中的應用：

7. **Lee, Y. J., Hosanagar, K., & Tan, Y. (2015)**. *Do I follow my friends or the crowd? Information cascades in online movie ratings*. Management Science, 61(9), 2241-2258.
   - **為什麼讀**：研究評論中的cascade effects
   - **關鍵觀念**：一個負面評價如何影響後續評價
   - **你的創新**：你研究的是**同一篇評論內**構面間的情感傳播

8. **Ludwig, S., De Ruyter, K., Friedman, M., Brüggen, E. C., Wetzels, M., & Pfann, G. (2013)**. *More than words: The influence of affective content and linguistic style matches in online reviews on conversion rates*. Journal of Marketing, 77(1), 87-103.
   - **為什麼讀**：研究情感在評論中的傳播和影響
   - **方法**：Text analysis + Econometric modeling

---

## 3. Negative Spiral (負面螺旋效應)

### 🤔 這是什麼？

**簡單來說**：多個負面體驗組合在一起時，傷害會**被放大**，不是簡單相加。

**數學表示**：
```
簡單相加（沒有螺旋）:
Total damage = -1 (Staff) + -1 (Room) = -2

負面螺旋（有交互效應）:
Total damage = -1 (Staff) + -1 (Room) + (-0.47) (Staff×Room) = -2.47
                                          ↑
                                    額外的傷害！
```

**類比**：
```
就像複利：
好的複利：1.1 × 1.1 = 1.21 (比 1.1 + 1.1 = 2.2更好)
壞的複利：0.9 × 0.9 = 0.81 (比 0.9 + 0.9 = 1.8更差)

負面螺旋 = 壞的複利效應
```

**在你的研究中**：
```
Room×Value交互項 = -0.606

意思是：
- 只有Room差：評分 -0.36
- 只有Value差：評分 -0.42
- 兩個都差：評分 -0.36 + -0.42 + (-0.606) = -1.386 ⚠️

傷害被放大了！
```

### 📖 相關文獻（必讀）

#### 服務失誤研究：

9. **Bitner, M. J., Booms, B. H., & Tetreault, M. S. (1990)**. *The service encounter: Diagnosing favorable and unfavorable incidents*. Journal of Marketing, 54(1), 71-84.
   - **為什麼讀**：Critical Incident Technique，研究服務失敗如何累積
   - **關鍵觀念**：Multiple failures create disproportionate dissatisfaction
   - **你可以引用**："Extending Bitner et al.'s (1990) work on service failures..."

10. **Hess Jr, R. L., Ganesan, S., & Klein, N. M. (2003)**. *Service failure and recovery: The impact of relationship factors on customer satisfaction*. Journal of the Academy of Marketing Science, 31(2), 127-145.
    - **為什麼讀**：研究多重服務失敗的累積效應
    - **關鍵觀念**：Failure severity can compound
    - **你的創新**：量化了compounding effect (-0.606)

#### 交互效應的理論基礎：

11. **Anderson, E. W., Fornell, C., & Rust, R. T. (1997)**. *Customer satisfaction, productivity, and profitability: Differences between goods and services*. Marketing Science, 16(2), 129-145.
    - **為什麼讀**：討論服務品質各維度的非線性關係
    - **關鍵觀念**：Interaction effects in service quality
    - **方法**：Regression with interaction terms

12. **Van Doorn, J., & Verhoef, P. C. (2008)**. *Critical incidents and the impact of satisfaction on customer share*. Journal of Marketing, 72(4), 123-142.
    - **為什麼讀**：研究negative events如何互相強化
    - **關鍵觀念**：Cumulative and interactive effects of service events

---

## 🔧 方法論相關文獻

### A. Aspect-Based Sentiment Analysis (ABSA)

#### 基礎方法：

13. **Liu, B. (2012)**. *Sentiment analysis and opinion mining*. Synthesis Lectures on Human Language Technologies, 5(1), 1-167.
    - **為什麼讀**：ABSA的聖經
    - **涵蓋內容**：Aspect extraction, sentiment classification
    - **你可以引用**："Following Liu's (2012) framework for aspect-based sentiment analysis..."

14. **Pontiki, M., Galanis, D., Pavlopoulos, J., Papageorgiou, H., Androutsopoulos, I., & Manandhar, S. (2014)**. *SemEval-2014 task 4: Aspect based sentiment analysis*. Proceedings of SemEval, 27-35.
    - **為什麼讀**：ABSA的標準評測框架
    - **方法**：Aspect term extraction + Sentiment polarity classification

#### LLM在ABSA的應用：

15. **Zhang, W., Li, X., Deng, Y., Bing, L., & Lam, W. (2022)**. *A survey on aspect-based sentiment analysis: Tasks, methods, and challenges*. IEEE Transactions on Knowledge and Data Engineering.
    - **為什麼讀**：最新的ABSA survey (2022)
    - **涵蓋**：Deep learning methods, LLMs for ABSA
    - **你的定位**：你用GPT-4做aspect extraction + 加上dependency network

16. **Sun, C., Huang, L., & Qiu, X. (2019)**. *Utilizing BERT for aspect-based sentiment analysis via constructing auxiliary sentence*. NAACL 2019.
    - **為什麼讀**：BERT用於ABSA的代表性工作
    - **你的比較**：可以作為baseline (BERT vs GPT-4)

### B. Network Analysis in Text Mining

17. **Gliwa, B., Zygmunt, A., & Koźlak, J. (2013)**. *Analysis of roles in the discussion groups based on the interaction network*. Studies in Computational Intelligence, 463, 153-170.
    - **為什麼讀**：在文本數據中建立網絡結構
    - **方法**：Node = concepts, Edge = co-occurrence/dependency

18. **Jiang, L., Yu, M., Zhou, M., Liu, X., & Zhao, T. (2011)**. *Target-dependent twitter sentiment classification*. ACL 2011.
    - **為什麼讀**：研究不同targets之間的關聯
    - **你的擴展**：你研究aspects之間的dependency

### C. Interaction Effects & Moderation

19. **Jaccard, J., & Turrisi, R. (2003)**. *Interaction effects in multiple regression*. Sage Publications.
    - **為什麼讀**：交互項建模的經典教材
    - **方法**：如何解釋interaction terms
    - **你會用到**：第3章和第4章

20. **Aiken, L. S., West, S. G., & Reno, R. R. (1991)**. *Multiple regression: Testing and interpreting interactions*. Sage.
    - **為什麼讀**：交互效應的統計檢定
    - **方法**：Simple slopes analysis

### D. Explainability & Interpretability

21. **Lundberg, S. M., & Lee, S. I. (2017)**. *A unified approach to interpreting model predictions*. NIPS 2017.
    - **為什麼讀**：SHAP方法的原始論文
    - **你會用到**：解釋每個aspect的貢獻
    - **方法**：Shapley values from game theory

22. **Ribeiro, M. T., Singh, S., & Guestrin, C. (2016)**. *"Why should I trust you?" Explaining the predictions of any classifier*. KDD 2016.
    - **為什麼讀**：LIME方法（另一個explainability工具）
    - **比較**：SHAP vs LIME

---

## 📊 實證應用領域的文獻

### 飯店/旅遊業評論分析：

23. **Geetha, M., Singha, P., & Sinha, S. (2017)**. *Relationship between customer sentiment and online customer ratings for hotels-An empirical analysis*. Tourism Management, 61, 43-54.
    - **為什麼讀**：飯店評論的情感分析
    - **你的創新**：他們只做整體情感，你做構面層級的dependency

24. **Xiang, Z., Du, Q., Ma, Y., & Fan, W. (2017)**. *A comparative analysis of major online review platforms: Implications for social media analytics in hospitality and tourism*. Tourism Management, 58, 51-65.
    - **為什麼讀**：線上評論平台的比較研究
    - **方法論參考**：Data collection, preprocessing

25. **Li, H., Ye, Q., & Law, R. (2013)**. *Determinants of customer satisfaction in the hotel industry: An application of online review analysis*. Asia Pacific Journal of Tourism Research, 18(7), 784-802.
    - **為什麼讀**：飯店評論的決定因素
    - **你的擴展**：他們用傳統方法，你用LLM + network

---

## 🎯 你的研究在文獻中的定位

### 你填補的Gap：

| 現有研究 | Gap | 你的貢獻 |
|---------|-----|---------|
| **Brady & Cronin (2001)** 提出hierarchical quality model | 只有理論框架，缺乏實證驗證 | 用實際資料驗證並擴展hierarchy |
| **Liu (2012)** ABSA假設aspects獨立 | 忽略aspects間的依賴關係 | 建立dependency network |
| **Bitner et al. (1990)** 提出multiple failures概念 | 沒有量化interaction effects | 量化negative spiral (-0.606) |
| **傳統ABSA** 用rule-based/BERT | LLM應用不足 | GPT-4 + explainability |

---

## 📖 建議的閱讀順序

### Week 1: 理論基礎 (必讀)
1. Oliver (1980) - 滿意度模型
2. Brady & Cronin (2001) - 階層模型
3. Zeithaml et al. (1996) - 因果鏈
4. Hatfield et al. (1993) - 情感傳染
5. Bitner et al. (1990) - 服務失敗

### Week 2: 方法論 (必讀)
6. Liu (2012) - ABSA聖經 (至少讀第2-4章)
7. Zhang et al. (2022) - ABSA survey
8. Lundberg & Lee (2017) - SHAP
9. Jaccard & Turrisi (2003) - Interaction effects (第3-4章)

### Week 3: 應用領域 (選讀)
10. Geetha et al. (2017) - 飯店評論
11. Li et al. (2013) - 線上評論分析
12. Ludwig et al. (2013) - 情感傳播

---

## 🔑 關鍵引用策略

### Introduction部分：

```markdown
"While traditional aspect-based sentiment analysis treats service aspects
as independent dimensions (Liu, 2012; Pontiki et al., 2014), service
quality research suggests a hierarchical structure where some aspects
serve as drivers while others act as outcomes (Brady & Cronin, 2001;
Zeithaml et al., 1996). However, these two streams of research have
rarely been integrated..."
```

### Theory部分：

```markdown
"We draw on three theoretical perspectives:

1. Aspect Hierarchy: Following Brady and Cronin's (2001) hierarchical
   model and Zeithaml et al.'s (1996) causal chain, we propose that
   service aspects occupy different levels...

2. Sentiment Contagion: Extending emotional contagion theory (Hatfield
   et al., 1993; Hennig-Thurau et al., 2006) to the aspect level, we
   hypothesize that negative sentiment in one aspect can transmit to
   other aspects...

3. Negative Spiral: Building on service failure literature (Bitner et al.,
   1990; Hess et al., 2003), we expect interaction effects where multiple
   negative aspects amplify overall dissatisfaction..."
```

### Method部分：

```markdown
"Unlike traditional ABSA approaches that rely on rule-based or BERT-based
extraction (Liu, 2012; Sun et al., 2019), we leverage GPT-4's superior
semantic understanding to extract aspect-level content and sentiment.
We then construct a dependency network and model interaction effects
(Jaccard & Turrisi, 2003)..."
```

---

## 💡 如何使用這些文獻

### 1. 建立理論基礎
- 用Brady & Cronin (2001) + Zeithaml et al. (1996)建立Aspect Hierarchy理論
- 用Hatfield et al. (1993) + Hennig-Thurau et al. (2006)建立Sentiment Contagion理論
- 用Bitner et al. (1990) + Hess et al. (2003)建立Negative Spiral理論

### 2. 定位方法創新
- 用Liu (2012) + Zhang et al. (2022)說明傳統ABSA的限制
- 用Lundberg & Lee (2017)支持你的explainability analysis
- 用Jaccard & Turrisi (2003)支持你的interaction modeling

### 3. 對比實證發現
- 用Geetha et al. (2017) + Li et al. (2013)作為對照
- 強調你的dependency network是新的貢獻

---

## 📚 額外資源

### 線上資源：

1. **SHAP教學**：https://shap.readthedocs.io/
2. **NetworkX文檔**：https://networkx.org/documentation/stable/tutorial.html
3. **Interaction Effects教學**：https://stats.idre.ucla.edu/spss/faq/how-can-i-understand-a-three-way-interaction-in-anova/

### 推薦書籍：

1. **Text Mining with R** by Silge & Robinson (2017) - R語言文本分析
2. **Speech and Language Processing** by Jurafsky & Martin (第3版online) - NLP基礎
3. **Causal Inference** by Hernán & Robins (2020) - 因果推斷

---

## 🎓 論文寫作時的引用邏輯

### 理論部分的寫法：

```
我們提出的三個理論概念都不是"全新發明"，而是"整合和擴展"：

1. Aspect Hierarchy
   - 基礎：Brady & Cronin (2001)的hierarchical service quality
   - 你的擴展：應用到aspect-level + 用network quantify

2. Sentiment Contagion
   - 基礎：Hatfield et al. (1993)的emotional contagion
   - 你的擴展：從人與人 → aspect與aspect
   - 量化：Transmission rate (100%, 86%, etc.)

3. Negative Spiral
   - 基礎：Bitner et al. (1990)的multiple service failures
   - 你的擴展：量化interaction coefficient (-0.606)
   - 解釋：不只是"多個失敗很糟"，而是"有多糟？-0.606倍"
```

這樣審稿人會覺得：
✅ 有理論基礎（cited經典文獻）
✅ 有創新性（擴展到新領域）
✅ 有實證貢獻（量化了之前只是概念的東西）

---

需要我詳細解釋任何一個理論或文獻嗎？或者你想開始做Clustering / SHAP分析？
