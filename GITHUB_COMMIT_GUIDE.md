# 🚀 GitHub Desktop Commit 指南

## 📋 準備完成！

所有檔案已經 staged，準備好提交到 GitHub。

---

## ✅ 已準備的檔案清單

### 核心應用程式
- ✅ `code/streamlit_app/taiwan_lda_explorer.py` - 主應用程式（支援展示模式）
- ✅ `code/streamlit_app/run_app.sh` - 啟動腳本

### 配置檔案
- ✅ `.streamlit/config.toml` - Streamlit 配置
- ✅ `.gitignore` - 更新允許展示資料
- ✅ `requirements.txt` - Python 套件需求

### 展示資料（Streamlit Cloud 專用）
- ✅ `data_demo/raw/taiwan/` - 5 家醫院評論資料
- ✅ `results_demo/taiwan_lda_k7/lda_k7_lda_model.pkl` - LDA 模型

### 文檔
- ✅ `STREAMLIT_DEPLOYMENT.md` - 部署指南
- ✅ `code/streamlit_app/README.md` - 應用程式說明
- ✅ `code/streamlit_app/UPDATES_2025_11_12.md` - 更新日誌
- ✅ 其他說明文件

---

## 📝 使用 GitHub Desktop 提交步驟

### 步驟 1：開啟 GitHub Desktop

確認您在正確的 repository：
```
LDA_hospital
```

### 步驟 2：檢查變更

您應該會看到以下變更：

#### 新增檔案（17 個）
- `.streamlit/config.toml`
- `STREAMLIT_DEPLOYMENT.md`
- `code/streamlit_app/` 目錄下的所有檔案
- `data_demo/` 展示資料
- `results_demo/` 展示模型

#### 修改檔案（2 個）
- `.gitignore`
- `requirements.txt`

### 步驟 3：填寫 Commit Message

**Summary（必填）**：
```
Add Streamlit web app for hospital LDA analysis
```

**Description（詳細說明）**：
```
Features:
- Interactive web interface with 4 analysis modules
- Hospital rating comparison across service topics
- Topic exploration with representative reviews
- Real-time review analysis with jieba tokenization
- Support for demo mode (5 hospitals) for Streamlit Cloud

Technical:
- Fixed K=7 topics (optimized configuration)
- Removed topic selection to simplify UX
- Card-based review display (expanded by default)
- Three-column visualization layout
- Multi-hospital rating comparison (bar/heatmap/line charts)

Deployment:
- Streamlit Cloud ready with demo data
- Environment variable support (USE_DEMO_DATA)
- Configuration files for cloud deployment

Updates:
- Moved wordcloud to overview page
- Removed redundant visualizations
- Optimized page structure and layout
```

### 步驟 4：Commit to main

點擊 **"Commit to main"** 按鈕

### 步驟 5：Push to origin

點擊 **"Push origin"** 按鈕，將變更推送到 GitHub

---

## 🌐 Streamlit Cloud 部署步驟

### 準備工作

確認 GitHub repository 已更新（完成上述 Push 步驟）

### 步驟 1：登入 Streamlit Cloud

1. 前往 https://share.streamlit.io
2. 點擊 **"Sign in"**
3. 選擇 **"Continue with GitHub"**
4. 授權 Streamlit 存取您的 GitHub

### 步驟 2：建立新應用程式

1. 點擊右上角 **"New app"**
2. 填寫資訊：

**Repository**:
```
您的 GitHub 使用者名稱/LDA_hospital
```

**Branch**:
```
main
```

**Main file path**:
```
code/streamlit_app/taiwan_lda_explorer.py
```

### 步驟 3：設定環境變數

點擊 **"Advanced settings..."**

在 **Secrets** 欄位中添加：
```toml
USE_DEMO_DATA = true
```

這會讓應用程式使用展示資料（5 家醫院）

### 步驟 4：部署

1. 點擊 **"Deploy!"**
2. 等待 3-5 分鐘進行部署
3. 觀察部署日誌確認沒有錯誤

### 步驟 5：測試應用程式

部署完成後：
1. 應用程式會自動開啟
2. 確認頂部顯示：📊 展示模式：使用 5 家醫院資料進行展示
3. 測試四個分析模組：
   - 📊 主題總覽
   - 🔍 主題深入探索
   - 🏥 醫院評分比較
   - 📈 統計儀表板

---

## ⚠️ 常見問題排除

### 問題 1：部署失敗 - 找不到模組

**解決方案**：
檢查 `requirements.txt` 是否包含所有必要套件：
- streamlit
- pandas
- numpy
- gensim
- jieba
- matplotlib
- seaborn
- openpyxl

### 問題 2：找不到資料檔案

**症狀**：❌ 找不到 K=7 的 LDA 模型

**解決方案**：
1. 確認 `data_demo/` 和 `results_demo/` 已推送到 GitHub
2. 檢查 Streamlit Cloud secrets 設定 `USE_DEMO_DATA = true`
3. 查看部署日誌確認檔案路徑

### 問題 3：中文字體顯示問題

**症狀**：圖表中文字顯示為方框

**解決方案**：
這是已知限制，Streamlit Cloud 預設沒有中文字體。
可以在應用程式中添加提示訊息說明。

### 問題 4：應用程式太慢

**解決方案**：
- 展示模式已經使用較少資料（5 家醫院）
- 可以進一步減少顯示的評論數量
- 考慮使用 Streamlit Cloud 付費方案獲得更多資源

---

## 📊 部署後檢查清單

- [ ] 應用程式能正常開啟
- [ ] 頂部顯示展示模式提示
- [ ] 主題總覽顯示 7 個主題
- [ ] 可以選擇不同主題進行探索
- [ ] 評論能正確顯示（有評分、內容、醫院）
- [ ] 醫院評分比較功能正常
- [ ] 三種視覺化（長條圖、熱力圖、折線圖）都能顯示
- [ ] 沒有 Python 錯誤訊息

---

## 🎉 分享您的應用程式

部署成功後，您會獲得一個 URL，例如：
```
https://your-app-name.streamlit.app
```

您可以：
- 分享此 URL 給同事和合作者
- 將 URL 加入論文或報告中
- 在 GitHub README 中添加應用程式連結

---

## 🔄 更新應用程式

當您需要更新應用程式：

1. 在本地修改程式碼
2. 使用 GitHub Desktop commit & push
3. Streamlit Cloud 會自動偵測變更並重新部署
4. 等待 2-3 分鐘即可看到更新

---

## 📞 需要協助？

### Streamlit 官方資源
- [Streamlit Cloud 文檔](https://docs.streamlit.io/streamlit-community-cloud)
- [Streamlit 論壇](https://discuss.streamlit.io/)
- [Streamlit Discord](https://discord.gg/streamlit)

### 檢查部署日誌
在 Streamlit Cloud 應用程式頁面：
1. 點擊右下角 **"Manage app"**
2. 查看 **"Logs"** 標籤
3. 找出錯誤訊息

### 常用除錯命令
在應用程式中添加：
```python
import sys
st.write(f"Python 版本: {sys.version}")
st.write(f"當前目錄: {os.getcwd()}")
st.write(f"BASE_DIR: {BASE_DIR}")
st.write(f"USE_DEMO: {USE_DEMO}")
```

---

**建立日期**: 2025-11-12
**適用版本**: Streamlit Cloud (Community tier)
**預估部署時間**: 5-10 分鐘

🎊 **準備好了嗎？開始您的第一次部署吧！**
