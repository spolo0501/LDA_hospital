# 2.5 Text Mining and Topic Modeling in Service Quality Research

Online reviews provide rich qualitative data at scale, but their unstructured format—free-form text lacking standardized categories—poses analytical challenges. Manual content analysis, while yielding deep insights (López et al., 2012; Greaves et al., 2013), is impractical for datasets exceeding a few hundred reviews. Analyzing thousands or millions of reviews requires **automated text mining** methods that can discover patterns, extract themes, and classify content computationally (Aggarwal and Zhai, 2012).

This section reviews text mining approaches for service quality research, with emphasis on **Latent Dirichlet Allocation (LDA) topic modeling**—the method employed in this study. We discuss LDA's theoretical foundations, practical applications, methodological challenges (particularly determining the number of topics), and its use in cross-cultural research.

---

## 2.5.1 Text Mining Approaches in Service Quality Research

### Overview of Text Mining Methods

Text mining (also called text analytics or natural language processing, NLP) encompasses computational methods for extracting meaningful information from unstructured text (Aggarwal and Zhai, 2012). Key approaches used in service quality research include:

**1. Frequency-Based Methods**

**Approach**: Count word frequencies, identify most common terms, calculate term frequency-inverse document frequency (TF-IDF) to find distinctive words.

**Applications**:
- Identifying which service attributes are most frequently mentioned (Gao et al., 2012)
- Comparing vocabulary across positive vs. negative reviews (Wallace et al., 2014)

**Limitations**:
- **No thematic structure**: Identifies words but not coherent topics
- **Context-insensitive**: "Not good" treated as two separate words (not, good) rather than a negated sentiment
- **Synonym problem**: "Doctor" and "physician" counted separately

**2. Sentiment Analysis**

**Approach**: Classify text as positive, negative, or neutral using:
- **Lexicon-based**: Dictionary of positive/negative words; count occurrences
- **Machine learning**: Train classifiers (Naive Bayes, SVM, neural networks) on labeled data

**Applications**:
- Predicting star ratings from review text (Wallace et al., 2014)
- Tracking sentiment trends over time (Gao et al., 2012)

**Limitations**:
- **Dimensionality reduction**: Collapses multiple service dimensions into single sentiment valence
- **Ignores aspect specificity**: Cannot distinguish satisfaction with doctors vs. nurses

**Recent Advances in Healthcare Sentiment Analysis**

Recent studies demonstrate improved sentiment analysis accuracy when combined with topic modeling. Yazdani et al. (2023) achieved 89-93% accuracy in detecting cancer patients' sentiments toward general services, healthcare services, and life expectancy using Persian-language free-text comments. By integrating topic modeling, they identified that the "metastasis" topic exhibited lower sentiment scores compared to "affable staff" and "chemotherapy" topics, revealing that sentiment varies not just by document but by thematic content within documents.

Nawab et al. (2020) demonstrated NLP's practical utility in extracting meaningful information from Press Ganey patient feedback surveys. With reimbursement increasingly tied to patient experience metrics (e.g., Hospital Consumer Assessment of Healthcare Providers and Systems - HCAHPS), hospitals leverage NLP for scalable, continuous monitoring beyond periodic structured surveys. This real-world implementation highlights NLP's shift from research tool to clinical operations support.

**3. Aspect-Based Sentiment Analysis (ABSA)**

**Approach**: Jointly extract **service aspects** (e.g., wait time, staff attitude) and **sentiment polarity** (positive/negative) for each aspect.

**Example**:
Review: "The doctor was excellent, but the wait time was terrible."
- Aspect 1: Doctor → Sentiment: Positive
- Aspect 2: Wait time → Sentiment: Negative

**Applications**:
- Identifying which aspects receive positive vs. negative evaluations (Liu, 2012)
- Constructing aspect-level ratings from unstructured text

**Limitations**:
- **Aspect lexicon required**: Must predetermine which aspects to extract (or learn them)
- **Complexity**: Requires syntactic parsing (dependency trees) to link aspects to sentiment words

**4. Topic Modeling**

**Approach**: Discover **latent topics** (themes) that probabilistically generate observed text, using unsupervised machine learning (Blei, 2012).

**Most common algorithm**: **Latent Dirichlet Allocation (LDA)** (Blei et al., 2003)

**Applications**:
- Discovering service quality dimensions from reviews **without predefined categories** (Hao and Zhang, 2016)
- Comparing topical content across hospitals, time periods, or countries

**Advantages over other methods**:
- **Unsupervised**: No manual labeling required (unlike supervised sentiment analysis)
- **Multidimensional**: Identifies multiple coexisting topics (unlike simple sentiment)
- **Probabilistic**: Quantifies topic prevalence and word-topic associations
- **Inductive**: Discovers dimensions from data rather than imposing researcher categories

**Recent Methodological Advances**

Text mining methods continue to evolve, particularly in healthcare applications. Sun et al. (2018) provide a comprehensive review of data processing and text mining technologies for electronic medical records (EMR), emphasizing that healthcare texts—characterized by diversity, incompleteness, and redundancy—require rigorous preprocessing before analysis. Named-entity recognition (NER) and relation extraction (RE) form the foundation for advanced text mining applications.

Recent studies demonstrate the value of combining multiple methods. van Buchem et al. (2022) developed the Artificial Intelligence Patient-Reported Experience Measure (AI-PREM), integrating open-ended questionnaires with an NLP pipeline that combines sentiment analysis and topic modeling. Applied to 534 vestibular schwannoma patients, the AI-PREM achieved 90% overlap between automated and manually extracted topics, with sentiment analysis F1 scores of 0.97 for positive and 0.63 for negative texts. The hierarchical visualization—structured by sentiment per question, topics per sentiment, and original responses per topic—enables healthcare professionals to efficiently prioritize patient experience improvements without being confined to closed-ended survey options.

Shah et al. (2021) similarly demonstrated the power of methodological integration. Analyzing 700,000 UK physician reviews from Iwantgreatcare.org using SentiNet (sentiment analysis) combined with LDA, they distinguished patient satisfaction drivers (hospital processes, physician competence) from dissatisfaction drivers (treatment experience, staff manner), achieving 88% F1-score in classification. These integrated approaches outperform single-method strategies, capturing both thematic structure (via LDA) and affective valence (via sentiment analysis).

**Alternative Approaches: Deep Learning for Topic Classification**

While LDA discovers topics unsupervised, supervised deep learning methods offer an alternative when labeled training data is available. Athira et al. (2021) applied BiLSTM with BERT word embeddings to breast cancer forum posts, achieving 79.5% F1-score in detecting seven predefined thematic categories (medication reviews, emotional support, financial concerns). The semi-supervised approach scaled manual annotations to millions of unlabeled posts.

Alhazzani et al. (2023) similarly demonstrated that customized BERT models (PX_BERT) outperform traditional machine learning in patient comment classification. Their 28 classifiers (including BiLSTM, BiGRU, AraBERTv02) achieved high F1-scores, with domain-adapted PX_BERT performing best.

**LDA vs. Deep Learning Trade-offs**:
- **LDA advantages**: Fully unsupervised (no labeled data required), probabilistic interpretation (topic proportions), discovers emergent themes without predefinition
- **Deep Learning advantages**: Higher classification accuracy when labels exist, captures context and word order (BERT), scales to multi-class fine-grained categories
- **Optimal choice**: LDA is ideal for **exploratory research** (discovering unknown dimensions), while deep learning suits **confirmatory classification** (assigning documents to known categories)

**Why LDA is ideal for cross-cultural service quality research**:

1. **No predefined dimensions**: Allows Taiwanese and U.S. reviews to reveal potentially different dimensional structures without forcing them into Western frameworks (SERVQUAL)

2. **Handles multiple languages**: While LDA requires separate preprocessing for Chinese and English, it discovers topics within each language corpus independently, enabling fair comparison

3. **Scalable**: Efficiently processes tens of thousands of reviews (our dataset: 5,007 Taiwan + U.S. reviews)

4. **Interpretability**: Topics are represented as word distributions (top keywords) that domain experts can label and interpret

**This study employs LDA** for these reasons, aligning with recent healthcare review research (Hao and Zhang, 2016; Wallace et al., 2014; Geletta et al., 2019).

---

## 2.5.2 Latent Dirichlet Allocation (LDA): Theoretical Foundations

### The Generative Model

LDA is a **generative probabilistic model** that assumes documents (reviews) are created through the following process (Blei et al., 2003):

**1. Choose a distribution over topics** for the document:
- Each document has a mixture of topics (e.g., 40% Topic 1 [Wait Time], 30% Topic 2 [Staff Attitude], 30% Topic 3 [Clinical Quality])
- This mixture is drawn from a **Dirichlet distribution** with parameter α (controls topic diversity per document)

**2. For each word in the document**:
- Choose a topic from the document's topic distribution (e.g., randomly select Topic 2 with 30% probability)
- Choose a word from that topic's word distribution (e.g., Topic 2 = Staff Attitude might generate "nurse" with 10% probability, "rude" with 5%, etc.)

**Metaphor**:
Think of LDA as modeling a cookbook:
- **Documents = Recipes**: Each recipe (review) is a mixture of cuisines (topics)
- **Topics = Cuisines**: Italian, Chinese, Mexican, etc.
- **Words = Ingredients**: "Tomato" appears frequently in Italian dishes, "soy sauce" in Chinese

A fusion recipe (document) might be 60% Italian, 40% Chinese. When the chef (generative process) writes the recipe, they draw from Italian ingredients 60% of the time and Chinese ingredients 40% of the time.

**LDA infers**:
- What cuisines (topics) exist (based on ingredient co-occurrence patterns)
- What proportion of each cuisine each recipe contains
- Which ingredients are characteristic of each cuisine

### Mathematical Formulation

**Notation**:
- K = number of topics (set by researcher)
- M = number of documents (reviews)
- N = number of words in vocabulary
- α = Dirichlet parameter for document-topic distributions (controls sparsity)
- β = Dirichlet parameter for topic-word distributions (controls sparsity)
- θ_d = topic distribution for document d (K-dimensional vector)
- φ_k = word distribution for topic k (N-dimensional vector)
- z_{dn} = topic assignment for word n in document d
- w_{dn} = observed word n in document d

**Generative process**:

For each topic k ∈ {1,...,K}:
- Draw word distribution φ_k ~ Dirichlet(β)

For each document d ∈ {1,...,M}:
- Draw topic distribution θ_d ~ Dirichlet(α)
- For each word position n ∈ {1,...,N_d}:
  - Draw topic z_{dn} ~ Multinomial(θ_d)
  - Draw word w_{dn} ~ Multinomial(φ_{z_{dn}})

**Inference goal**: Given observed words W = {w_{dn}}, infer hidden variables θ (document-topic distributions), φ (topic-word distributions), and Z (topic assignments).

**Inference algorithms**:
- **Variational Bayes** (Blei et al., 2003): Approximates posterior distributions
- **Gibbs sampling** (Griffiths and Steyvers, 2004): Markov Chain Monte Carlo (MCMC) sampling
- **Gensim library** (used in this study): Implements variational inference

### Model Parameters

**Two key hyperparameters** control LDA behavior:

**α (alpha): Document-topic concentration**
- **Low α (e.g., 0.01)**: Documents are sparse over topics (each document focuses on few topics)
- **High α (e.g., 1.0)**: Documents are dense over topics (each document mixes many topics)
- **"symmetric"** (Gensim default): α = 1/K (equal prior probability for all topics)

**For reviews**: Low α is typical because each review usually discusses 1-3 topics, not all topics.

**β (beta/eta): Topic-word concentration**
- **Low β**: Topics are sparse over words (each topic characterized by few words)
- **High β**: Topics are dense over words (each topic uses many words)
- **"auto"** (Gensim): Learns β from data

**This study uses**: α = symmetric, β = auto (following Hao and Zhang, 2016).

**Other parameters**:
- **Iterations**: Number of training passes through data (this study: 100)
- **Passes**: Number of epochs (this study: 10)
- **Random state**: Seed for reproducibility (this study: 42)

---

## 2.5.3 LDA in Healthcare Service Quality Research

### Existing Applications

LDA has been applied to healthcare reviews and clinical texts:

**Hao and Zhang (2016): Chinese physician reviews**
- **Data**: 59,000 reviews from Haodf.com (China)
- **Method**: LDA with K = 7 topics (selected by coherence score)
- **Topics identified**:
  1. Physician expertise and reputation
  2. Treatment effectiveness
  3. Consultation communication
  4. Service attitude
  5. Medical costs
  6. Hospital environment
  7. Wait times
- **Contribution**: Demonstrated LDA can discover service quality dimensions without predefined categories; findings aligned with but extended SERVQUAL

**Wallace et al. (2014): U.S. physician reviews**
- **Data**: 58,000 RateMDs reviews (U.S.)
- **Method**: LDA + supervised learning to predict ratings
- **Topics identified**: 10 topics including interpersonal manner, technical competence, wait time, office staff, billing
- **Finding**: Topic proportions strongly predicted star ratings (R² = 0.68)

**Doing-Harris and Zeng-Treitler (2011): Patient forum posts**
- **Data**: Online diabetes forum discussions
- **Method**: LDA to identify health topics discussed by patients
- **Topics**: Medication side effects, dietary management, emotional support, insurance issues
- **Application**: Constructed patient-centric health vocabulary for consumer health informatics

**Arnold et al. (2016): Clinical notes**
- **Data**: Radiology reports from hospitals
- **Method**: LDA for case-based retrieval (finding similar cases)
- **Topics**: Anatomical regions and diagnostic findings
- **Contribution**: LDA enables clinical decision support

**Geletta et al. (2019): LDA for clinical trial termination prediction**
- **Data**: ClinicalTrials.gov repository (structured + unstructured narrative)
- **Method**: LDA extracted 25 topics from trial narrative descriptions; Random Forest prediction combining structured data and LDA topics
- **Finding**: Models incorporating LDA topics (Model 2) significantly outperformed models using structured data alone (Model 1) in predicting trial terminations, with enhanced sensitivity and specificity
- **Contribution**: Validated LDA's predictive utility—demonstrating that latent topics extracted from unstructured text capture risk factors invisible in structured data. This extends LDA's application beyond descriptive thematic analysis to predictive modeling for clinical decision support

**Altintas et al. (2021): LDA for social media health discussions**
- **Data**: Reddit cancer disease forum posts
- **Method**: LDA with coherence testing and t-SNE visualization for topic relationships
- **Topics identified**: Cancer treatment experiences, patient support, disease progression, side effects management
- **Contribution**: Demonstrated LDA's applicability to informal social media texts (beyond formal reviews), with coherence tests validating topic quality

**Danek et al. (2023): LDA for real-time policy monitoring**
- **Data**: 3,647 Google reviews of six Berlin COVID-19 mass vaccination centers (December 2020-December 2021)
- **Method**: Topic modeling identified five optimal latent topics; keyword extraction (47 salient keywords); sentiment analysis tracked rating changes over time
- **Topics identified**: Organization, friendliness/responsiveness, patient flow/wait time
- **Key findings**: Average ratings declined from 4.7 to 4.1 over one year; "appointment" and "wait" keywords dominated negative reviews
- **Contribution**: Showcased online reviews for **real-time monitoring** of newly established healthcare infrastructures, informing policy adjustments during pandemic response

**Synthesis**: LDA successfully discovers interpretable topics in healthcare texts across diverse contexts—physician and hospital reviews (Hao & Zhang, 2016; Wallace et al., 2014), patient forums (Doing-Harris & Zeng-Treitler, 2011; Altintas et al., 2021), clinical notes (Arnold et al., 2016), and clinical trial narratives (Geletta et al., 2019). Topics often align with but extend existing theoretical frameworks (e.g., SERVQUAL), validating LDA as both a discovery and predictive tool. Recent applications demonstrate LDA's utility for real-time policy monitoring (Danek et al., 2023), expanding its role beyond post-hoc analysis to dynamic quality surveillance.

---

## 2.5.4 Determining the Optimal Number of Topics (K)

**The most critical methodological decision** in LDA is selecting K, the number of topics. Unlike some machine learning algorithms that learn the optimal number of clusters from data (e.g., Dirichlet Process Mixture Models), standard LDA requires the researcher to specify K a priori.

**The challenge**: Too few topics (K=2-3) yield coarse, uninformative themes (e.g., "positive sentiment" vs. "negative sentiment"). Too many topics (K=20-30) create fragmented, redundant themes that are difficult to interpret and may reflect noise rather than meaningful dimensions.

### Approaches to Selecting K

**1. Statistical Performance Metrics**

**Coherence Score (C_v)**

Coherence measures the **semantic similarity of top words within topics** (Röder et al., 2015). It is currently the **gold standard** metric for LDA topic quality.

**Formula** (simplified):
C_v averages the normalized pointwise mutual information (NPMI) between pairs of top words in each topic, weighted by their context vector similarity.

High coherence = words in a topic frequently co-occur and are semantically related.

**Typical usage**:
- Train LDA models with K ∈ {2, 3, 4, ..., 20}
- Compute coherence for each K
- Select K that maximizes coherence

**Limitation**: **Maximizing coherence does not guarantee interpretability** (Chang et al., 2009). A topic with keywords {"good," "bad," "happy," "sad"} may have high coherence (emotion words co-occur) but is not a useful service quality dimension.

**Perplexity**

Perplexity measures **model fit** to held-out data (lower = better). It evaluates how well the model predicts unseen words.

**Formula**:
Perplexity = exp(-log likelihood / total words)

**Limitation**: **Perplexity and interpretability are often negatively correlated** (Chang et al., 2009). Models with low perplexity (best predictive fit) may have topics humans find incoherent.

**Why?**: Perplexity optimizes prediction, which may be achieved by splitting coherent topics into fine-grained sub-topics (e.g., splitting "Staff Attitude" into "Nurse Attitude," "Receptionist Attitude," "Doctor Attitude"—statistically beneficial but conceptually redundant).

**2. Elbow Method**

**Approach**: Plot coherence (or perplexity) against K. Look for an "elbow point" where incremental improvements diminish.

**Example**:
- K=2: Coherence = 0.35
- K=5: Coherence = 0.50 (large increase)
- K=10: Coherence = 0.52 (small increase)
- K=15: Coherence = 0.51 (decrease)

**Conclusion**: K=5 or K=10 are elbow candidates.

**Limitation**: Elbow is often **ambiguous**—no clear inflection point.

**3. Domain Expert Evaluation**

**Approach**: Have domain experts (healthcare professionals, service quality researchers) review top keywords and sample reviews for each candidate K, assessing:
- **Semantic clarity**: Do top-10 keywords form a coherent theme?
- **Distinctiveness**: Are topics non-overlapping (low keyword overlap)?
- **Actionability**: Can hospital managers derive specific improvement strategies?

**Gold standard**: Chang et al. (2009) found expert evaluation (word intrusion test) is the **best predictor of topic usefulness**, but it is labor-intensive.

**4. Theoretical Validation**

**Approach**: Compare discovered topics to **established frameworks** (e.g., SERVQUAL, Dagger et al., 2007). Select K that yields topics aligned with theory.

**Rationale**: If LDA with K=5 produces topics mapping to SERVQUAL's five dimensions, this provides **construct validity**.

**Caution**: Overly prioritizing theoretical alignment risks **confirmation bias**—forcing data into preconceived frameworks, negating LDA's inductive advantage.

**5. Stability Analysis**

**Approach**: Train LDA multiple times with different random seeds. Measure **topic stability** (do the same topics emerge?). Select K that produces stable topics across runs.

**Metric**: Calculate Jaccard similarity of top-N keywords across runs. High similarity = stable topics.

**6. Hybrid Multi-Criteria Approach**

**This study's approach** (detailed in Section 3.3.2 of the manuscript):

We employ a **multi-criteria decision framework** integrating:
1. **Coherence score**: Quantitative performance metric
2. **Elbow method**: Visual inspection for diminishing returns
3. **Interpretability assessment**: Two researchers independently evaluate topic clarity
4. **Theoretical validation**: Compare to SERVQUAL and healthcare-specific frameworks
5. **Distribution balance**: Ensure topics have reasonable prevalence (avoid extreme dominance or fragmentation)

**Critical insight**: **Statistical optimization alone (maximizing coherence) can yield substantively uninformative models**. In our pilot analysis, K=2 achieved the highest coherence (0.464) but merely separated positive from negative sentiment—statistically optimal but managerially useless. K=5 had lower coherence (0.433) but produced five interpretable service quality dimensions with clear action implications.

**Methodological contribution**: This multi-criteria approach addresses a gap in LDA practice, where many studies (e.g., Hao and Zhang, 2016) select K based solely on coherence maximization without assessing interpretability.

---

## 2.5.5 Cross-Cultural Topic Modeling: Methodological Considerations

Applying LDA to reviews from **different languages and cultural contexts** introduces unique challenges.

### Language-Specific Preprocessing

**Challenge 1: Segmentation**

- **English**: Words separated by spaces; tokenization is straightforward
- **Chinese**: No word boundaries; requires segmentation algorithms (e.g., jieba)
  - **Error source**: Ambiguous segmentations (e.g., "银行/银" [bank] vs. "银/行" [silver + walk])
  - **Mitigation**: Custom medical dictionaries to guide segmentation (this study: 68 medical terms)

**Challenge 2: Stopwords**

- **Universal stopwords**: Function words (的, 了, is, the)
- **Domain stopwords**: "Hospital" and "醫院" are ubiquitous in reviews but uninformative
- **Cultural stopwords**: Politeness markers (請, 謝謝) in Chinese reviews may be formulaic, not substantive

**This study**: Separate stopword lists for Chinese (84 words) and English (TBD), iteratively refined.

**Challenge 3: Stemming/Lemmatization**

- **English**: "Doctor," "doctors," "doctor's" → "doctor" (stemming)
- **Chinese**: Less morphological variation; minimal stemming needed

**Challenge 4: Cross-Linguistic NLP Validation**

Cross-linguistic applications validate NLP methods' robustness across languages. Alhazzani et al. (2023) successfully classified Arabic patient experience comments into 25 categories using deep learning (BiLSTM, BiGRU) and customized BERT models (PX_BERT, AraBERTv02). The domain-adapted PX_BERT, pre-trained on patient experience texts, outperformed general Arabic BERT models, achieving the highest F1-scores. This demonstrates two critical principles for cross-cultural text mining:

1. **Language-specific models are essential**: General-purpose NLP models trained on English (or standard Arabic) underperform compared to domain-adapted, language-specific models.

2. **Preprocessing requirements vary**: Arabic text required specialized tokenization, morphological analysis, and diacritical mark handling—preprocessing steps unnecessary for English but critical for Arabic NLP accuracy.

Similarly, Yazdani et al. (2023) applied sentiment analysis and topic modeling to Persian-language cancer patient feedback from Tehran University's Cancer Institute. Achieving 89-93% accuracy in sentiment classification across service dimensions, they extracted themes such as "metastasis" (lower sentiment scores) and "affable staff" (higher sentiment scores). Topic-level sentiment analysis revealed that while patients expressed dissatisfaction with appointment booking services, they reported positive sentiments toward chemotherapy care and staff interactions.

**Implication for this study**: These cross-linguistic validations underscore the importance of language-specific preprocessing for Chinese (Traditional) reviews in Taiwan. Standard NLP tools trained on English or Simplified Chinese may not perform optimally. This study employs:
- **Jieba segmentation** with custom medical dictionaries (68 terms) for Traditional Chinese
- **Iteratively refined stopword lists** (84 Chinese stopwords) tailored to hospital review corpora
- **Separate LDA training** for Taiwan and U.S. corpora (rather than forcing translation or multilingual models), ensuring culturally authentic topic discovery

### Topic Alignment Across Languages

**Challenge**: LDA models trained on Taiwan and U.S. data independently produce two sets of topics. How to **compare** them?

**Approach 1: Manual Semantic Matching**

Researchers review top keywords and representative reviews for each topic in both countries, identifying semantically equivalent topics.

**Example**:
- Taiwan Topic 2: 時間, 掛號, 等待 (time, registration, wait) → **Wait Time**
- U.S. Topic 5: wait, appointment, delay, long → **Wait Time**
- **Match**: Both are "Wait Time" dimensions

**Limitation**: Subjective; inter-rater agreement required.

**Approach 2: Topic Model Translation**

Train LDA on English data, **translate** Chinese reviews to English (or vice versa), then compare topic assignments.

**Limitation**: Translation introduces errors; cultural nuances lost.

**Approach 3: Multilingual Topic Models**

Polylingual LDA (Mimno et al., 2009) jointly models documents in multiple languages using aligned documents (e.g., Wikipedia articles in Chinese and English about the same entity).

**Limitation**: Requires **parallel corpora** (same content in both languages). Hospital reviews are not parallel—Taiwan and U.S. reviews describe different hospitals.

**This study employs Approach 1**: Manual semantic matching with dual-language researchers (author team includes native Chinese and English speakers). We validate matches through:
- Keyword semantic equivalence (via translation and cultural interpretation)
- Review content similarity (sampling representative reviews from matched topics)

### Comparability Considerations

**Ensuring fair comparison**:

1. **Equivalent preprocessing**: Apply analogous text cleaning (stopword removal, filtering by document length) to both corpora

2. **Comparable K**: If selecting K=7 for Taiwan, use K=7 for U.S. (or nearby range, e.g., K=6-8) to enable structural comparison

3. **Balanced sample sizes**: Ensure Taiwan and U.S. datasets are comparable in size. If one is 10× larger, downsample to avoid volume-driven topic differences

**This study**: Taiwan = 5,007 reviews; U.S. = TBD (target comparable size, 5,000-8,000)

---

## 2.5.6 Limitations of LDA and Mitigation Strategies

### Limitation 1: Bag-of-Words Assumption

**Issue**: LDA treats documents as **bags of words**, ignoring word order and syntax.

**Example**: "The doctor is not rude" and "The doctor is rude, not kind" contain the same words {doctor, is, not, rude} but opposite meanings.

**Mitigation**:
- **Bigrams/trigrams**: Include multi-word phrases (e.g., "not good" as single token)
- **This study**: Includes medical bigrams (e.g., "急診室" emergency room, "護理師" nursing staff)

### Limitation 2: Number of Topics Must Be Specified

**Issue**: K is not learned from data; researcher must choose.

**Mitigation**: Multi-criteria selection framework (Section 2.5.4).

### Limitation 3: Topic Labels Are Post-Hoc

**Issue**: LDA outputs word distributions (e.g., Topic 3 = {nurse: 0.08, rude: 0.05, attitude: 0.07}). Researchers must **interpret** and **label** topics (e.g., "Staff Attitude").

**Subjectivity**: Different researchers may label differently.

**Mitigation**:
- **Inter-rater agreement**: Two researchers independently label; discuss discrepancies
- **Representative reviews**: Examine reviews with high Topic 3 probability to validate label

**This study**: Two researchers labeled topics; 100% agreement achieved.

### Limitation 4: Topics May Be Non-Interpretable

**Issue**: Some topics emerge as "junk topics" mixing unrelated words or "stopword topics" with generic terms.

**Mitigation**:
- **Iterative refinement**: Retrain LDA with additional stopwords if junk topics appear
- **Discard non-interpretable topics**: Report only coherent topics

### Limitation 5: Short Documents

**Issue**: Reviews vary in length; very short reviews (5-10 words) provide sparse signals for topic inference.

**Mitigation**: **Minimum token threshold**—exclude reviews with <3 tokens after preprocessing.

**This study**: Excluded reviews with <3 tokens, yielding final dataset of 5,007 reviews (from 5,283 initial).

---

## Summary: LDA as the Optimal Method for Cross-Cultural Service Quality Discovery

This section establishes:

1. **LDA is ideal for exploratory service quality research**: Unlike supervised methods (sentiment analysis) that impose categories or frequency methods (word counts) that lack thematic structure, LDA **discovers latent dimensions** from data without predefinition (Blei et al., 2003).

2. **LDA has proven validity in healthcare**: Studies by Hao and Zhang (2016), Wallace et al. (2014), and others demonstrate LDA topics align with established service quality frameworks while revealing additional nuances.

3. **Topic number selection is critical**: Maximizing coherence alone can yield uninformative models (Chang et al., 2009). **Multi-criteria frameworks** integrating coherence, interpretability, and theoretical validation are necessary—a methodological contribution of this study.

4. **Cross-cultural LDA is feasible but challenging**: Language-specific preprocessing and topic alignment require careful methodology. Manual semantic matching by bilingual researchers is the most appropriate approach when parallel corpora are unavailable.

5. **LDA limitations are manageable**: Bag-of-words assumptions, pre-specified K, and subjective labeling are addressed through bigrams, multi-criteria selection, and inter-rater validation.

**Justification for this study's methodology**: LDA enables **inductive discovery** of service quality dimensions in Taiwan and U.S. hospital reviews, allowing dimensions to emerge organically from each cultural/institutional context rather than forcing both into Western frameworks (SERVQUAL). This aligns with calls for context-adapted service quality models (Dagger et al., 2007) and addresses the gap in cross-cultural healthcare quality research using patient-generated online content.

The next section (2.6) synthesizes Sections 2.1-2.5 to articulate specific research gaps and this study's contributions.

---

## References for Section 2.5

Aggarwal, C.C., & Zhai, C. (2012). *Mining text data*. Springer Science & Business Media: New York.

Alhazzani, N. Z., Al-Turaiki, I. M., & Alkhodair, S. A. (2023). Text classification of patient experience comments in Saudi dialect using deep learning techniques. *Applied Sciences*, 13(18), Article 10305. https://doi.org/10.3390/app131810305

Altintas, V., Albayrak, M., & Topal, K. (2021). Topic modeling with latent Dirichlet allocation for cancer disease posts. *Journal of the Faculty of Engineering and Architecture of Gazi University*, 36(4), 2195-2208. https://doi.org/10.17341/gazimmfd.734730

Arnold, C.W., El-Saden, S.M., Bui, A.A., & Taira, R. (2016). Clinical case-based retrieval using latent topic analysis. *AMIA Annual Symposium Proceedings*, 295-304.

Athira, B., Jones, J., Idicula, S. M., Kulanthaivel, A., & Zhang, E. (2021). Annotating and detecting topics in social media forum and modelling the annotation to derive directions—A case study. *Journal of Big Data*, 8, Article 59. https://doi.org/10.1186/s40537-021-00429-7

Blei, D.M. (2012). Probabilistic topic models. *Communications of the ACM*, 55(4), 77-84.

Blei, D.M., Ng, A.Y., & Jordan, M.I. (2003). Latent dirichlet allocation. *Journal of Machine Learning Research*, 3, 993-1022.

Chang, J., Gerrish, S., Wang, C., Boyd-Graber, J., & Blei, D.M. (2009). Reading tea leaves: How humans interpret topic models. *Advances in Neural Information Processing Systems*, 22, 288-296.

Dagger, T.S., Sweeney, J.C., & Johnson, L.W. (2007). A hierarchical model of health service quality: scale development and investigation of an integrated model. *Journal of Service Research*, 10(2), 123-142.

Danek, S., Büttner, M., Krois, J., & Schwendicke, F. (2023). How do users respond to mass vaccination centers? A cross-sectional study using natural language processing on online reviews to explore user experience and satisfaction with COVID-19 vaccination centers. *Vaccines*, 11(1), Article 144. https://doi.org/10.3390/vaccines11010144

Doing-Harris, K.M., & Zeng-Treitler, Q. (2011). Computer-assisted update of a consumer health vocabulary through mining of social network data. *Journal of Medical Internet Research*, 13(2), e37.

Gao, G.G., McCullough, J.S., Agarwal, R., & Jha, A.K. (2012). A changing landscape of physician quality reporting: analysis of patients' online ratings of their physicians over a 5-year period. *Journal of Medical Internet Research*, 14(1), e38.

Geletta, S., Follett, L., & Laugerman, M. (2019). Latent Dirichlet Allocation in predicting clinical trial terminations. *BMC Medical Informatics and Decision Making*, 19, Article 224. https://doi.org/10.1186/s12911-019-0973-y

Greaves, F., Pape, U.J., King, D., Darzi, A., Majeed, A., Wachter, R.M., & Millett, C. (2013). Associations between web-based patient ratings and objective measures of hospital quality. *Archives of Internal Medicine*, 172(5), 435-436.

Griffiths, T.L., & Steyvers, M. (2004). Finding scientific topics. *Proceedings of the National Academy of Sciences*, 101(Suppl. 1), 5228-5235.

Hao, H., & Zhang, K. (2016). The voice of Chinese health consumers: a text mining approach to web-based physician reviews. *Journal of Medical Internet Research*, 18(5), e108.

Liu, B. (2012). Sentiment analysis and opinion mining. *Synthesis Lectures on Human Language Technologies*, 5(1), 1-167.

López, A., Detz, A., Ratanawongsa, N., & Sarkar, U. (2012). What patients say about their doctors online: a qualitative content analysis. *Journal of General Internal Medicine*, 27(6), 685-692.

Mimno, D., Wallach, H.M., Naradowsky, J., Smith, D.A., & McCallum, A. (2009). Polylingual topic models. *Proceedings of the 2009 Conference on Empirical Methods in Natural Language Processing*, 880-889.

Nawab, K., Ramsey, G., & Schreiber, R. (2020). Natural language processing to extract meaningful information from patient experience feedback. *Applied Clinical Informatics*, 11(2), 242-250. https://doi.org/10.1055/s-0040-1708049

Röder, M., Both, A., & Hinneburg, A. (2015). Exploring the space of topic coherence measures. *Proceedings of the Eighth ACM International Conference on Web Search and Data Mining (WSDM)*, 399-408.

Shah, A. M., Yan, X., Tariq, S., & Ali, M. (2021). What patients like or dislike in physicians: Analyzing drivers of patient satisfaction and dissatisfaction using a digital topic modeling approach. *Information Processing & Management*, 58(3), Article 102516. https://doi.org/10.1016/j.ipm.2021.102516

Sun, W., Cai, Z., Li, Y., Liu, F., Fang, S., & Wang, G. (2018). Data processing and text mining technologies on electronic medical records: A review. *Journal of Healthcare Engineering*, 2018, Article 4302425. https://doi.org/10.1155/2018/4302425

van Buchem, M. M., Neve, O. M., Kant, I. M. J., Steyerberg, E. W., Boosman, H., & Hensen, E. F. (2022). Analyzing patient experiences using natural language processing: Development and validation of the artificial intelligence patient reported experience measure (AI-PREM). *BMC Medical Informatics and Decision Making*, 22, Article 199. https://doi.org/10.1186/s12911-022-01923-5

Wallace, B.C., Paul, M.J., Sarkar, U., Trikalinos, T.A., & Dredze, M. (2014). A large-scale quantitative analysis of latent factors and sentiment in online doctor reviews. *Journal of the American Medical Informatics Association*, 21(6), 1098-1103.

Yazdani, A., Shamloo, M., Khaki, M., & Nahvijou, A. (2023). Use of sentiment analysis for capturing hospitalized cancer patients' experience from free-text comments in the Persian language. *BMC Medical Informatics and Decision Making*, 23, Article 259. https://doi.org/10.1186/s12911-023-02358-2
