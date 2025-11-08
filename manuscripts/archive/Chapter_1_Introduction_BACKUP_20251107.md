# Chapter 1: Introduction

## 1.1 The Global Challenge of Healthcare Quality

Healthcare service quality remains one of the most pressing challenges facing health systems worldwide. According to the World Health Organization, inadequate quality of care contributes to millions of preventable patient harms annually, with significant variations across countries and healthcare systems (WHO, 2020). While substantial research has examined healthcare quality within individual nations, a critical question remains largely unanswered: Do patients in different healthcare systems—particularly those with fundamentally different organizational structures—prioritize the same service quality dimensions? Understanding these cross-national patterns is essential for identifying universal healthcare challenges that transcend system boundaries, as well as culture-specific concerns that require tailored interventions.

The contrast between Taiwan's single-payer National Health Insurance system and the United States' multi-payer, market-based system provides an ideal natural experiment for examining how healthcare system structure influences patient satisfaction. Despite both nations achieving high healthcare outcomes by international standards, their patients navigate vastly different care delivery and financing mechanisms. Whether these structural differences translate into divergent patient priorities regarding service quality remains an empirical question with significant theoretical and practical implications.

---

## 1.2 Research Gaps and Methodological Challenges

### Limitations of Traditional Quality Assessment

Traditional healthcare quality assessment relies predominantly on structured instruments such as SERVQUAL (Parasuraman et al., 1988) and healthcare-adapted variants (Dagger et al., 2007). While these instruments provide standardized measurement, they suffer from systematic limitations particularly problematic in cross-cultural research. First, researcher-imposed frameworks constrain patient expression to predetermined dimensions that may not capture culture-specific priorities or emerging concerns (Carman, 1990). Second, cross-cultural translation introduces measurement non-equivalence, with survey items carrying different connotations across languages and response styles varying systematically by culture (Harzing, 2006). Third, social desirability bias may suppress honest criticism, particularly in cultures emphasizing social harmony. Finally, temporal lag between survey design and data collection means findings may be outdated before publication.

### The Opportunity of Online Patient Reviews

The proliferation of online patient reviews on platforms like Google Maps presents methodological opportunities to address these limitations. These unsolicited patient narratives offer authenticity (no researcher prompting), immediacy (real-time sentiment), scale (thousands of reviews), cross-cultural comparability (identical platform mechanisms), and richness (contextual details and emotional intensity) (Ranard et al., 2016). However, extracting service quality dimensions from massive volumes of unstructured, multilingual narratives requires analytical methods that avoid imposing predetermined frameworks while enabling rigorous cross-national comparison.

### Critical Gaps in Current Knowledge

Three critical gaps constrain theoretical advancement and practical application:

**Gap 1: Absence of Methodologically Comparable Cross-National Studies**. Existing healthcare quality research remains predominantly single-country in focus. The limited cross-national studies employ different methodologies across countries, making direct comparison problematic (Fung et al., 2008). No prior study has applied identical analytical methods to comparable patient-generated data across drastically different healthcare systems (single-payer versus multi-payer) to identify both universal and system-specific quality dimensions.

**Gap 2: Limited Application of Unsupervised Topic Modeling in Cross-Lingual Healthcare Research**. Latent Dirichlet Allocation (LDA) demonstrates power in extracting latent themes from large text corpora without researcher-imposed categories (Blei et al., 2003). While increasingly applied to hospitality and retail service reviews, LDA remains underutilized in healthcare contexts and exceedingly rare in cross-lingual applications. No prior study has developed a systematic framework for applying LDA across Chinese and English hospital reviews to enable semantic mapping and cross-cultural comparison.

**Gap 3: Unresolved Theoretical Debate on Universal vs. Culture-Specific Quality Dimensions**. Service quality theory contains a fundamental unresolved tension: Are quality dimensions universal across cultures and contexts, or fundamentally shaped by cultural values and system structures (Brady and Cronin, 2001)? While conceptual arguments exist on both sides, empirical evidence remains limited and contradictory. What remains absent is empirical quantification of which specific dimensions transcend system boundaries (universal challenges) versus which emerge uniquely from particular healthcare structures or cultural contexts (system-specific concerns).

---

## 1.3 Research Objectives

This study addresses these three critical gaps through a methodologically innovative comparative analysis of patient reviews from Taiwan and the United States. We pose three research questions:

**RQ1**: What service quality dimensions emerge from patient reviews of hospitals in Taiwan versus the United States when analyzed using identical unsupervised topic modeling methods?

**RQ2**: Which service quality dimensions represent universal concerns that transcend healthcare system structures, and which are system-specific or culture-specific?

**RQ3**: How do different healthcare system structures (single-payer vs. multi-payer) influence the composition and relative importance of patient satisfaction determinants?

To answer these questions, we analyze 5,007 patient reviews from Taiwan's 26 top-tier medical centers and 3,363 reviews from 28 leading U.S. hospitals using seven-topic Latent Dirichlet Allocation models. Through cross-lingual semantic mapping and comparative analysis, we identify both shared and divergent quality dimensions, quantifying their prevalence and association with patient satisfaction.

---

## 1.4 Theoretical and Methodological Contributions

### Theoretical Contributions

This study makes four significant contributions to service quality theory and healthcare quality research.

First, by employing data-driven, unsupervised topic modeling rather than predetermined survey dimensions, we provide empirical validation that patients' natural discourse about healthcare quality spontaneously organizes into multiple distinct dimensions—seven in both countries. We discover culture-specific dimensions absent from Western frameworks: Taiwan's distinct "Interpersonal Attitude" dimension (17.3% of reviews) reflecting collectivist cultural emphasis on interpersonal harmony, and the United States' "Billing and Insurance" dimension (12-15% of reviews) unique to multi-payer systems. These findings demonstrate that while multidimensionality is universal, the specific dimensional structure requires cultural and system contextualization.

Second, we provide quantitative evidence that healthcare system structure affects not only access and clinical outcomes, but fundamentally shapes which quality dimensions patients prioritize. We introduce the concept of "system tax": the measurable satisfaction penalty imposed by system structure independent of clinical care quality. Billing concerns generate 12-15% of negative U.S. reviews but are virtually absent in Taiwan's single-payer system.

Third, we empirically establish that emergency care represents the single largest quality concern in both nations, comprising approximately 30% of reviews in each country with similarly low satisfaction scores. This striking convergence across dramatically different healthcare systems identifies emergency department crowding and quality as a universal structural challenge rather than a culture-specific or system-specific failure.

Fourth, by analyzing Taiwanese patient reviews using methods identical to U.S. analysis, we provide empirical foundation for truly cross-cultural theory development. Our findings support a hybrid theoretical model: certain quality dimensions (medical professionalism, emergency care) operate universally, while others (interpersonal warmth expectations, billing transparency) require cultural and system contextualization.

### Methodological Contributions

Beyond theoretical advancement, this study contributes a replicable framework for cross-lingual LDA analysis in healthcare and service quality research, comprising three methodological innovations.

First, we develop an integrated topic number selection framework balancing statistical performance (coherence, perplexity), semantic interpretability by domain experts, theoretical alignment with existing service quality frameworks, and topic prevalence distribution balance. This framework addresses a persistent challenge in applied LDA research: statistical optima frequently diverge from practical utility.

Second, we establish a systematic cross-lingual semantic mapping protocol enabling cross-cultural comparison while respecting linguistic and cultural differences. This protocol involves independent LDA extraction in each language, expert semantic interpretation of topics using representative reviews, dimensional alignment based on conceptual equivalence rather than literal translation, and quantitative comparison of aligned dimensions' prevalence and sentiment.

Third, we link unsupervised topic extraction with structured satisfaction ratings at the review level, quantifying each dimension's association with overall patient satisfaction. This integration enables prioritization based on both prevalence (how often patients mention a dimension) and impact (how strongly it influences overall ratings).

---

## 1.5 Practical Implications

Our findings provide actionable guidance for hospital administrators and health policymakers in both nations. Taiwan's hospitals should prioritize emergency care transformation (30.9% of reviews, 1.79 stars) and service attitude training (17.3% of reviews, 1.69 stars). U.S. hospitals should address emergency wait time reduction and billing transparency and simplification (12-15% of negative reviews). For policymakers, Taiwan should develop national emergency care standards and service quality certification emphasizing interpersonal communication competencies, while the United States should accelerate price transparency regulations and standardize insurance explanation documents. International cooperation should focus on cross-national emergency care best practice exchanges and developing culturally adapted patient satisfaction measurement tools.

---

## 1.6 Structure of This Paper

The remainder of this paper proceeds as follows. Chapter 2 reviews relevant literature on service quality theory, cross-cultural healthcare research, healthcare systems comparison, online reviews as data sources, and topic modeling applications. Chapter 3 details our data collection from Taiwan and U.S. hospital reviews and our LDA analytical approach. Chapter 4 presents extracted quality dimensions for each country, cross-national comparisons, and associations with patient satisfaction. Chapter 5 discusses theoretical implications, practical recommendations, and study limitations. Chapter 6 concludes with contributions and future research directions.

---

## References

Blei, D.M., Ng, A.Y., & Jordan, M.I. (2003). Latent Dirichlet allocation. *Journal of Machine Learning Research*, 3, 993-1022.

Brady, M.K., & Cronin, J.J. (2001). Some new thoughts on conceptualizing perceived service quality: A hierarchical approach. *Journal of Marketing*, 65(3), 34-49.

Carman, J.M. (1990). Consumer perceptions of service quality: An assessment of the SERVQUAL dimensions. *Journal of Retailing*, 66(1), 33-55.

Dagger, T.S., Sweeney, J.C., & Johnson, L.W. (2007). A hierarchical model of health service quality: Scale development and investigation of an integrated model. *Journal of Service Research*, 10(2), 123-142.

Fung, C.H., Lim, Y.W., Mattke, S., Damberg, C., & Shekelle, P.G. (2008). Systematic review: The evidence that publishing patient care performance data improves quality of care. *Annals of Internal Medicine*, 148(2), 111-123.

Harzing, A.W. (2006). Response styles in cross-national survey research: A 26-country study. *International Journal of Cross Cultural Management*, 6(2), 243-266.

Parasuraman, A., Zeithaml, V.A., & Berry, L.L. (1988). SERVQUAL: A multiple-item scale for measuring consumer perceptions of service quality. *Journal of Retailing*, 64(1), 12-40.

Ranard, B.L., Werner, R.M., Antanavicius, T., Schwartz, H.A., Smith, R.J., Meisel, Z.F., Asch, D.A., Ungar, L.H., & Merchant, R.M. (2016). Yelp reviews of hospital care can supplement and inform traditional surveys of the patient experience of care. *Health Affairs*, 35(4), 697-705.

World Health Organization. (2020). *Patient safety*. Retrieved from https://www.who.int/news-room/fact-sheets/detail/patient-safety
