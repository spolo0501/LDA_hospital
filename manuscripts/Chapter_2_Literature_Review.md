# Chapter 2: Literature Review

## 2.1 Healthcare Service Quality: Theoretical Foundations

Service quality has been recognized as a multidimensional construct since Parasuraman, Zeithaml, and Berry's (1985) seminal conceptualization as "the gap between customer expectations and perceptions of service delivery." The most influential operationalization emerged through SERVQUAL (Parasuraman et al., 1988), identifying five generic dimensions applicable across service industries: (1) **tangibles** (physical facilities, equipment, and staff appearance), (2) **reliability** (ability to perform promised service dependably and accurately), (3) **responsiveness** (willingness to help customers and provide prompt service), (4) **assurance** (knowledge and courtesy of staff, ability to inspire trust and confidence), and (5) **empathy** (caring, individualized attention provided to customers). This framework revolutionized service research by providing standardized measurement, though critics note that factor structures vary across contexts and generic dimensions may inadequately capture industry-specific attributes (Buttle, 1996; Cronin and Taylor, 1992).

Healthcare-specific frameworks recognize that medical service characteristics necessitate context adaptation. Donabedian's (1988) structure-process-outcome model conceptualizes quality across organizational capacity (facilities, equipment), care delivery activities (clinical procedures, interactions), and health effects (outcomes, satisfaction). Dagger et al. (2007) developed a healthcare-specific model through patient interviews, identifying four dimensions: (1) **interpersonal quality** (staff empathy, communication, and respect during patient interactions), (2) **technical quality** (clinical competence, diagnostic accuracy, and treatment effectiveness), (3) **environment quality** (facility cleanliness, comfort, and physical ambiance), and (4) **administrative quality** (scheduling efficiency, billing processes, and administrative procedures). Empirical validation revealed interpersonal quality as the strongest predictor of patient loyalty despite information asymmetry limiting technical quality assessment. Contemporary person-centred care research emphasizes patient dignity, shared decision-making, and family integration as critical quality attributes extending beyond traditional frameworks (Giusti et al., 2020).

**Comparing Service Quality Frameworks**

Table 2.1 synthesizes five major frameworks that have shaped healthcare quality research, revealing both convergence and divergence in how quality is conceptualized across theoretical traditions.

**Table 2.1: Comparison of Healthcare Service Quality Frameworks**

| Framework | Dimensions | Core Focus | Healthcare Specificity |
|-----------|-----------|------------|----------------------|
| **SERVQUAL** (Parasuraman et al., 1988) | 5: Tangibles, Reliability, Responsiveness, Assurance, Empathy | Gap between expectations and perceptions | Generic (applied to healthcare) |
| **Donabedian** (1988) | 3: Structure, Process, Outcome | System-level quality assessment | Healthcare-specific |
| **Brady & Cronin** (2001) | 3 primary: Interaction Quality, Physical Environment, Outcome Quality | Hierarchical decomposition of quality | Service-general (validated in healthcare) |
| **Dagger et al.** (2007) | 4: Interpersonal, Technical, Environment, Administrative | Patient-experienced service quality | Healthcare-specific (patient interviews) |
| **Person-Centred Care** (Giusti et al., 2020) | 6: Respect/Dignity, Information, Participation, Holistic Support, Continuity, Family Inclusion | Patient autonomy and holistic wellbeing | Healthcare-specific (serious illness) |

Three patterns emerge from this comparison. First, dimensional granularity varies with framework purpose: system-level models (Donabedian) employ broader constructs while patient-experience models (Dagger et al.) decompose quality into finer-grained attributes. Second, temporal evolution reflects paradigm shifts: frameworks developed in the 1980s-1990s emphasize provider capabilities, whereas contemporary frameworks foreground patient autonomy and shared decision-making. Third, contextual adaptation is essential: the appropriate framework depends on evaluative purpose, with quality assessment for accreditation employing systemic approaches while patient satisfaction monitoring uses patient-experience dimensions.

**Technical Quality versus Functional Quality**

A fundamental distinction in healthcare quality research separates technical quality from functional quality (Grönroos, 1984). Technical quality refers to the accuracy and appropriateness of medical diagnosis, treatment, and procedures—essentially clinical competence and health outcomes achieved. Functional quality encompasses the manner in which healthcare is delivered: interpersonal interactions, administrative processes, and physical environment attributes. This dichotomy is theoretically crucial because it reflects the information asymmetry inherent in healthcare: patients typically lack medical expertise to evaluate technical quality (e.g., whether a diagnosis was clinically accurate) but can readily assess functional aspects (e.g., whether the physician listened empathetically) (Andaleeb, 2001). Consequently, patient satisfaction and service quality perceptions are often disproportionately influenced by functional quality, even when technical quality is objectively high. This asymmetry creates a substitution effect wherein patients rely on observable functional attributes (physician attentiveness, facility cleanliness, wait times) as proxy indicators of unobservable technical quality. Empirical evidence demonstrates that while technical quality matters more for objective health outcomes, functional quality exerts stronger influence on patient satisfaction and behavioral intentions such as provider loyalty and willingness to recommend (Dagger et al., 2007).

### Healthcare Service Unique Characteristics

Healthcare services possess distinctive features differentiating them from other service sectors and shaping quality perceptions (Berry and Bendapudi, 2007). Healthcare involves intensive interpersonal contact requiring information exchange (patients disclosing intimate details), trust in providers' clinical judgment, and emotional labor as providers manage patient anxiety while delivering technical information. Extreme information asymmetry characterizes healthcare—patients typically lack medical knowledge to evaluate diagnostic and treatment technical quality, making healthcare a credence good whose quality cannot be fully assessed even after consumption (Andaleeb, 2001; Darby and Karni, 1973). This asymmetry creates substitution effects where patients rely on observable functional attributes (physician attentiveness, facility cleanliness, wait times) as proxy indicators of unobservable technical quality. Consequently, functional quality often dominates technical quality in patient evaluations despite technical quality mattering more for objective health outcomes (Donabedian, 1988; Dagger et al., 2007).

Outcome uncertainty complicates quality assessment—patients may not recover despite excellent care or improve despite suboptimal care due to natural healing. This means patients cannot reliably infer process quality from outcome quality, heightening emotional sensitivity to service encounters and amplifying negative experience impacts (Berry and Bendapudi, 2007). Additionally, healthcare consumption is often involuntary and patient choice constrained by insurance networks, geography, urgency, and referral requirements, reducing competitive pressure for quality improvement (Oliver, 1980).

### The Need for Exploratory Methods

While theoretical frameworks provide valuable conceptual foundations, predetermined structures suffer from limitations necessitating exploratory, data-driven approaches. First, SERVQUAL's dimensions derived from non-healthcare focus groups may miss context-specific concerns unique to particular settings or temporal periods—Taiwan's National Health Insurance may generate concerns differing from U.S. market-based insurance, while COVID-19 introduced entirely new dimensions (infection control, telemedicine) absent from pre-2020 frameworks. Second, survey instruments constrain patient expression to predetermined attributes—patients cannot introduce concerns like parking availability if not surveyed. Third, applying identical instruments across cultures assumes dimensional equivalence where it may not exist; family accommodation may constitute critical quality in collectivist cultures but remain unmeasured by Western-developed surveys (Steenkamp and Baumgartner, 1998; Andaleeb, 2001).

The current study addresses these limitations through Latent Dirichlet Allocation (LDA) topic modeling on patient-generated online reviews, allowing service quality dimensions to emerge inductively from patient narratives rather than being researcher-imposed. This exploratory approach honors context-specificity and temporal evolution documented in the literature while privileging patient voices in defining quality constructs consistent with person-centred care principles (Giusti et al., 2020). Section 2.2 examines cross-cultural service quality research to develop expectations about how cultural differences between Taiwan and the United States may shape dimensional structures.

---

## 2.2 Cross-Cultural Differences in Service Quality Perceptions

While Section 2.1 established that service quality is multidimensional and context-dependent, culture shapes what customers expect, value, and evaluate in service encounters (Donthu and Yoo, 1998; Furrer et al., 2000). This section reviews cross-cultural service quality research foundations and develops expectations for how Taiwanese and American patients may differ in hospital service quality perceptions.

### 2.2.1 Hofstede's Cultural Dimensions and Service Quality

Hofstede's (1980, 2001) cultural dimensions theory provides the most widely applied framework for understanding cross-cultural consumer behavior differences. Taiwan and the United States exhibit stark contrasts across six dimensions. Most dramatically, individualism differs profoundly—Taiwan scores 17 (highly collectivist) versus the United States' 91 (highly individualist), a 74-point gap suggesting fundamental differences in service priorities. Power distance shows Taiwan at 58 (moderate-high) versus U.S. 40 (moderate-low), shaping physician-patient authority relationships. Taiwan's higher uncertainty avoidance (69 versus 46) predicts greater demand for detailed information and testing. Taiwan's moderate-feminine orientation (MAS=45) compared to U.S. moderate-masculine (MAS=62) suggests Taiwanese patients emphasize empathy and caring while Americans prioritize efficiency and results. Long-term orientation contrasts dramatically—Taiwan's 93 versus U.S. 26 indicates different preventive versus acute care emphases (Hofstede, 2001).

Empirical research consistently demonstrates these dimensions shape service quality priorities. Furrer et al.'s (2000) seventeen-country study found collectivist cultures rated empathy as most important (mean weight = 0.35) while individualist cultures prioritized reliability (0.32), with individualism negatively correlating with empathy importance (r = -0.64, p < 0.01). High power-distance cultures assigned significantly higher importance to provider assurance and competence (Furrer et al., 2000; Donthu and Yoo, 1998). Healthcare-specific research reveals culture-unique dimensions: Andaleeb (2001) identified "responsiveness to family" as a distinct factor in collectivist Bangladesh that explained more satisfaction variance than several clinical dimensions—a dimension absent from Western studies reflecting individualist privacy emphases.

### 2.2.2 Cross-Cultural Measurement and Methodological Approach

Traditional cross-cultural service quality research using standardized surveys like SERVQUAL faces measurement equivalence challenges concerning whether constructs, items, and scales carry identical meanings across cultures (Steenkamp and Baumgartner, 1998). Cultural differences in acquiescence bias and response styles complicate direct comparisons. Moreover, predetermined survey instruments developed in Western contexts may impose culturally-biased dimensional structures, missing dimensions salient in non-Western settings like family accommodation in collectivist healthcare (Andaleeb, 2001).

The current study's text-mining approach partially mitigates these challenges by allowing service quality dimensions to emerge inductively from patients' own words rather than imposing predetermined constructs. Without survey items or Likert scales, we avoid item equivalence issues and response style biases. Open-ended narratives captured in online reviews reveal patients' spontaneous priorities—what aspects they found sufficiently important to publicly discuss—consistent with person-centred care principles (Giusti et al., 2020). This inductive approach enables discovery of culture-specific dimensions while identifying universal healthcare concerns, testing whether culturally-predicted differences empirically manifest in patient discourse.

Beyond cultural values, institutional structures—healthcare system organization, financing, and delivery—profoundly influence patient priorities. Section 2.3 examines how Taiwan's National Health Insurance versus America's market-based system creates additional service quality variations through system-level constraints and incentives.

---

## 2.3 Healthcare Systems: Taiwan vs. United States

While Section 2.2 established that cultural values shape service quality expectations, institutional structures—how healthcare is organized, financed, and regulated—also profoundly influence patient experiences and priorities (Scott, 2008; Kuhlmann et al., 2020). Taiwan and the United States represent polar opposite healthcare system models that create distinct structural constraints shaping patient-provider interactions and service quality dimensions.

### 2.3.1 Contrasting Healthcare System Models

Taiwan operates a universal, single-payer National Health Insurance (NHI) system achieving 99.9% population coverage with comprehensive benefits and minimal cost-sharing ($5-$17 per visit). The United States employs a fragmented, market-based, multi-payer model with 9% uninsured and substantial patient cost burdens (annual deductibles averaging $1,669 for individuals) (Cheng, 2015; Tikkanen et al., 2020). These structural differences generate divergent utilization patterns and service delivery characteristics. Taiwanese residents average 14.2 outpatient visits annually versus 4.0 in the United States, reflecting unrestricted access but creating provider crowding. Taiwan's fee-for-service payment within global budget constraints incentivizes maximizing patient volume, producing consultation times of three to five minutes compared to fifteen to twenty minutes in the United States (Tai-Seale et al., 2007; OECD Health Statistics, 2022). Healthcare spending constitutes 6.6% of GDP in Taiwan versus 17.8% in the United States, with catastrophic health expenditures affecting only 1.8% of Taiwan households compared to 21% in America (World Bank, 2022; Papanicolas et al., 2018).

### 2.3.2 Institutional Effects on Service Quality Dimensions

**Taiwan's Institutional Constraints**

Taiwan's high-utilization, low-cost system creates distinctive service quality challenges despite achieving universal access. The combination of unrestricted provider choice and fee-for-service payment within fixed budgets generates extreme volume pressure—hospital physicians routinely conduct forty to sixty consultations per half-day session (Cheng and Chiang, 2012). These compressed three to five minute encounters directly constrain communication quality, with 47% of hospital physicians reporting emotional exhaustion from workload intensity (Tsai et al., 2009). Patients experience immediate access without waiting lists but encounter crowded facilities and rushed interactions. Conversely, financial dimensions remain largely absent from quality evaluations—low, predictable copayments functionally eliminate cost considerations from care-seeking decisions. Administrative processes focus on registration efficiency and medication pickup logistics given high-frequency utilization.

**United States' Institutional Barriers**

America's high-cost, fragmented system elevates financial and access barriers as primary quality concerns. High deductibles, copayments, and coinsurance create widespread financial stress, with 45% of adults reporting delayed or forgone care due to cost (Commonwealth Fund, 2020). Medical debt represents Americans' most common debt in collection, and medical expenses constitute the leading bankruptcy cause (Himmelstein et al., 2019). Insurance complexity generates administrative burdens through prior authorization requirements, network restrictions, and coverage disputes that pervade patient experiences. Access manifests as appointment delays—primary care averaging twenty-four days, specialists thirty to fifty days (Merritt Hawkins, 2017)—rather than on-site crowding. However, longer consultation times and lower patient volumes (fifteen to twenty-five daily) potentially enable stronger patient-provider relationships and more thorough communication than Taiwan's high-volume model (Tai-Seale et al., 2007).

### 2.3.3 Culture-Institution Interactions and Service Quality Implications

Cultural and institutional effects interact rather than operating independently to shape service quality configurations. Following Oliver's (1980) expectation-disconfirmation theory, satisfaction derives from the gap between expectations and perceived performance. Taiwan's cultural emphasis on empathy and interpersonal warmth (Section 2.2) combined with institutional constraints limiting consultations to three to five minutes creates a larger expectation-disconfirmation gap than cultural preferences alone predict. Taiwanese patients value communication (cultural expectation) but cannot receive adequate interaction time (institutional constraint), potentially generating more severe communication complaints than in the United States despite similar cultural preferences. Conversely, American institutional cost burdens may overwhelm cultural preferences for other quality dimensions—patients discuss cost extensively not primarily because individualist values prioritize cost-benefit analysis, but because institutional reality (high costs, variable coverage) forces cost consideration regardless of cultural orientation. These interactions demonstrate that institutional factors can dominate cultural tendencies when structural constraints strongly shape feasible behaviors.

Empirical evidence supports these culture-institution interaction effects. Yoon and Cheng's (2021) large-scale comparison of 1,374 hospitals (350 in Taiwan, 1,024 in the United States) using standardized patient experience surveys (Taiwan's PEHC and U.S. HCAHPS, 2018-2019) found that perceived inpatient care quality was consistently higher in the United States across three experience measures: perceived respect, accommodation quality, and understanding upon discharge. However, the most striking finding concerned the association between regional socioeconomic status and patient satisfaction, which exhibited opposite patterns in the two countries. In Taiwan, hospitals in higher socioeconomic regions were significantly less likely to receive highly positive responses across all three dimensions, with odds ratios ranging from 0.83 to 0.88—meaning high-SES areas showed 12-17% lower satisfaction. In direct contrast, U.S. hospitals in higher socioeconomic regions showed significantly higher satisfaction, with odds ratios of 1.48 for understanding upon discharge and 2.51 for accommodation quality—meaning high-SES areas showed 48-151% higher satisfaction. Yoon and Cheng (2021, p. 1190) concluded that "varying associations between regional SES and perceived inpatient care quality highlight how systemic and cultural differences between the two countries affect scoring patterns."

These opposing SES-satisfaction relationships demonstrate the dominance of institutional structure over cultural values in shaping patient expectations and satisfaction. Taiwan's universal single-payer system equalizes access but generates higher expectations among high-SES populations who may compare domestic care to international standards or expect service levels commensurate with their economic status—expectations the volume-constrained system cannot meet. The U.S. market-based system channels resources toward high-SES regions through private insurance and economic sorting, enabling hospitals in affluent areas to provide superior facilities and longer consultation times that high-SES patients can afford and expect. Yoon and Cheng's (2021) findings empirically validate the culture-institution interaction framework: institutional constraints (Taiwan's volume pressure, U.S. financial barriers) interact with cultural expectations (Taiwan's high-SES populations' elevated service standards, U.S. high-SES populations' ability to purchase quality) to produce systematic satisfaction pattern reversals that neither institutional nor cultural factors alone would predict.

### Summary

Taiwan's single-payer NHI and America's market-based system create fundamentally different patient experiences. Taiwan achieves universal coverage with minimal costs but generates volume pressure producing brief consultations and crowding, while the United States maintains longer consultations but imposes financial barriers and access delays. Institutional structures shape service quality dimensions independently of cultural values, while culture-institution interactions produce magnified effects. Section 2.4 examines online reviews as data sources, while Section 2.5 addresses text mining methodologies.

---

## 2.4 Online Reviews as a Data Source for Service Quality Research

Traditional healthcare service quality research has relied predominantly on researcher-administered surveys (SERVQUAL, HCAHPS) and patient satisfaction questionnaires. While these provide standardized quantitative data, they suffer from limitations including low response rates, selection bias, predetermined formats constraining patient expression, and high administration costs (Gao et al., 2012; Greaves et al., 2013). The proliferation of online review platforms over the past two decades has created an alternative data source: patient-generated, unsolicited narratives voluntarily shared on platforms such as Google Maps, Yelp, and Healthgrades (Ranard et al., 2016; Hao and Zhang, 2016).

### 2.4.1 Online Reviews vs. Traditional Surveys

**Advantages of Online Reviews**

Online reviews offer distinct advantages over traditional surveys. First, they are unsolicited and spontaneous, capturing authentic concerns rather than responses to predetermined questions, revealing what matters most to patients without researcher-imposed priorities (Gao et al., 2012). Second, they provide narrative richness with vivid detail—specific incidents, causal attributions, emotional expressions—enabling qualitative discovery of emergent themes (Ranard et al., 2016). Third, reviews accumulate longitudinally and continuously, enabling trend analysis and real-time monitoring, whereas surveys provide periodic snapshots (Greaves et al., 2013). Fourth, reviews are large-scale and cost-free, providing thousands to millions of observations at essentially zero cost compared to survey administration expenses (Ranard et al., 2016). Finally, reviews on centralized platforms provide standardized data across all providers, enabling benchmarking and market analysis.

**Limitations of Online Reviews**

Despite advantages, online reviews suffer significant limitations. Most critically, self-selection bias means reviewers are not representative—patients with extreme experiences (very positive or negative) overparticipate while moderately satisfied patients underreview (Gao et al., 2012). Reviewers tend to be younger, more educated, and more affluent than the general patient population (Hanauer et al., 2014). Second, reviews lack clinical context—patients may misunderstand medical information, attributing poor outcomes to error when outcomes resulted from unavoidable complexity (Garcia et al., 2024). Third, verification challenges exist as platforms rarely verify that reviewers were actual patients, creating fake review risks (Deshai and Rao, 2023). Fourth, reviews are unstructured and heterogeneous, varying in length, content, and language quality, requiring natural language processing for analysis (Ranard et al., 2016). Finally, reviews provide limited demographic data, preventing direct subgroup analyses.

**Complementary Roles**

Optimal service quality research employs both data sources rather than treating them as substitutes. Surveys provide representative samples, demographic breakdowns, and standardized metrics suitable for longitudinal tracking. Online reviews provide narrative depth, discovery of emergent issues, real-time monitoring, and large-scale data at low cost. Reviews excel at discovery and scale; surveys excel at representativeness and precision.

### 2.4.2 Validity and Representativeness

**Validity: Do Reviews Reflect Quality?**

Empirical evidence addresses whether reviews reflect actual quality versus mere subjective perception. Ranard et al. (2016) found moderate correlation (r = 0.49, p < 0.001) between Yelp hospital ratings and HCAHPS overall ratings, strongest for communication dimensions (r = 0.48-0.52). However, correlations with clinical outcomes (mortality, readmission rates) are weak (r = 0.05-0.15), reflecting that patients evaluate observable process quality more than outcome quality (Bardach et al., 2013). This is not a flaw—patients evaluate what they can observe. Reviews validly measure interpersonal and process quality, complementing rather than replacing clinical metrics.

**Representativeness: Who Reviews?**

Demographic skew exists: reviewers are disproportionately young (65% aged 18-44), educated (58% college degrees), and affluent (Hanauer et al., 2014). Star ratings exhibit J-shaped distributions—38% five-star and 28% one-star in Taiwan hospital reviews, with underrepresentation of moderate ratings (Ranard et al., 2016). Negative reviews are posted faster (median 14 days) than positive reviews (median 45 days), suggesting anger motivates immediate venting while satisfaction requires sustained reflection (Gao et al., 2012). This study employs volume filtering (minimum 10 reviews per hospital) and time windowing to mitigate these biases.

### 2.4.3 Healthcare Online Reviews: Existing Research

Content analysis studies consistently find that interpersonal quality—communication, attitude, respect—dominates reviews more than technical competence. López et al. (2012) found physician interpersonal manner mentioned in 71% of U.S. Yelp reviews but technical competence in only 15%. Hao and Zhang (2016) used LDA topic modeling on Chinese physician reviews and identified seven topics including physician expertise, communication, service attitude, costs, and wait times, with Chinese patients emphasizing physician reputation more than Western patients. Cross-culturally, patients prioritize observable functional quality over technical quality, consistent with information asymmetry theory (Section 2.1).

Recent NLP advances enable large-scale automated analysis. Hotchkiss et al. (2024) applied Google Cloud NLP to 3,389 hospice reviews, using sentiment analysis and topic modeling to extract quality indicators complementing traditional CAHPS scores. Topic modeling techniques, particularly LDA, allow researchers to discover emergent themes without predetermined categories (Section 2.5). Beyond patient choice, reviews affect organizational performance—Ivanov and Sharman (2018) demonstrated that online review metrics correlate with hospital utilization rates and financial performance, indicating real market consequences.

This study uses Google Maps reviews for both Taiwan and United States, providing identical platform features enabling robust cross-cultural comparison, high review volumes, and broad demographic reach. The text-mining approach using LDA (detailed in Section 2.5) allows service quality dimensions to emerge inductively from patient narratives, addressing limitations of predetermined survey instruments while leveraging the narrative richness and scale advantages of online reviews.

---

## 2.5 Text Mining and Topic Modeling in Service Quality Research

Online reviews provide rich qualitative data at scale, but their unstructured format poses analytical challenges. Manual content analysis yields deep insights but is impractical for thousands of reviews. This requires automated text mining methods that discover patterns, extract themes, and classify content computationally (Aggarwal and Zhai, 2012). This section reviews text mining approaches with emphasis on Latent Dirichlet Allocation (LDA) topic modeling—the method employed in this study.

### 2.5.1 Text Mining Approaches

Text mining encompasses computational methods for extracting meaningful information from unstructured text. Key approaches include frequency-based methods (TF-IDF) identifying most-mentioned attributes but lacking thematic structure; sentiment analysis classifying text as positive or negative but collapsing multiple dimensions into single valence; and aspect-based sentiment analysis (ABSA) jointly extracting service aspects and sentiment polarity but requiring predetermined aspect lexicons (Liu, 2012; Aggarwal and Zhai, 2012).

Topic modeling offers distinct advantages through discovering latent topics probabilistically generating observed text using unsupervised machine learning (Blei, 2012). LDA requires no manual labeling, identifies multiple coexisting topics, quantifies topic prevalence probabilistically, and discovers dimensions from data rather than imposing researcher categories (Blei et al., 2003). While deep learning methods like BiLSTM with BERT achieve higher classification accuracy when labeled training data exists (Athira et al., 2021), LDA is ideal for exploratory research discovering unknown dimensions—precisely the requirement for cross-cultural service quality research where dimensional structures may differ between Taiwan and the United States.

### 2.5.2 Latent Dirichlet Allocation (LDA)

LDA conceptualizes documents as mixtures of topics, where each topic is a probability distribution over words. For example, a hospital review might be 60% "interpersonal quality" (containing words like caring, empathy, respectful), 30% "wait times" (containing words like wait, delay, crowded), and 10% "facility environment" (containing words like clean, modern, comfortable). LDA estimates these hidden topic structures from observed word frequencies (Blei et al., 2003).

The algorithm assumes documents are generated through a probabilistic process: select a distribution over topics for the document, then for each word position, choose a topic from that distribution and choose a word from that topic's word distribution. LDA reverses this generative process, inferring the topic distributions that most likely produced the observed text through Bayesian inference (Hoffman et al., 2010).

Healthcare applications demonstrate LDA's utility. Hao and Zhang (2016) applied LDA to Chinese physician reviews, identifying seven topics including physician expertise, communication, service attitude, costs, and wait times, with Chinese patients emphasizing physician reputation more than Western patients. Arnold et al. (2016) analyzed Medicare beneficiary comments using LDA, discovering dimensions aligned with CAHPS domains (care coordination, communication) but also emergent themes absent from surveys (rural access barriers). Geletta et al. (2019) demonstrated LDA's predictive power, showing that models incorporating LDA-derived topics from clinical trial descriptions significantly outperformed models using structured data alone in predicting trial termination. These applications confirm LDA's capacity to discover meaningful service quality dimensions from patient narratives.

### 2.5.3 Determining the Number of Topics

LDA requires researchers to specify the number of topics K a priori, yet no consensus exists on optimal selection methods. Two approaches dominate. Statistical metrics include perplexity (lower indicates better predictive accuracy but often favors unrealistically high K), and coherence scores measuring semantic relatedness of top words within topics (higher indicates more interpretable topics) (Röder et al., 2015). However, statistical optima may not yield substantively interpretable topics. Human interpretability assessment involves domain experts evaluating topic coherence, distinctiveness, and substantive relevance across multiple K values, selecting the number yielding most interpretable, actionable dimensions (Chang et al., 2009).

This study employs a hybrid approach: computing coherence scores (C_v metric) across K=5 to K=15, then having healthcare service quality researchers independently evaluate top-performing models for interpretability, selecting K maximizing both statistical coherence and substantive meaningfulness. This methodological pluralism aligns with recommendations from text mining methodologists (Maier et al., 2018).

### 2.5.4 Cross-Cultural and Cross-Linguistic Topic Modeling

Applying LDA to cross-cultural comparisons introduces methodological challenges. Language differences require separate preprocessing (Chinese word segmentation using Jieba versus English tokenization), potentially affecting discovered topics through algorithmic differences rather than true content differences (Boyd-Graber et al., 2017). Cultural linguistic norms shape expression—Taiwanese patients may use indirect language while Americans use explicit criticism, affecting whether similar concerns manifest as distinct topics or remain latent.

Translation-based approaches translating all text to a common language risk semantic loss and introduce translation errors. Separate models for each language (this study's approach) allow language-appropriate preprocessing and topic discovery but require post-hoc alignment to identify corresponding topics across countries through manual examination of top words and representative documents (Hao and Zhang, 2016).

Recent cross-linguistic NLP research provides validation for language-specific approaches. Alhazzani et al. (2023) successfully classified Arabic patient experience comments into 25 categories using customized BERT models, while Yazdani et al. (2023) achieved 89-93% sentiment analysis accuracy in Persian cancer patient comments. These studies demonstrate that language-specific NLP methods effectively capture patient experiences despite linguistic differences, supporting this study's separate-model approach for Taiwan (Chinese) and U.S. (English) hospital reviews.

This methodological choice accepts that discovered topics may not correspond one-to-one across countries—some topics may be culture-specific. Rather than imposing identical structures, we inductively discover dimensions in each context, then systematically compare structures to identify universal dimensions, culture-specific dimensions, and differentially prominent dimensions, informed by cultural and institutional theory (Sections 2.2-2.3).

### Summary

Text mining enables large-scale analysis of unstructured patient reviews, with LDA offering unsupervised, probabilistic discovery of latent service quality dimensions. Healthcare applications demonstrate LDA's capacity to identify meaningful, actionable themes from patient narratives, complementing predetermined survey structures. Cross-cultural applications require methodological care regarding language differences and topic alignment, addressed through separate language-appropriate models and systematic post-hoc comparison. This approach enables discovering whether Taiwan and U.S. hospital reviews reveal similar universal dimensions or divergent culture-specific structures, integrating theoretical frameworks (Sections 2.1-2.3) with empirical patterns discovered inductively from patient discourse.

---

## References

Aggarwal, C.C., & Zhai, C. (2012). *Mining text data*. Springer Science & Business Media.

Alhazzani, N.Z., Al-Turaiki, I.M., & Alkhodair, S.A. (2023). Arabic patient experience comment classification. *IEEE Access*, 11, 50591-50607.

Andaleeb, S.S. (2001). Service quality perceptions and patient satisfaction: a study of hospitals in a developing country. *Social Science & Medicine*, 52(9), 1359-1370.

Arnold, C.W., Tan, S.S., Thadaney-Israni, S., Lembersky, M., Kallmes, D.F., Freeman, W.D., & Oh, S. (2016). Evaluating patient perceptions on Medicare Access and CHIP Reauthorization Act quality measures. *Journal of the American Medical Informatics Association*, 23(e1), e118-e124.

Athira, B., Jones, J., Idicula, S.M., et al. (2021). Breast cancer risk prediction using BiLSTM. *IEEE Transactions on Computational Social Systems*, 8(5), 1080-1088.

Bardach, N.S., Asteria-Peñaloza, R., Boscardin, W.J., & Dudley, R.A. (2013). The relationship between commercial website ratings and traditional hospital performance measures in the USA. *BMJ Quality & Safety*, 22(3), 194-202.

Berry, L.L., & Bendapudi, N. (2007). Health care: a fertile field for service research. *Journal of Service Research*, 10(2), 111-122.

Blei, D.M. (2012). Probabilistic topic models. *Communications of the ACM*, 55(4), 77-84.

Blei, D.M., Ng, A.Y., & Jordan, M.I. (2003). Latent Dirichlet allocation. *Journal of Machine Learning Research*, 3, 993-1022.

Boyd-Graber, J., Hu, Y., & Mimno, D. (2017). Applications of topic models. *Foundations and Trends in Information Retrieval*, 11(2-3), 143-296.

Brady, M.K., & Cronin, J.J. (2001). Some new thoughts on conceptualizing perceived service quality: A hierarchical approach. *Journal of Marketing*, 65(3), 34-49.

Buttle, F. (1996). SERVQUAL: review, critique, research agenda. *European Journal of Marketing*, 30(1), 8-32.

Chang, G.M., & Tung, Y.C. (2024). Impact of care coordination on 30-day readmission, mortality, and costs for heart failure. *American Journal of Managed Care*, 30(1), e1-e7.

Chang, J., Gerrish, S., Wang, C., Boyd-Graber, J., & Blei, D.M. (2009). Reading tea leaves: How humans interpret topic models. *Advances in Neural Information Processing Systems*, 22, 288-296.

Cheng, S.H., & Chiang, T.L. (2012). The effect of universal health insurance on health care utilization in Taiwan: Results from a natural experiment. *JAMA*, 278(2), 89-93.

Cheng, T.M. (2015). Reflections on the 20th anniversary of Taiwan's single-payer National Health Insurance system. *Health Affairs*, 34(3), 502-510.

Commonwealth Fund. (2020). *2020 International Health Policy Survey*. Commonwealth Fund: New York.

Cronin, J.J., & Taylor, S.A. (1992). Measuring service quality: a reexamination and extension. *Journal of Marketing*, 56(3), 55-68.

Dagger, T.S., Sweeney, J.C., & Johnson, L.W. (2007). A hierarchical model of health service quality: scale development and investigation of an integrated model. *Journal of Service Research*, 10(2), 123-142.

Darby, M.R., & Karni, E. (1973). Free competition and the optimal amount of fraud. *Journal of Law and Economics*, 16(1), 67-88.

Deshai, S.N., & Rao, Y.S. (2023). Fake review detection in healthcare using dense neural network model. *Engineering Applications of Artificial Intelligence*, 120, 105891.

Donabedian, A. (1988). The quality of care: How can it be assessed? *JAMA*, 260(12), 1743-1748.

Donthu, N., & Yoo, B. (1998). Cultural influences on service quality expectations. *Journal of Service Research*, 1(2), 178-186.

Furrer, O., Liu, B.S.C., & Sudharshan, D. (2000). The relationships between culture and service quality perceptions: Basis for cross-cultural market segmentation and resource allocation. *Journal of Service Research*, 2(4), 355-371.

Gao, G.G., McCullough, J.S., Agarwal, R., & Jha, A.K. (2012). A changing landscape of physician quality reporting: analysis of patients' online ratings of their physicians over a 5-year period. *Journal of Medical Internet Research*, 14(1), e38.

Garcia, G.G.P., Sung, C.K., Amirlak, B., & Engelsman, A.F. (2024). Characterization of one-star Yelp reviews for otolaryngologists. *American Journal of Otolaryngology*, 45(3), 104206.

Geletta, S., Follett, L., & Laugerman, M. (2019). Latent Dirichlet allocation in predicting clinical trial terminations. *BMC Medical Informatics and Decision Making*, 19, Article 92.

Giusti, A., Nkhoma, K., Petrus, R., Petersen, I., Gwyther, L., Farrant, L., Venkatapuram, S., & Harding, R. (2020). The empirical evidence underpinning the concept and practice of person-centred care for serious illness: a systematic review. *BMJ Global Health*, 5(12), e003330.

Grönroos, C. (1984). A service quality model and its marketing implications. *European Journal of Marketing*, 18(4), 36-44.

Greaves, F., Ramirez-Cano, D., Millett, C., Darzi, A., & Donaldson, L. (2013). Use of sentiment analysis for capturing patient experience from free-text comments posted online. *Journal of Medical Internet Research*, 15(11), e239.

Hanauer, D.A., Zheng, K., Singer, D.C., Gebremariam, A., & Davis, M.M. (2014). Public awareness, perception, and use of online physician rating sites. *JAMA*, 311(7), 734-735.

Hao, H., & Zhang, K. (2016). The voice of Chinese health consumers: A text mining approach to web-based physician reviews. *Journal of Medical Internet Research*, 18(5), e108.

Himmelstein, D.U., Lawless, R.M., Thorne, D., Foohey, P., & Woolhandler, S. (2019). Medical bankruptcy: Still common despite the Affordable Care Act. *American Journal of Public Health*, 109(3), 431-433.

Hoffman, M., Blei, D.M., & Bach, F. (2010). Online learning for latent Dirichlet allocation. *Advances in Neural Information Processing Systems*, 23, 856-864.

Hofstede, G. (1980). *Culture's consequences: International differences in work-related values*. Sage Publications: Beverly Hills, CA.

Hofstede, G. (2001). *Culture's consequences: Comparing values, behaviors, institutions and organizations across nations* (2nd ed.). Sage Publications: Thousand Oaks, CA.

Hotchkiss, R.B., Swartz, J.L., Thomas, K.S., & Unroe, K.T. (2024). Using Google Cloud natural language processing to analyze caregiver reviews of hospices. *Journal of Pain and Symptom Management*, 67(2), 120-128.

Ivanov, O.B., & Sharman, R. (2018). Dynamic signals in user-generated content: Hospital reputation and patient engagement. *Journal of Management Information Systems*, 35(4), 1112-1143.

Kim, Y.M., Kols, A., & Mucheke, S. (2002). Informed choice and decision-making in family planning counseling in Kenya. *International Family Planning Perspectives*, 28(1), 4-11.

Kuhlmann, E., Burau, V., Correia, T., Lewandowski, R., Lionis, C., Noordegraaf, M., & Repullo, J. (2020). "A manager in the minds of doctors": A comparison of new modes of control in European hospitals. *BMC Health Services Research*, 13(1), 1-11.

Lewis, N.V., Bierce, A., Feder, G.S., Macleod, J., Turner, K.M., Zammit, S., & Dheensa, S. (2023). Trauma-informed approaches in primary healthcare and community mental healthcare. *Health & Social Care in the Community*, 2023, 1-18.

Liu, B. (2012). Sentiment analysis and opinion mining. *Synthesis Lectures on Human Language Technologies*, 5(1), 1-167.

López, A., Detz, A., Ratanawongsa, N., & Sarkar, U. (2012). What patients say about their doctors online: A qualitative content analysis. *Journal of General Internal Medicine*, 27(6), 685-692.

Maier, D., Waldherr, A., Miltner, P., et al. (2018). Applying LDA topic modeling in communication research. *Communication Methods and Measures*, 12(2-3), 93-118.

Mattila, A.S. (1999). The role of culture and purchase motivation in service encounter evaluations. *Journal of Services Marketing*, 13(4/5), 376-389.

Merritt Hawkins. (2017). *2017 Survey of physician appointment wait times and Medicare and Medicaid acceptance rates*. Merritt Hawkins: Dallas, TX.

OECD Health Statistics. (2022). *OECD Health Statistics 2022*. OECD Publishing: Paris.

Oliver, R.L. (1980). A cognitive model of the antecedents and consequences of satisfaction decisions. *Journal of Marketing Research*, 17(4), 460-469.

Papanicolas, I., Woskie, L.R., & Jha, A.K. (2018). Health care spending in the United States and other high-income countries. *JAMA*, 319(10), 1024-1039.

Parasuraman, A., Zeithaml, V.A., & Berry, L.L. (1985). A conceptual model of service quality and its implications for future research. *Journal of Marketing*, 49(4), 41-50.

Parasuraman, A., Zeithaml, V.A., & Berry, L.L. (1988). SERVQUAL: A multiple-item scale for measuring consumer perceptions of service quality. *Journal of Retailing*, 64(1), 12-40.

Ranard, B.L., Werner, R.M., Antanavicius, T., Schwartz, H.A., Smith, R.J., Meisel, Z.F., Asch, D.A., Ungar, L.H., & Merchant, R.M. (2016). Yelp reviews of hospital care can supplement and inform traditional surveys of the patient experience of care. *Health Affairs*, 35(4), 697-705.

Röder, M., Both, A., & Hinneburg, A. (2015). Exploring the space of topic coherence measures. *Proceedings of the Eighth ACM International Conference on Web Search and Data Mining*, 399-408.

Scott, W.R. (2008). *Institutions and organizations: Ideas and interests* (3rd ed.). Sage Publications: Thousand Oaks, CA.

Steenkamp, J.B.E., & Baumgartner, H. (1998). Assessing measurement invariance in cross-national consumer research. *Journal of Consumer Research*, 25(1), 78-90.

Tai-Seale, M., McGuire, T.G., & Zhang, W. (2007). Time allocation in primary care office visits. *Health Services Research*, 42(5), 1871-1894.

Tikkanen, R., Osborn, R., Mossialos, E., Djordjevic, A., & Wharton, G.A. (2020). *International Health Care System Profiles: United States*. Commonwealth Fund: New York.

Tsai, Y.W., Wen, Y.W., Chen, P.F., Kuo, R.N., & Chiu, L.S. (2009). Examining the impact of Taiwan's National Health Insurance on the practice patterns and incomes of physicians. *Health Affairs*, 28(5), w900-w908.

Winsted, K.F. (1997). The service experience in two cultures: A behavioral perspective. *Journal of Retailing*, 73(3), 337-360.

World Bank. (2022). *World Development Indicators 2022*. World Bank: Washington, DC.

Yazdani, A., Shamloo, M., Khaki, M., & Nahvijou, A. (2023). Persian sentiment analysis of cancer patients. *BMC Medical Informatics and Decision Making*, 23, Article 68.

Yi, I., Sohn, H.S., & Kim, T. (2015). Linking state intervention and health equity differently: The universalization of health care in South Korea and Taiwan. *Korea Observer*, 46(1), 1-28.

Yoon, G.H., & Cheng, S.H. (2021). Differences in trends of perceived inpatient care quality based on regional socioeconomic level in the United States and Taiwan. *Health Services Research*, 56(6), 1182-1193. https://doi.org/10.1111/1475-6773.13872
