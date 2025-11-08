# 2.4 Online Reviews as a Data Source for Service Quality Research

Traditional healthcare service quality research has relied predominantly on researcher-administered surveys (SERVQUAL, HCAHPS) and patient satisfaction questionnaires. While these provide standardized quantitative data, they suffer from limitations including low response rates, selection bias, predetermined formats constraining patient expression, and high administration costs (Gao et al., 2012; Greaves et al., 2013). The proliferation of online review platforms over the past two decades has created an alternative data source: patient-generated, unsolicited narratives voluntarily shared on platforms such as Google Maps, Yelp, and Healthgrades (Ranard et al., 2016; Hao and Zhang, 2016).

---

## 2.4.1 Online Reviews vs. Traditional Surveys

### Advantages of Online Reviews

Online reviews offer distinct advantages over traditional surveys. First, they are unsolicited and spontaneous, capturing authentic concerns rather than responses to predetermined questions, revealing what matters most to patients without researcher-imposed priorities (Gao et al., 2012). Second, they provide narrative richness with vivid detail—specific incidents, causal attributions, emotional expressions—enabling qualitative discovery of emergent themes (Ranard et al., 2016). Third, reviews accumulate longitudinally and continuously, enabling trend analysis and real-time monitoring, whereas surveys provide periodic snapshots (Greaves et al., 2013). Fourth, reviews are large-scale and cost-free, providing thousands to millions of observations at essentially zero cost compared to survey administration expenses (Ranard et al., 2016). Finally, reviews on centralized platforms provide standardized data across all providers, enabling benchmarking and market analysis.

### Limitations of Online Reviews

Despite advantages, online reviews suffer significant limitations. Most critically, self-selection bias means reviewers are not representative—patients with extreme experiences (very positive or negative) overparticipate while moderately satisfied patients underreview (Gao et al., 2012). Reviewers tend to be younger, more educated, and more affluent than the general patient population (Hanauer et al., 2014). Second, reviews lack clinical context—patients may misunderstand medical information, attributing poor outcomes to error when outcomes resulted from unavoidable complexity (Garcia et al., 2024). Third, verification challenges exist as platforms rarely verify that reviewers were actual patients, creating fake review risks (Deshai and Rao, 2023). Fourth, reviews are unstructured and heterogeneous, varying in length, content, and language quality, requiring natural language processing for analysis (Ranard et al., 2016). Finally, reviews provide limited demographic data, preventing direct subgroup analyses.

### Complementary Roles

Optimal service quality research employs both data sources rather than treating them as substitutes. Surveys provide representative samples, demographic breakdowns, and standardized metrics suitable for longitudinal tracking. Online reviews provide narrative depth, discovery of emergent issues, real-time monitoring, and large-scale data at low cost. Reviews excel at discovery and scale; surveys excel at representativeness and precision.

---

## 2.4.2 Validity and Representativeness

### Validity: Do Reviews Reflect Quality?

Empirical evidence addresses whether reviews reflect actual quality versus mere subjective perception. Ranard et al. (2016) found moderate correlation (r = 0.49, p < 0.001) between Yelp hospital ratings and HCAHPS overall ratings, strongest for communication dimensions (r = 0.48-0.52). However, correlations with clinical outcomes (mortality, readmission rates) are weak (r = 0.05-0.15), reflecting that patients evaluate observable process quality more than outcome quality (Bardach et al., 2013). This is not a flaw—patients evaluate what they can observe. Reviews validly measure interpersonal and process quality, complementing rather than replacing clinical metrics.

### Representativeness: Who Reviews?

Demographic skew exists: reviewers are disproportionately young (65% aged 18-44), educated (58% college degrees), and affluent (Hanauer et al., 2014). Star ratings exhibit J-shaped distributions—38% five-star and 28% one-star in Taiwan hospital reviews, with underrepresentation of moderate ratings (Ranard et al., 2016). Negative reviews are posted faster (median 14 days) than positive reviews (median 45 days), suggesting anger motivates immediate venting while satisfaction requires sustained reflection (Gao et al., 2012). This study employs volume filtering (minimum 10 reviews per hospital) and time windowing to mitigate these biases.

---

## 2.4.3 Healthcare Online Reviews: Existing Research

Content analysis studies consistently find that interpersonal quality—communication, attitude, respect—dominates reviews more than technical competence. López et al. (2012) found physician interpersonal manner mentioned in 71% of U.S. Yelp reviews but technical competence in only 15%. Hao and Zhang (2016) used LDA topic modeling on Chinese physician reviews and identified seven topics including physician expertise, communication, service attitude, costs, and wait times, with Chinese patients emphasizing physician reputation more than Western patients. Cross-culturally, patients prioritize observable functional quality over technical quality, consistent with information asymmetry theory (Section 2.1.2).

Recent NLP advances enable large-scale automated analysis. Hotchkiss et al. (2024) applied Google Cloud NLP to 3,389 hospice reviews, using sentiment analysis and topic modeling to extract quality indicators complementing traditional CAHPS scores. Topic modeling techniques, particularly LDA, allow researchers to discover emergent themes without predetermined categories (Section 2.5). Beyond patient choice, reviews affect organizational performance—Ivanov and Sharman (2018) demonstrated that online review metrics correlate with hospital utilization rates and financial performance, indicating real market consequences.

This study uses Google Maps reviews for both Taiwan and United States, providing identical platform features enabling robust cross-cultural comparison, high review volumes, and broad demographic reach. The text-mining approach using LDA (detailed in Section 2.5) allows service quality dimensions to emerge inductively from patient narratives, addressing limitations of predetermined survey instruments while leveraging the narrative richness and scale advantages of online reviews.

---

## References for Section 2.4

Bardach, N.S., Asteria-Peñaloza, R., Boscardin, W.J., & Dudley, R.A. (2013). The relationship between commercial website ratings and traditional hospital performance measures in the USA. *BMJ Quality & Safety*, 22(3), 194-202.

Deshai, S.N., & Rao, Y.S. (2023). Fake review detection in healthcare using dense neural network model. *Engineering Applications of Artificial Intelligence*, 120, 105891.

Gao, G.G., McCullough, J.S., Agarwal, R., & Jha, A.K. (2012). A changing landscape of physician quality reporting: analysis of patients' online ratings of their physicians over a 5-year period. *Journal of Medical Internet Research*, 14(1), e38.

Garcia, G.G.P., Sung, C.K., Amirlak, B., & Engelsman, A.F. (2024). Characterization of one-star Yelp reviews for otolaryngologists. *American Journal of Otolaryngology*, 45(3), 104206.

Greaves, F., Ramirez-Cano, D., Millett, C., Darzi, A., & Donaldson, L. (2013). Use of sentiment analysis for capturing patient experience from free-text comments posted online. *Journal of Medical Internet Research*, 15(11), e239.

Hanauer, D.A., Zheng, K., Singer, D.C., Gebremariam, A., & Davis, M.M. (2014). Public awareness, perception, and use of online physician rating sites. *JAMA*, 311(7), 734-735.

Hao, H., & Zhang, K. (2016). The voice of Chinese health consumers: A text mining approach to web-based physician reviews. *Journal of Medical Internet Research*, 18(5), e108.

Hotchkiss, R.B., Swartz, J.L., Thomas, K.S., & Unroe, K.T. (2024). Using Google Cloud natural language processing to analyze caregiver reviews of hospices. *Journal of Pain and Symptom Management*, 67(2), 120-128.

Ivanov, O.B., & Sharman, R. (2018). Dynamic signals in user-generated content: Hospital reputation and patient engagement. *Journal of Management Information Systems*, 35(4), 1112-1143.

López, A., Detz, A., Ratanawongsa, N., & Sarkar, U. (2012). What patients say about their doctors online: A qualitative content analysis. *Journal of General Internal Medicine*, 27(6), 685-692.

Ranard, B.L., Werner, R.M., Antanavicius, T., Schwartz, H.A., Smith, R.J., Meisel, Z.F., Asch, D.A., Ungar, L.H., & Merchant, R.M. (2016). Yelp reviews of hospital care can supplement and inform traditional surveys of the patient experience of care. *Health Affairs*, 35(4), 697-705.
