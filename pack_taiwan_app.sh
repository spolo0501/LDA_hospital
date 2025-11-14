#!/bin/bash

# 台灣醫院 LDA 分析系統 - 打包腳本
# Taiwan Hospital LDA Analysis - Packaging Script

echo "======================================================================="
echo "📦 台灣醫院 LDA 分析系統 - 打包分享包"
echo "   Taiwan Hospital LDA Analysis - Creating Share Package"
echo "======================================================================="
echo ""

# 設定路徑
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PACKAGE_NAME="Taiwan_Hospital_LDA_Analysis"
PACKAGE_DIR="$SCRIPT_DIR/$PACKAGE_NAME"

# 清理舊的打包目錄
if [ -d "$PACKAGE_DIR" ]; then
    echo "🧹 清理舊的打包目錄..."
    rm -rf "$PACKAGE_DIR"
fi

if [ -f "$SCRIPT_DIR/${PACKAGE_NAME}.zip" ]; then
    rm -f "$SCRIPT_DIR/${PACKAGE_NAME}.zip"
fi

# 建立打包目錄結構
echo "📁 建立目錄結構..."
mkdir -p "$PACKAGE_DIR/code/streamlit_app"
mkdir -p "$PACKAGE_DIR/results/taiwan_lda_k7"
mkdir -p "$PACKAGE_DIR/.streamlit"

# 拷貝 Streamlit 應用程式
echo "📋 拷貝應用程式檔案..."
cp "$SCRIPT_DIR/code/streamlit_app/taiwan_lda_explorer.py" "$PACKAGE_DIR/code/streamlit_app/"

# 拷貝模型和資料
echo "📊 拷貝模型和資料檔案..."
cp "$SCRIPT_DIR/results/taiwan_lda_k7/lda_k7_lda_model.pkl" "$PACKAGE_DIR/results/taiwan_lda_k7/"
cp "$SCRIPT_DIR/results/taiwan_lda_k7/lda_k7_topic_word_distribution.xlsx" "$PACKAGE_DIR/results/taiwan_lda_k7/" 2>/dev/null || true
cp "$SCRIPT_DIR/results/taiwan_lda_k7/lda_k7_document_topic_distribution.xlsx" "$PACKAGE_DIR/results/taiwan_lda_k7/" 2>/dev/null || true

# 拷貝視覺化圖表（如果存在）
if [ -d "$SCRIPT_DIR/results/taiwan_lda_k7/visualizations" ]; then
    echo "🖼️  拷貝視覺化圖表..."
    mkdir -p "$PACKAGE_DIR/results/taiwan_lda_k7/visualizations"
    cp "$SCRIPT_DIR/results/taiwan_lda_k7/visualizations"/*.png "$PACKAGE_DIR/results/taiwan_lda_k7/visualizations/" 2>/dev/null || true
fi

# 拷貝 Streamlit 配置
echo "⚙️  拷貝配置檔案..."
if [ -f "$SCRIPT_DIR/.streamlit/config.toml" ]; then
    cp "$SCRIPT_DIR/.streamlit/config.toml" "$PACKAGE_DIR/.streamlit/"
fi

# 生成 requirements.txt
echo "📝 生成 requirements.txt..."
cat > "$PACKAGE_DIR/requirements.txt" << 'EOF'
streamlit==1.51.0
pandas>=2.0.0
numpy>=1.24.0
gensim>=4.3.0
matplotlib>=3.7.0
seaborn>=0.12.0
plotly>=5.14.0
scikit-learn>=1.3.0
scipy>=1.11.0
openpyxl>=3.1.0
wordcloud>=1.9.0
EOF

# 生成 README.md
echo "📖 生成 README.md..."
cat > "$PACKAGE_DIR/README.md" << 'EOF'
# 🏥 台灣醫院 LDA 主題分析系統

Taiwan Hospital LDA Topic Analysis System

---

## 📦 包含內容

1. **互動式 Streamlit 應用程式** - 完整的 LDA 主題分析系統
2. **LDA 模型與資料** - 台灣 26 家醫院，5,007 則評論，K=7 主題模型
3. **視覺化圖表** - 所有分析圖表（如果有）

---

## 🚀 快速開始

### ⚡ 方法 1：使用啟動腳本（推薦）

**Mac / Linux**:
```bash
chmod +x run_app.sh
./run_app.sh
```

**Windows**:
雙擊 `run_app.bat`

### 📝 方法 2：手動啟動

#### Mac / Linux

```bash
# 1. 建立虛擬環境（首次執行）
python3 -m venv .venv
source .venv/bin/activate

# 2. 安裝套件（首次執行）
pip install -r requirements.txt

# 3. 啟動應用程式
cd code/streamlit_app
python -m streamlit run taiwan_lda_explorer.py --server.port 8501
```

#### Windows

```cmd
# 1. 建立虛擬環境（首次執行）
python -m venv .venv
.venv\Scripts\activate

# 2. 安裝套件（首次執行）
pip install -r requirements.txt

# 3. 啟動應用程式
cd code\streamlit_app
python -m streamlit run taiwan_lda_explorer.py --server.port 8501
```

---

## 📊 應用程式功能

### 1. 📊 主題總覽
- 7 個主題的分布與比例
- 主題標籤與關鍵詞
- 主題情緒分析

### 2. 🔍 主題深入探索
- 選擇特定主題深入分析
- 查看該主題的代表性評論
- 關鍵詞詞雲視覺化
- 主題內評論統計

### 3. 🏥 醫院評分比較
- 26 家醫院的評分分布
- 各醫院主題比例對比
- 醫院排名分析

### 4. 📈 統計儀表板
- 整體資料集統計
- 評分分布分析
- 主題相關性矩陣
- 進階統計指標

---

## 💻 系統需求

- **Python**: 3.9 或以上
- **記憶體**: 至少 2GB
- **硬碟空間**: 約 500MB（含虛擬環境）
- **作業系統**: Windows 10+, macOS 10.14+, Linux

### 安裝 Python

如果還沒安裝 Python：
- 下載連結：https://www.python.org/downloads/
- 安裝時請勾選「Add Python to PATH」

---

## 🐛 常見問題

### Q: 執行 run_app.sh 說「Permission denied」？
**A**: 執行 `chmod +x run_app.sh` 後再試

### Q: 找不到 Python？
**A**:
- Mac: 使用 `python3` 而不是 `python`
- Windows: 確認安裝時有勾選「Add to PATH」

### Q: 套件安裝失敗？
**A**:
```bash
# 升級 pip
pip install --upgrade pip

# 重新安裝
pip install -r requirements.txt
```

### Q: 應用程式無法啟動？
**A**:
1. 檢查是否在正確目錄：`cd code/streamlit_app`
2. 檢查 Python 版本：`python --version`（應該 >= 3.9）
3. 確認虛擬環境已啟動（命令列前面有 `.venv`）

### Q: 瀏覽器沒有自動開啟？
**A**: 手動開啟：http://localhost:8501

---

## 📊 資料集資訊

- **醫院數量**: 26 家台灣醫院
- **評論總數**: 5,007 則
- **主題數量**: K=7
- **模型類型**: Gensim LDA
- **分析期間**: 2024-2025

---

## 📞 需要協助？

如果遇到問題，請聯繫：[您的聯絡方式]

---

## 📄 授權說明

本專案僅供學術研究使用，請勿用於商業用途或公開發布。

---

**最後更新**: 2025-11-12
**版本**: 1.0.0
EOF

# 生成 Mac/Linux 啟動腳本
echo "🖥️  生成 Mac/Linux 啟動腳本..."
cat > "$PACKAGE_DIR/run_app.sh" << 'EOF'
#!/bin/bash

echo "======================================================================"
echo "🏥 台灣醫院 LDA 主題分析系統"
echo "   Taiwan Hospital LDA Topic Analysis System"
echo "======================================================================"
echo ""

# 檢查 Python
if ! command -v python3 &> /dev/null; then
    echo "❌ 錯誤: 找不到 Python 3"
    echo "   請先安裝 Python: https://www.python.org/downloads/"
    echo ""
    read -p "按任意鍵退出..."
    exit 1
fi

echo "✅ 找到 Python: $(python3 --version)"

# 建立虛擬環境（如果不存在）
if [ ! -d ".venv" ]; then
    echo ""
    echo "📦 首次執行：建立虛擬環境..."
    python3 -m venv .venv

    if [ $? -ne 0 ]; then
        echo "❌ 虛擬環境建立失敗"
        read -p "按任意鍵退出..."
        exit 1
    fi
fi

# 啟動虛擬環境
echo "🔧 啟動虛擬環境..."
source .venv/bin/activate

# 檢查 Streamlit 是否已安裝
if ! python -c "import streamlit" 2>/dev/null; then
    echo ""
    echo "📦 首次執行：安裝必要套件（需要 2-3 分鐘）..."
    echo "   請耐心等候..."
    echo ""

    pip install -q -r requirements.txt

    if [ $? -ne 0 ]; then
        echo "❌ 套件安裝失敗"
        echo "   請檢查網路連線後重試"
        read -p "按任意鍵退出..."
        exit 1
    fi

    echo "✅ 套件安裝完成！"
fi

# 啟動應用程式
echo ""
echo "======================================================================"
echo "🚀 啟動應用程式..."
echo "======================================================================"
echo ""
echo "📊 資料集資訊:"
echo "   🏥 台灣: 5,007 則評論, 26 家醫院, K=7 主題"
echo ""
echo "🌐 應用程式將在瀏覽器中開啟"
echo "   本地網址: http://localhost:8501"
echo ""
echo "⚠️  按 Ctrl+C 可停止應用程式"
echo "======================================================================"
echo ""

cd code/streamlit_app
python -m streamlit run taiwan_lda_explorer.py --server.port 8501

# 停用虛擬環境
deactivate
EOF

chmod +x "$PACKAGE_DIR/run_app.sh"

# 生成 Windows 啟動腳本
echo "🪟  生成 Windows 啟動腳本..."
cat > "$PACKAGE_DIR/run_app.bat" << 'EOF'
@echo off
chcp 65001 >nul
echo ======================================================================
echo 🏥 台灣醫院 LDA 主題分析系統
echo    Taiwan Hospital LDA Topic Analysis System
echo ======================================================================
echo.

REM 檢查 Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ 錯誤: 找不到 Python
    echo    請先安裝 Python: https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

for /f "tokens=*" %%i in ('python --version') do set PYTHON_VERSION=%%i
echo ✅ 找到 Python: %PYTHON_VERSION%

REM 建立虛擬環境（如果不存在）
if not exist ".venv" (
    echo.
    echo 📦 首次執行：建立虛擬環境...
    python -m venv .venv

    if errorlevel 1 (
        echo ❌ 虛擬環境建立失敗
        pause
        exit /b 1
    )
)

REM 啟動虛擬環境
echo 🔧 啟動虛擬環境...
call .venv\Scripts\activate

REM 檢查 Streamlit 是否已安裝
python -c "import streamlit" 2>nul
if errorlevel 1 (
    echo.
    echo 📦 首次執行：安裝必要套件（需要 2-3 分鐘）...
    echo    請耐心等候...
    echo.

    pip install -q -r requirements.txt

    if errorlevel 1 (
        echo ❌ 套件安裝失敗
        echo    請檢查網路連線後重試
        pause
        exit /b 1
    )

    echo ✅ 套件安裝完成！
)

REM 啟動應用程式
echo.
echo ======================================================================
echo 🚀 啟動應用程式...
echo ======================================================================
echo.
echo 📊 資料集資訊:
echo    🏥 台灣: 5,007 則評論, 26 家醫院, K=7 主題
echo.
echo 🌐 應用程式將在瀏覽器中開啟
echo    本地網址: http://localhost:8501
echo.
echo ⚠️  按 Ctrl+C 可停止應用程式
echo ======================================================================
echo.

cd code\streamlit_app
python -m streamlit run taiwan_lda_explorer.py --server.port 8501

REM 停用虛擬環境
deactivate
EOF

# 計算大小
echo ""
echo "📊 計算打包大小..."
PACKAGE_SIZE=$(du -sh "$PACKAGE_DIR" | cut -f1)

# 建立 zip 壓縮檔
echo "🗜️  壓縮打包檔案..."
cd "$SCRIPT_DIR"
zip -r -q "${PACKAGE_NAME}.zip" "$PACKAGE_NAME"

ZIP_SIZE=$(du -sh "${PACKAGE_NAME}.zip" | cut -f1)

# 完成
echo ""
echo "======================================================================="
echo "✅ 打包完成！"
echo "======================================================================="
echo ""
echo "📦 打包內容:"
echo "   - Streamlit 應用程式"
echo "   - LDA 模型檔案 (Taiwan K=7)"
echo "   - 視覺化圖表"
echo "   - 自動化啟動腳本 (Mac/Linux/Windows)"
echo ""
echo "📁 檔案位置:"
echo "   目錄: $PACKAGE_DIR"
echo "   壓縮檔: $SCRIPT_DIR/${PACKAGE_NAME}.zip"
echo ""
echo "📊 檔案大小:"
echo "   解壓縮前: $ZIP_SIZE"
echo "   解壓縮後: $PACKAGE_SIZE"
echo ""
echo "🎯 分享方式:"
echo "   1. Email 附件"
echo "   2. Dropbox / Google Drive 分享連結"
echo "   3. USB 隨身碟直接拷貝"
echo ""
echo "📧 朋友使用步驟:"
echo "   1. 解壓縮 ${PACKAGE_NAME}.zip"
echo "   2. 執行 run_app.sh (Mac) 或 run_app.bat (Windows)"
echo "   3. 等待瀏覽器自動開啟"
echo "======================================================================"
