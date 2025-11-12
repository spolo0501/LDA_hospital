# 學術寫作風格指南

## 目的
確保論文各章節保持一致的寫作風格，符合 SSCI 頂級期刊標準。

---

## 核心原則

### ✅ 推薦做法

1. **簡潔性（Conciseness）**
   - 段落長度：100-130 字為佳
   - 句子長度：平均 20-25 字
   - 避免冗長的背景說明和過多細節

2. **精準性（Precision）**
   - 用精確的學術用語，避免模糊表達
   - 範例：
     - ✅ "a persistent challenge"（精準）
     - ❌ "one of the most pressing challenges"（過度強調）

3. **直接性（Directness）**
   - 直接陳述研究問題和貢獻
   - 避免過度鋪陳和「暖場」
   - 範例：
     - ✅ "Three gaps limit current understanding."（直接）
     - ❌ "There are three critical gaps that constrain theoretical and practical progress."（冗長）

4. **批判性（Critical Engagement）**
   - 引用文獻時應指出其局限性
   - 範例：
     - ✅ "However, their study relied on structured surveys with predefined dimensions, limiting..."
     - ❌ "Yoon and Cheng (2021) found that..."（只陳述，無批判）

---

### ❌ 避免做法

1. **過度細節（Over-detailing）**
   - ❌ 列舉所有保險類型（Medicare, Medicaid, employer-sponsored...）
   - ✅ 用概括性描述（"combines private, employer-based, and government insurance programs"）

2. **冗長句式（Long Sentences）**
   - ❌ 單句超過 40 字
   - ✅ 拆成兩句，邏輯更清晰

3. **非正式用語（Informal Language）**
   - ❌ "system tax"（比喻性用語）
   - ✅ "financial complexity and administrative burden"（學術用語）

4. **過度使用被動語態（Excessive Passive Voice）**
   - ❌ "It is recognized that..."
   - ✅ "We recognize that..."

---

## 段落結構範例

### 理想段落結構（以 Introduction 第 2 段為例）

```
1. Topic sentence（主題句）：點出段落主旨
2. Context（背景）：簡要說明背景
3. Contrast/Comparison（對比）：如適用
4. Implication（意涵）：段落結論
```

**範例**（GPT 版本）：
```
The contrasting structures of Taiwan's single-payer...offer an ideal context.
[主題句]

Both nations achieve strong health outcomes, yet patients navigate markedly
different pathways to care. [背景]

Taiwan's NHI provides...In contrast, the U.S. system combines... [對比]

The central theoretical issue is...—an underexplored question with important
policy implications. [意涵]
```

---

## Research Gap 陳述策略

### 有力的 Gap 陳述結構

```
[文獻回顧] → [識別局限] → [指出缺失] → [本研究如何填補]
```

**範例**：
```
Most studies remain single-country [文獻現況],
and cross-national comparisons often employ inconsistent methodologies [局限],
impeding direct comparison [後果].
To date, no research has applied identical computational methods... [缺失陳述]
```

---

## 文獻引用策略

### 引用目的優先順序

1. **建立 Gap**（最重要）
   - 引用 → 指出局限 → 本研究的價值

2. **建立理論基礎**
   - 引用經典文獻支持核心概念

3. **展示研究現況**
   - 概述領域內的主要發現

### 引用格式偏好

- ✅ 作者主語：Yoon and Cheng (2021) found...
- ✅ 括號引用：Healthcare quality varies widely (WHO, 2020)
- ❌ 過度引用：避免單句多次引用

---

## Claude Code 的角色定位

### Claude Code 應該做的事

1. ✅ 檢查邏輯一致性
2. ✅ 補充參考文獻格式
3. ✅ 確保章節間的連貫性
4. ✅ 版本控制和備份
5. ✅ 指出明顯的語法或邏輯錯誤

### Claude Code 應避免的事

1. ❌ 主動改寫 GPT 已精煉的句子
2. ❌ 增加不必要的細節
3. ❌ 改變已確定的寫作風格
4. ❌ 未經確認就大幅修改內容

**原則**：如果 GPT 版本已經簡潔清晰，Claude Code 只做「技術性修正」，不做「風格性改寫」。

---

## 目標期刊參考

根據 SSCI 頂級期刊（如 *Health Services Research*, *Journal of Service Research*）的風格：

- 段落：簡潔有力，避免冗長
- 語氣：客觀、精準、有批判性
- 句式：主動語態為主，短句優先
- 引用：目的明確，與論述緊密結合

---

## 版本記錄

- **2025-11-12**：初始版本，基於 GPT vs Codex 版本比較的經驗建立

---

**使用方式**：
1. Claude Code 在撰寫或修改內容前，參考此指南
2. 如需調整風格偏好，更新本文件並通知 Claude Code
3. 定期檢視，確保與實際需求一致
