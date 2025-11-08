# 2.1 Healthcare Service Quality: Theoretical Foundations

## 2.1.1 Service Quality Dimensions and Frameworks

### The Multidimensional Nature of Service Quality

Service quality has been recognized as a multidimensional construct since the seminal work of Parasuraman, Zeithaml, and Berry (1985), who conceptualized it as "the gap between customer expectations and perceptions of service delivery." This gap model laid the foundation for understanding that service quality cannot be reduced to a single global evaluation but rather comprises distinct, evaluable dimensions that collectively shape customer assessments.

**SERVQUAL: The Foundational Framework**

The most influential operationalization of service quality emerged through the SERVQUAL instrument (Parasuraman et al., 1988), which identified five generic dimensions applicable across service industries:

1. **Tangibles**: Physical facilities, equipment, and appearance of personnel
2. **Reliability**: Ability to perform the promised service dependably and accurately
3. **Responsiveness**: Willingness to help customers and provide prompt service
4. **Assurance**: Knowledge and courtesy of employees and their ability to inspire trust and confidence
5. **Empathy**: Caring, individualized attention provided to customers

The SERVQUAL framework revolutionized service quality research by providing a standardized, psychometrically validated measurement tool. Its 22-item scale has been applied across diverse contexts including banking (Avkiran, 1994), retail (Dabholkar et al., 1996), and telecommunications (Kettinger and Lee, 1994), demonstrating broad generalizability. The underlying logic—that service quality is inherently multidimensional and must be assessed across multiple attributes—has achieved paradigmatic status in service research (Brady and Cronin, 2001).

However, SERVQUAL has also attracted substantial criticism. Cronin and Taylor (1992) challenged the gap-based conceptualization, arguing that performance-only measures (SERVPERF) better predict service quality. Buttle (1996) raised concerns about the five-dimensional structure, noting that factor analyses across different contexts often yield varying numbers of dimensions (ranging from 3 to 9), questioning the universal applicability of the five-factor model. Most critically for context-specific applications, scholars have argued that generic dimensions may fail to capture industry-specific quality attributes (Dagger et al., 2007; Brady and Cronin, 2001).

### Healthcare-Specific Service Quality Models

Recognizing the limitations of generic frameworks, researchers have developed healthcare-adapted service quality models that account for the unique characteristics of medical service delivery.

**Brady and Cronin's Hierarchical Model**

Brady and Cronin (2001) proposed a hierarchical conceptualization that decomposes service quality into three primary dimensions, each comprising three sub-dimensions:

1. **Interaction Quality**
   - Attitude (friendliness, courtesy, empathy)
   - Behavior (responsiveness, helpfulness)
   - Expertise (knowledge, competence)

2. **Physical Environment Quality**
   - Ambient conditions (temperature, noise, cleanliness)
   - Design (layout, functionality, aesthetics)
   - Social factors (crowding, other patients)

3. **Outcome Quality**
   - Waiting time
   - Tangible outcomes (treatment results)
   - Valence (emotional response to service experience)

This hierarchical structure is theoretically significant because it distinguishes between **process** (how service is delivered) and **outcome** (what is delivered), a distinction particularly salient in healthcare where patients may lack the technical knowledge to evaluate clinical outcomes but can assess interpersonal interactions and environmental factors (Donabedian, 1988).

**Dagger et al.'s Healthcare Service Quality Model**

Dagger, Sweeney, and Johnson (2007) developed a context-specific model for healthcare based on extensive qualitative research with patients. Their framework identifies four key dimensions:

1. **Interpersonal Quality**: Staff empathy, courtesy, and communication effectiveness
2. **Technical Quality**: Clinical competence, accuracy of diagnosis and treatment
3. **Environment Quality**: Cleanliness, comfort, and ambiance of facilities
4. **Administrative Quality**: Appointment scheduling, waiting times, billing processes

Importantly, Dagger et al. (2007) empirically demonstrated that these four dimensions have differential impacts on patient satisfaction and behavioral intentions (e.g., recommending the provider, returning for future care). **Interpersonal quality** emerged as the strongest predictor of patient loyalty, even when controlling for technical quality—a finding that underscores the "high-touch" nature of healthcare services.

**The Technical-Functional Quality Dichotomy**

A foundational distinction in healthcare service quality research is Grönroos' (1984) differentiation between **technical quality** (what service is delivered) and **functional quality** (how service is delivered). In medical contexts:

- **Technical quality** refers to clinical accuracy, diagnostic precision, treatment effectiveness, and adherence to medical protocols—essentially, the medical outcome.
- **Functional quality** encompasses the manner of service delivery: physician-patient communication, staff attitudes, waiting times, and facility conditions.

This dichotomy is theoretically crucial because it reflects the **information asymmetry** inherent in healthcare: patients typically lack the medical expertise to evaluate technical quality (e.g., whether a diagnosis was clinically accurate), but can readily assess functional aspects (e.g., whether the doctor listened empathetically) (Andaleeb, 2001). Consequently, patient satisfaction and service quality perceptions are often disproportionately influenced by functional quality, even when technical quality is objectively high (Chang et al., 2013).

### The Evolution and Debate: How Many Dimensions?

Despite the theoretical consensus that service quality is multidimensional, **the optimal number of dimensions remains contested**. Empirical studies have identified varying dimensional structures:

- **Two dimensions**: Technical vs. functional quality (Grönroos, 1984)
- **Three dimensions**: Interaction, environment, outcome (Brady & Cronin, 2001)
- **Four dimensions**: Interpersonal, technical, environment, administrative (Dagger et al., 2007)
- **Five dimensions**: SERVQUAL's tangibles, reliability, responsiveness, assurance, empathy (Parasuraman et al., 1988)
- **Six dimensions**: Choi et al. (2004) found six factors in Korean hospitals
- **Nine dimensions**: Andaleeb (2001) identified nine dimensions in Bangladesh

This variability suggests three important insights:

1. **Context-dependency**: Service quality structures may vary across industries, cultures, and institutional settings (Ladhari, 2009). A hospital's quality dimensions may differ from a hotel's, and quality perceptions in Taiwan may differ from those in the United States.

2. **Methodological sensitivity**: The number of identified dimensions depends on the research method. Confirmatory factor analysis (CFA) with predetermined items tends to reproduce existing structures (e.g., SERVQUAL's five dimensions), while exploratory approaches (e.g., qualitative research, topic modeling) may reveal different or additional dimensions (Dagger et al., 2007).

3. **Level of abstraction**: Hierarchical models (Brady & Cronin, 2001) reconcile divergent findings by distinguishing between **higher-order dimensions** (e.g., interaction quality) and **sub-dimensions** (e.g., staff attitude, staff expertise). The appropriate level depends on the research objective: managerial applications may require granular sub-dimensions, while theoretical models may focus on broader constructs.

### Implications for the Present Study

This review establishes three foundational principles guiding our research:

**Principle 1: Multidimensionality is fundamental**
Service quality cannot be reduced to a single metric. Any valid assessment must identify and measure multiple distinct dimensions. Our use of topic modeling aligns with this principle by discovering latent dimensions without researcher-imposed constraints.

**Principle 2: Dimensions are context-specific**
The exact number and nature of dimensions vary across industries and contexts. Healthcare dimensions differ from retail; hospital outpatient care may differ from emergency services. Therefore, **data-driven discovery** of dimensions (via LDA) is more appropriate than imposing SERVQUAL's generic five dimensions.

**Principle 3: Exploratory methods complement confirmatory approaches**
While SERVQUAL and its variants provide validated measurement scales, they inherently limit discovery to predetermined constructs. Patient-generated online reviews may reveal emergent concerns (e.g., COVID-19 safety protocols, telemedicine accessibility) not captured in surveys designed before these issues became salient. Topic modeling enables inductive theory building.

These principles justify our methodological choice: rather than measuring Taiwan and U.S. hospitals against SERVQUAL's five dimensions (a confirmatory approach), we use LDA to **discover** what dimensions patients in each country naturally discuss and evaluate—an exploratory, data-driven approach suited to cross-cultural comparison where dimensional structures may differ.

---

## 2.1.2 Context-Specific Service Quality in Healthcare

### The Unique Characteristics of Healthcare Services

Healthcare services possess distinctive features that differentiate them from other service sectors and necessitate context-adapted quality frameworks (Berry and Bendapudi, 2007). These characteristics fundamentally shape how patients perceive, evaluate, and prioritize service quality dimensions.

**1. High-Contact, High-Stakes Interactions**

Healthcare delivery involves **intensive interpersonal contact** between patients and providers (physicians, nurses, technicians) over extended periods, often during moments of physical distress or emotional vulnerability (Berry and Bendapudi, 2007). Unlike a routine retail transaction, a medical consultation involves:

- **Information exchange**: Patients must disclose intimate personal information (symptoms, medical history, lifestyle factors)
- **Trust requirements**: Patients must trust providers with their physical wellbeing and, in severe cases, their lives
- **Emotional labor**: Providers must manage patients' anxiety, fear, and uncertainty while delivering technically accurate information

This high-contact nature means that **interpersonal quality**—how providers communicate, show empathy, and build rapport—assumes disproportionate importance in healthcare compared to low-contact services like online banking (Dagger et al., 2007). Empirical evidence consistently shows that physician communication style and nursing staff courtesy are among the strongest predictors of patient satisfaction, often exceeding the influence of clinical outcomes (Ware et al., 1983; Clever et al., 2008).

**2. Information Asymmetry and Credence Qualities**

Healthcare services are characterized by extreme **information asymmetry**: patients typically lack the medical knowledge to evaluate the technical quality of diagnosis and treatment (Andaleeb, 2001). In economic terms, healthcare is a **credence good**—a product whose quality cannot be fully assessed even after consumption (Darby and Karni, 1973).

Consider a patient diagnosed with hypertension:
- The patient cannot independently verify whether the diagnosis is accurate
- The patient cannot assess whether the prescribed medication is optimal among alternatives
- Even after treatment, the patient may not know if health improvement resulted from the medication or other factors

This asymmetry creates a **substitution effect**: patients rely on **observable, functional attributes** (e.g., physician attentiveness, facility cleanliness, wait times) as **proxy indicators** of unobservable technical quality (Andaleeb, 2001). If a doctor spends 20 minutes explaining a diagnosis thoroughly, patients infer high competence; if a hospital is spotless, patients assume surgical precision.

This has profound implications for service quality assessment: **functional quality often dominates technical quality in patient evaluations**, not because functional aspects are objectively more important for health outcomes, but because they are more observable and thus more influential in shaping patient perceptions (Donabedian, 1988).

**3. Outcome Uncertainty and Risk**

Medical outcomes are inherently uncertain. Even with excellent care, patients may not recover; conversely, patients may improve despite suboptimal care due to natural healing processes (Berry and Bendapudi, 2007). This **outcome uncertainty** complicates quality assessment in two ways:

First, patients cannot reliably use **outcome quality** (health improvement) to infer **process quality** (medical care). A patient who recovers may still rate service poorly if they experienced long wait times or rude staff; a patient whose condition worsens may still rate service highly if providers were empathetic and communicative.

Second, because health consequences can be severe (disability, chronic illness, death), healthcare involves **high perceived risk** (Mitchell, 1999). This heightens patients' emotional sensitivity to service encounters, amplifying the impact of negative experiences (e.g., a dismissive comment from a nurse may be remembered more vividly than hours of competent care).

**4. Involuntary Consumption and Limited Choice**

Unlike discretionary services (restaurants, hotels), healthcare consumption is often **involuntary**—patients seek care due to illness or injury, not for enjoyment (Berry and Bendapudi, 2007). Furthermore, choice may be constrained by:

- **Insurance networks**: In the U.S., patients' provider choices are limited by insurance plans
- **Geographic accessibility**: Rural patients may have few local options
- **Urgency**: Emergency patients cannot "shop around"
- **Specialist referrals**: Patients may be directed to specific specialists

This limited choice means that **patient satisfaction does not perfectly align with service quality**. A patient may be dissatisfied but continue using a hospital due to lack of alternatives. Conversely, hospitals may have less competitive pressure to improve quality if patients cannot easily switch providers.

### Technical Quality vs. Functional Quality: The Dual Pathways

Building on Grönroos' (1984) foundational distinction, healthcare researchers have extensively studied how technical and functional quality independently and jointly influence patient outcomes.

**Defining the Constructs**

- **Technical Quality (Clinical Quality)**: The accuracy and appropriateness of medical diagnosis, treatment, and procedures. This includes adherence to evidence-based protocols, clinical outcomes (e.g., infection rates, readmission rates), and professional competence. Technical quality is what Donabedian (1988) termed "outcome quality"—the actual health improvement achieved.

- **Functional Quality (Service Delivery Quality)**: The manner in which healthcare is delivered. This encompasses interpersonal interactions (communication, empathy, respect), administrative processes (appointment scheduling, wait times, billing), and physical environment (facility cleanliness, comfort, equipment modernity). Functional quality corresponds to Donabedian's "process quality."

**Empirical Evidence on Differential Effects**

A large body of empirical research has examined the relative importance of technical vs. functional quality:

1. **Patient satisfaction is more strongly influenced by functional quality** (Chang et al., 2013; Andaleeb, 2001)
   - Ware et al. (1983): In a study of 1,800 patients, physician communication and interpersonal manner explained 30% of satisfaction variance, while technical competence explained only 9%
   - Clever et al. (2008): Empathetic communication increased satisfaction scores by 1.2 points (on a 5-point scale), equivalent to eliminating a 30-minute wait time

2. **Technical quality matters more for objective health outcomes** (Donabedian, 1988)
   - Hospital infection rates, surgical mortality, and readmission rates correlate strongly with adherence to clinical protocols (technical quality) but show weak correlations with patient satisfaction (functional quality)

3. **The two dimensions are not substitutable** (Dagger et al., 2007)
   - Excellent interpersonal care cannot compensate for poor clinical outcomes
   - Conversely, technically successful treatment delivered with poor communication still yields low patient satisfaction
   - **Implication**: Hospitals must excel at both dimensions; strength in one does not offset weakness in the other

**Why Functional Quality Dominates Patient Perceptions**

Three mechanisms explain why functional quality disproportionately influences patient evaluations despite technical quality being medically more consequential:

1. **Observability**: Patients can directly evaluate wait times, staff politeness, and facility cleanliness, but lack expertise to assess diagnostic accuracy (Andaleeb, 2001)

2. **Immediacy**: Functional failures (e.g., long waits, rude staff) are experienced in real-time during the service encounter, while technical failures may only become apparent later or remain undetected (Berry and Bendapudi, 2007)

3. **Emotional salience**: Negative interpersonal interactions trigger stronger emotional reactions (anger, humiliation) than abstract technical concerns (Chang et al., 2013)

### Determinants of Patient Satisfaction: Beyond Quality Dimensions

While service quality is a primary driver of patient satisfaction, research has identified additional determinants:

**1. Expectation Disconfirmation**

Following Oliver's (1980) expectation-disconfirmation theory, satisfaction is determined not by absolute quality but by the gap between expectations and perceptions. A rural clinic with modest facilities may yield high satisfaction if it exceeds patients' low expectations, while a prestigious academic hospital may disappoint patients with inflated expectations (Fisk et al., 1990).

**Cross-cultural implication**: Taiwanese and American patients may have different baseline expectations shaped by their respective healthcare systems (universal coverage vs. market-based), potentially leading to different satisfaction levels for objectively similar service quality.

**2. Outcome Valence**

Patients who experience positive health outcomes (symptom relief, successful surgery) rate service quality more favorably, even when controlling for actual service delivery (Ware et al., 1983). This **outcome bias** means that satisfaction partially reflects clinical results, not just service processes.

**3. Patient Characteristics**

Demographic and psychographic factors moderate quality perceptions:
- **Age**: Older patients report higher satisfaction, possibly due to lower expectations or greater gratitude (Hall and Dornan, 1988)
- **Education**: Highly educated patients may be more critical and expect more detailed communication (Kane et al., 1997)
- **Health status**: Sicker patients may be more forgiving if they perceive providers are trying to help (Ware et al., 1983)

**4. Prior Experience and Loyalty**

Repeat patients evaluate service more leniently than first-time patients, suggesting that **familiarity** and **trust accumulation** buffer against isolated negative experiences (Zeithaml et al., 1996).

### Why Exploratory Methods Are Necessary

The preceding review demonstrates that while theoretical frameworks (SERVQUAL, Brady & Cronin's hierarchical model, Dagger et al.'s four dimensions) provide valuable conceptual foundations, they suffer from **three limitations that necessitate exploratory, data-driven approaches**:

**Limitation 1: Predetermined Dimensions May Miss Context-Specific Concerns**

SERVQUAL's five dimensions were derived from focus groups in repair/maintenance, banking, long-distance telephone, securities brokerage, and credit card services—**not healthcare** (Parasuraman et al., 1988). While adaptations exist (e.g., Dagger et al., 2007), these were developed in specific healthcare contexts (Australia, U.S.) and may not capture concerns unique to other settings.

For example:
- Taiwan's National Health Insurance system may generate unique concerns about **referral processes** or **freedom to choose specialists**—issues less salient in the U.S. where insurance networks impose stricter constraints
- The COVID-19 pandemic introduced new dimensions (**infection control, telemedicine quality**) not present in pre-2020 frameworks
- Cultural factors may elevate certain dimensions (e.g., **physician authority** in high power-distance cultures like Taiwan vs. **shared decision-making** in low power-distance cultures like the U.S.)

**Solution**: Inductive topic modeling allows dimensions to emerge from patient narratives rather than being imposed by researchers.

**Limitation 2: Survey Instruments Constrain Patient Expression**

Likert-scale surveys (e.g., "Rate the friendliness of staff on a 1-5 scale") force patients to evaluate predetermined attributes. Patients cannot introduce new concerns or describe experiences in their own words. If a patient's primary complaint is **parking availability**—an issue not included in the survey—it goes unrecorded.

**Solution**: Online reviews are **unsolicited, open-ended patient narratives** where patients freely choose what aspects to discuss, revealing their authentic priorities.

**Limitation 3: Cross-Cultural Invariance Assumptions**

Applying the same survey instrument (e.g., SERVQUAL) across cultures assumes **dimensional equivalence**—that the same dimensions exist and carry the same meaning in both contexts (Steenkamp and Baumgartner, 1998). However:

- **Semantic non-equivalence**: The concept of "empathy" may be culturally interpreted differently
- **Dimensional non-equivalence**: Some dimensions may exist in one culture but not another (e.g., "family accommodation" may be critical in collectivist cultures where family involvement in care is expected, but absent in individualist cultures)

**Solution**: Rather than imposing identical dimensional structures on Taiwan and U.S. data, we use LDA to **independently discover** dimensions in each country, then **compare** whether similar or different structures emerge—a more appropriate approach for exploratory cross-cultural research.

### Summary: Theoretical Foundations for the Present Study

This section establishes the following theoretical scaffolding:

1. **Service quality is multidimensional** (Parasuraman et al., 1985, 1988), requiring measurement across multiple attributes rather than a single global rating

2. **Healthcare service quality has unique characteristics** (Berry & Bendapudi, 2007)—high-contact, information asymmetry, outcome uncertainty—that differentiate it from generic services

3. **Functional quality disproportionately influences patient perceptions** (Chang et al., 2013; Andaleeb, 2001) due to observability, even though technical quality is medically more consequential

4. **The number and nature of dimensions are context-dependent** (Ladhari, 2009), varying across industries, cultures, and institutional settings

5. **Predetermined frameworks (SERVQUAL) may miss emergent, context-specific concerns** (Buttle, 1996), justifying exploratory, data-driven approaches

These principles lead to our research design: using **Latent Dirichlet Allocation (LDA) topic modeling** on patient-generated online reviews to **inductively discover** service quality dimensions in Taiwan and the United States, comparing whether the same or different dimensional structures emerge across the two healthcare systems and cultural contexts.

The next section reviews cross-cultural service quality research to develop expectations about how cultural and institutional differences between Taiwan and the U.S. may shape service quality dimensions.

---

## References for Section 2.1

Andaleeb, S.S. (2001). Service quality perceptions and patient satisfaction: a study of hospitals in a developing country. *Social Science & Medicine*, 52(9), 1359-1370.

Avkiran, N.K. (1994). Developing an instrument to measure customer service quality in branch banking. *International Journal of Bank Marketing*, 12(6), 10-18.

Berry, L.L., & Bendapudi, N. (2007). Health care: a fertile field for service research. *Journal of Service Research*, 10(2), 111-122.

Brady, M.K., & Cronin, J.J. (2001). Some new thoughts on conceptualizing perceived service quality: a hierarchical approach. *Journal of Marketing*, 65(3), 34-49.

Buttle, F. (1996). SERVQUAL: review, critique, research agenda. *European Journal of Marketing*, 30(1), 8-32.

Chang, C.S., Chen, S.Y., & Lan, Y.T. (2013). Service quality, trust, and patient satisfaction in interpersonal-based medical service encounters. *BMC Health Services Research*, 13(1), 1-11.

Choi, K.S., Cho, W.H., Lee, S., Lee, H., & Kim, C. (2004). The relationships among quality, value, satisfaction and behavioral intention in health care provider choice: A South Korean study. *Journal of Business Research*, 57(8), 913-921.

Clever, S.L., Jin, L., Levinson, W., & Meltzer, D.O. (2008). Does doctor–patient communication affect patient satisfaction with hospital care? Results of an analysis with a novel instrumental variable. *Health Services Research*, 43(5p1), 1505-1519.

Cronin, J.J., & Taylor, S.A. (1992). Measuring service quality: a reexamination and extension. *Journal of Marketing*, 56(3), 55-68.

Dabholkar, P.A., Thorpe, D.I., & Rentz, J.O. (1996). A measure of service quality for retail stores: scale development and validation. *Journal of the Academy of Marketing Science*, 24(1), 3-16.

Dagger, T.S., Sweeney, J.C., & Johnson, L.W. (2007). A hierarchical model of health service quality: scale development and investigation of an integrated model. *Journal of Service Research*, 10(2), 123-142.

Darby, M.R., & Karni, E. (1973). Free competition and the optimal amount of fraud. *Journal of Law and Economics*, 16(1), 67-88.

Donabedian, A. (1988). The quality of care: How can it be assessed? *JAMA*, 260(12), 1743-1748.

Fisk, T.A., Brown, C.J., Cannizzaro, K., & Naftal, B. (1990). Creating patient satisfaction and loyalty. *Journal of Health Care Marketing*, 10(2), 5-15.

Grönroos, C. (1984). A service quality model and its marketing implications. *European Journal of Marketing*, 18(4), 36-44.

Hall, J.A., & Dornan, M.C. (1988). What patients like about their medical care and how often they are asked: a meta-analysis of the satisfaction literature. *Social Science & Medicine*, 27(9), 935-939.

Kane, R.L., Maciejewski, M., & Finch, M. (1997). The relationship of patient satisfaction with care and clinical outcomes. *Medical Care*, 35(7), 714-730.

Kettinger, W.J., & Lee, C.C. (1994). Perceived service quality and user satisfaction with the information services function. *Decision Sciences*, 25(5‐6), 737-766.

Ladhari, R. (2009). A review of twenty years of SERVQUAL research. *International Journal of Quality and Service Sciences*, 1(2), 172-198.

Mitchell, V.W. (1999). Consumer perceived risk: conceptualizations and models. *European Journal of Marketing*, 33(1/2), 163-195.

Oliver, R.L. (1980). A cognitive model of the antecedents and consequences of satisfaction decisions. *Journal of Marketing Research*, 17(4), 460-469.

Parasuraman, A., Zeithaml, V.A., & Berry, L.L. (1985). A conceptual model of service quality and its implications for future research. *Journal of Marketing*, 49(4), 41-50.

Parasuraman, A., Zeithaml, V.A., & Berry, L.L. (1988). SERVQUAL: A multiple-item scale for measuring consumer perceptions of service quality. *Journal of Retailing*, 64(1), 12-40.

Steenkamp, J.B.E., & Baumgartner, H. (1998). Assessing measurement invariance in cross-national consumer research. *Journal of Consumer Research*, 25(1), 78-90.

Ware, J.E., Snyder, M.K., Wright, W.R., & Davies, A.R. (1983). Defining and measuring patient satisfaction with medical care. *Evaluation and Program Planning*, 6(3-4), 247-263.

Zeithaml, V.A., Berry, L.L., & Parasuraman, A. (1996). The behavioral consequences of service quality. *Journal of Marketing*, 60(2), 31-46.
