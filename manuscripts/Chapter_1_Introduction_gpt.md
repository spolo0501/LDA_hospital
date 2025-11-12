# Chapter 1: Introduction (GPT Version)

**說明**：此版本由 ChatGPT GPTS 生成，更符合 SSCI 期刊學術風格

---

1. Introduction (Revised and Condensed for SSCI)

Healthcare service quality remains a persistent global challenge. The World Health Organization (2020) estimates that millions of patients suffer preventable harm each year due to inadequate care quality, with outcomes varying widely across health systems. Although extensive research has explored healthcare quality within single nations, a key question remains unresolved: Do patients in fundamentally different healthcare systems prioritize the same dimensions of service quality? Understanding cross-national patterns can reveal universal challenges that transcend system boundaries and system-specific issues that arise from distinct institutional and cultural contexts. This distinction is essential for policy—while universal dimensions facilitate the transfer of best practices, system-specific ones demand tailored interventions.

The contrasting structures of Taiwan's single-payer National Health Insurance (NHI) and the United States' multi-payer, market-based system offer an ideal context for exploring how systemic design shapes patient perceptions. Both nations achieve strong health outcomes, yet patients navigate markedly different pathways to care. Taiwan's NHI provides universal coverage through a government-administered program with standardized fee schedules, reducing financial burden for most patients. In contrast, the U.S. system combines private, employer-based, and government insurance programs, producing significant variation in access and costs. Consequently, patients in multi-payer systems may prioritize financial complexity and administrative burden, while those in single-payer systems may emphasize access and capacity constraints. The central theoretical issue is not only which dimensions matter, but also how system structure determines the composition of perceived quality dimensions—an underexplored question with important policy implications.

Empirical evidence supports these systemic contrasts. Yoon and Cheng (2021), analyzing 1,374 hospitals in  **Taiwan and the United States** , found significant cross-national differences in perceived inpatient care quality, with **U.S. hospitals receiving higher average ratings** and **opposite socioeconomic satisfaction gradients** between the two systems. However, their study relied on structured surveys with predefined dimensions, limiting the discovery of emergent or culturally specific quality indicators. Such limitations are common in traditional instruments like SERVQUAL (Parasuraman et al., 1988) and its healthcare adaptations (Dagger et al., 2007). While these tools ensure measurement consistency, they also constrain expression, impose Western-centric assumptions, and risk cultural or linguistic non-equivalence (Carman, 1990; Harzing, 2006). Moreover, social desirability bias and time lags between instrument design and data collection can obscure evolving patient concerns—particularly in rapidly changing health systems.

The growing availability of online patient reviews (e.g., Google Maps, Yelp) offers a methodological alternative. These unsolicited narratives provide authentic, immediate, large-scale insights into patient experiences (Ranard et al., 2016). They capture spontaneous perceptions, emotional nuance, and cross-cultural variation beyond what structured surveys can reveal. Yet, extracting coherent dimensions from multilingual, unstructured data requires analytical approaches that avoid imposing preconceived frameworks while enabling cross-system comparison.

Three gaps limit current understanding.
First, most studies remain single-country, and cross-national comparisons often employ inconsistent methodologies, impeding direct comparison (Fung et al., 2008). To date, no research has applied identical computational methods to patient-generated data across structurally divergent systems to identify universal versus system-specific service quality dimensions.
Second, Latent Dirichlet Allocation (LDA) (Blei et al., 2003)—a topic modeling technique that uncovers latent themes without researcher bias—remains underutilized in healthcare research and is rarely applied across languages. No prior study has systematically compared Chinese and English hospital reviews using LDA for cross-lingual semantic mapping.
Third, service quality theory still grapples with whether perceived quality is universal or context-dependent (Brady & Cronin, 2001). We lack empirical evidence quantifying the proportion of patient-perceived dimensions that transcend national boundaries versus those shaped by system structures or cultural values.

To address these gaps, this study conducts a comparative analysis of online hospital reviews from Taiwan and the United States. We ask:
(1) Which service quality dimensions emerge from hospital reviews in each country when analyzed using identical unsupervised methods?
(2) Which dimensions are universal versus country-specific?
(3) Through what mechanisms do system structures and cultural contexts shape these differences?

We analyze 5,007 reviews from 26 Taiwanese medical centers and 3,240 reviews from 28 U.S. hospitals, applying LDA topic modeling and cross-lingual semantic mapping to identify and compare quality dimensions. This design enables quantification of universal versus system-specific concerns and exploration of how institutional and cultural factors influence patient discourse.

The remainder of this paper proceeds as follows. Section 2 reviews literature on service quality theory, cross-cultural healthcare comparisons, online review analysis, and topic modeling. Section 3 details data collection, preprocessing, and modeling procedures. Section 4 presents results identifying universal and system-specific dimensions and their statistical significance. Section 5 concludes with theoretical, methodological, and policy implications, as well as directions for future research.

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

Yoon, G.H., & Cheng, S.H. (2021). Differences in trends of perceived inpatient care quality based on regional socioeconomic level in the United States and Taiwan. *Health Services Research*, 56(6), 1182-1193. https://doi.org/10.1111/1475-6773.13872

---

**版本資訊**：
- 生成日期：2025-11-12
- 來源：ChatGPT GPTS
- 修訂日期：2025-11-12 (Claude Code 修正邏輯錯誤並補充參考文獻)
- 特色：符合 SSCI 期刊學術寫作風格
