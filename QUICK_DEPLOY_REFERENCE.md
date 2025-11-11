# ⚡ 快速部署參考卡

## 🎯 5 分鐘部署到 Streamlit Cloud

---

### ✅ 檔案已準備完成

所有需要的檔案都已經 staged 並準備好 commit。

---

### 📝 GitHub Desktop 操作（3 步驟）

#### 1. Commit Message
```
Summary: Add Streamlit web app for hospital LDA analysis

Description:
Interactive web app with 4 modules: overview, exploration, comparison, stats
- Hospital rating comparison across topics
- Real-time review analysis
- Demo mode with 5 hospitals for Streamlit Cloud
```

#### 2. Commit to main
點擊 **"Commit to main"** 按鈕

#### 3. Push origin
點擊 **"Push origin"** 按鈕

---

### 🌐 Streamlit Cloud 設定（3 步驟）

#### 1. 建立 App
- Repository: `您的帳號/LDA_hospital`
- Branch: `main`
- Main file: `code/streamlit_app/taiwan_lda_explorer.py`

#### 2. 設定 Secrets
點擊 "Advanced settings"，添加：
```toml
USE_DEMO_DATA = true
```

#### 3. Deploy！
點擊 **"Deploy!"** 按鈕

---

### ✨ 等待 3-5 分鐘

部署完成後會自動開啟應用程式。

---

### 🎊 完成！

您的應用程式現在已經上線：
```
https://your-app.streamlit.app
```

---

### 📊 功能檢查

- [ ] 主題總覽（7 個主題）
- [ ] 主題探索（關鍵詞 + 評論）
- [ ] 醫院評分比較（長條圖、熱力圖、折線圖）
- [ ] 統計儀表板

---

### 🐛 如果遇到問題

1. 檢查 Streamlit Cloud "Manage app" → "Logs"
2. 確認 secrets 設定正確
3. 確認所有檔案都已推送到 GitHub

---

**詳細指南**: 參考 `GITHUB_COMMIT_GUIDE.md`
