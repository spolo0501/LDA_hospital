# Zotero 完整使用指南

**目標**：使用 Zotero 批次下載剩餘 46 篇期刊論文

---

## 📥 第一步：安裝 Zotero

### 1. 安裝 Zotero 主程式

**Mac 用戶（推薦使用 Homebrew）**：
```bash
brew install --cask zotero
```

**或手動下載**：
- 前往：https://www.zotero.org/download/
- 下載 "Zotero 7 for Mac"
- 安裝 .dmg 檔案

### 2. 安裝瀏覽器擴充功能（重要！）

這是批次下載 PDF 的關鍵工具。

**Chrome/Edge 用戶**：
- 前往：https://www.zotero.org/download/connectors
- 點擊 "Install Chrome Connector"
- 或直接訪問：https://chrome.google.com/webstore/detail/zotero-connector/ekhagklcjbdpajgpjgmbionohlpdbjgc

**Safari 用戶**：
- Zotero 7 已內建 Safari 擴充功能
- 開啟 Zotero → Preferences → Advanced → Enable Safari extension

---

## 📚 第二步：匯入文獻清單

### 方法 1：直接匯入 RIS 檔案（推薦）

1. **開啟 Zotero**

2. **創建新資料夾（Collection）**：
   - 點擊左上角的 "New Collection" 按鈕（資料夾圖示）
   - 命名為：`Hospital LDA Research - 56 Papers`

3. **匯入 RIS 檔案**：
   ```
   File → Import...
   ```
   - 選擇：`all_references.ris`
   - 位置：`/Users/simon/Library/CloudStorage/Dropbox/paper/Working paper/Hospitals/LDA_hospital/manuscripts/references/all_references.ris`
   - 確認：✅ Place imported collections and items into new collection
   - 點擊 "Import"

4. **確認匯入成功**：
   - 應該會看到 75 篇文獻（包含書籍）
   - 期刊論文應該是 56 篇

---

## 🌐 第三步：連接學校 VPN

**非常重要**：必須在下載 PDF 前連接學校 VPN！

### 東海大學 VPN 連線（假設您的學校）

如果您還沒設定 VPN，請：

1. 聯繫學校圖書館或 IT 部門
2. 取得 VPN 設定資訊
3. 安裝 VPN 軟體（通常是 Cisco AnyConnect 或 Pulse Secure）

### 確認 VPN 已連線

測試方式：
```bash
# 訪問一個需要訂閱的期刊，看是否能存取
open "https://onlinelibrary.wiley.com"
```

如果能看到 "Full Text" 或 "PDF" 下載選項，表示 VPN 正常運作。

---

## 📥 第四步：批次下載 PDF

### 方法 A：使用 Zotero 內建功能（推薦）

1. **選擇所有需要下載 PDF 的文獻**：
   - 在 Zotero 左側點擊您剛創建的 Collection
   - 按 `Cmd + A`（Mac）選擇全部文獻
   - 或按住 `Shift` 點擊第一篇和最後一篇

2. **執行批次下載**：
   - 右鍵點擊選中的文獻
   - 選擇：`Find Available PDFs`（或 `尋找可用的 PDF`）
   - Zotero 會自動開始搜尋和下載

3. **等待下載完成**：
   - Zotero 會在右下角顯示進度
   - 可能需要 10-30 分鐘（取決於網速和可用性）
   - 成功下載的文獻會顯示 📎 圖示

### 方法 B：使用瀏覽器擴充功能逐一下載

如果批次下載失敗，可以手動補充：

1. **在 Zotero 中選擇一篇沒有 PDF 的文獻**
2. **右鍵 → "Show in Google Scholar"**
3. **在 Google Scholar 頁面**：
   - 瀏覽器工具列會出現 Zotero 圖示
   - 點擊圖示會自動儲存文獻
   - 如果有 PDF，會自動下載

---

## 📊 第五步：檢查下載結果

### 查看下載統計

```bash
# 在 Zotero 中建立搜尋條件
Saved Search → New Search...
Name: "Papers with PDF"
Match: all
Conditions:
  - Attachment File Type | is | PDF
```

### 識別未下載的文獻

```bash
# 建立另一個搜尋
Saved Search → New Search...
Name: "Papers without PDF"
Match: all
Conditions:
  - Item Type | is | Journal Article
  - Attachment File Type | is not | PDF
```

### 查看 Zotero 儲存的 PDF 位置

預設位置：
```
/Users/simon/Zotero/storage/
```

每篇文獻的 PDF 會存在獨立的資料夾中。

---

## 🔧 第六步：匯出 PDF 到我們的專案資料夾

### 方法 1：使用 Zotero 匯出

1. **選擇所有有 PDF 的文獻**
2. **右鍵 → Export Files...**
3. **選擇匯出位置**：
   ```
   /Users/simon/Library/CloudStorage/Dropbox/paper/Working paper/Hospitals/LDA_hospital/manuscripts/references/pdfs/
   ```

### 方法 2：使用 Python 腳本自動複製和重命名

我可以為您創建一個腳本：

```python
# 功能：
# 1. 讀取 Zotero 資料庫
# 2. 找到所有已下載的 PDF
# 3. 按照我們的命名規範複製到 pdfs/ 資料夾
# 4. 命名格式：Author_Year_Title.pdf
```

---

## 💡 進階技巧

### 1. 設定代理伺服器（如果 VPN 有問題）

```
Zotero → Preferences → Advanced → Network
Configure Proxy
```

### 2. 增加下載超時時間

如果網路較慢：
```
Zotero → Preferences → Advanced → Config Editor
搜尋：extensions.zotero.downloadDelay
設定為：2000（2秒）
```

### 3. 手動添加 PDF

對於 Zotero 無法自動下載的文獻：

1. **手動下載 PDF**
2. **拖曳到 Zotero 中對應的文獻**
3. **或右鍵 → Add Attachment → Attach Stored Copy of File**

---

## 🎯 完整工作流程總結

```bash
# 1. 安裝（5 分鐘）
brew install --cask zotero

# 2. 設定瀏覽器擴充功能（2 分鐘）
# 訪問 https://www.zotero.org/download/connectors

# 3. 連接學校 VPN（1 分鐘）
# 使用學校提供的 VPN 軟體

# 4. 匯入文獻（2 分鐘）
# Zotero → File → Import → 選擇 all_references.ris

# 5. 批次下載（20-30 分鐘，自動）
# 選擇全部 → 右鍵 → Find Available PDFs

# 6. 檢查結果（5 分鐘）
# 使用 Saved Search 查看成功/失敗的文獻

# 7. 手動補充（視需要，30-60 分鐘）
# 對於未成功下載的文獻手動處理
```

**總預估時間**：1.5-2 小時（大部分時間是自動下載）

---

## ❓ 常見問題

### Q1: Zotero 找不到 PDF？

**A**: 可能原因：
1. ❌ 未連接 VPN → 連接學校 VPN
2. ❌ 學校沒有訂閱該期刊 → 嘗試其他方法
3. ❌ 期刊網站改版 → 手動下載後拖入 Zotero
4. ❌ DOI 或 URL 資訊不完整 → 手動補充 metadata

### Q2: 下載的 PDF 檔名很亂？

**A**: Zotero 使用隨機資料夾名稱儲存。需要：
- 使用 Zotero 內建的 "Rename File from Parent Metadata" 功能
- 或使用 ZotFile 外掛（推薦）
- 或使用我提供的 Python 腳本重命名

### Q3: 可以在不同電腦同步嗎？

**A**: 可以！
1. 註冊 Zotero 帳號：https://www.zotero.org/user/register
2. Preferences → Sync → 登入帳號
3. 免費版提供 300MB 儲存空間（不含 PDF）
4. 或使用 WebDAV 同步（可搭配 Dropbox）

### Q4: 如何與 Bookends 整合？

**A**: 兩種方式：
1. **匯出 RIS 再匯入 Bookends**：
   ```
   Zotero → 選擇文獻 → 右鍵 → Export Items...
   Format: RIS → 儲存 → 在 Bookends 中匯入
   ```

2. **同時使用兩個軟體**：
   - Zotero 用於下載 PDF
   - Bookends 用於文獻管理和 Word 插入引用

---

## 🚀 快速開始（懶人包）

如果您趕時間，最簡單的流程：

```bash
# 1. 安裝 Zotero
brew install --cask zotero

# 2. 開啟 Zotero，匯入 RIS
# File → Import → 選擇 all_references.ris

# 3. 連接學校 VPN

# 4. 批次下載
# Cmd+A 全選 → 右鍵 → Find Available PDFs

# 5. 等待 20-30 分鐘

# 6. 完成！
```

---

## 📞 需要協助？

如果遇到問題，請告訴我：
1. 卡在哪個步驟？
2. 出現什麼錯誤訊息？
3. 成功下載了多少篇？

我可以：
- 幫您創建自動化腳本
- 提供更詳細的步驟說明
- 建議其他下載方法

---

## 🎁 額外工具推薦

### ZotFile 外掛（強烈推薦）

**功能**：
- 自動重命名 PDF（使用作者、年份、標題）
- 自動移動 PDF 到指定資料夾
- 平板同步（iPad 閱讀）
- 提取 PDF 註解

**安裝**：
1. 下載：http://zotfile.com/
2. Zotero → Tools → Add-ons → Install Add-on From File
3. 選擇下載的 .xpi 檔案

**設定 ZotFile 自動重命名**：
```
Tools → ZotFile Preferences → Renaming Rules
Format: {%a_}{%y_}{%t}
結果：Yoon_2021_Taiwan_USA_comparison.pdf
```

---

**建立時間**：2025-11-13
**適用版本**：Zotero 7.x
**系統**：macOS（其他系統步驟類似）
