# Streamlit Cloud 自動同步指南

**您的應用**：https://ldahospital-2ieba7vqilmu6tqbjzxy8j.streamlit.app

---

## 🎯 最簡單的方式：一鍵同步

### 方法 1：執行同步腳本（推薦）

在終端機中執行：

```bash
cd "/Users/simon/Library/CloudStorage/Dropbox/paper/Working paper/Hospitals/LDA_hospital"
./sync_to_streamlit.sh
```

腳本會：
1. ✅ 顯示目前的變更
2. ✅ 詢問您是否確認推送
3. ✅ 要求輸入提交訊息（可選）
4. ✅ 自動推送到 GitHub
5. ✅ Streamlit Cloud 自動更新（1-2 分鐘）

---

### 方法 2：請 Claude Code 幫您推送

直接告訴我：

- **"幫我推送到 GitHub"**
- **"更新 Streamlit"**
- **"同步到 Streamlit Cloud"**

我會自動執行所有步驟！

---

### 方法 3：手動 Git 命令

```bash
cd "/Users/simon/Library/CloudStorage/Dropbox/paper/Working paper/Hospitals/LDA_hospital"

# 加入變更
git add code/streamlit_app/

# 提交
git commit -m "更新 Streamlit 應用"

# 推送
git push origin main
```

---

## 🔄 Streamlit Cloud 自動部署

**重要**：Streamlit Cloud 已經設定為**自動部署**！

每當您推送到 GitHub：
1. **GitHub 收到推送** ✅
2. **Streamlit Cloud 偵測到變更** ✅
3. **自動重新部署**（約 1-2 分鐘）✅
4. **應用程式更新完成** ✅

**您不需要手動在 Streamlit Cloud 做任何事情！**

---

## 📊 檢查部署狀態

### 在 Streamlit Cloud 查看：

1. 前往：https://share.streamlit.io
2. 登入您的帳號（spolo0501）
3. 找到您的應用
4. 可以看到：
   - ✅ 最新 commit
   - ✅ 部署狀態
   - ✅ 部署歷史
   - ✅ 錯誤日誌（如果有）

---

## 💡 工作流程範例

### 情境 1：更新 Streamlit 程式碼

```bash
# 1. 編輯您的 Streamlit 程式
vim code/streamlit_app/taiwan_lda_explorer.py

# 2. 執行同步腳本
./sync_to_streamlit.sh

# 3. 等待 1-2 分鐘
# 4. 開啟瀏覽器查看更新
open https://ldahospital-2ieba7vqilmu6tqbjzxy8j.streamlit.app
```

### 情境 2：使用 Claude Code

```
您：更新了 Streamlit 應用，幫我推送到 GitHub

Claude Code：
✅ 檢查變更
✅ 提交並推送
✅ 提醒您等待 Streamlit Cloud 更新
```

---

## 🛠️ 只會同步這些檔案

根據 `.gitignore` 設定，只有以下內容會上傳：

✅ **會上傳**：
- `code/streamlit_app/` - Streamlit 應用程式
- `data_demo/` - 展示資料
- `results_demo/` - 展示結果
- `requirements.txt` - 套件清單
- `.streamlit/config.toml` - 設定檔
- `README.md` - 說明文件

❌ **不會上傳**（保留在本地）：
- `manuscripts/` - 論文手稿
- `Literature_Review/` - 文獻回顧
- `data/raw/` - 完整資料
- `results/` - 完整結果
- 所有指南和腳本

---

## ⚡ 快速參考

| 動作 | 命令 |
|------|------|
| 一鍵同步 | `./sync_to_streamlit.sh` |
| 查看變更 | `git status` |
| 手動推送 | `git add . && git commit -m "更新" && git push` |
| 請 Claude 幫忙 | "幫我推送到 GitHub" |

---

## 🐛 常見問題

### Q1: 推送後 Streamlit 沒有更新？

**A**: 等待 2-3 分鐘，或：
1. 前往 Streamlit Cloud
2. 點擊您的應用
3. 點擊右上角 "⋮" → "Reboot app"

### Q2: 看到錯誤訊息？

**A**: 檢查 Streamlit Cloud 的錯誤日誌：
1. 前往 https://share.streamlit.io
2. 點擊您的應用
3. 查看 "Logs" 標籤

### Q3: 想回到之前的版本？

**A**: 使用 Git 回退：
```bash
git log --oneline  # 查看歷史
git checkout <commit-id>  # 回到特定版本
git push origin main  # 推送
```

或告訴我："幫我回到上一個版本"

---

## 📞 需要協助？

直接告訴我：
- "幫我推送到 GitHub"
- "同步到 Streamlit Cloud"
- "檢查 Git 狀態"
- "查看最近的 commits"

我會自動幫您執行！

---

**最後更新**：2025-11-13
**您的應用**：https://ldahospital-2ieba7vqilmu6tqbjzxy8j.streamlit.app
