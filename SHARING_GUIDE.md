# 專案分享指南

## 🎯 分享方式選擇

### 方案 1：完整打包（含資料+模型）✅ 推薦

**適用對象**：合作者、需要立即使用應用程式的人

**優點**：接收者可以直接運行，不需要重新處理資料或訓練模型

**打包方法**：
```bash
cd /path/to/LDA_hospital/..
tar -czf Taiwan_Hospital_LDA_Complete.tar.gz LDA_hospital/ \
  --exclude='LDA_hospital/venv' \
  --exclude='LDA_hospital/__pycache__' \
  --exclude='LDA_hospital/**/__pycache__' \
  --exclude='LDA_hospital/**/*.pyc' \
  --exclude='LDA_hospital/.DS_Store'
```

**包含內容**：
- ✅ 程式碼
- ✅ 原始資料 (data/raw/)
- ✅ 處理後資料 (data/processed/)
- ✅ LDA 模型 (results/*/*.pkl)
- ✅ 分析結果和圖表
- ✅ 文檔

**接收者步驟**：
1. 解壓縮：`tar -xzf Taiwan_Hospital_LDA_Complete.tar.gz`
2. 進入目錄：`cd LDA_hospital/code/streamlit_app`
3. 執行腳本：`./run_app.sh`

---

### 方案 2：僅程式碼（透過 Git）

**適用對象**：想要從頭開始、學習流程的人

**優點**：檔案小、適合版本控制

**分享方法**：
```bash
# 如果已經是 Git 倉庫
git add .
git commit -m "Update project"
git push

# 或打包程式碼
git archive --format=tar.gz --output=Taiwan_Hospital_LDA_Code.tar.gz HEAD
```

**包含內容**：
- ✅ 程式碼
- ✅ 文檔
- ❌ 資料檔案（需自行準備）
- ❌ 模型檔案（需重新訓練）

**接收者步驟**：
1. 克隆或解壓專案
2. 準備資料（放到 data/raw/taiwan/）
3. 執行前處理：`python code/preprocessing/data_preprocessing.py`
4. 訓練模型：`python code/lda_analysis/lda_analysis.py`
5. 啟動應用程式：`./run_app.sh`

---

### 方案 3：展示版（含 demo 資料）

**適用對象**：僅需展示功能、不需完整資料的人

**說明**：需要先創建 demo 資料集（抽樣版）

**優點**：檔案小、快速展示

---

## 🔧 接收者設置步驟

### 1. 系統需求
- Python 3.8 或更高版本
- macOS / Linux / Windows

### 2. 安裝依賴
```bash
cd LDA_hospital

# 方法 A：使用啟動腳本（自動處理）
chmod +x code/streamlit_app/run_app.sh
cd code/streamlit_app
./run_app.sh

# 方法 B：手動安裝
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. 啟動應用程式
```bash
cd code/streamlit_app
./run_app.sh
```

或直接使用 Streamlit：
```bash
streamlit run code/streamlit_app/taiwan_lda_explorer.py
```

### 4. 瀏覽器訪問
應用程式會自動開啟瀏覽器，或手動訪問：
- 本地：http://localhost:8501

---

## ⚠️ 常見問題

### Q1: secrets.toml 錯誤
**A**: 已修復！程式碼會自動處理沒有 secrets.toml 的情況。

### Q2: 找不到資料或模型檔案
**A**: 檢查以下路徑是否存在：
```
LDA_hospital/
├── data/
│   ├── raw/taiwan/          ← 至少要有這個
│   └── processed/taiwan/
└── results/
    └── taiwan_lda_k7/       ← 至少要有這個
        └── lda_k7_lda_model.pkl
```

### Q3: ARM64 vs x86_64 架構問題
**A**: `run_app.sh` 會自動處理：
- Apple Silicon (M1/M2)：使用 ARM64
- Intel Mac：使用 x86_64
- 其他系統：自動適配

### Q4: 虛擬環境建立失敗
**A**: 確認 Python 版本：
```bash
python3 --version  # 應該是 3.8 或更高
```

---

## 📊 資料結構說明

接收者需要確保以下結構：

```
LDA_hospital/
├── code/
│   ├── streamlit_app/
│   │   ├── taiwan_lda_explorer.py  ← 主程式
│   │   └── run_app.sh              ← 啟動腳本
│   ├── preprocessing/
│   └── lda_analysis/
├── data/
│   ├── raw/taiwan/*.xlsx           ← 原始資料
│   └── processed/taiwan/*.txt      ← 處理後資料
├── results/
│   └── taiwan_lda_k7/              ← K=7 的結果
│       ├── *.pkl                   ← 模型檔案
│       └── visualizations/*.png    ← 圖表
├── requirements.txt                ← 套件需求
└── README.md                       ← 專案說明
```

---

## 🚀 快速測試

接收者可以用以下指令快速測試：

```bash
# 1. 解壓並進入目錄
tar -xzf Taiwan_Hospital_LDA_Complete.tar.gz
cd LDA_hospital

# 2. 檢查檔案結構
ls -la data/raw/taiwan/
ls -la results/taiwan_lda_k7/

# 3. 啟動應用程式
cd code/streamlit_app
chmod +x run_app.sh
./run_app.sh

# 4. 應該會自動開啟瀏覽器到 http://localhost:8501
```

---

## 📝 版本記錄

- **2025-11-13**: 修復 secrets.toml 錯誤，新增 ARM64 支援
- **2025-11-11**: 初始版本

---

**最後更新**: 2025-11-13
