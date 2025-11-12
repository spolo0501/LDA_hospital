# Chapter 3: Methodology

This chapter describes our research design and analytical procedures for extracting and comparing service quality dimensions from Taiwan and U.S. hospital patient reviews. We employed Latent Dirichlet Allocation (LDA) topic modeling—an unsupervised machine learning approach that discovers latent thematic structures in large text corpora without imposing predetermined categories—to identify quality dimensions as they naturally emerge from patient discourse. Our methodological approach comprises five stages: data collection from Google Maps reviews, Chinese and English text preprocessing, independent LDA modeling for each country, cross-lingual semantic mapping to identify universal versus system-specific dimensions, and statistical hypothesis testing with multi-method validation.

---

## 3.1 Research Design

This study employed a comparative cross-national design analyzing patient-generated online reviews from hospitals in Taiwan and the United States. We selected these two countries for comparison because they represent contrasting healthcare system structures—Taiwan's single-payer National Health Insurance versus the United States' multi-payer, market-based system—while both achieving high healthcare outcomes by international standards. This natural experiment design enables us to isolate the effects of system structure on patient quality priorities while controlling for overall healthcare performance levels.

Our analytical strategy proceeded through distinct stages designed to balance methodological rigor with practical interpretability. Rather than impose predetermined quality dimensions through structured surveys, we adopted an unsupervised, data-driven approach allowing dimensions to emerge organically from patient narratives. This choice addresses a fundamental limitation of cross-cultural service quality research: predetermined instruments may impose etic (researcher-imposed) frameworks that miss emic (culture-specific) priorities (Berry, 1989). By conducting independent topic modeling within each linguistic context before attempting cross-national comparison, we preserved each culture's authentic dimensional structure while enabling systematic semantic mapping to identify convergence and divergence.

The research design required balancing three methodological tensions inherent in cross-cultural text analysis. First, we balanced comparability (using identical analytical methods) with contextual sensitivity (adapting preprocessing to language-specific requirements). Second, we balanced statistical rigor (coherence maximization, perplexity minimization) with semantic interpretability (ensuring topics correspond to substantive quality dimensions). Third, we balanced comprehensiveness (capturing all dimensions mentioned in reviews) with parsimony (selecting interpretable topic numbers). Our solutions to these tensions are detailed in subsequent sections.

---

## 3.2 Data Collection

We collected patient reviews from Google Maps, the dominant online review platform in both Taiwan and the United States. Google Maps offers three methodological advantages over alternative platforms: universal accessibility enabling cross-national comparison without platform-specific biases, mandatory association of reviews with verified hospital locations ensuring data authenticity, and standardized rating structure (1-5 stars) facilitating quantitative comparison across languages and cultures.

### 3.2.1 Taiwan Hospital Selection and Data Collection

For Taiwan, we focused on medical centers—the highest tier in Taiwan's hospital accreditation system. Medical centers provide comprehensive tertiary care including complex surgeries, intensive care, and advanced diagnostics, representing the apex of Taiwan's healthcare quality hierarchy. We identified all 26 medical centers recognized by Taiwan's Ministry of Health and Welfare as of 2024, encompassing major academic medical centers such as National Taiwan University Hospital, Taipei Veterans General Hospital, and Chang Gung Memorial Hospital System facilities. These institutions account for a disproportionate share of complex care delivery and serve as training sites for Taiwan's medical professionals, making them particularly salient for quality assessment.

Data collection occurred in July 2024 using automated web scraping techniques compliant with Google's Terms of Service. For each hospital, we extracted all available Chinese-language reviews containing textual content (excluding star-only ratings). The final Taiwan dataset comprised 5,007 reviews spanning from 2018 to 2024, with review length ranging from brief one-sentence comments to detailed multi-paragraph narratives. The median review length was 47 Chinese characters (approximately 12-15 words in English equivalence). Reviews exhibited substantial rating variance: 32.4% rated 1 star (highly negative), 8.7% rated 2 stars, 7.2% rated 3 stars, 9.1% rated 4 stars, and 42.6% rated 5 stars (highly positive), indicating the dataset captured both positive and negative experiences.

### 3.2.2 U.S. Hospital Selection and Data Collection

For the United States, we selected 28 top-ranked hospitals from the U.S. News & World Report "Best Hospitals" Honor Roll, which evaluates hospitals based on clinical outcomes, patient safety, and care quality across multiple specialties. This selection strategy parallels our Taiwan approach by focusing on elite institutions. Included hospitals represented diverse geographic regions (Northeast, South, Midwest, West) and institutional types (academic medical centers, specialty hospitals, integrated health systems), with prominent examples including Mayo Clinic, Cleveland Clinic, Johns Hopkins Hospital, and Massachusetts General Hospital.

Data collection followed identical procedures as Taiwan, occurring in July 2024. We collected only English-language reviews to maintain linguistic comparability. The final U.S. dataset comprised 3,240 reviews from the same 2018-2024 timeframe. U.S. reviews averaged slightly longer than Taiwan reviews (median 62 words), potentially reflecting cultural differences in communication style (individualistic cultures tend toward more elaborate verbal expression; Hall, 1976). Rating distribution showed 28.6% at 1 star, 7.3% at 2 stars, 8.9% at 3 stars, 13.8% at 4 stars, and 41.4% at 5 stars, exhibiting similar bi-modal distribution as Taiwan with concentration at positive and negative extremes.

### 3.2.3 Ethical Considerations and Data Limitations

All collected reviews were publicly available user-generated content posted voluntarily by patients or family members on a public platform. No personally identifiable information was collected beyond the review text and rating. To protect patient privacy, we do not reproduce full review texts in publications; instead, we provide anonymized excerpts and aggregated statistics. This research was determined exempt from IRB review under 45 CFR 46.104(d)(2) as analysis of publicly available data without individual identification.

We acknowledge three data limitations. First, Google Maps reviewers represent a self-selected sample potentially biased toward younger, more technologically proficient, and more strongly satisfied or dissatisfied patients (extremity bias). However, research suggests online review distributions correlate reasonably with validated patient satisfaction surveys (Ranard et al., 2016). Second, we cannot verify reviewer identity or confirm they were actual patients versus family members or companions. This limitation is inherent to all online review research but is partially mitigated by Google's requirement that reviewers have location history at the reviewed hospital. Third, our focus on elite hospitals limits generalizability to community hospitals or rural facilities, though these top-tier institutions disproportionately influence healthcare quality standards and practices.

---

## 3.3 Text Preprocessing

Rigorous text preprocessing is essential for LDA performance, as topic modeling algorithms are sensitive to noise, stop words, and linguistic artifacts that can distort thematic extraction (Schofield et al., 2017). We developed language-specific preprocessing pipelines that balanced standardization with linguistic authenticity.

### 3.3.1 Chinese Text Preprocessing (Taiwan Reviews)

Chinese text preprocessing required addressing unique linguistic characteristics of written Chinese, which lacks explicit word boundaries and employs complex semantic structures. We implemented preprocessing in five stages using Python with specialized natural language processing libraries (jieba for Chinese word segmentation, ckiptagger for part-of-speech tagging).

First, we performed text cleaning to remove non-textual elements: HTML tags, URLs, email addresses, and non-Chinese characters (numbers, punctuation, English letters). We preserved Chinese punctuation temporarily to aid segmentation accuracy, removing it in later stages. Second, we conducted word segmentation using the jieba library with a custom medical dictionary containing 1,847 healthcare-specific terms (e.g., "急診室" [emergency room], "掛號" [registration], "住院" [hospitalization], "護理師" [nurse]). This custom dictionary prevented segmentation errors that treat multi-character medical terms as separate words, which would obscure medical semantics.

Third, we applied part-of-speech tagging to identify word categories, retaining only nouns, verbs, and adjectives as these word classes carry substantive semantic meaning relevant to service quality dimensions. We removed function words (prepositions, conjunctions, particles) and numerical expressions that contribute little thematic content. Fourth, we filtered stop words using a comprehensive Chinese stop word list (1,893 terms) augmented with domain-specific additions such as "很" (very), "就" (then), "真的" (really), and "覺得" (feel). These high-frequency modifiers appear across all topics, reducing topic distinctiveness without adding semantic value.

Fifth, we constructed custom medical terminology preservation lists to ensure critical healthcare terms survived preprocessing. For example, compound terms like "醫療品質" (medical quality), "服務態度" (service attitude), and "急診室" (emergency room) were preserved as unified tokens rather than segmented into constituent characters. This domain knowledge integration substantially improved topic interpretability by maintaining medical semantic units.

The preprocessing pipeline reduced the Taiwan corpus from 5,007 reviews containing 384,562 total characters to 5,007 documents containing 127,349 meaningful tokens, with an average of 25.4 tokens per review after preprocessing. We validated preprocessing quality through random sampling: two researchers independently reviewed 100 randomly selected preprocessed documents, confirming that medical terms were appropriately preserved, stop words effectively removed, and substantive content retained with 94% agreement.

### 3.3.2 English Text Preprocessing (U.S. Reviews)

English preprocessing followed parallel logic adapted to English linguistic structure. English benefits from explicit word boundaries (spaces) but faces different challenges including verb conjugations, plural forms, and compound word variations that can fragment semantically equivalent terms.

Our English pipeline proceeded through similar stages. First, we converted all text to lowercase to ensure case-insensitive term matching (e.g., "Doctor," "doctor," and "DOCTOR" treated as identical). Second, we removed punctuation, numbers, URLs, email addresses, and non-alphabetic characters, with exceptions for medical abbreviations (e.g., "ER" for emergency room, "ICU" for intensive care unit). Third, we tokenized text into individual words using spaCy, a robust NLP library optimized for English linguistic structure.

Fourth, we removed English stop words (articles, prepositions, pronouns, common verbs like "is," "are," "have") using the standard NLTK stop word list (179 terms) supplemented with review-specific additions such as "hospital," "care," "time," and "patient." While these terms appear relevant to healthcare, their ubiquity across all topics reduces discriminatory power. We preserved certain domain-critical terms that might appear in standard stop lists, such as "pain," "emergency," and "wait," as these carry substantive quality-related meaning.

Fifth, we applied lemmatization using spaCy's lemmatizer to reduce words to their base forms: "nurses" → "nurse," "waited" → "wait," "billing" → "bill." Lemmatization improves topic coherence by consolidating semantically equivalent variants, though we avoided aggressive stemming (which can create semantically ambiguous stems like "car" from both "care" and "caring"). Sixth, we retained only nouns, verbs, and adjectives based on spaCy's part-of-speech tagging, removing adverbs, interjections, and other low-content word classes.

The preprocessing reduced the U.S. corpus from 3,240 reviews containing 201,024 total words to 3,240 documents with 89,472 meaningful tokens, averaging 27.6 tokens per review. Two researchers independently validated 100 randomly selected preprocessed documents, achieving 96% agreement that preprocessing preserved medical semantic content while removing noise.

### 3.3.3 Preprocessing Philosophy: Language-Specific Adaptation

While we employed parallel preprocessing logic for both languages, we deliberately avoided mechanical translation or forcing Chinese text into English structures. Chinese medical discourse exhibits distinct rhetorical patterns—greater use of implicit subjects, higher tolerance for syntactic ambiguity, and more frequent deployment of four-character idioms (成語) conveying culturally specific meanings. Preserving these authentic linguistic patterns ensures that extracted topics reflect genuine Chinese patient priorities rather than Western conceptual impositions translated into Chinese.

Similarly, English reviews exhibited culture-specific patterns such as explicit service recovery narratives ("I complained and they finally..."), direct criticism rare in collectivist cultures ("The nurse was incompetent"), and frequent deployment of superlatives ("absolutely terrible," "incredible experience"). Our preprocessing retained these culturally embedded expression patterns, accepting that perfect cross-linguistic equivalence is neither achievable nor desirable when the goal is capturing authentic cultural priorities.

---

## 3.4 Latent Dirichlet Allocation (LDA) Modeling

Latent Dirichlet Allocation (Blei et al., 2003) is a generative probabilistic model that assumes documents are mixtures of latent topics, where each topic is characterized by a probability distribution over words. Unlike supervised classification which requires predetermined categories, LDA discovers topics inductively from word co-occurrence patterns, making it particularly suited for exploratory identification of service quality dimensions without researcher-imposed frameworks.

### 3.4.1 LDA Conceptual Foundation

LDA operates on a key intuition: documents that discuss similar themes exhibit similar word distributions. For example, reviews discussing emergency care will frequently co-mention words like "emergency," "wait," "hours," and "urgent," while reviews about surgical care co-mention "surgery," "operation," "recovery," and "surgeon." LDA identifies these latent thematic structures by modeling each document as a probabilistic mixture of topics and each topic as a probabilistic distribution over vocabulary.

Formally, LDA assumes the following generative process for each document in a corpus. First, for each document d, draw a topic proportion θ_d from a Dirichlet distribution with parameter α, representing the mixture of topics in that document. Second, for each word position n in document d, draw a topic assignment z_dn from the multinomial distribution θ_d. Third, draw the observed word w_dn from the topic-specific word distribution φ_z parameterized by β. The model's goal is to invert this generative process: given observed words, infer the latent topic structures (φ) and document-topic distributions (θ) that best explain the data.

This probabilistic framework offers three advantages over alternative approaches. First, unlike clustering methods that assign each document to a single category, LDA allows documents to belong partially to multiple topics, reflecting realistic complexity where a single review might discuss both emergency wait times and nursing professionalism. Second, LDA provides interpretable topics through word probability distributions, enabling researchers to understand topics through their characteristic vocabulary rather than opaque mathematical constructs. Third, LDA's Bayesian foundation allows incorporation of prior knowledge through hyperparameter selection while remaining primarily data-driven.

### 3.4.2 Model Implementation and Parameter Selection

We implemented LDA using Python's gensim library (version 4.3.0), which employs variational Bayesian inference for parameter estimation. Hyperparameter selection required balancing computational efficiency, model fit, and semantic interpretability. We set the Dirichlet prior α = 0.1 (encouraging document-topic sparsity, reflecting that most reviews focus on few dimensions) and β = 0.01 (encouraging topic-word sparsity, creating focused topics with distinctive vocabularies). These asymmetric priors prevent topics from collapsing into uniform distributions while remaining weakly informative, allowing data to dominate inference.

For each country's corpus, we trained LDA models with varying topic numbers K ∈ {5, 6, 7, 8, 9, 10} to identify optimal dimensionality. Training employed 50 passes through the corpus with iterative updates every review, ensuring convergence. We configured the model to return the top 20 words per topic ranked by probability for interpretability analysis. All models were trained on standard computational hardware (Intel i7 processor, 16GB RAM), with training times ranging from 12 minutes (K=5) to 28 minutes (K=10) per language.

Critical to reproducibility, we set random seeds (seed=42) to ensure consistent results across runs. LDA's reliance on stochastic initialization can produce different topics across runs, particularly for marginal topics with weak signals. By fixing random seeds and documenting all hyperparameters, we enable exact replication of our results—a practice unfortunately rare in applied LDA research but essential for scientific rigor.

### 3.4.3 Topic Number Selection Framework

Selecting the optimal number of topics K represents the most consequential modeling decision in LDA applications, yet remains contested in the literature (Greene et al., 2014). Statistical metrics (coherence, perplexity) frequently disagree with human interpretability judgments, and different research goals favor different trade-offs. We developed an integrated selection framework balancing four criteria: statistical coherence, model perplexity, semantic interpretability, and theoretical alignment.

**Criterion 1: Topic Coherence**. Coherence quantifies how frequently words within a topic co-occur in the same documents, with higher coherence indicating semantically cohesive topics that humans judge as interpretable (Röder et al., 2015). We calculated C_V coherence scores for each K using gensim's CoherenceModel, which computes normalized pointwise mutual information for top-N words. For Taiwan, coherence peaked at K=5 (C_V = 0.4326) before declining at K=7 (C_V = 0.4175). For the U.S., coherence was highest at K=6 (C_V = 0.4029) versus K=7 (C_V = 0.3891).

**Criterion 2: Model Perplexity**. Perplexity measures how well the model predicts held-out documents, with lower values indicating better fit. We computed perplexity using 10-fold cross-validation. Taiwan models showed monotonic perplexity improvement from K=5 (perplexity = -7.2834) to K=7 (perplexity = -7.5039), suggesting additional topics improved model fit. U.S. models exhibited similar patterns with K=6 (perplexity = -7.2254) performing slightly better than K=7 (perplexity = -7.1983).

**Criterion 3: Semantic Interpretability**. Two healthcare researchers (one with clinical training, one with healthcare management expertise) independently reviewed top-20 keywords and representative reviews for each topic across all K values, rating topics on interpretability (1=unclear amalgam, 5=distinct coherent dimension). We calculated inter-rater agreement using Cohen's κ and reconciled disagreements through discussion. For Taiwan, K=7 received the highest interpretability ratings (mean=4.43, κ=0.81) because it successfully isolated "Facility and Environment Quality" as a distinct dimension from administrative processes, and separated surgical specialty care from general professional quality—distinctions consistent with healthcare service quality theory (Brady & Cronin, 2001). K=5 exhibited high statistical coherence but merged conceptually distinct dimensions, reducing practical utility.

**Criterion 4: Theoretical Alignment**. We evaluated whether extracted topics aligned with established service quality frameworks (SERVQUAL's five dimensions: reliability, responsiveness, assurance, empathy, tangibles; Dagger et al.'s three-level hierarchy: interaction quality, physical environment quality, outcome quality). Models achieving clear mapping to theoretical dimensions received higher scores, as this alignment supports construct validity and facilitates integration with existing literature.

**Final Selection**. For Taiwan, we selected K=7 despite slightly lower coherence than K=5, prioritizing semantic interpretability and theoretical alignment. The seven topics provided clearer separation between emergency care and general professional quality, isolated facility concerns as a distinct dimension, and differentiated inpatient versus outpatient experiences. For the U.S., we selected K=6, which achieved optimal coherence and successfully isolated the theoretically important "Billing and Insurance" dimension while maintaining clear semantic boundaries between other topics.

Importantly, we do not claim K=7 and K=6 are objectively "correct" topic numbers—topic modeling involves irreducible researcher judgment. However, our transparent multi-criteria framework provides methodological justification for these choices and enables readers to evaluate whether alternative topic numbers might yield different theoretical conclusions. We provide coherence and perplexity statistics for K ∈ {5, 6, 7, 8} in Appendix A to support replication attempts.

---

## 3.5 Cross-National Semantic Mapping

With topics extracted independently for Taiwan (K=7) and the U.S. (K=6), we faced the challenge of enabling cross-national comparison while respecting linguistic and cultural differences. Direct topic-to-topic matching risks imposing false equivalence between semantically distinct dimensions. We developed a systematic semantic mapping protocol that identifies genuine conceptual overlaps while preserving culture-specific dimensions.

### 3.5.1 Mapping Methodology

Semantic mapping proceeded through three stages. First, two bilingual researchers (native Chinese speakers fluent in English with healthcare backgrounds) independently reviewed all topics from both countries, examining top-20 keywords, top-15 representative reviews (reviews with topic probability ≥ 0.90), and rating distributions. Researchers created initial conceptual labels in both languages capturing each topic's substantive focus.

Second, researchers independently identified cross-national mappings by assessing semantic similarity on three dimensions: (1) keyword overlap after translation equivalence (e.g., Chinese "醫生" and English "doctor"), (2) thematic content convergence based on representative reviews, and (3) functional equivalence in service quality frameworks (whether topics address the same service quality subdomain). We classified topic pairs as High similarity (>70% thematic overlap, clear conceptual equivalence), Medium similarity (50-70% overlap, substantial but imperfect alignment), or Low similarity (<50% overlap, distinct dimensions).

Third, researchers met to reconcile discrepancies through structured discussion, with disagreements resolved through examination of additional representative reviews and consultation of service quality literature. Initial agreement was 83% (10 of 12 proposed mappings), with all disagreements involving Medium versus Low similarity classifications. Final consensus achieved 100% agreement on four universal dimensions (present in both countries) and four system-specific dimensions (present in only one country).

### 3.5.2 Classification Criteria and Methodological Rationale

The tripartite similarity classification (High/Medium/Low) reflects a crucial methodological principle: statistical significance does not justify cross-national rating comparisons when dimensions measure substantively different constructs. While independent samples t-tests can be computed for any topic pair, valid causal inference requires semantic equivalence (Harkness et al., 2003). For example, Taiwan's "Medical Professional Quality" dimension combines physicians and nurses with emphasis on respect and gratitude, while the U.S. "Nursing Care Quality" dimension isolates nursing with emphasis on responsiveness and staffing ratios. Although both relate to healthcare workers, they measure partially different constructs (different personnel, different evaluative criteria). Comparing their ratings risks attributing differences to culture when they may reflect different referents (physicians versus nurses) or different system factors (staffing levels, professional autonomy).

We therefore limit quantitative rating comparisons to High-similarity dimensions only, using Medium-similarity dimensions for qualitative thematic comparison and Low-similarity dimensions to identify culture-specific or system-specific concerns. This conservative approach strengthens our conclusions by ensuring that statistically significant differences reflect genuine cross-national patterns rather than measurement artifacts.

### 3.5.3 Mapping Results

Our semantic mapping identified four universal dimensions achieving High or Medium similarity: Emergency Care (High similarity—both countries' dimensions centrally address emergency department services, waiting times, and urgent care access), Professional/Nursing Care (Medium similarity—both address healthcare worker competence but with different personnel focus and evaluative emphasis), Outpatient Services (Medium similarity—both involve outpatient care but Taiwan emphasizes administrative processes while U.S. emphasizes clinical quality and appointment access), and Inpatient/Critical Care (Medium similarity—both involve hospitalization but Taiwan addresses routine stays while U.S. focuses on critical care and family support during life-threatening illness).

We also identified four system-specific dimensions appearing in only one country. Taiwan exhibits two unique dimensions: Service Attitude Issues (17.3% of reviews, 1.69 stars)—addressing interpersonal treatment, staff impatience, and perceived rudeness, with no U.S. equivalent standalone dimension—and Facility & Environment Quality (8.1%, 2.73 stars)—addressing parking scarcity, crowding, and cleanliness issues reflecting infrastructure strain from high utilization rates. The United States exhibits two unique dimensions: Billing & Insurance Issues (4.1%, 2.92 stars)—addressing surprise medical bills, insurance coverage denials, and billing errors, entirely absent from Taiwan's single-payer structure—and Overall Positive Experience (9.5%, 3.96 stars)—a distinct praise dimension reflecting American review culture's tendency toward explicit positive endorsements.

The emergence of both universal and system-specific dimensions supports our theoretical framework: core concerns (emergency care, professional competence) transcend system boundaries (universal), while system structure and cultural context shape which additional dimensions achieve salience (contingent). This pattern reconciles apparently contradictory claims in the service quality literature regarding universality versus cultural specificity.

---

## 3.6 Statistical Testing and Hypothesis Validation

With dimensions identified and mapped, we conducted statistical analyses to test cultural and institutional hypotheses and quantify the magnitude of cross-national differences. Our statistical approach balanced rigor (controlling Type I error) with pragmatism (acknowledging the methodological constraints of semantic equivalence).

### 3.6.1 Analytical Strategy

We employed three types of comparisons matched to data structure and semantic validity. First, presence versus absence comparisons identify dimensions that emerge in one country but not the other, providing the clearest evidence of system-specific or culture-specific quality concerns. These comparisons require no statistical testing—the presence or absence of a dimension in a country's topic structure constitutes definitive descriptive evidence. Second, proportion differences compare how frequently patients discuss particular dimensions, quantifying relative salience using chi-square tests for independence. These tests assess whether the proportion of reviews assigned to a dimension differs significantly between countries. Third, rating differences compare patient satisfaction within semantically equivalent dimensions using independent samples t-tests, but only for dimensions achieving High semantic similarity.

This tiered approach acknowledges that while all comparisons are statistically computable, only some are substantively interpretable. We prioritize presence/absence patterns and proportion differences over rating comparisons, using rating differences only when semantic equivalence justifies the comparison.

### 3.6.2 Proportion Comparisons: Chi-Square Tests

To compare dimensional salience, we computed the proportion of reviews predominantly associated with each topic (defined as reviews where that topic achieved the highest probability among all topics for that review). For universal dimensions appearing in both countries, we constructed 2×2 contingency tables (Country × Discussed Topic or Not) and applied chi-square tests of independence to assess whether proportions differed significantly between Taiwan and the United States.

For example, Emergency Care comprised 30.9% of Taiwan reviews (1,546 of 5,007) versus 34.8% of U.S. reviews (1,128 of 3,240). The chi-square test assesses whether this 3.9 percentage point difference exceeds chance variation: χ²(1) = 13.74, p < .001, Cramér's V = 0.041. Despite a small effect size, the large combined sample (N = 8,247) provides sufficient power to detect this genuine cross-national difference, supporting Hypothesis H4 regarding American culture's greater emphasis on efficiency and time consciousness.

We applied Bonferroni correction for multiple comparisons (α = 0.05 / 4 universal dimensions = 0.0125) to control family-wise error rate. All reported proportion differences remained significant after correction, indicating robust patterns rather than capitalization on chance.

### 3.6.3 Rating Comparisons: Independent Samples t-Tests

For rating comparisons, we extracted all reviews predominantly assigned to a particular topic in each country and compared mean ratings using Welch's t-test (which does not assume equal variances). Critically, we limited these comparisons to dimensions achieving High semantic similarity. Only Emergency Care met this threshold, as both countries' dimensions centrally focused on emergency department services and waiting times with >70% thematic overlap.

Emergency Care showed Taiwan mean rating M_TW = 1.79 stars (SD = 1.47, n = 1,546) versus U.S. mean M_US = 3.25 stars (SD = 1.62, n = 1,128). The independent samples t-test yielded t(2672) = 19.97, p < .001, Cohen's d = 0.782 (medium-large effect size). This 1.46-star difference represents a substantively meaningful gap—American patients rate emergency care 81% higher than Taiwanese patients despite both countries showing emergency care concerns. We interpret this gap as reflecting system structure effects: Taiwan's single-payer system removes financial barriers, increasing utilization including non-urgent cases and causing severe overcrowding, while the U.S. multi-payer system's access barriers maintain lower patient volume relative to capacity.

For Medium-similarity dimensions (Professional/Nursing Care, Outpatient Services, Inpatient Care), we computed t-tests for descriptive purposes and report them in Chapter 4's Table 4.3, but we do not use these results for hypothesis testing. As detailed in Section 4.2.3, these dimensions exhibit only Medium semantic similarity due to different personnel focus (Taiwan: physicians+nurses; U.S.: nurses only), different evaluative emphases (Taiwan: gratitude and respect; U.S.: responsiveness and staffing), or different patient populations (Taiwan: routine care; U.S.: critical care). Comparing ratings across these semantically distinct dimensions risks attributing differences to culture or system structure when they may reflect measurement artifacts (different referents, different aspects of care).

### 3.6.4 Effect Size Interpretation

Beyond p-values, we report Cohen's d effect sizes for all rating comparisons to quantify practical significance. We follow standard interpretive conventions: d = 0.2 (small effect), d = 0.5 (medium effect), d = 0.8 (large effect). Our observed effect sizes range from d = 0.512 (Inpatient Care) to d = 0.892 (Professional/Nursing Care), all exceeding medium threshold and several achieving large effect status. These substantial effect sizes indicate that institutional and cultural forces exert powerful, measurable influences on patient satisfaction that transcend random variation or measurement error—lending confidence to our theoretical interpretations.

---

## 3.7 Topic Validation

A critical challenge in LDA applications is ensuring that researcher-assigned topic labels genuinely reflect topic content rather than subjective interpretation (Chang et al., 2009). While LDA discovers topics algorithmically, labeling them (e.g., "Emergency Medical Services," "Billing & Insurance Issues") requires researcher judgment. Without systematic validation, readers cannot assess whether labels accurately capture patient concerns or reflect researcher preconceptions. We addressed this challenge through a multi-method validation approach combining quantitative metrics and qualitative assessment.

### 3.7.1 Representative Text Analysis

For each topic in both countries, we extracted reviews with topic probability ≥ 0.90, identifying reviews that quintessentially represent each dimension. Two researchers (one with clinical background, one with healthcare management expertise) independently reviewed these high-probability texts to confirm substantive alignment with assigned labels. Alignment was assessed binarily: does the review's actual content correspond to the label's semantic meaning? Across both countries' topics (13 topics total: 7 Taiwan, 6 U.S.), alignment rate reached 95% (124 of 130 sampled high-probability reviews), indicating strong content validity.

For example, Taiwan Topic 3 (Service Attitude Issues) exhibited high-probability reviews such as: "護士態度有夠差勁,做什麼都不告知,問了問題也不耐煩" [The nursing staff had terrible attitudes, didn't explain anything, and were impatient when answering questions] (probability = 0.985, rating = 1 star). This negative interpersonal tone aligned precisely with the topic's characteristic keywords ("態度" [attitude], "不耐煩" [impatient], "護士" [nurse]) and the presence of negation markers ("不" [not]), corroborating label validity. Similarly, U.S. Topic 6 (Billing & Insurance Issues) contained reviews like: "Received a surprise bill of $8,000 three months after my procedure. Insurance should have covered this but they refuse. Endless phone calls with billing department led nowhere" (probability = 0.97, rating = 1 star). The review's explicit focus on surprise bills, insurance disputes, and billing department frustrations perfectly matched the assigned label.

Cases of misalignment (5% of high-probability reviews) involved boundary cases where reviews discussed multiple dimensions simultaneously, with the assigned topic capturing only the primary theme. For instance, one Taiwan review assigned to Emergency Care (probability = 0.91) also discussed parking difficulties (Facility dimension), but emergency care clearly dominated the narrative. We consider such cases acceptable given LDA's probabilistic nature—reviews genuinely do address multiple dimensions.

### 3.7.2 Keyword Overlap Analysis

To assess discriminant validity—whether topics represent genuinely distinct dimensions rather than arbitrary subdivisions of a single underlying construct—we calculated pairwise keyword overlap rates using the top-10 keywords per topic. High overlap (>30%) suggests poor differentiation; low overlap (<20%) indicates clear semantic boundaries. Mimno et al. (2011) recommend mean overlap below 20% as a threshold for topic distinction.

For Taiwan's seven topics, mean pairwise overlap was 16.2% (range: 0-30%), meeting the recommended threshold. Topics 2 (Registration & Billing Process) and 3 (Service Attitude Issues) showed zero overlap, indicating perfect discrimination. The highest overlap occurred between Topics 1 (Medical Professional Quality) and 4 (Facility & Environment Quality) at 30%, driven by shared general medical terms ("醫生" [doctor], "醫師" [physician], "沒有" [not have]). However, representative reviews revealed clear semantic distinction: Topic 1 focused on clinical competence and professional expertise, while Topic 4 addressed physical infrastructure (parking, waiting areas, facility cleanliness). This demonstrates that keyword overlap analysis requires interpretation—some overlap from domain-general vocabulary is inevitable and does not invalidate topic distinction if reviews address fundamentally different concerns.

For U.S. topics (six dimensions), mean overlap was 14.8% (range: 0-25%), also below the 20% threshold. Topics 2 (Emergency & Waiting Time) and 6 (Billing & Insurance Issues) exhibited zero overlap despite both reflecting system problems, confirming these represent genuinely distinct dimensions. Highest overlap occurred between Topics 1 (Critical Care & Family Support) and 5 (Overall Positive Experience) at 25%, sharing terms like "care," "staff," and "thank." Yet Topic 1's additional keywords ("dad," "life," "ICU," "surgery") versus Topic 5's superlatives ("great," "best," "excellent") differentiate life-threatening critical care narratives from general praise, validating their separate classification.

These results support discriminant validity: topics capture meaningfully different dimensions rather than arbitrary segmentation. However, we acknowledge some overlap is expected and acceptable given (1) domain-specific vocabulary naturally appearing across contexts (all reviews mention doctors, care, hospitals) and (2) LDA's soft clustering allowing reviews to partially belong to multiple topics.

### 3.7.3 Internal Consistency

We assessed topic coherence through mean topic probability within each topic—the average probability assigned to the dominant topic across all reviews where that topic was dominant. Higher mean probabilities indicate unambiguous topic assignment and strong internal consistency. For Taiwan topics, mean topic probabilities ranged from 0.597 to 0.711, all substantially exceeding the 0.50 threshold for clear assignment. Topic 1 (Medical Professional Quality) showed the highest consistency (0.711), indicating reviews assigned to this topic strongly and unambiguously focused on professional competence. U.S. topics exhibited similar patterns (range: 0.603-0.695), with Topic 5 (Overall Positive Experience) achieving highest consistency (0.695), reflecting clear semantic focus.

Additionally, we examined whether rating variance within topics aligned with expected valence. Topics representing satisfaction dimensions should exhibit high mean ratings with relatively low variance (consistent positivity), while problem dimensions should show low mean ratings with potentially higher variance (varying severity of complaints). Taiwan Topic 1 (Medical Professional Quality, satisfaction dimension) showed mean = 4.67 stars, SD = 1.01 (low variance, consistent positivity). In contrast, Topic 3 (Service Attitude Issues, complaint dimension) showed mean = 1.69 stars, SD = 1.33 (higher variance, consistent negativity with variation in complaint severity). These patterns validate that topics capture dimensions with coherent affective valence rather than random mixtures.

### 3.7.4 Theoretical Alignment

To establish construct validity, we mapped data-driven LDA topics onto established service quality frameworks. We assessed alignment with Parasuraman et al.'s (1988) SERVQUAL five dimensions (Reliability, Responsiveness, Assurance, Empathy, Tangibles) and Dagger et al.'s (2007) three-level healthcare quality hierarchy (Interaction Quality, Physical Environment Quality, Outcome Quality).

For Taiwan's seven topics, we achieved strong theoretical correspondence: Topic 1 (Medical Professional Quality) mapped to SERVQUAL's Assurance dimension and Dagger et al.'s Interaction Quality/Technical subcategory; Topic 2 (Registration & Billing Process) aligned with Responsiveness and Administrative Quality; Topic 3 (Service Attitude Issues) corresponded to Empathy and Interpersonal Quality; Topic 4 (Facility & Environment Quality) matched Tangibles and Physical Environment Quality; Topic 5 (Surgical & Specialty Care) aligned with Assurance and Technical Quality (specialized); Topic 6 (Inpatient Care Experience) mapped to comprehensive Interaction Quality during hospitalization; Topic 7 (Emergency Medical Services) corresponded to Reliability and Responsiveness in acute care contexts. This 7-for-7 correspondence demonstrates that unsupervised LDA recovered dimensions consistent with theory-driven frameworks developed through decades of service quality research.

U.S. topics showed similar alignment: Emergency Care (Responsiveness), Nursing Care Quality (Assurance/Empathy), Outpatient Services (Reliability), Critical Care & Family Support (Assurance/Empathy in critical contexts), Billing & Insurance Issues (Administrative Quality/Responsiveness in financial domains), and Overall Positive Experience (holistic Outcome Quality). Notably, the U.S. Billing & Insurance dimension represents an institutional extension of service quality theory: financial accessibility and transparency as a distinct quality subdomain specific to multi-payer systems.

This strong theoretical alignment provides external validation that LDA extracted substantively meaningful dimensions rather than statistical artifacts. The convergence between data-driven topic modeling and theory-driven instruments supports construct validity and facilitates integration of our findings with existing service quality literature.

### 3.7.5 Validation Summary and Limitations

Table 3.1 summarizes validation results across all metrics. All four validation methods yielded positive results: representative text analysis achieved 95% alignment (exceeding 80% threshold), keyword overlap averaged 16% (below 20% threshold), internal consistency showed mean topic probabilities of 0.60-0.71 (above 0.50 threshold), and theoretical alignment achieved complete mapping to established frameworks. These multiple validation procedures triangulate evidence supporting the robustness and interpretability of our topic labels.

**[Table 3.1: Summary of Validation Metrics]**

| Validation Method | Metric | Taiwan Result | U.S. Result | Threshold | Interpretation |
|-------------------|--------|---------------|-------------|-----------|----------------|
| Representative text analysis | Alignment rate | 95% | 95% | >80% | ✓ High content validity |
| Keyword overlap | Mean overlap | 16.2% | 14.8% | <20% | ✓ Good discrimination |
| Internal consistency | Mean topic probability | 0.597–0.711 | 0.603–0.695 | >0.50 | ✓ Clear assignment |
| Theoretical alignment | Framework mapping | 7/7 topics | 6/6 topics | Majority | ✓ Strong construct validity |

However, we acknowledge validation limitations. First, topic labels required researcher interpretation despite systematic validation—alternative labels (e.g., "Diagnostic Process Quality" instead of "Medical Diagnosis & Examination") might be equally valid. While we validated that labels accurately reflect content, labeling remains inherently subjective. Second, the 30% keyword overlap between some Taiwan topic pairs reflects shared medical terminology (醫生/doctor, 醫師/physician) inherent to domain-specific corpora. Although representative reviews confirmed conceptual distinction, linguistic overlap is unavoidable. Third, we did not conduct formal inter-coder reliability with external expert panels due to resource constraints. Future research should incorporate independent expert validation panels to further strengthen label validity claims.

Despite these limitations, our multi-method validation approach provides substantially stronger evidence for topic validity than the common practice of relying solely on keyword inspection. By triangulating quantitative metrics (coherence, overlap, internal consistency) with qualitative assessment (representative texts, theoretical alignment), we offer a replicable template for validating topic interpretations in future LDA applications.

---

## 3.8 Summary of Methodological Approach

This chapter detailed our five-stage analytical process: (1) collecting 5,007 Taiwan and 3,240 U.S. patient reviews from Google Maps, (2) implementing language-specific preprocessing pipelines preserving medical semantic content, (3) extracting topics via LDA with K=7 for Taiwan and K=6 for U.S. selected through integrated coherence-interpretability-theory criteria, (4) conducting cross-lingual semantic mapping identifying four universal and four system-specific dimensions based on systematic similarity classification, and (5) performing statistical hypothesis testing with presence/absence comparisons, chi-square tests for proportion differences, and t-tests limited to High-similarity dimensions, alongside multi-method topic validation.

Our approach makes three methodological contributions. First, we developed an integrated topic number selection framework balancing statistical optimization with semantic interpretability and theoretical grounding—addressing a persistent gap in applied LDA research. Second, we established a systematic cross-lingual semantic mapping protocol that enables cross-cultural comparison while respecting linguistic differences and avoiding false equivalence. Third, we introduced a conservative statistical testing strategy that limits quantitative comparisons to semantically equivalent dimensions, strengthening causal inferences about cultural and institutional effects.

The next chapter presents findings from this analytical approach, describing extracted quality dimensions for each country, cross-national comparisons revealing universal and system-specific patterns, and statistical hypothesis tests quantifying the magnitude of cultural and institutional influences on patient satisfaction.

---

## References

Berry, J.W. (1989). Imposed etics-emics-derived etics: The operationalization of a compelling idea. *International Journal of Psychology*, 24(6), 721-735.

Blei, D.M., Ng, A.Y., & Jordan, M.I. (2003). Latent Dirichlet allocation. *Journal of Machine Learning Research*, 3, 993-1022.

Brady, M.K., & Cronin, J.J. (2001). Some new thoughts on conceptualizing perceived service quality: A hierarchical approach. *Journal of Marketing*, 65(3), 34-49.

Chang, J., Gerrish, S., Wang, C., Boyd-Graber, J., & Blei, D.M. (2009). Reading tea leaves: How humans interpret topic models. *Advances in Neural Information Processing Systems*, 22, 288-296.

Dagger, T.S., Sweeney, J.C., & Johnson, L.W. (2007). A hierarchical model of health service quality: Scale development and investigation of an integrated model. *Journal of Service Research*, 10(2), 123-142.

Greene, D., O'Callaghan, D., & Cunningham, P. (2014). How many topics? Stability analysis for topic models. In *Proceedings of the European Conference on Machine Learning and Principles and Practice of Knowledge Discovery in Databases* (pp. 498-513). Springer.

Hall, E.T. (1976). *Beyond culture*. Garden City, NY: Anchor Press.

Harkness, J.A., Van de Vijver, F.J.R., & Mohler, P.P. (Eds.). (2003). *Cross-cultural survey methods*. Hoboken, NJ: Wiley.

Mimno, D., Wallach, H., Talley, E., Leenders, M., & McCallum, A. (2011). Optimizing semantic coherence in topic models. *Proceedings of the 2011 Conference on Empirical Methods in Natural Language Processing*, 262-272.

Parasuraman, A., Zeithaml, V.A., & Berry, L.L. (1988). SERVQUAL: A multiple-item scale for measuring consumer perceptions of service quality. *Journal of Retailing*, 64(1), 12-40.

Ranard, B.L., Werner, R.M., Antanavicius, T., Schwartz, H.A., Smith, R.J., Meisel, Z.F., Asch, D.A., Ungar, L.H., & Merchant, R.M. (2016). Yelp reviews of hospital care can supplement and inform traditional surveys of the patient experience of care. *Health Affairs*, 35(4), 697-705.

Röder, M., Both, A., & Hinneburg, A. (2015). Exploring the space of topic coherence measures. *Proceedings of the Eighth ACM International Conference on Web Search and Data Mining*, 399-408.

Schofield, A., Magnusson, M., & Mimno, D. (2017). Pulling out the stops: Rethinking stopword removal for topic models. *Proceedings of the 15th Conference of the European Chapter of the Association for Computational Linguistics*, 2, 432-436.

---

**End of Chapter 3**
