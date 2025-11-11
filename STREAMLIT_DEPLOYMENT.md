# 🚀 Streamlit Cloud 部署指南

## 📋 部署前準備

### 問題：資料檔案太大
由於 GitHub 有檔案大小限制（100MB），而我們的專案包含：
- 原始評論資料：28 個 Excel 檔案
- LDA 模型：約 556KB

這些檔案無法直接推送到 GitHub。

---

## ✅ 解決方案：使用 GitHub Releases 或外部儲存

### 方案 1：GitHub Releases（推薦）

1. **打包資料檔案**
```bash
cd /Users/simon/Library/CloudStorage/Dropbox/paper/Working\ paper/Hospitals/LDA_hospital

# 打包模型檔案
tar -czf lda_models.tar.gz results/taiwan_lda_k7/*.pkl

# 打包原始資料（分批，避免單一檔案過大）
cd data/raw/taiwan
split -b 90m -d <(tar -czf - *.xlsx) hospital_data_part_
```

2. **上傳到 GitHub Release**
   - 在 GitHub repo 建立新的 Release
   - 上傳 `lda_models.tar.gz`
   - 上傳資料分割檔案

3. **修改應用程式在啟動時下載**

### 方案 2：使用雲端儲存（Google Drive/Dropbox）

較簡單但速度較慢的方案。

---

## 🎯 簡化方案：僅部署展示版本

由於完整資料過大，建議部署**展示版本**：

### 特色：
- ✅ 使用範例資料（5-10 家醫院）
- ✅ 保留完整功能
- ✅ 快速載入
- ✅ 展示系統能力

### 步驟：

#### 1. 創建範例資料目錄

```bash
# 在專案根目錄
mkdir -p data_demo/raw/taiwan
mkdir -p results_demo/taiwan_lda_k7

# 複製少量資料作為展示
cp data/raw/taiwan/0_國立臺灣大學醫學院附設醫院_2183.xlsx data_demo/raw/taiwan/
cp data/raw/taiwan/1_臺北榮民總醫院_3511.xlsx data_demo/raw/taiwan/
cp data/raw/taiwan/2_三軍總醫院_3511.xlsx data_demo/raw/taiwan/
cp data/raw/taiwan/12_長庚醫療財團法人林口長庚紀念醫院_2975.xlsx data_demo/raw/taiwan/
cp data/raw/taiwan/14_中國醫藥大學附設醫院_1850.xlsx data_demo/raw/taiwan/

# 複製模型
cp results/taiwan_lda_k7/lda_k7_lda_model.pkl results_demo/taiwan_lda_k7/
```

#### 2. 修改 .gitignore

將 `data_demo/` 和 `results_demo/` 從忽略列表移除：

```bash
# 在 .gitignore 添加例外
!data_demo/
!results_demo/
```

#### 3. 創建環境變數配置

創建 `.streamlit/secrets.toml`（僅本地使用，不提交到 Git）：

```toml
# 本地開發使用完整資料
USE_DEMO_DATA = false
DATA_DIR = "data"
RESULTS_DIR = "results"
```

在 Streamlit Cloud 設定環境變數：
```toml
# 線上部署使用展示資料
USE_DEMO_DATA = true
DATA_DIR = "data_demo"
RESULTS_DIR = "results_demo"
```

#### 4. 修改應用程式路徑

在 `taiwan_lda_explorer.py` 中使用環境變數：

```python
import os

# 根據環境選擇資料目錄
USE_DEMO = os.getenv('USE_DEMO_DATA', 'false').lower() == 'true'
if USE_DEMO:
    RAW_DATA_DIR = BASE_DIR / "data_demo" / "raw" / "taiwan"
    RESULTS_DIR = BASE_DIR / "results_demo"
else:
    RAW_DATA_DIR = BASE_DIR / "data" / "raw" / "taiwan"
    RESULTS_DIR = BASE_DIR / "results"
```

---

## 📝 Git Commit 清單

需要提交的檔案：

### 核心應用程式
- [x] `code/streamlit_app/taiwan_lda_explorer.py`
- [x] `code/streamlit_app/run_app.sh`
- [x] `code/streamlit_app/UPDATES_2025_11_12.md`

### 配置檔案
- [x] `requirements.txt`
- [x] `.streamlit/config.toml`
- [x] `.gitignore`（已存在）

### 文檔
- [x] `README.md`（如果需要更新）
- [x] `STREAMLIT_DEPLOYMENT.md`（本檔案）

### 展示資料（如果使用簡化方案）
- [ ] `data_demo/raw/taiwan/*.xlsx`（5-10 個檔案）
- [ ] `results_demo/taiwan_lda_k7/lda_k7_lda_model.pkl`

---

## 🌐 Streamlit Cloud 部署步驟

### 1. 推送到 GitHub

使用 GitHub Desktop：
1. 查看變更檔案
2. 寫 commit message：
   ```
   Add Streamlit app for hospital LDA analysis

   - Interactive web interface with 4 modules
   - Hospital rating comparison across topics
   - Topic exploration with review display
   - Fixed K=7 topics
   ```
3. Commit to main
4. Push origin

### 2. 連接 Streamlit Cloud

1. 前往 https://share.streamlit.io
2. 登入（使用 GitHub 帳號）
3. 點擊「New app」
4. 選擇：
   - Repository: 您的 repo
   - Branch: main
   - Main file path: `code/streamlit_app/taiwan_lda_explorer.py`

### 3. 設定環境變數（如果使用簡化方案）

在 Advanced settings 中添加：
```
USE_DEMO_DATA=true
```

### 4. Deploy！

點擊 Deploy，等待 3-5 分鐘。

---

## ⚠️ 注意事項

### 資料隱私
- 確認評論資料不含個人隱私資訊
- 如有敏感資料，使用私有 GitHub repo

### 效能考量
- Streamlit Cloud 免費版有資源限制
- 建議使用展示資料版本（5-10 家醫院）
- 完整版本需要付費方案或自行架設

### 維護
- 定期更新 requirements.txt
- 監控應用程式錯誤日誌
- 回應使用者反饋

---

## 🔗 相關資源

- [Streamlit Cloud 文檔](https://docs.streamlit.io/streamlit-community-cloud)
- [GitHub Large File Storage (LFS)](https://git-lfs.github.com/)
- [Streamlit Secrets Management](https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app/secrets-management)

---

## 📞 需要協助？

如遇到部署問題：
1. 檢查 Streamlit Cloud logs
2. 驗證 requirements.txt 版本
3. 確認檔案路徑正確
4. 測試本地環境是否正常

---

**建立日期**: 2025-11-12
**適用版本**: Streamlit v1.28+
