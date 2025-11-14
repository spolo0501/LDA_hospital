# 文獻批次下載指南

## 📊 統計資訊

- **總文獻數**: 75 篇
- **期刊論文**: 56 篇 (可下載)
- **書籍**: 5 本
- **研究報告**: 6 份
- **會議論文**: 4 篇

---

## 🎯 推薦下載方法（按優先順序）

### 方法 1: 透過學校圖書館代理（最推薦）

假設你的學校有訂閱這些期刊，這是最合法且最可靠的方法。

#### 步驟：

1. **確認已連接學校 VPN** ✅ (你已完成)

2. **使用學校圖書館的期刊資料庫**
   - 常見資料庫：
     - Web of Science
     - ProQuest
     - EBSCO
     - JSTOR
     - ScienceDirect
     - Wiley Online Library
     - Springer Link
     - SAGE Journals

3. **搜尋並下載**
   - 方式 A: 在資料庫中搜尋文章標題
   - 方式 B: 使用 DOI 直接存取
   - 方式 C: 透過期刊名稱 → 卷期 → 文章

---

### 方法 2: 透過 Google Scholar（次推薦）

Google Scholar 常常會顯示免費的 PDF 連結（如果有的話）。

#### 步驟：

1. 開啟 `pdfs/_download_list.txt`
2. 點擊每篇文章的 Google Scholar 連結
3. 在搜尋結果右側尋找 **[PDF]** 按鈕
4. 如果有 [PDF] 按鈕，直接下載
5. 如果沒有，點擊標題連結，通常會透過學校代理自動登入

---

### 方法 3: 使用自動化工具

我為你準備了幾個自動化選項：

#### 選項 A: 使用 Zotero（推薦）

Zotero 有很好的自動 PDF 下載功能：

1. **安裝 Zotero**
   ```bash
   brew install --cask zotero
   ```

2. **匯入 RIS 檔案**
   - 在 Zotero 中：File → Import → 選擇 `all_references.ris`

3. **設定學校代理**
   - Edit → Preferences → Advanced → Network
   - 設定你學校的 Proxy 伺服器

4. **批次下載 PDF**
   - 選擇所有文獻
   - 右鍵 → Find Available PDFs
   - Zotero 會自動搜尋並下載

#### 選項 B: 使用 Bookends + Papers

如果你用 Bookends：

1. 匯入 RIS 檔案到 Bookends
2. 使用 Papers 應用程式整合
3. Papers 會自動搜尋 PDF

---

### 方法 4: Sci-Hub（備用方案）

⚠️ **注意**: Sci-Hub 的合法性在某些地區有爭議，請自行判斷是否使用。

1. 開啟 `pdfs/_download_list.txt`
2. 每篇文章都有 Sci-Hub 連結
3. 點擊連結通常可以直接下載 PDF

---

## 🤖 半自動化下載腳本

我為你準備了一個半自動化的下載腳本，可以：
- 透過 DOI 自動查找 PDF
- 透過 Google Scholar 查找免費 PDF
- 生成下載報告

### 使用方式：

```bash
cd manuscripts/references
python3 download_papers.py
```

這個腳本會：
1. ✅ 自動下載有直接 PDF 連結的文獻
2. 📝 為無法自動下載的文獻生成清單
3. 🔗 提供 Google Scholar 和 Sci-Hub 連結

---

## 📁 下載後的檔案組織

建議的檔案結構：

```
manuscripts/references/
├── all_references.ris          # RIS 文獻檔案（已完成）
├── pdfs/                       # PDF 存放目錄（已建立）
│   ├── Blei_2003_Latent_Dirichlet_allocation.pdf
│   ├── Brady_2001_Some_new_thoughts...pdf
│   └── ... (其他 PDF)
├── _download_list.txt          # 下載清單（已生成）
└── download_papers.py          # 下載腳本（已建立）
```

---

## 🎯 最重要的文獻（優先下載）

以下是你論文中最常引用的核心文獻，建議優先下載：

### 理論基礎類（10 篇）

1. **Parasuraman et al. (1988)** - SERVQUAL
   - Journal of Retailing, 64(1), 12-40

2. **Parasuraman et al. (1985)** - Service quality conceptual model
   - Journal of Marketing, 49(4), 41-50

3. **Brady & Cronin (2001)** - Hierarchical service quality
   - Journal of Marketing, 65(3), 34-49

4. **Dagger et al. (2007)** - Healthcare service quality model
   - Journal of Service Research, 10(2), 123-142

5. **Hofstede (1980, 2001)** - Culture's consequences
   - Book (請從圖書館借閱或購買)

6. **Furrer et al. (2000)** - Culture and service quality
   - Journal of Service Research, 2(4), 355-371

7. **Donabedian (1988)** - Quality of care assessment
   - JAMA, 260(12), 1743-1748

8. **Berry & Bendapudi (2007)** - Healthcare service research
   - Journal of Service Research, 10(2), 111-122

9. **Grönroos (1984)** - Service quality model
   - European Journal of Marketing, 18(4), 36-44

10. **Donthu & Yoo (1998)** - Cultural influences on service quality
    - Journal of Service Research, 1(2), 178-186

### 方法論類（5 篇）

11. **Blei et al. (2003)** - Latent Dirichlet Allocation
    - Journal of Machine Learning Research, 3, 993-1022

12. **Blei (2012)** - Probabilistic topic models
    - Communications of the ACM, 55(4), 77-84

13. **Ranard et al. (2016)** - Yelp reviews of hospital care
    - Health Affairs, 35(4), 697-705

14. **Hao & Zhang (2016)** - Chinese health consumers voice
    - Journal of Medical Internet Research, 18(5), e108

15. **Steenkamp & Baumgartner (1998)** - Measurement invariance
    - Journal of Consumer Research, 25(1), 78-90

### 台美醫療系統類（5 篇）

16. **Yoon & Cheng (2021)** - Taiwan-USA hospital comparison ⭐ 最重要
    - Health Services Research, 56(6), 1182-1193
    - DOI: 10.1111/1475-6773.13872

17. **Cheng (2015)** - Taiwan's NHI 20th anniversary
    - Health Affairs, 34(3), 502-510

18. **Cheng & Chiang (2012)** - Universal health insurance effect
    - JAMA, 278(2), 89-93

19. **Tai-Seale et al. (2007)** - Time allocation in primary care
    - Health Services Research, 42(5), 1871-1894

20. **Tikkanen et al. (2020)** - US healthcare system profile
    - Commonwealth Fund Report

---

## 💡 下載技巧

### 技巧 1: 批次下載
- 不要一次下載全部，分批下載（每次 10-15 篇）
- 避免觸發網站的反爬蟲機制

### 技巧 2: 使用瀏覽器擴充功能
- **Zotero Connector** - 在瀏覽器中一鍵儲存文獻
- **Unpaywall** - 自動尋找免費的合法 PDF

### 技巧 3: DOI 查詢
- 許多文獻可以透過 DOI 直接存取
- 格式：https://doi.org/[DOI]
- 例如：https://doi.org/10.1111/1475-6773.13872

### 技巧 4: 利用 ResearchGate
- 很多作者會在 ResearchGate 上傳自己的論文
- 可以直接搜尋作者名稱和論文標題

---

## ⚠️ 常見問題

### Q1: 某些期刊學校沒有訂閱怎麼辦？
**A**: 可以試試：
1. 館際互借（ILL - Interlibrary Loan）
2. 聯繫作者索取 PDF（通常作者很願意分享）
3. 使用 ResearchGate 請求全文

### Q2: 下載的 PDF 檔案名稱很亂？
**A**: 我的腳本已經自動生成了規範的檔案名稱：
- 格式：`作者_年份_標題.pdf`
- 例如：`Blei_2003_Latent_Dirichlet_allocation.pdf`

### Q3: 如何確認已下載的文獻？
**A**: 使用以下指令：
```bash
cd manuscripts/references/pdfs
ls -1 | wc -l  # 顯示已下載數量
```

---

## 📞 需要協助？

如果在下載過程中遇到問題：

1. 檢查 VPN 連線是否正常
2. 確認學校圖書館訂閱狀況
3. 聯繫圖書館員尋求協助
4. 使用 Google Scholar 尋找替代來源

---

## ✅ 下載完成檢查清單

- [ ] 已連接學校 VPN
- [ ] 已下載所有 56 篇期刊論文
- [ ] 已下載 20 篇核心文獻
- [ ] PDF 檔案已按規範命名
- [ ] 已匯入 Bookends 或 Zotero
- [ ] 已檢查 PDF 內容完整性

---

**最後更新**: 2025-11-13
**下載清單位置**: `manuscripts/references/pdfs/_download_list.txt`
**PDF 存放位置**: `manuscripts/references/pdfs/`
