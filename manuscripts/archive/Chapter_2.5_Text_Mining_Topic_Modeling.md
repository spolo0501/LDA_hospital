# 2.5 Text Mining and Topic Modeling in Service Quality Research

Online reviews provide rich qualitative data at scale, but their unstructured format poses analytical challenges. Manual content analysis yields deep insights but is impractical for thousands of reviews. This requires automated text mining methods that discover patterns, extract themes, and classify content computationally (Aggarwal and Zhai, 2012). This section reviews text mining approaches with emphasis on Latent Dirichlet Allocation (LDA) topic modeling—the method employed in this study.

---

## 2.5.1 Text Mining Approaches

Text mining encompasses computational methods for extracting meaningful information from unstructured text. Key approaches include frequency-based methods (TF-IDF) identifying most-mentioned attributes but lacking thematic structure; sentiment analysis classifying text as positive or negative but collapsing multiple dimensions into single valence; and aspect-based sentiment analysis (ABSA) jointly extracting service aspects and sentiment polarity but requiring predetermined aspect lexicons (Liu, 2012; Aggarwal and Zhai, 2012).

Topic modeling offers distinct advantages through discovering latent topics probabilistically generating observed text using unsupervised machine learning (Blei, 2012). LDA requires no manual labeling, identifies multiple coexisting topics, quantifies topic prevalence probabilistically, and discovers dimensions from data rather than imposing researcher categories (Blei et al., 2003). While deep learning methods like BiLSTM with BERT achieve higher classification accuracy when labeled training data exists (Athira et al., 2021), LDA is ideal for exploratory research discovering unknown dimensions—precisely the requirement for cross-cultural service quality research where dimensional structures may differ between Taiwan and the United States.

---

## 2.5.2 Latent Dirichlet Allocation (LDA)

LDA conceptualizes documents as mixtures of topics, where each topic is a probability distribution over words. For example, a hospital review might be 60% "interpersonal quality" (containing words like caring, empathy, respectful), 30% "wait times" (containing words like wait, delay, crowded), and 10% "facility environment" (containing words like clean, modern, comfortable). LDA estimates these hidden topic structures from observed word frequencies (Blei et al., 2003).

The algorithm assumes documents are generated through a probabilistic process: select a distribution over topics for the document, then for each word position, choose a topic from that distribution and choose a word from that topic's word distribution. LDA reverses this generative process, inferring the topic distributions that most likely produced the observed text through Bayesian inference (Hoffman et al., 2010).

Healthcare applications demonstrate LDA's utility. Hao and Zhang (2016) applied LDA to Chinese physician reviews, identifying seven topics including physician expertise, communication, service attitude, costs, and wait times, with Chinese patients emphasizing physician reputation more than Western patients. Arnold et al. (2016) analyzed Medicare beneficiary comments using LDA, discovering dimensions aligned with CAHPS domains (care coordination, communication) but also emergent themes absent from surveys (rural access barriers). Geletta et al. (2019) demonstrated LDA's predictive power, showing that models incorporating LDA-derived topics from clinical trial descriptions significantly outperformed models using structured data alone in predicting trial termination. These applications confirm LDA's capacity to discover meaningful service quality dimensions from patient narratives.

---

## 2.5.3 Determining the Number of Topics

LDA requires researchers to specify the number of topics K a priori, yet no consensus exists on optimal selection methods. Two approaches dominate. Statistical metrics include perplexity (lower indicates better predictive accuracy but often favors unrealistically high K), and coherence scores measuring semantic relatedness of top words within topics (higher indicates more interpretable topics) (Röder et al., 2015). However, statistical optima may not yield substantively interpretable topics. Human interpretability assessment involves domain experts evaluating topic coherence, distinctiveness, and substantive relevance across multiple K values, selecting the number yielding most interpretable, actionable dimensions (Chang et al., 2009).

This study employs a hybrid approach: computing coherence scores (C_v metric) across K=5 to K=15, then having healthcare service quality researchers independently evaluate top-performing models for interpretability, selecting K maximizing both statistical coherence and substantive meaningfulness. This methodological pluralism aligns with recommendations from text mining methodologists (Maier et al., 2018).

---

## 2.5.4 Cross-Cultural and Cross-Linguistic Topic Modeling

Applying LDA to cross-cultural comparisons introduces methodological challenges. Language differences require separate preprocessing (Chinese word segmentation using Jieba versus English tokenization), potentially affecting discovered topics through algorithmic differences rather than true content differences (Boyd-Graber et al., 2017). Cultural linguistic norms shape expression—Taiwanese patients may use indirect language while Americans use explicit criticism, affecting whether similar concerns manifest as distinct topics or remain latent.

Translation-based approaches translating all text to a common language risk semantic loss and introduce translation errors. Separate models for each language (this study's approach) allow language-appropriate preprocessing and topic discovery but require post-hoc alignment to identify corresponding topics across countries through manual examination of top words and representative documents (Hao and Zhang, 2016).

Recent cross-linguistic NLP research provides validation for language-specific approaches. Alhazzani et al. (2023) successfully classified Arabic patient experience comments into 25 categories using customized BERT models, while Yazdani et al. (2023) achieved 89-93% sentiment analysis accuracy in Persian cancer patient comments. These studies demonstrate that language-specific NLP methods effectively capture patient experiences despite linguistic differences, supporting this study's separate-model approach for Taiwan (Chinese) and U.S. (English) hospital reviews.

This methodological choice accepts that discovered topics may not correspond one-to-one across countries—some topics may be culture-specific. Rather than imposing identical structures, we inductively discover dimensions in each context, then systematically compare structures to identify universal dimensions, culture-specific dimensions, and differentially prominent dimensions, directly testing cultural and institutional hypotheses (Sections 2.2-2.3).

---

## Summary

Text mining enables large-scale analysis of unstructured patient reviews, with LDA offering unsupervised, probabilistic discovery of latent service quality dimensions. Healthcare applications demonstrate LDA's capacity to identify meaningful, actionable themes from patient narratives, complementing predetermined survey structures. Cross-cultural applications require methodological care regarding language differences and topic alignment, addressed through separate language-appropriate models and systematic post-hoc comparison. This approach enables testing whether Taiwan and U.S. hospital reviews reveal similar universal dimensions or divergent culture-specific structures, integrating theoretical expectations (Sections 2.1-2.3) with empirical patterns discovered inductively from patient discourse.

---

## References for Section 2.5

Aggarwal, C.C., & Zhai, C. (2012). *Mining text data*. Springer Science & Business Media.

Alhazzani, N.Z., Al-Turaiki, I.M., & Alkhodair, S.A. (2023). Arabic patient experience comment classification. *IEEE Access*, 11, 50591-50607.

Arnold, C.W., Tan, S.S., Thadaney-Israni, S., Lembersky, M., Kallmes, D.F., Freeman, W.D., & Oh, S. (2016). Evaluating patient perceptions on Medicare Access and CHIP Reauthorization Act quality measures. *Journal of the American Medical Informatics Association*, 23(e1), e118-e124.

Athira, B., Jones, J., Idicula, S.M., et al. (2021). Breast cancer risk prediction using BiLSTM. *IEEE Transactions on Computational Social Systems*, 8(5), 1080-1088.

Blei, D.M. (2012). Probabilistic topic models. *Communications of the ACM*, 55(4), 77-84.

Blei, D.M., Ng, A.Y., & Jordan, M.I. (2003). Latent Dirichlet allocation. *Journal of Machine Learning Research*, 3, 993-1022.

Boyd-Graber, J., Hu, Y., & Mimno, D. (2017). Applications of topic models. *Foundations and Trends in Information Retrieval*, 11(2-3), 143-296.

Chang, J., Gerrish, S., Wang, C., Boyd-Graber, J., & Blei, D.M. (2009). Reading tea leaves: How humans interpret topic models. *Advances in Neural Information Processing Systems*, 22, 288-296.

Geletta, S., Follett, L., & Laugerman, M. (2019). Latent Dirichlet allocation in predicting clinical trial terminations. *BMC Medical Informatics and Decision Making*, 19, Article 92.

Hao, H., & Zhang, K. (2016). The voice of Chinese health consumers: A text mining approach to web-based physician reviews. *Journal of Medical Internet Research*, 18(5), e108.

Hoffman, M., Blei, D.M., & Bach, F. (2010). Online learning for latent Dirichlet allocation. *Advances in Neural Information Processing Systems*, 23, 856-864.

Liu, B. (2012). Sentiment analysis and opinion mining. *Synthesis Lectures on Human Language Technologies*, 5(1), 1-167.

Maier, D., Waldherr, A., Miltner, P., et al. (2018). Applying LDA topic modeling in communication research. *Communication Methods and Measures*, 12(2-3), 93-118.

Röder, M., Both, A., & Hinneburg, A. (2015). Exploring the space of topic coherence measures. *Proceedings of the Eighth ACM International Conference on Web Search and Data Mining*, 399-408.

Yazdani, A., Shamloo, M., Khaki, M., & Nahvijou, A. (2023). Persian sentiment analysis of cancer patients. *BMC Medical Informatics and Decision Making*, 23, Article 68.
