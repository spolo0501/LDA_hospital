# 章節協作流程指南

## 目的
定義 GPT 與 Claude Code 在論文寫作中的明確分工，確保高效協作且避免文獻錯誤。

---

## 📂 檔案命名與存放位置

### 主要檔案（正式版本）
```
manuscripts/
├── Chapter_1_Introduction.md          # 第一章（正式版）
├── Chapter_2_Literature_Review.md     # 第二章（正式版）
├── Chapter_3_Methodology.md           # 第三章（正式版）
├── Chapter_4_Results.md                # 第四章（正式版）
├── Chapter_5_Conclusions.md            # 第五章（正式版）
└── Full_Manuscript.md                  # 完整論文（整合版，可選）
```

### 臨時檔案（GPT 初稿）
```
manuscripts/drafts/
├── Chapter_2_gpt_draft.md             # GPT 生成的 Chapter 2 初稿
├── Chapter_3_gpt_draft.md             # GPT 生成的 Chapter 3 初稿
└── ...
```

### 備份檔案
```
manuscripts/versions/
├── Chapter_1_v1_codex_20251112.md
├── Chapter_2_v1_original_20251112.md
└── ...
```

---

## 🔄 標準協作流程（每個章節適用）

### Step 1：GPT 撰寫初稿
**由您操作**：
1. 在 GPT 中撰寫章節內容
2. 特別注意文獻引用的正確性
3. 完成後複製完整內容

**檔案命名**：
- 如果是新章節：複製到 `manuscripts/Chapter_X_[ChapterName].md`
- 如果是修訂版：複製到 `manuscripts/drafts/Chapter_X_gpt_draft.md`

---

### Step 2：通知 Claude Code 進行檢查
**您告訴我**：
```
請檢查 Chapter_2_Literature_Review.md，重點檢查：
1. 邏輯錯誤
2. 文獻引用正確性
3. 補充參考文獻列表
```

**我會執行的檢查清單**：

#### ✅ 檢查 1：邏輯一致性
- [ ] 段落之間的邏輯連貫性
- [ ] 論述是否有跳躍或矛盾
- [ ] 研究問題與文獻回顧的對應性
- [ ] 與其他章節的連貫性（如 RQs 在各章是否一致）

#### ✅ 檢查 2：文獻引用正確性（**重點**）
- [ ] **引用格式**：APA 7th 格式是否正確
- [ ] **作者姓名**：是否拼寫正確
- [ ] **年份**：是否與 References 一致
- [ ] **引用位置**：是否合理（避免濫用或錯置）
- [ ] **引用內容**：簡要確認引用的論述是否合理（不會去查原文，但會標記可疑處）

**我會標記的問題範例**：
```
⚠️ 可能問題：
- Line 45: "Smith (2020)" 在 References 中找不到
- Line 67: "(Jones et al., 2019)" 格式錯誤，應為 "Jones et al. (2019)"
- Line 89: 引用 "Brady & Cronin (2001)" 但論述內容似乎不符（建議您確認）
```

#### ✅ 檢查 3：補充 References
- [ ] 將所有內文引用整理到 References 段落
- [ ] 按照 APA 7th 格式統一排版
- [ ] 字母順序排序
- [ ] 確認格式一致性（斜體、標點、縮排等）

#### ✅ 檢查 4：版本備份
- [ ] 自動備份到 `versions/` 目錄
- [ ] 更新 `VERSION_CONTROL.md`

---

### Step 3：我回報檢查結果
**我會提供的報告格式**：

```markdown
## 檢查報告：Chapter 2 Literature Review

### ✅ 通過項目
- 段落邏輯連貫
- 與 Chapter 1 的 RQs 對應正確
- 整體架構完整

### ⚠️ 需要確認的問題

#### 1. 文獻引用問題（3 處）
- **Line 45**: "Smith (2020)" 在 References 中找不到
  - 建議：請確認是否應為 "Smith (2021)" 或刪除此引用

- **Line 89**: 引用 "Brady & Cronin (2001)" 討論 SERVQUAL
  - 可疑原因：Brady & Cronin (2001) 主要討論階層模型，非 SERVQUAL
  - 建議：確認是否應引用 "Parasuraman et al. (1988)"

- **Line 120**: "(Johnson, 2019, p. 45)" 包含頁碼
  - 提醒：APA 7th 一般引用不需頁碼（除非直接引述）

#### 2. 邏輯問題（1 處）
- **Line 67-68**: 提到 "three gaps" 但只列出兩個
  - 建議：補充第三個 gap 或改為 "two gaps"

### ✅ 已完成修正
- 補充 15 筆參考文獻到 References
- 統一 APA 7th 格式
- 建立備份：`versions/Chapter_2_v1_20251112.md`

### 📋 建議下一步
1. 請您確認上述 3 處文獻引用問題
2. 確認後告訴我，我會進行最終修正
3. 或者您可以直接在 GPT 修正後再貼回來
```

---

### Step 4：您決定如何處理
**選項 A**：您在 GPT 修正後再貼回來
```
我已經在 GPT 修正了，請重新檢查 Chapter_2_Literature_Review.md
```

**選項 B**：您確認問題後由我直接修正
```
Line 45 應該刪除，Line 89 改為 Parasuraman et al. (1988)，請幫我修正
```

**選項 C**：您確認沒問題
```
這些引用都是正確的，請直接更新版本記錄
```

---

## 🛡️ 文獻引用保護機制

### 我會做的檢查（自動）
1. **交叉比對**：內文引用 vs. References 列表
2. **格式檢查**：APA 7th 格式是否正確
3. **常見錯誤**：
   - 作者姓名拼寫不一致
   - 年份不一致
   - et al. 使用錯誤（2 位作者不用 et al.）
   - 標點符號錯誤（& vs. and）

### 我**不會**做的事（避免誤判）
❌ 不會去查原文確認引用內容是否正確
❌ 不會主動改變您的論述邏輯
❌ 不會刪除看起來「可疑」的引用（只會標記）

### 您需要確認的事
✅ 引用的研究內容是否正確
✅ 引用的位置是否恰當
✅ 是否有更合適的文獻

---

## 📝 實際範例

### 範例：Chapter 2 協作流程

#### 您的操作
```
1. 在 GPT 完成 Chapter 2 的撰寫
2. 複製內容到 Chapter_2_Literature_Review.md
3. 告訴我：「請檢查 Chapter 2」
```

#### 我的操作
```
1. 讀取 Chapter_2_Literature_Review.md
2. 執行 4 項檢查
3. 生成檢查報告
4. 標記需要確認的問題
```

#### 您的回應
```
情境 A：「Line 89 確實有誤，請改為 Parasuraman et al. (1988)」
情境 B：「這些引用都正確，請繼續」
情境 C：「我回 GPT 修正後再給你」
```

#### 我的最終動作
```
1. 執行您確認的修正（如有）
2. 補充完整的 References
3. 建立備份
4. 更新 VERSION_CONTROL.md
```

---

## 🚨 常見文獻錯誤與預防

### 類型 1：張冠李戴（引用內容錯誤）
**範例**：
```
錯誤：Brady & Cronin (2001) developed SERVQUAL...
正確：Parasuraman et al. (1988) developed SERVQUAL...
```
**預防**：GPT 撰寫時請明確指定要引用的研究

---

### 類型 2：年份錯誤
**範例**：
```
內文：Smith (2020)
References：Smith, J. (2021). ...
```
**預防**：我會自動交叉檢查並標記

---

### 類型 3：格式不一致
**範例**：
```
錯誤：Smith and Jones (2020)
正確：Smith & Jones (2020)
```
**預防**：我會自動統一為 APA 7th 格式

---

### 類型 4：漏列或多列 References
**範例**：
```
問題 A：內文引用了 "Chen (2019)" 但 References 沒有
問題 B：References 有 "Lee (2018)" 但內文沒引用
```
**預防**：我會標記不一致處，您決定是補充或刪除

---

## 🔧 工具與指令

### 快速指令（您可以使用）

```bash
# 檢查特定章節
「請檢查 Chapter_2_Literature_Review.md」

# 只檢查文獻
「請檢查 Chapter 3 的文獻引用」

# 比較兩個版本
「請比較 Chapter_2_Literature_Review.md 和 drafts/Chapter_2_gpt_draft.md」

# 整合檢查
「請檢查 Chapter 1-5 的 RQs 是否一致」
```

---

## 📊 檢查清單範本

每次檢查時我會使用此清單：

```markdown
## Chapter X 檢查清單

### 邏輯檢查
- [ ] 段落邏輯連貫
- [ ] 與其他章節一致
- [ ] 研究問題對應正確

### 文獻檢查
- [ ] 內文引用格式正確
- [ ] References 完整無遺漏
- [ ] 引用位置合理
- [ ] 無明顯張冠李戴

### 技術檢查
- [ ] 版本備份完成
- [ ] VERSION_CONTROL.md 更新
- [ ] 檔案命名正確

### 需要確認的問題
- [ ] [列出所有可疑問題]
```

---

## 🎯 流程總結

| 步驟 | 負責人 | 任務 | 輸出 |
|-----|-------|------|------|
| 1 | 您 + GPT | 撰寫章節內容 | Markdown 檔案 |
| 2 | 您 | 複製到指定位置 | `Chapter_X.md` |
| 3 | 您 | 通知 Claude Code | 「請檢查 Chapter X」 |
| 4 | Claude Code | 執行 4 項檢查 | 檢查報告 |
| 5 | 您 | 確認問題 | 修正指示 |
| 6 | Claude Code | 執行修正與備份 | 最終版本 |

---

## ❓ 常見問題

### Q1：如果我只想改一小段，也要完整流程嗎？
**A**：小修改可以直接告訴我：
```
請把 Chapter 2 第 3 段的 "Smith (2020)" 改為 "Smith (2021)"
```
我會直接修改並確認 References 是否需要更新。

---

### Q2：如果我不確定引用是否正確怎麼辦？
**A**：標記給我檢查：
```
Chapter 2 Line 89 引用 Brady & Cronin (2001) 討論 SERVQUAL，
但我不確定是否正確，請幫我檢查
```
我會標記為「需確認」，您可以回 GPT 問或自己查證。

---

### Q3：可以一次檢查多個章節嗎？
**A**：可以，但建議分開：
```
推薦：「請檢查 Chapter 2」→ 確認 → 「請檢查 Chapter 3」
可行：「請檢查 Chapter 2 和 Chapter 3」（但報告會較長）
```

---

### Q4：如果發現 References 有重複怎麼辦？
**A**：我會自動去重並告知：
```
⚠️ 發現重複文獻：
- Parasuraman et al. (1988) 出現 2 次（Line 23 和 Line 67）
已自動合併為 1 筆
```

---

## 📌 重要提醒

### ✅ 您應該做的
1. 在 GPT 撰寫時就注意文獻引用的準確性
2. 複製內容時確認完整（包括 References）
3. 對我的檢查報告進行確認（特別是文獻問題）

### ✅ 我會做的
1. 檢查邏輯、格式、一致性
2. 標記可疑的文獻引用
3. 補充和整理 References
4. 版本管理和備份

### ❌ 我不會做的
1. 改變您的論述風格
2. 主動刪除「看起來奇怪」的內容
3. 未經確認就修改文獻引用

---

## 📅 版本記錄

- **2025-11-12**：初始版本，定義 GPT + Claude Code 協作流程
- **重點**：文獻引用保護機制，避免 GPT 可能的「幻覺」引用

---

**最後更新**：2025-11-12
**維護者**：Simon + Claude Code
