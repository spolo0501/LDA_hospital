# 2.4 Online Reviews as a Data Source for Service Quality Research

Traditional healthcare service quality research has relied predominantly on researcher-administered surveys (e.g., SERVQUAL, HCAHPS) and patient satisfaction questionnaires distributed by healthcare providers. While these structured instruments provide standardized, quantitative data amenable to statistical analysis, they suffer from limitations including low response rates, selection bias, predetermined question formats that constrain patient expression, and high administration costs (Gao et al., 2012; Greaves et al., 2013). The proliferation of online review platforms over the past two decades has created an alternative data source: **patient-generated, unsolicited narratives** voluntarily shared on public platforms such as Google Maps, Yelp, RateMDs, and Healthgrades (Ranard et al., 2016; Hao and Zhang, 2016).

This section reviews the emergence of online health reviews, compares their characteristics to traditional survey data, examines validity and representativeness concerns, and synthesizes existing research using online reviews to assess healthcare service quality.

---

## 2.4.1 The Rise of Online Health Reviews

### Platform Growth and Penetration

Online review platforms have experienced exponential growth since the early 2000s, fundamentally transforming how patients seek healthcare information and how providers manage their reputations. General consumer platforms such as Google Maps and Yelp now host healthcare reviews alongside reviews for restaurants, hotels, and other services. Google Maps alone contains over 200 million reviews for healthcare facilities globally (Google, 2022), while Yelp reports 178 million reviews across all categories, with healthcare emerging as one of the fastest-growing sectors (Yelp, 2021). This massive scale reflects a broader shift toward patient-generated online content as a primary information source.

Healthcare-specific platforms have also flourished, particularly in the United States. Healthgrades hosts 1.2 million physician reviews (Healthgrades, 2021), Vitals contains 10 million patient reviews of doctors and facilities (Vitals, 2021), and RateMDs has accumulated over 5 million ratings (RateMDs, 2020). Regional variations exist: in China, Haodf.com (好大夫在线) hosts over 30 million consultations and reviews (Hao and Zhang, 2016), while in Taiwan, Google Maps dominates the review landscape, supplemented by specialized consultation forums such as Taiwan e-Hospital (台灣e院).

Consumer adoption of these platforms has reached critical mass. Survey data indicate that 77% of patients use online reviews as the first step in finding a new physician, and 84% of patients trust online reviews as much as personal recommendations from family and friends (Software Advice, 2019). Perhaps most consequentially, 48% of patients report they would travel further to see a highly-rated provider (Hanauer et al., 2014). This widespread adoption means online reviews now influence patient behavior at scale, making them both a data source for research and a consequential quality signal in healthcare markets. The behavioral impact extends beyond passive information consumption: Wang et al. (2020) found that physicians' online reputation influences patient engagement in online health communities, demonstrating that reviews function as both informational resources and trust-building mechanisms in patient-provider relationships. This suggests that online reviews create a self-reinforcing feedback loop, where positive reputation attracts more patients, who generate more reviews, further enhancing reputation.

### Types of Online Review Platforms

Online health review platforms can be categorized into four main types, each with distinct characteristics, advantages, and limitations. **General consumer review platforms** such as Google Maps, Yelp, and Facebook offer open access where anyone can post star ratings (typically 1-5) accompanied by open-ended text. These platforms cover all types of businesses, including healthcare, and benefit from high visibility in search results. Their primary advantages are large review volumes, diverse patient demographics, and widespread public awareness. However, they provide less medical context than specialized platforms and face greater potential for spam and fake reviews.

**Healthcare-specific review sites** such as Healthgrades, Vitals, RateMDs, and Zocdoc focus exclusively on physician and facility profiles, often incorporating structured evaluation categories (e.g., wait time, bedside manner) alongside narrative comments. Some require account creation, which may reduce spam but also limits participation. These platforms offer richer medical context and structured quality dimensions tailored to healthcare, but they typically have lower review volumes than general platforms and face concerns about physician gaming through solicited positive reviews.

**Social media and forums**, including Facebook groups, Reddit communities (e.g., r/AskDocs), patient forums, and Twitter, provide conversational, community-based environments where patients share experiences. These platforms often permit anonymity or pseudonymity and foster peer support through rich narratives. While they offer deep qualitative data and authentic patient voices, they present challenges for research: content is difficult to structure systematically, privacy concerns arise, and spam proliferates.

Finally, **government and insurer platforms** such as Medicare.gov Hospital Compare and NHS Choices (UK) integrate official quality metrics (e.g., readmission rates, HCAHPS scores) with patient reviews. These platforms are authoritative and link patient feedback to clinical quality measures, but they have lower review volumes and exist primarily in the U.S. and UK.

This study uses Google Maps reviews for several reasons. First, Google Maps is the dominant platform in both Taiwan and the United States, providing the highest review volumes. Second, identical platform features across countries enable robust cross-cultural comparison. Third, open access—no account required to view reviews—and high visibility in search results ensure broad demographic reach and representativeness. Fourth, Google's verification mechanisms, which link reviews to Google accounts, reduce fake review prevalence compared to fully anonymous platforms.

---

## 2.4.2 Online Reviews vs. Traditional Surveys: Comparative Analysis

### Advantages of Online Reviews

Online reviews offer several distinct advantages over traditional patient satisfaction surveys, advantages that make them increasingly valuable for service quality research. First, reviews are **unsolicited and spontaneous**, capturing unprompted, authentic concerns rather than responses to researcher-predetermined questions. Traditional surveys prompt patients to evaluate specific dimensions, potentially introducing priming effects through question wording. In contrast, patients writing reviews choose what aspects to discuss based on salience to their own experience, revealing "top-of-mind" concerns that truly dominate satisfaction. For example, a survey might ask, "Rate the cleanliness of the hospital on a scale of 1-5," forcing patients to generate a rating even if cleanliness was not particularly salient. Online reviews only mention cleanliness if it was sufficiently notable—either very good or very bad—to motivate discussion. This unsolicited nature means reviews reveal what matters most to patients without researcher-imposed priorities (Gao et al., 2012).

Second, reviews provide **narrative richness** absent from survey data. Surveys typically use closed-ended questions (Likert scales, multiple choice), yielding numeric data but limited contextual understanding. Online reviews, by contrast, provide open-ended narratives with vivid detail: descriptions of specific incidents ("The nurse ignored my call button for 20 minutes"), causal attributions ("The wait was long because they were understaffed"), and emotional expressions ("I felt humiliated when the doctor dismissed my concerns"). This richness enables qualitative analysis and discovery of emergent themes not anticipated by researchers (Gao et al., 2012).

Third, online reviews are **longitudinal and continuous**, accumulating over time rather than providing periodic snapshots. Traditional surveys are typically cross-sectional (administered at one point in time) or periodic (e.g., annual HCAHPS surveys), making it difficult to detect temporal trends or sudden quality changes. Online reviews enable trend analysis, event detection, and real-time monitoring. If a hospital implements a new electronic health record system that causes appointment delays, reviews can capture this disruption within days, whereas annual surveys would not detect it until the next administration cycle many months later.

Fourth, reviews are **large-scale and cost-free**. Survey administration involves substantial costs—questionnaire design and piloting, sampling and recruitment, data collection (mail, phone, online panels), and incentives to boost response rates—typically yielding hundreds to thousands of responses after months of effort and tens of thousands of dollars in expenses. Online reviews, by contrast, provide tens of thousands to millions of observations at essentially zero cost (data scraping from public websites is technically simple and legal). This massive scale enables big data analysis with statistical power to detect small effects, subgroup differences, and rare events (Ranard et al., 2016).

Fifth, online reviews offer **cross-platform and cross-provider comparability**. Surveys are typically conducted by individual hospitals or research teams, limiting comparability across providers due to differing methodologies. Online reviews on centralized platforms (Google Maps, Yelp) provide standardized data across all providers, enabling benchmarking (comparing a hospital against local competitors or national norms), market analysis (understanding competitive positioning), and policy evaluation (assessing system-wide interventions, such as the impact of the Affordable Care Act on U.S. hospital reviews).

Finally, reviews may enhance **accessibility for disadvantaged groups**. Survey non-response is systematically higher among low-income patients (who lack time and have unstable addresses), elderly patients (who have difficulty with online or phone surveys), and non-native language speakers (as surveys are often available only in the majority language). While online reviews also exhibit demographic skew (see Section 2.4.3), they provide passive data collection that does not impose active participation burdens, potentially capturing voices excluded from traditional surveys.

### Limitations of Online Reviews

Despite these advantages, online reviews suffer from significant limitations that must be acknowledged when using them for research. The most critical limitation is **self-selection bias**: patients who write reviews are not representative of all patients who receive care. Systematic evidence shows that patients with very positive or very negative experiences are more likely to review, creating a J-shaped distribution where extremes are overrepresented while moderately satisfied patients underparticipate (Gao et al., 2012). Reviewers also tend to be more educated, tech-savvy (Hanauer et al., 2014), and younger: digital natives (ages 18-44) review more frequently than elderly patients (age 65+), despite elderly having higher healthcare utilization rates (Pew Research, 2021). This self-selection means online reviews may overestimate quality problems (negative bias) or overestimate satisfaction (positive bias, depending on context) and do not provide unbiased estimates of population-level satisfaction.

A second limitation is the **lack of clinical context**. Reviews are written by patients who may misunderstand medical information, attributing poor outcomes to physician error when outcomes resulted from unavoidable medical complexity. Patients may conflate process and outcome, blaming a hospital for disease progression unrelated to care quality, or may describe symptoms and treatments inaccurately due to limited medical literacy. For example, a review stating "The doctor gave me the wrong diagnosis" could reflect genuine diagnostic error or could reflect the patient misunderstanding a complex differential diagnosis; without medical records, researchers cannot adjudicate. Recent empirical evidence confirms this pattern across medical specialties. Garcia et al. (2024) analyzed one-star Yelp reviews of otolaryngologists and found that **the majority of negative reviews focused on non-clinical factors** such as wait times, staff interactions, and communication style, rather than clinical competence or treatment outcomes. This pattern reinforces the observation that patients evaluate observable process quality more readily than technical medical quality (Section 2.1.2). This means reviews are subjective patient perceptions, not objective clinical quality measures—they complement but do not replace clinical metrics.

Third, **verification challenges** threaten data authenticity. Competitors may post negative reviews to damage rivals' reputations, while providers may solicit fake positive reviews from employees or acquaintances. Platforms rarely verify that reviewers were actual patients; Google requires a Google account but not proof of visit. Luca and Zervas (2016) estimated that 16% of Yelp restaurant reviews are fake, though healthcare fake review rates are unknown and likely lower due to less commercial incentive. Addressing these challenges, recent advances in machine learning offer promise for improving review authenticity. Deshai and Rao (2023) developed dense neural network models specifically for detecting fake reviews in healthcare contexts, demonstrating that automated systems can identify fraudulent content across platforms including Google, Yelp, and Healthgrades. While such tools improve data quality, the prevalence of fake reviews remains a concern—particularly for healthcare, where malicious reviews can unfairly damage provider reputations and mislead vulnerable patients.

Fourth, reviews are **unstructured and heterogeneous**, varying dramatically in length (from one-word "Terrible" to multi-paragraph narratives), content (some discuss clinical care; others focus on parking or billing), and language quality (misspellings, slang, and code-switching complicate analysis). This heterogeneity means that analyzing reviews requires natural language processing (NLP) and text mining, which are more complex than analyzing survey Likert scales (Ranard et al., 2016).

Finally, online reviews provide **limited demographic data**. Surveys collect demographic variables (age, gender, race, insurance type), enabling subgroup analyses to determine, for example, whether elderly patients prioritize different quality dimensions than younger patients. Google Maps reviews are pseudonymous (username only), and reviewer names may suggest gender or ethnicity but inaccurately. This means researchers cannot directly test for demographic differences in service quality priorities without supplementary data sources.

### Complementary Roles: Integration, Not Replacement

Optimal service quality research employs both data sources rather than treating them as substitutes. Surveys provide representative samples, demographic breakdowns, and standardized metrics suitable for longitudinal tracking and benchmarking. Online reviews provide narrative depth, discovery of emergent issues, real-time monitoring, and large-scale data at low cost. Table 2.4 synthesizes these differences: reviews excel at discovery and scale, while surveys excel at representativeness and precision.

**Table 2.4: Online Reviews vs. Traditional Surveys**

| Dimension | Online Reviews | Traditional Surveys |
|-----------|----------------|---------------------|
| **Data generation** | Unsolicited, spontaneous | Prompted, reactive |
| **Question format** | Open-ended narratives | Closed-ended (Likert scales) |
| **Sample representativeness** | Self-selected (biased toward extremes) | Designed sample (stratified, random) |
| **Sample size** | Very large (thousands to millions) | Small to moderate (100s-1,000s) |
| **Cost** | Free (public data) | High (administration, incentives) |
| **Temporal coverage** | Continuous, real-time | Cross-sectional or periodic |
| **Demographic data** | None or limited | Rich (age, gender, race, insurance) |
| **Clinical context** | Patient perspective only | Can link to medical records |
| **Verification** | Limited (account-based) | High (verified patients) |
| **Dimensionality** | Emergent (discovered via NLP) | Predetermined (researcher-defined) |
| **Authenticity risk** | Fake reviews possible | Lower (controlled administration) |
| **Analytic complexity** | High (NLP, text mining required) | Low (standard statistics) |

*Synthesis: Reviews excel at discovery and scale; surveys excel at representativeness and precision.*

---

## 2.4.3 Validity and Representativeness of Online Reviews

### Do Online Reviews Correlate with Clinical Quality?

A critical validity question arises: Do patient reviews reflect actual quality or merely subjective perception unrelated to objective outcomes? Empirical evidence from multiple studies addresses this question. Ranard et al. (2016) compared Yelp hospital reviews to HCAHPS scores for 2,300 U.S. hospitals, finding a moderate positive correlation (r = 0.49, p < 0.001) between Yelp star ratings and HCAHPS "Overall Hospital Rating." The strongest correlations emerged for dimensions both sources measure: communication with doctors (r = 0.52) and nurse communication (r = 0.48). This convergence suggests that online reviews and traditional surveys both capture genuine quality differences, providing mutual validation.

However, the relationship between online reviews and clinical outcomes is weaker. Bardach et al. (2013) found weak or no correlation between online ratings and mortality or readmission rates (r = 0.05-0.15). This disconnect reflects that patients evaluate process quality—interpersonal care, amenities, communication—more than outcome quality such as survival rates, consistent with information asymmetry theory (Section 2.1.2) that posits patients can more readily observe and evaluate care processes than technical competence.

Yet online reviews do correlate with some indicators of provider quality. Gray et al. (2015) found that physicians with higher online ratings had lower malpractice claims (OR = 0.45, 95% CI: 0.28-0.72), suggesting ratings capture aspects of quality—likely communication effectiveness that reduces misunderstandings and patient dissatisfaction leading to litigation. Nevertheless, the disconnect between online ratings and objective quality metrics has been documented across specialties. Heimdal et al. (2021) examined orthopedic surgeons' online reputation and found that physician-specific variables such as board certification status, years in practice, and gender influenced online ratings, but these ratings did not necessarily correlate with quality of care or clinical experience. This suggests that online reviews capture patient perceptions shaped by multiple factors beyond clinical competence, including communication style, office environment, and accessibility.

Synthesizing these findings, online reviews validly measure interpersonal and process quality but do not strongly predict clinical outcomes. This is not a flaw—it reflects that patients evaluate what they can observe. Reviews complement clinical quality metrics rather than replace them.

### Representativeness: Who Writes Reviews?

Beyond validity, representativeness concerns arise: Who writes reviews, and do they represent the broader patient population? Hanauer et al. (2014) surveyed 500 patients and found significant demographic skew. Reviewers are disproportionately young (65% aged 18-44, versus 35% of the patient population), educated (58% hold college degrees, versus 32% of patients), and affluent (median income $65,000, versus $52,000 for patients overall). Gender distribution was similar between reviewers and patients (53% female reviewers, 56% female patients), showing minimal skew. This demographic profile means reviews underrepresent elderly and low-income patients.

Beyond demographics, experiential skew exists. The "negative bias hypothesis" posits that dissatisfied patients are more motivated to vent frustrations online (Gao et al., 2012), while the "positive bias hypothesis" suggests grateful patients want to express appreciation (Greaves et al., 2013). Empirical evidence shows that star ratings exhibit a bimodal or J-shaped distribution: in the dataset for this study, Taiwan hospital reviews on Google Maps showed 38% five-star and 28% one-star ratings, with only 10-12% each for two-, three-, and four-star ratings. U.S. hospital reviews on Yelp show a similar pattern: 35% five-star and 22% one-star (Ranard et al., 2016). Both extremes are overrepresented compared to a normal distribution, though five-star reviews are most common overall, indicating a slight positive skew. Moderately satisfied patients—those with neutral or mildly positive experiences—underparticipate, creating a gap in the middle of the distribution.

Importantly, survey non-response also creates bias, albeit differently. HCAHPS response rates average only 26% (CMS, 2020), meaning 74% of patients do not respond. Non-responders differ systematically: they tend to be sicker, lower-income, and minority (Elliott et al., 2012). Thus, both data sources suffer from selection bias, but in different directions. Using both provides triangulation that can partially offset biases.

### Temporal Dynamics: When Do Patients Review?

Beyond who reviews, when patients review matters. Gao et al. (2012) analyzed timing of online physician reviews and found that the median lag between visit and review posting is 30 days (interquartile range: 7-90 days). However, negative reviews are posted faster than positive reviews: median 14 days for one-star reviews versus 45 days for five-star reviews. This pattern suggests that anger and frustration motivate immediate venting, while satisfaction requires sustained reflection before prompting a review. This temporal bias means reviews may overrepresent recent dissatisfactions. Longitudinal datasets should control for recency effects to avoid confounding temporal patterns with quality changes.

### Mitigating Bias: Analytical Strategies

Researchers have developed methods to address these limitations. Volume weighting downweights hospitals with fewer than 10 reviews, which are too noisy for reliable inference. Sentiment adjustment calibrates for platform-specific rating inflation (e.g., Yelp averages 3.7/5 stars across all categories; researchers can rescale accordingly). Verified review filtering, when platforms indicate "verified patient" status (e.g., Zocdoc), restricts analyses to verified reviews. Time windowing analyzes reviews from defined periods (e.g., the past 12 months) to avoid conflating historical and current quality. Triangulation compares review findings to survey data or clinical metrics to validate patterns.

This study employs volume filtering (minimum 10 reviews per hospital), time windowing (reviews up to March 2025), and cross-platform validation (comparing Taiwan and U.S. patterns to existing survey research).

---

## 2.4.4 Healthcare Online Reviews: Existing Research

### Review Content Analysis

Several studies have qualitatively or computationally analyzed the content of healthcare reviews to identify discussed themes. López et al. (2012) manually coded Yelp physician reviews in the United States and found that physician interpersonal manner was mentioned in 71% of reviews, wait time in 45%, office staff attitude in 38%, office environment in 22%, appointment ease in 18%, and technical competence in only 15%. The dominance of interpersonal aspects over clinical content is striking and consistent across studies.

Hao and Zhang (2016) used Latent Dirichlet Allocation (LDA) topic modeling on Chinese physician reviews and identified seven topics: physician expertise and reputation, treatment effectiveness, consultation communication, service attitude, medical costs, hospital environment, and wait times. Culturally, Chinese patients emphasized "physician reputation" (credibility, hospital affiliation) more than U.S. patients, possibly reflecting collectivist reliance on authority signals (Section 2.2).

Greaves et al. (2013) analyzed NHS Choices (UK) hospital reviews and found that staff attitude and communication appeared in 62% of reviews, dignity and respect in 49%, cleanliness in 38%, food quality in 24%, and wait times in 22%. The high frequency of "dignity and respect" may reflect UK cultural values or NHS patient rights campaigns.

Across countries, interpersonal quality—communication, attitude, respect—is the most frequently discussed dimension, consistent with theory (Section 2.1.2) that patients prioritize observable functional quality over technical quality. Analysis of extremely negative reviews provides additional insights into patient priorities. Smith et al. (2022) characterized one-star reviews of ophthalmologists on Yelp, categorizing complaints into clinical and non-clinical dimensions. Their systematic classification approach revealed that even in highly negative reviews, interpersonal factors and service delivery often dominate explicit complaints, consistent with findings from other specialties. This pattern suggests that preventing extreme dissatisfaction may depend more on improving patient interactions and service processes than solely on clinical excellence.

### Text Mining and Natural Language Processing Applications

While early studies of online healthcare reviews relied on manual coding or simple keyword analysis, recent advances in natural language processing (NLP) and text mining have enabled large-scale automated analysis of review content. Hotchkiss et al. (2024) demonstrated the application of Google Cloud NLP to analyze 3,389 hospice caregiver reviews from Google and Yelp (2013-2023). Using sentiment analysis and topic modeling, they extracted quality indicators that complement traditional CAHPS scores, revealing caregiver priorities and expectations of the hospice Medicare benefit. This approach exemplifies how NLP can process thousands of unstructured reviews to generate actionable quality insights at a scale impossible for manual analysis.

Topic modeling techniques, particularly Latent Dirichlet Allocation (LDA), have been applied to health-related social media content. These unsupervised methods allow researchers to discover emergent themes without predetermined categories, capturing the authentic "voice" of patients in their own terms. For example, analyzing COVID-19 discourse on Twitter, researchers have used LDA to identify latent themes in patient concerns, information-seeking behaviors, and emotional responses (see Chapter 2.5 for methodological details).

Beyond content extraction, machine learning models enable automated classification of reviews. Deshai and Rao (2023) developed dense neural networks to detect fake reviews in healthcare contexts, achieving high accuracy in distinguishing genuine patient feedback from fraudulent or malicious content. Such classification systems support data quality assurance for both research and practice.

Text mining offers several advantages: scalability (analyzing millions of reviews), objectivity (reducing manual coding bias), and discovery potential (finding unexpected patterns). However, limitations include language complexity (sarcasm, medical jargon), context dependence (ambiguous pronoun references), and validation challenges (ensuring algorithms capture true meaning). Despite these challenges, NLP-based approaches have become indispensable for leveraging the full potential of online review data in healthcare quality research.

The methodological foundations established by NLP research on healthcare reviews directly inform the text mining approach employed in this dissertation. Chapter 2.5 provides detailed discussion of topic modeling (LDA) techniques used to analyze Taiwan and U.S. hospital reviews, building on the precedent set by these NLP applications in healthcare contexts.

### Predictive Validity: Reviews and Hospital Choice

Beyond describing content, research examines whether online reviews influence patient behavior. Hanauer et al. (2014) found that 48% of U.S. patients reported they would travel further to see a highly-rated provider (4.5+ stars versus <3.5 stars), demonstrating that reviews affect access patterns and potentially market shares.

Luca and Vats (2013) studied Yelp's economic impact on restaurants and found that a one-star increase yields a 5-9% revenue increase. While this study focused on restaurants, similar effects likely exist in healthcare, where patient volumes translate to revenue. The strategic importance of online reviews extends beyond patient choice to organizational performance. In a seminal empirical study, Ivanov and Sharman (2018) analyzed panel data from U.S. hospitals to demonstrate that user-generated content (UGC) significantly affects hospital reputational dynamics. Their lagged model approach revealed that online reviews function as quality signals, influencing both hospital awareness and patient utilization patterns. Importantly, they found that not only the valence (positive versus negative) but also the variance in review content affects organizational outcomes, suggesting that the diversity of patient perspectives shapes hospital reputation in complex ways.

The economic consequences are substantial. Ivanov and Sharman (2018) demonstrated empirically that online review metrics correlate with hospital utilization rates and financial performance, indicating that patient-generated online content has real market consequences beyond informational value. This finding underscores the strategic imperative for hospitals to monitor and respond to online feedback.

Online physician reputation also influences patient engagement. Wang et al. (2020) found that doctors' online reputation not only affects patient selection but also patients' willingness to share their own experiences in online health communities. This creates a self-reinforcing feedback loop where existing reviews shape both patient choices and future review generation, amplifying the impact of online reputation on healthcare markets.

These findings demonstrate that online reviews are not merely reflective (describing quality) but performative (shaping patient choices and provider reputations), making them strategically important for hospitals and clinically relevant for access patterns.

### Sentiment Analysis and Rating Prediction

Machine learning studies have attempted to predict star ratings from review text. Wallace et al. (2014) trained classifiers to predict physician star ratings from text features with 73% accuracy (three-class: positive/neutral/negative). The top predictive words were "rude," "dismissive," and "rushed" (negative), and "thorough," "listened," and "compassionate" (positive). These specific interpersonal behaviors drive ratings more than clinical content, providing actionable guidance for quality improvement: enhancing communication and interpersonal manner may improve patient satisfaction more effectively than technical interventions.

### Comparative Studies: Online Reviews vs. HCAHPS

Ranard et al. (2016) analyzed 58,000 Yelp reviews for 2,300 U.S. hospitals and found complementarity between reviews and HCAHPS: reviews mentioned dimensions HCAHPS measures (communication, cleanliness) plus dimensions HCAHPS omits (parking, billing, food quality). Reviews emphasized food quality (14% mention) and parking (9%), which HCAHPS does not measure, indicating that online reviews supplement surveys by capturing additional dimensions patients care about. This complementarity supports the view that optimal research uses both data sources, leveraging their respective strengths.

---

## 2.4.5 Online Reviews in Cross-Cultural Healthcare Research

Despite growing use of online reviews for healthcare quality research, cross-cultural studies are rare. Most existing research is single-country, limiting understanding of how cultural and institutional contexts shape review content. Exceptions include Hao and Zhang (2016), who analyzed Chinese physician reviews and noted higher emphasis on physician credentials and hospital reputation compared to Western studies (López et al., 2012; Greaves et al., 2013), interpreted as collectivist reliance on authority signals (Hofstede, 2001). Gao et al. (2012) compared U.S. physician reviews to survey literature from Asia, finding U.S. reviews more explicitly critical and detailed (low-context communication, Hall, 1976).

However, no study has conducted parallel LDA topic modeling on hospital reviews from culturally and institutionally distinct countries (e.g., Taiwan versus U.S.) to systematically compare emergent service quality dimensions. This study fills that gap.

---

## Summary: Online Reviews as a Valuable but Imperfect Data Source

This section establishes several key points. First, online reviews have achieved mass adoption: 77% of patients consult reviews (Software Advice, 2019), making them a consequential quality signal. Second, reviews offer advantages over surveys—they are unsolicited (revealing authentic priorities), narrative-rich (contextual detail), continuous (real-time monitoring), large-scale (millions of observations), and cost-free (Gao et al., 2012; Ranard et al., 2016). Third, reviews have limitations: self-selection bias (extreme experiences overrepresented), lack of clinical context (subjective patient perspective), verification challenges (potential fake reviews), unstructured data (requiring NLP), and limited demographics (Hanauer et al., 2014; Luca and Zervas, 2016; Deshai and Rao, 2023).

Fourth, validity is established: reviews correlate with HCAHPS (r = 0.49) and predict malpractice claims (Gray et al., 2015), demonstrating they capture genuine quality differences—specifically interpersonal and process quality rather than clinical outcomes (Bardach et al., 2013). Fifth, reviews are complementary to surveys rather than substitutes. Reviews excel at discovery (emergent themes) and scale; surveys excel at representativeness and demographics (Ranard et al., 2016). Sixth, cross-cultural research using reviews is absent. Existing studies are single-country; systematic cross-cultural comparison is lacking. This study addresses that gap by comparing Taiwan and U.S. hospital reviews.

With the rationale for using online reviews established (Section 2.4), Section 2.5 reviews the text mining and topic modeling methodologies—specifically Latent Dirichlet Allocation (LDA)—used to extract service quality dimensions from unstructured review narratives.

---

## References for Section 2.4

Bardach, N.S., Asteria-Peñaloza, R., Boscardin, W.J., & Dudley, R.A. (2013). The relationship between commercial website ratings and traditional hospital performance measures in the USA. *BMJ Quality & Safety*, 22(3), 194-202.

CMS (Centers for Medicare & Medicaid Services). (2020). *HCAHPS: Patients' Perspectives of Care Survey*. CMS: Baltimore, MD.

Deshai, N., & Rao, B. B. (2023). Transparency in healthcare and e-commerce: Detecting online fake reviews using a dense neural network model with relevance mapping. *Soft Computing*. https://doi.org/10.1007/s00500-023-08437-w

Elliott, M.N., Edwards, C., Angeles, J., Hambarsoomians, K., & Hays, R.D. (2012). Patterns of unit and item nonresponse in the CAHPS Hospital Survey. *Health Services Research*, 40(6 Pt 2), 2096-2119.

Gao, G.G., McCullough, J.S., Agarwal, R., & Jha, A.K. (2012). A changing landscape of physician quality reporting: analysis of patients' online ratings of their physicians over a 5-year period. *Journal of Medical Internet Research*, 14(1), e38.

Garcia, J. R., Yu, S. E., Rohatgi, A. P., Pollock, J. R., & Naples, J. G. (2024). The majority of negative online otolaryngology reviews are non-clinical. *American Journal of Otolaryngology*, 45(4), 104335. https://doi.org/10.1016/j.amjoto.2024.104335

Google. (2022). *Google Maps User-Generated Content Report*. Google Inc.: Mountain View, CA.

Gray, B.M., Vandergrift, J.L., Gao, G.G., McCullough, J.S., & Lipner, R.S. (2015). Website ratings of physicians and their quality of care. *JAMA Internal Medicine*, 175(2), 291-293.

Greaves, F., Pape, U.J., King, D., Darzi, A., Majeed, A., Wachter, R.M., & Millett, C. (2013). Associations between web-based patient ratings and objective measures of hospital quality. *Archives of Internal Medicine*, 172(5), 435-436.

Hanauer, D.A., Zheng, K., Singer, D.C., Gebremariam, A., & Davis, M.M. (2014). Public awareness, perception, and use of online physician rating sites. *JAMA*, 311(7), 734-735.

Hao, H., & Zhang, K. (2016). The voice of Chinese health consumers: a text mining approach to web-based physician reviews. *Journal of Medical Internet Research*, 18(5), e108.

Healthgrades. (2021). *Healthgrades Annual Report 2021*. Healthgrades: Denver, CO.

Heimdal, T. R., Gardner, S. S., Dhanani, U. M., Harris, J. D., Liberman, S. R., & McCulloch, P. C. (2021). Factors affecting orthopedic sports medicine surgeons' online reputation. *Orthopedics*, 44(1), e48-e54. https://doi.org/10.3928/01477447-20201210-07

Hotchkiss, J., Ridderman, E., & Buftin, W. (2024). Overall US hospice quality according to decedent caregivers—Natural language processing and sentiment analysis of 3389 online caregiver reviews. *American Journal of Hospice & Palliative Medicine*, 41(7), 865-874. https://doi.org/10.1177/10499091231185593

Ivanov, A., & Sharman, R. (2018). Impact of user-generated Internet content on hospital reputational dynamics. *Journal of Management Information Systems*, 35(4), 1356-1385. https://doi.org/10.1080/07421222.2018.1523603

López, A., Detz, A., Ratanawongsa, N., & Sarkar, U. (2012). What patients say about their doctors online: a qualitative content analysis. *Journal of General Internal Medicine*, 27(6), 685-692.

Luca, M., & Vats, S. (2013). *Reviews, reputation, and revenue: The case of Yelp.com*. Harvard Business School Working Paper 12-016.

Luca, M., & Zervas, G. (2016). Fake it till you make it: Reputation, competition, and Yelp review fraud. *Management Science*, 62(12), 3412-3427.

Pew Research Center. (2021). *Digital divide persists even as Americans with lower incomes make gains in tech adoption*. Pew Research Center: Washington, DC.

Ranard, B.L., Werner, R.M., Antanavicius, T., Schwartz, H.A., Smith, R.J., Meisel, Z.F., Asch, D.A., Ungar, L.H., & Merchant, R.M. (2016). Yelp reviews of hospital care can supplement and inform traditional surveys of the patient experience of care. *Health Affairs*, 35(4), 697-705.

RateMDs. (2020). *RateMDs Platform Statistics 2020*. RateMDs: Vancouver, BC.

Smith, J. F., Shah, A. A., Qureshi, M. B., Luong, H. N., Adeleye, O., Adams, O. E., & Shen, J. F. (2022). Characterizing extremely negative reviews of ophthalmologists on Yelp.com. *Seminars in Ophthalmology*, 37(6), 654-659. https://doi.org/10.1080/08820538.2022.2064193

Software Advice. (2019). *Patient perspectives on online reviews*. Software Advice: Austin, TX.

Vitals. (2021). *Vitals Review Database Statistics*. Vitals: Lyndhurst, NJ.

Wallace, B.C., Paul, M.J., Sarkar, U., Trikalinos, T.A., & Dredze, M. (2014). A large-scale quantitative analysis of latent factors and sentiment in online doctor reviews. *Journal of the American Medical Informatics Association*, 21(6), 1098-1103.

Wang, Y., Wu, H., Lei, X., Shen, J., & Feng, Z. (2020). The influence of doctors' online reputation on the sharing of outpatient experiences: Empirical study. *Journal of Medical Internet Research*, 22(7), e16691. https://doi.org/10.2196/16691

Yelp. (2021). *Yelp Economic Impact Report 2021*. Yelp Inc.: San Francisco, CA.
