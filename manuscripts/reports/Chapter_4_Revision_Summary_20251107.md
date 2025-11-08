# Chapter 4 Revision Summary
**Date**: 2025-11-07
**Purpose**: Strengthen methodological rigor of hypothesis testing by focusing only on defensible comparisons

---

## Key Problems Identified

### 1. **Semantic Equivalence Issue**
- **Problem**: We were comparing ratings across dimensions with only "Medium" semantic similarity
- **Example**: Taiwan's "Medical Professional Quality" (physicians + nurses, gratitude focus) vs. USA's "Nursing Care Quality" (nurses only, responsiveness focus)
- **Why problematic**: These measure partially different constructs (different personnel, different evaluation criteria)
- **User concern**: "這兩個比較好像也不完全正確，因為它是不同的構面"

### 2. **Too Many Weak Hypotheses**
- **Problem**: 11 hypotheses tested, but 5 had insufficient evidence (H3, H5, H6, IH3, IH5)
- **User concern**: "寫這麼多感覺有點混亂" - Too many hypotheses creates confusion
- **Solution**: Focus only on 4 hypotheses with strong, defensible evidence

---

## Major Revisions Made

### **Section 4.2.1: Universal Dimensions**

**Before**: Direct rating comparisons for all 4 universal dimensions without acknowledging semantic differences

**After**:
- ✅ **Emergency Care**: Full rating comparison (High semantic similarity = >70% overlap)
- ⚠️ **Professional/Nursing Care**: Rating difference noted but flagged as descriptive only (Medium similarity)
- ⚠️ **Outpatient Services**: Rating difference noted but not used for hypothesis testing (Medium similarity)
- ⚠️ **Inpatient/Critical Care**: Rating difference noted but not used for hypothesis testing (Medium similarity)

**Key addition**: "These dimensions measure partially different constructs (different personnel, different evaluation criteria), complicating direct rating comparison."

---

### **Section 4.2.3: Statistical Robustness → Methodological Considerations**

**Title changed** to reflect focus on methodology rather than just statistical significance

**New content**:
- Explicit semantic similarity criteria (High >70%, Medium 50-70%, Low <50%)
- Detailed explanation of why Medium-similarity dimensions can't support rating comparisons
- Statement: "Cross-national rating comparisons require semantic equivalence—dimensions must measure substantively similar constructs"
- Reference to cross-cultural methodology literature (Harkness et al., 2003)

---

### **Section 4.3: Hypothesis Testing (Complete Rewrite)**

#### **New Structure**

**4.3.1 Institutional Hypothesis: The "System Tax" (IH1)**
- **Method**: Presence vs. absence comparison
- **Evidence**: USA has billing/insurance dimension (4.1%), Taiwan has none
- **Conclusion**: ✓✓ Strongly Supported

**4.3.2 Cultural Hypothesis: Time Consciousness (H4)**
- **Method**: Chi-square test (proportion) + t-test (rating) **for High-similarity dimension only**
- **Evidence**:
  - Proportion: US 34.8% vs TW 30.9% (χ²=13.74, p<.001)
  - Rating: US 3.25★ vs TW 1.79★ (t=19.97, p<.001, d=0.782)
  - Linguistic: US uses "hour," "hours" prominently
- **Key justification**: "We compare the Emergency Care dimension—the only dimension achieving **High semantic similarity**"
- **Conclusion**: ✓✓ Strongly Supported

**4.3.3 Cultural Hypothesis: Interpersonal Sensitivity (H1, Revised)**
- **Method**: Presence vs. absence comparison **instead of rating comparison**
- **Evidence**: Taiwan has "Service Attitude Issues" dimension (17.3%), USA has none
- **Methodological note added**: "We deliberately avoid comparing Taiwan's Medical Professional Quality (4.67★) with USA's Nursing Care Quality (3.00★) despite statistical significance... These dimensions exhibit only Medium semantic similarity"
- **Conclusion**: ✓✓ Supported (cleaner evidence than rating comparison)

**4.3.4 Institutional Hypothesis: Administrative Complaints (IH4)**
- **Method**: Qualitative comparison of dimension content
- **Evidence**: Taiwan complains about process delays, USA complains about financial complexity
- **Conclusion**: ✓✓ Supported

**4.3.5 Hypotheses Not Tested**
- Explicitly lists H3, H5, H6, IH3, IH5 as requiring methods beyond LDA
- Acknowledges as study limitations
- Recommends for future research

**4.3.6 Theoretical Implications**
- (1) Institutional effects dominate dimensional composition
- (2) **Rating comparisons require semantic equivalence** (NEW KEY POINT)
- (3) Service quality is simultaneously universal and contingent

---

### **Table 4.3: Semantic Mapping (Modified)**

**Changed notation**:
- Emergency Care: Full statistical reporting (no marker)
- Other 3 dimensions: Parentheses + dagger symbol (†) to indicate descriptive status

**New table note**:
> "†Medium-similarity dimensions have different semantic foci; rating comparisons reported for descriptive purposes but not used for hypothesis testing (see Section 4.2.3). Only Emergency Care (High similarity) supports valid cross-national rating comparison."

---

### **Summary Section (Updated)**

**Added new paragraph on hypothesis testing**:
> "Four hypotheses received strong empirical support with rigorous methodological justification: IH1 (multi-payer system tax), H4 (American time consciousness), H1 (Taiwanese interpersonal sensitivity), and IH4 (system-specific administrative complaints). We tested only hypotheses where our data provide clear, defensible evidence—**relying on presence/absence comparisons and limiting rating comparisons to dimensions with High semantic similarity (emergency care only)**."

**New theoretical contribution added**:
> "(4) Cross-national comparison requires semantic equivalence—statistical significance alone does not justify rating comparisons across semantically distinct dimensions; (5) Presence/absence patterns provide cleaner evidence than rating comparisons when dimensions measure different constructs."

---

## Methodological Framework Established

### **Three Types of Valid Comparisons**

1. **Presence vs. Absence** (strongest evidence)
   - Example: US has billing dimension, Taiwan doesn't
   - No semantic equivalence required

2. **Proportion Differences** (requires same general domain)
   - Example: Emergency care 34.8% vs 30.9%
   - Chi-square test

3. **Rating Differences** (requires HIGH semantic similarity only)
   - Example: Emergency care 3.25★ vs 1.79★
   - Independent samples t-test
   - **Critical requirement**: >70% thematic overlap

### **Key Methodological Principle**

> "Statistical significance does not justify cross-national rating comparisons when dimensions measure different constructs"

---

## Word Count Changes

- **Before**: ~2,942 words
- **After**: ~4,100 words
- **Increase**: ~1,158 words (+39%)
- **Reason**: Added extensive methodological justification
- **Journal appropriateness**: Still reasonable length; stronger methods justify slightly longer section

---

## Files Modified

1. ✅ `Chapter_4_Results.md` - Complete revision
2. ✅ All sections internally consistent
3. ✅ Table 4.3 notation updated
4. ✅ Summary section aligned with new approach

---

## Key Strengths of Revised Approach

1. **Methodologically Defensible**: Only compares what can be validly compared
2. **Transparent**: Explicitly acknowledges limitations
3. **Conservative**: Avoids over-interpreting statistical significance
4. **Clear**: Separates High-similarity (valid comparison) from Medium-similarity (descriptive only)
5. **Still Strong**: 4 hypotheses with solid support is better than 11 with mixed quality

---

## User Feedback Addressed

✅ **"這兩個比較好像也不完全正確，因為它是不同的構面"**
→ Now explicitly acknowledge Medium-similarity dimensions measure different constructs

✅ **"寫這麼多感覺有點混亂"**
→ Reduced from 11 hypotheses to 4 with strong evidence

✅ **"我們能不能夠做一下篩選"**
→ Screened hypotheses to keep only those with clear, defensible evidence

✅ **"保留可以有強力證據支持的"**
→ Focused on IH1, H4, H1, IH4 with presence/absence or High-similarity evidence

✅ **"我們可能要寫清楚我們是怎麼做的"**
→ Added extensive methodological justification in Sections 4.2.3 and 4.3 intro

---

## Recommendation

**This revision is ready for journal submission.** The methodological conservatism strengthens rather than weakens the paper—reviewers will appreciate the careful attention to semantic equivalence and the transparent acknowledgment of what can and cannot be tested with topic modeling data.

**End of Revision Summary**
