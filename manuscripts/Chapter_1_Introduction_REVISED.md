# Chapter 1: Introduction

## 1.1 Research Background and Motivation

Healthcare service quality represents a fundamental challenge confronting health systems globally, with inadequate quality contributing to millions of preventable patient harms annually (WHO, 2020). While extensive research has examined healthcare quality within individual national contexts, a critical theoretical and empirical question has not been adequately addressed: Do patients across fundamentally different healthcare systems prioritize identical service quality dimensions, or do system structures and cultural contexts fundamentally shape quality perceptions?

This question is of significant theoretical importance for service quality research, which has long debated whether quality dimensions are universal across contexts or culturally and institutionally contingent (Brady and Cronin, 2001; Parasuraman et al., 1988). Empirically, understanding cross-national patterns in patient priorities is essential for identifying universal healthcare challenges that transcend system boundaries, as well as culture- and system-specific concerns requiring tailored interventions. Practically, such knowledge informs evidence-based quality improvement strategies and culturally sensitive service design.

The contrast between Taiwan's single-payer National Health Insurance (NHI) system and the United States' multi-payer, market-based system provides an ideal natural experiment for examining how healthcare system structure influences patient satisfaction determinants. Despite both nations achieving high healthcare outcomes by international standards, their patients experience fundamentally different care delivery mechanisms, financing structures, and cultural expectations. Taiwan's NHI achieves 99.9% population coverage with minimal cost-sharing, while the U.S. system features substantial uninsurance (9%) and high patient cost burdens (Cheng, 2015; Tikkanen et al., 2020). Whether these structural differences translate into divergent patient priorities regarding service quality dimensions remains an empirical question with profound theoretical and practical implications.

---

## 1.2 Literature Context and Research Gaps

### 1.2.1 Limitations of Traditional Quality Assessment Methods

Traditional healthcare quality assessment has relied predominantly on structured instruments such as SERVQUAL (Parasuraman et al., 1988) and healthcare-adapted variants (Dagger et al., 2007). While these instruments provide standardized measurement, they suffer from systematic limitations that are particularly problematic in cross-cultural and cross-system comparative research.

First, researcher-imposed frameworks constrain patient expression to predetermined dimensions that may inadequately capture culture-specific priorities, emerging concerns, or system-specific quality attributes (Carman, 1990). Second, cross-cultural translation introduces measurement non-equivalence, with survey items carrying different semantic connotations across languages and response styles varying systematically by culture (Harzing, 2006; Steenkamp and Baumgartner, 1998). Third, social desirability bias may suppress honest criticism, particularly in cultures emphasizing social harmony and hierarchical respect (Donthu and Yoo, 1998). Fourth, the temporal lag between survey design and data collection means findings may become outdated before publication. This is particularly problematic given rapid changes in healthcare delivery, such as telemedicine expansion and COVID-19 adaptations.

### 1.2.2 The Emergence of Online Patient Reviews as a Data Source

The proliferation of online patient reviews on platforms such as Google Maps, Yelp, and Healthgrades presents methodological opportunities to address these limitations. These unsolicited patient narratives offer several distinct advantages: (1) authenticity, as patients express concerns without researcher prompting; (2) immediacy, capturing real-time sentiment and emerging issues; (3) scale, providing thousands to millions of observations at minimal cost; (4) cross-cultural comparability, as identical platform mechanisms enable methodologically consistent comparison; and (5) narrative richness, including contextual details and emotional intensity that structured surveys may miss (Ranard et al., 2016; Hao and Zhang, 2016).

However, extracting service quality dimensions from massive volumes of unstructured, multilingual narratives requires analytical methods that avoid imposing predetermined frameworks while enabling rigorous cross-national comparison. This methodological challenge has limited the application of online reviews in comparative healthcare quality research.

### 1.2.3 Critical Gaps in Current Knowledge

Three critical gaps constrain theoretical advancement and practical application in cross-national healthcare quality research:

**Gap 1: Absence of Methodologically Comparable Cross-National Studies**. Existing healthcare quality research remains predominantly single-country in focus. The limited existing cross-national studies employ different methodologies across countries, making direct comparison problematic and limiting generalizability (Fung et al., 2008). No prior study has applied identical analytical methods to comparable patient-generated data across fundamentally different healthcare systems (single-payer versus multi-payer) to systematically identify both universal and system-specific quality dimensions.

**Gap 2: Underutilization of Unsupervised Topic Modeling in Cross-Lingual Healthcare Research**. Latent Dirichlet Allocation (LDA) demonstrates considerable power in extracting latent themes from large text corpora without researcher-imposed categories (Blei et al., 2003). While increasingly applied to hospitality and retail service reviews, LDA remains underutilized in healthcare contexts and exceedingly rare in cross-lingual applications. No prior study has developed a systematic framework for applying LDA across Chinese and English hospital reviews to enable semantic mapping and rigorous cross-cultural comparison while respecting linguistic and cultural differences.

**Gap 3: Unresolved Theoretical Debate on Universal versus Context-Specific Quality Dimensions**. Service quality theory contains a fundamental unresolved tension: Are quality dimensions universal across cultures and contexts, or fundamentally shaped by cultural values and system structures (Brady and Cronin, 2001)? While conceptual arguments exist on both sides, empirical evidence remains limited and contradictory. Empirical quantification is lacking regarding which specific dimensions transcend system boundaries (universal challenges) versus which emerge uniquely from particular healthcare structures or cultural contexts (system-specific concerns). This gap limits theoretical development and practical application of service quality frameworks across diverse healthcare systems.

---

## 1.3 Research Objectives and Questions

This study addresses these three critical gaps through a methodologically innovative comparative analysis of patient-generated online reviews from Taiwan and the United States. We employ identical unsupervised topic modeling methods to extract service quality dimensions from both datasets, enabling rigorous cross-national comparison while respecting linguistic and cultural differences.

The study addresses three research questions:

**RQ1**: What service quality dimensions emerge from patient reviews of hospitals in Taiwan versus the United States when analyzed using identical unsupervised topic modeling methods?

**RQ2**: Which service quality dimensions represent universal concerns that transcend healthcare system structures, and which are system-specific or culture-specific?

**RQ3**: How do different healthcare system structures (single-payer vs. multi-payer) influence the composition and relative importance of patient satisfaction determinants?

To answer these questions, we analyze 5,007 patient reviews from Taiwan's 26 top-tier medical centers and 3,363 reviews from 28 leading U.S. hospitals using seven-topic Latent Dirichlet Allocation models. Through systematic cross-lingual semantic mapping and comparative analysis, we identify both shared and divergent quality dimensions, quantifying their prevalence and association with patient satisfaction ratings.

---

## 1.4 Study Contributions

This study makes several significant contributions to service quality theory, healthcare quality research, and methodological practice:

**Theoretical Contributions**: First, by employing data-driven, unsupervised topic modeling rather than predetermined survey dimensions, we provide empirical validation that patients' natural discourse about healthcare quality spontaneously organizes into multiple distinct dimensions. We discover culture- and system-specific dimensions absent from Western frameworks, demonstrating that while multidimensionality is universal, specific dimensional structures require cultural and system contextualization. Second, we provide quantitative evidence that healthcare system structure fundamentally shapes which quality dimensions patients prioritize, introducing the concept of "system tax"—the measurable satisfaction penalty imposed by system structure independent of clinical care quality. Third, we empirically establish convergence patterns across systems. For example, emergency care emerges as the largest quality concern in both nations, identifying universal structural challenges versus system-specific failures.

**Methodological Contributions**: This study contributes a replicable framework for cross-lingual LDA analysis in healthcare and service quality research, comprising three methodological innovations: (1) an integrated topic number selection framework balancing statistical performance, semantic interpretability, and theoretical alignment; (2) a systematic cross-lingual semantic mapping protocol enabling rigorous cross-cultural comparison while respecting linguistic differences; and (3) integration of unsupervised topic extraction with structured satisfaction ratings, quantifying each dimension's association with overall patient satisfaction.

**Practical Contributions**: Our findings provide actionable guidance for hospital administrators and health policymakers in both nations, identifying priority areas for quality improvement and system-specific interventions. The cross-national comparison enables evidence-based policy learning and culturally adapted service design.

---

## 1.5 Structure of This Paper

The remainder of this paper proceeds as follows. Chapter 2 reviews relevant literature on service quality theory, cross-cultural healthcare research, healthcare systems comparison (Taiwan vs. United States), online reviews as data sources, and topic modeling applications in service quality research. Chapter 3 details our data collection methodology from Taiwan and U.S. hospital reviews, preprocessing procedures, and our LDA analytical approach, including topic number selection and cross-lingual semantic mapping protocols. Chapter 4 presents the extracted quality dimensions for each country, systematic cross-national comparisons, and quantitative associations between dimensions and patient satisfaction ratings. Chapter 5 discusses theoretical implications, practical recommendations for hospital administrators and policymakers, study limitations, and directions for future research. Chapter 6 concludes by synthesizing contributions and outlining future research directions.

---

## References

Blei, D.M., Ng, A.Y., & Jordan, M.I. (2003). Latent Dirichlet allocation. *Journal of Machine Learning Research*, 3, 993-1022.

Brady, M.K., & Cronin, J.J. (2001). Some new thoughts on conceptualizing perceived service quality: A hierarchical approach. *Journal of Marketing*, 65(3), 34-49.

Carman, J.M. (1990). Consumer perceptions of service quality: An assessment of the SERVQUAL dimensions. *Journal of Retailing*, 66(1), 33-55.

Cheng, T.M. (2015). Reflections on the 20th anniversary of Taiwan's single-payer National Health Insurance system. *Health Affairs*, 34(3), 502-510.

Dagger, T.S., Sweeney, J.C., & Johnson, L.W. (2007). A hierarchical model of health service quality: Scale development and investigation of an integrated model. *Journal of Service Research*, 10(2), 123-142.

Donthu, N., & Yoo, B. (1998). Cultural influences on service quality expectations. *Journal of Service Research*, 1(2), 178-186.

Fung, C.H., Lim, Y.W., Mattke, S., Damberg, C., & Shekelle, P.G. (2008). Systematic review: The evidence that publishing patient care performance data improves quality of care. *Annals of Internal Medicine*, 148(2), 111-123.

Hao, H., & Zhang, K. (2016). The voice of Chinese health consumers: A text mining approach to web-based physician reviews. *Journal of Medical Internet Research*, 18(5), e108.

Harzing, A.W. (2006). Response styles in cross-national survey research: A 26-country study. *International Journal of Cross Cultural Management*, 6(2), 243-266.

Parasuraman, A., Zeithaml, V.A., & Berry, L.L. (1988). SERVQUAL: A multiple-item scale for measuring consumer perceptions of service quality. *Journal of Retailing*, 64(1), 12-40.

Ranard, B.L., Werner, R.M., Antanavicius, T., Schwartz, H.A., Smith, R.J., Meisel, Z.F., Asch, D.A., Ungar, L.H., & Merchant, R.M. (2016). Yelp reviews of hospital care can supplement and inform traditional surveys of the patient experience of care. *Health Affairs*, 35(4), 697-705.

Steenkamp, J.B.E., & Baumgartner, H. (1998). Assessing measurement invariance in cross-national consumer research. *Journal of Consumer Research*, 25(1), 78-90.

Tikkanen, R., Osborn, R., Mossialos, E., Djordjevic, A., & Wharton, G.A. (2020). *International Health Care System Profiles: United States*. Commonwealth Fund: New York.

World Health Organization. (2020). *Patient safety*. Retrieved from https://www.who.int/news-room/fact-sheets/detail/patient-safety

