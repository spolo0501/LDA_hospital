# 🎁 台美醫院評論比較分析 - 分享包指南

## Share Package Guide

本指南說明如何將專案打包給朋友在本機運行。

---

## 📦 方案總覽

### 🎯 最佳組合：HTML報告 + 本機運行

| 方案 | 適用情境 | 優點 | 缺點 |
|------|---------|------|------|
| **HTML報告** | 快速瀏覽 | 無需安裝、檔案小(0.23MB) | 靜態、無互動 |
| **本機運行** | 深度探索 | 完整互動、最安全 | 需安裝Python |

---

## 📊 方案 1：HTML 報告（靜態）

### 檔案位置
```
reports/Taiwan_USA_Comparison_Report_20251112_085910.html
```

### 分享方式
1. **Email 附件** - 檔案只有 0.23 MB
2. **Dropbox/Google Drive** - 分享連結
3. **USB 隨身碟** - 直接拷貝

### 朋友使用方式
```
1. 下載 HTML 檔案
2. 雙擊開啟（會用預設瀏覽器打開）
3. 完成！
```

### 特色
- ✅ 包含所有圖表和分析
- ✅ 完整的研究結論
- ✅ 美觀的排版
- ✅ 可列印成PDF

---

## 💻 方案 2：本機運行 Streamlit（互動）

### 🎯 準備分享包

#### 步驟 1：打包必要檔案

創建一個資料夾 `Taiwan_USA_Hospital_Analysis`，包含：

```
Taiwan_USA_Hospital_Analysis/
├── README.md                          # 使用說明（下面會提供）
├── requirements.txt                    # Python 套件清單
├── run_app.sh                         # 啟動腳本（Mac/Linux）
├── run_app.bat                        # 啟動腳本（Windows）
├── code/
│   └── streamlit_app/
│       ├── taiwan_usa_comparison.py   # 主程式
│       └── comparison_config.py        # 配置檔案
├── results/
│   ├── taiwan_lda_k7/
│   │   └── lda_k7_lda_model.pkl      # 台灣模型
│   └── usa_lda_k7/
│       ├── usa_gensim_lda_k6_model.pkl           # 美國模型
│       └── usa_k6_topic_analysis_20251107_122236.csv  # 美國資料
└── .streamlit/
    └── config.toml                    # Streamlit 配置
```

#### 步驟 2：生成檔案清單

**自動化腳本**（我可以幫您寫）：
```bash
#!/bin/bash
# pack_for_sharing.sh

# 建立打包目錄
mkdir -p Taiwan_USA_Hospital_Analysis

# 拷貝必要檔案
cp -r code/streamlit_app Taiwan_USA_Hospital_Analysis/code/
cp requirements.txt Taiwan_USA_Hospital_Analysis/
cp -r results Taiwan_USA_Hospital_Analysis/
cp -r .streamlit Taiwan_USA_Hospital_Analysis/

# 生成 README
cat > Taiwan_USA_Hospital_Analysis/README.md << 'EOF'
# 台美醫院評論比較分析系統

## 快速開始

### Mac/Linux:
```bash
chmod +x run_app.sh
./run_app.sh
```

### Windows:
直接雙擊 `run_app.bat`

應用程式會在瀏覽器自動開啟！

EOF

# 壓縮
zip -r Taiwan_USA_Analysis.zip Taiwan_USA_Hospital_Analysis/

echo "✅ 打包完成！檔案：Taiwan_USA_Analysis.zip"
```

---

### 👥 朋友使用步驟

#### 🖥️ Mac / Linux 使用者

```bash
# 1. 解壓縮
unzip Taiwan_USA_Analysis.zip
cd Taiwan_USA_Hospital_Analysis

# 2. 建立虛擬環境（只需執行一次）
python3 -m venv .venv
source .venv/bin/activate

# 3. 安裝套件（只需執行一次）
pip install -r requirements.txt

# 4. 啟動應用程式
cd code/streamlit_app
python -m streamlit run taiwan_usa_comparison.py --server.port 8503
```

#### 🪟 Windows 使用者

```cmd
# 1. 解壓縮
# 雙擊 Taiwan_USA_Analysis.zip 並解壓縮

# 2. 開啟 CMD，進入目錄
cd Taiwan_USA_Hospital_Analysis

# 3. 建立虛擬環境（只需執行一次）
python -m venv .venv
.venv\Scripts\activate

# 4. 安裝套件（只需執行一次）
pip install -r requirements.txt

# 5. 啟動應用程式
cd code\streamlit_app
python -m streamlit run taiwan_usa_comparison.py --server.port 8503
```

#### ⚡ 使用啟動腳本（更簡單）

**Mac/Linux**:
```bash
chmod +x run_app.sh
./run_app.sh
```

**Windows**:
雙擊 `run_app.bat`

---

### 📋 朋友需要的前置條件

1. **Python 3.9+** - [下載連結](https://www.python.org/downloads/)
   - Mac: 通常已預裝
   - Windows: 需要下載安裝

2. **網路連線**（僅首次安裝套件時需要）

3. **5 分鐘時間**（首次設定）

---

### 🛠️ 自動化啟動腳本

#### `run_app.sh` (Mac/Linux)

```bash
#!/bin/bash

echo "🌏 台美醫院評論比較分析系統"
echo "================================"

# 檢查 Python
if ! command -v python3 &> /dev/null; then
    echo "❌ 找不到 Python 3"
    echo "請先安裝 Python: https://www.python.org/downloads/"
    exit 1
fi

# 建立虛擬環境（如果不存在）
if [ ! -d ".venv" ]; then
    echo "📦 首次執行：建立虛擬環境..."
    python3 -m venv .venv
fi

# 啟動虛擬環境
source .venv/bin/activate

# 檢查套件（如果沒安裝）
if ! python -c "import streamlit" 2>/dev/null; then
    echo "📦 首次執行：安裝必要套件（需要 2-3 分鐘）..."
    pip install -r requirements.txt
fi

# 啟動應用程式
echo "🚀 啟動應用程式..."
cd code/streamlit_app
python -m streamlit run taiwan_usa_comparison.py --server.port 8503

# 當用戶按 Ctrl+C 時停止
deactivate
```

#### `run_app.bat` (Windows)

```batch
@echo off
echo 🌏 台美醫院評論比較分析系統
echo ================================

REM 檢查 Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ 找不到 Python
    echo 請先安裝 Python: https://www.python.org/downloads/
    pause
    exit /b 1
)

REM 建立虛擬環境（如果不存在）
if not exist ".venv" (
    echo 📦 首次執行：建立虛擬環境...
    python -m venv .venv
)

REM 啟動虛擬環境
call .venv\Scripts\activate

REM 檢查套件
python -c "import streamlit" 2>nul
if errorlevel 1 (
    echo 📦 首次執行：安裝必要套件（需要 2-3 分鐘）...
    pip install -r requirements.txt
)

REM 啟動應用程式
echo 🚀 啟動應用程式...
cd code\streamlit_app
python -m streamlit run taiwan_usa_comparison.py --server.port 8503

REM 停用虛擬環境
deactivate
```

---

### 📊 檔案大小估計

| 項目 | 大小 |
|------|------|
| Python 程式碼 | < 1 MB |
| LDA 模型檔案 | ~2 MB |
| 評論資料 | ~5 MB |
| **總計（壓縮前）** | **~8 MB** |
| **總計（zip壓縮後）** | **~3-4 MB** |

✅ **非常小**，可以用 Email 傳送！

---

### 🔒 資料安全性

#### ✅ 優點
1. 資料**完全不離開**朋友的電腦
2. 不需要上傳到任何雲端服務
3. 朋友用完可以直接刪除
4. 沒有任何網路傳輸風險

#### ⚠️ 注意事項
1. 提醒朋友**不要分享**給其他人
2. 原始評論資料已包含在內
3. 如果擔心，可以只包含**聚合後的統計資料**（不含原始評論）

---

### 🎯 簡化版：只包含統計結果

如果您想**更安全**，可以建立一個「輕量版」：

```
Taiwan_USA_Hospital_Analysis_Lite/
├── README.md
├── requirements.txt
├── taiwan_usa_comparison_lite.py   # 修改版（不載入原始評論）
└── results/
    ├── taiwan_stats.pkl            # 只包含統計資料
    └── usa_stats.pkl               # 只包含統計資料
```

這樣：
- ✅ 不包含原始評論文字
- ✅ 檔案更小（< 1 MB）
- ✅ 仍可顯示所有圖表和統計
- ❌ 無法展示個別評論內容

---

### 💡 我的最終建議

#### 🎁 給朋友的完整包：

1. **HTML 報告** (0.23 MB)
   - 用於快速瀏覽
   - 無需安裝任何東西

2. **本機運行包** (3-4 MB zip)
   - 用於深度探索
   - 完整互動功能
   - 包含自動化啟動腳本

#### 📧 分享方式

**Email**:
```
主旨：台美醫院評論比較分析

Hi [朋友名字],

附件包含兩個檔案：

1. HTML 報告（Taiwan_USA_Report.html）
   - 雙擊即可在瀏覽器開啟
   - 適合快速瀏覽研究結果

2. 互動版本（Taiwan_USA_Analysis.zip）
   - 解壓縮後執行 run_app.sh (Mac) 或 run_app.bat (Windows)
   - 首次執行需要 5 分鐘安裝（之後只需 10 秒）
   - 可以自己探索和互動

需要 Python 3.9+，如果還沒安裝：
https://www.python.org/downloads/

有任何問題隨時問我！

Best regards,
Simon
```

---

### 📞 常見問題

#### Q1: 朋友沒有 Python 怎麼辦？
**A**: 先給 HTML 報告，如果想深度探索再安裝 Python

#### Q2: 可以在手機上看嗎？
**A**: HTML 報告可以，Streamlit 需要電腦

#### Q3: 檔案太大無法 Email？
**A**: 使用 Dropbox/Google Drive 分享連結

#### Q4: 擔心資料外泄？
**A**: 使用「輕量版」（只含統計資料）

---

## ✅ 下一步

我可以幫您：
1. ✅ 生成完整的打包腳本
2. ✅ 建立 Windows 和 Mac 的啟動腳本
3. ✅ 建立簡化版的「朋友使用指南」
4. ✅ 測試整個流程

請告訴我您想要哪些！
