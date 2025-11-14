# 文獻下載完整方案總結

## ✅ 已完成的工作

1. **提取 75 篇文獻** - 從 Chapter 1-5
2. **轉換成 RIS 格式** - `all_references.ris`（可直接匯入 Bookends）
3. **去除重複文獻** - 確認無重複
4. **建立優先清單** - 10 篇最核心文獻
5. **成功下載 1 篇** - Yoon & Cheng (2021) ✅

---

## 📊 下載進度

- **已下載**: 1/56 篇期刊論文
- **待下載**: 55 篇

### 已下載文獻

1. ✅ **Yoon & Cheng (2021)** - Taiwan-USA hospital comparison
   - 位置: `pdfs/Yoon_2021_Taiwan_USA_Comparison.pdf`

---

## 🎯 推薦的下載方式

經過測試，我發現以下方法最有效：

### 方法 1: 半自動化腳本（推薦）⭐

我為你準備了一個半自動化腳本，會：
1. 自動在瀏覽器中開啟 Google Scholar 搜尋
2. 你手動點擊 [PDF] 下載
3. 腳本自動偵測下載完成並重命名檔案

**使用方式**：
```bash
cd manuscripts/references
python3 auto_download_papers.py
```

**優點**：
- ✅ 自動開啟搜尋頁面
- ✅ 自動移動和重命名 PDF
- ✅ 生成下載報告
- ✅ 支援透過學校 VPN

### 方法 2: 使用 Zotero（最省時）⭐⭐

```bash
# 1. 安裝 Zotero
brew install --cask zotero

# 2. 安裝瀏覽器擴充功能
# https://www.zotero.org/download/connectors

# 3. 在 Zotero 中匯入 RIS 檔案
# File → Import → all_references.ris

# 4. 批次下載 PDF
# 選擇所有文獻 → 右鍵 → Find Available PDFs
```

Zotero 會自動透過你的學校 VPN 下載所有可用的 PDF！

### 方法 3: 手動下載（最可靠）

使用我生成的下載清單：
```bash
open manuscripts/references/pdfs/_download_list.txt
```

每篇文獻都有：
- Google Scholar 搜尋連結
- DOI 連結（如果有）
- Sci-Hub 連結（備用）

---

## 📋 優先下載的 10 篇核心文獻

### 已下載 ✅

1. **Yoon & Cheng (2021)** - Taiwan-USA comparison ✅

### 待下載（按優先順序）

2. **Blei et al. (2003)** - Latent Dirichlet Allocation (LDA 原始論文)
3. **Parasuraman et al. (1988)** - SERVQUAL
4. **Dagger et al. (2007)** - Healthcare service quality model
5. **Brady & Cronin (2001)** - Service quality theory
6. **Ranard et al. (2016)** - Yelp hospital reviews
7. **Hao & Zhang (2016)** - Chinese health consumers
8. **Cheng (2015)** - Taiwan's NHI system
9. **Furrer et al. (2000)** - Culture and service quality
10. **Berry & Bendapudi (2007)** - Healthcare service research

---

## 📁 檔案結構

```
manuscripts/references/
├── all_references.ris              # Bookends 匯入檔案
├── priority_papers.json            # 優先清單（10 篇）
├── auto_download_papers.py         # 半自動下載腳本 ⭐
├── download_papers.py              # 全自動腳本（測試中）
├── batch_download_instructions.md  # 詳細說明
├── README_BOOKENDS_IMPORT.md       # Bookends 說明
└── pdfs/
    ├── Yoon_2021_Taiwan_USA_Comparison.pdf  # ✅ 已下載
    ├── _download_list.txt           # 所有 56 篇的下載連結
    └── download_report.txt          # 下載報告（運行腳本後生成）
```

---

## 🚀 快速開始

### 選項 A: 使用半自動化腳本（推薦新手）

```bash
cd "/Users/simon/Library/CloudStorage/Dropbox/paper/Working paper/Hospitals/LDA_hospital/manuscripts/references"

python3 auto_download_papers.py
```

腳本會：
1. 逐一開啟 Google Scholar 搜尋
2. 等待你點擊 [PDF] 下載
3. 自動移動和重命名檔案

### 選項 B: 使用 Zotero（推薦有經驗者）

1. 安裝 Zotero
2. 匯入 `all_references.ris`
3. 一鍵批次下載所有 PDF

### 選項 C: 手動下載（最可靠）

1. 開啟 `pdfs/_download_list.txt`
2. 逐一點擊 Google Scholar 連結
3. 下載 PDF 並手動重命名

---

## 💡 下載技巧

### 1. 確認 VPN 連線

```bash
# 確認已連接學校 VPN
# 測試連線
curl -I https://onlinelibrary.wiley.com
```

### 2. 使用瀏覽器擴充功能

- **Unpaywall** - 自動找免費 PDF
- **Zotero Connector** - 一鍵儲存文獻

### 3. 批次下載

不要一次下載全部，分批進行：
- 第一批：10 篇核心文獻（priority_papers.json）
- 第二批：理論基礎類（15 篇）
- 第三批：方法論類（15 篇）
- 第四批：其他（16 篇）

### 4. 檢查完整性

下載後檢查 PDF 是否完整：
```bash
cd pdfs
ls -lh *.pdf | awk '{print $5, $9}'
```

---

## 📞 遇到問題？

### Q: 某些期刊學校沒有訂閱？

**A**: 試試：
1. 館際互借（ILL）
2. 聯繫作者索取（通常很願意分享）
3. ResearchGate 請求全文

### Q: Google Scholar 顯示「我不是機器人」？

**A**:
1. 使用不同的搜尋引擎（Web of Science, PubMed）
2. 等待一段時間再試
3. 使用學校圖書館的資料庫

### Q: 下載的 PDF 打不開？

**A**:
1. 檢查檔案大小（小於 100KB 通常有問題）
2. 重新下載
3. 嘗試不同的下載源

---

## ✅ 下載完成檢查清單

- [ ] 已連接學校 VPN
- [ ] 已下載 10 篇核心文獻
- [ ] 已下載理論基礎類（15 篇）
- [ ] 已下載方法論類（15 篇）
- [ ] 已下載其他文獻（16 篇）
- [ ] 已檢查所有 PDF 完整性
- [ ] 已匯入 Bookends
- [ ] 已整理檔案命名

---

## 📈 進度追蹤

運行腳本後會自動生成：
- `pdfs/download_report.txt` - 詳細下載報告
- 包含成功/失敗清單
- 記錄下載時間

---

**最後更新**: 2025-11-13
**當前進度**: 1/56 篇已下載
**預估時間**: 約 2-3 小時完成全部下載（使用半自動化腳本）
