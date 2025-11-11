#!/bin/bash
# 台灣醫院 LDA 分析 Streamlit 應用程式啟動腳本

echo "🏥 啟動台灣醫院 LDA 分析系統..."
echo "================================"
echo ""

# 取得腳本所在目錄
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# 切換到專案根目錄（上兩層）
PROJECT_ROOT="$SCRIPT_DIR/../.."
cd "$PROJECT_ROOT"

# 檢測 CPU 架構（檢查實際 CPU 型號，不只是當前 shell）
CPU_BRAND=$(sysctl -n machdep.cpu.brand_string 2>/dev/null || echo "")
if [[ "$CPU_BRAND" == *"Apple"* ]]; then
    echo "🍎 檢測到 Apple Silicon ($CPU_BRAND)"
    # 強制使用 ARM64 架構
    PYTHON_CMD="arch -arm64 python3"
    VENV_PYTHON="arch -arm64 venv/bin/python"
    VENV_PIP="arch -arm64 venv/bin/pip"
    STREAMLIT_CMD="arch -arm64"
else
    ARCH=$(uname -m)
    if [ "$ARCH" = "arm64" ]; then
        echo "🍎 檢測到 ARM64 架構"
        PYTHON_CMD="python3"
        VENV_PYTHON="venv/bin/python"
        VENV_PIP="venv/bin/pip"
        STREAMLIT_CMD=""
    else
        echo "💻 檢測到 Intel (x86_64)"
        PYTHON_CMD="python3"
        VENV_PYTHON="venv/bin/python"
        VENV_PIP="venv/bin/pip"
        STREAMLIT_CMD=""
    fi
fi
echo ""

# 檢查虛擬環境
if [ ! -d "venv" ]; then
    echo "❌ 找不到虛擬環境！"
    echo "正在建立虛擬環境..."
    $PYTHON_CMD -m venv venv
    echo "✅ 虛擬環境建立完成"
    echo ""
    echo "正在安裝套件..."
    $VENV_PIP install --upgrade pip setuptools wheel --quiet
    $VENV_PIP install -r requirements.txt --quiet
    echo "✅ 套件安裝完成"
    echo ""
else
    echo "✅ 找到虛擬環境"
fi

# 驗證並修復套件
echo "🔍 檢查套件狀態..."
if ! $VENV_PYTHON -c "import streamlit" &> /dev/null; then
    echo "❌ 找不到 streamlit，正在安裝..."
    $VENV_PIP install -r requirements.txt --quiet
fi

# 檢查 numpy/pandas 是否能正常導入
if ! $VENV_PYTHON -c "import numpy, pandas" &> /dev/null 2>&1; then
    echo "⚠️  偵測到套件導入問題，正在修復..."
    $VENV_PIP uninstall numpy pandas -y --quiet
    $VENV_PIP install numpy==1.26.4 pandas --quiet
    echo "✅ 套件已修復"
fi

# 清理 Python 快取
find . -type d -name "__pycache__" ! -path "./venv/*" -exec rm -rf {} + 2>/dev/null

echo ""
echo "📂 工作目錄: $(pwd)"
echo "🐍 Python: $VENV_PYTHON"
echo "📦 套件版本:"
$VENV_PYTHON -c "import platform, streamlit, pandas, numpy; print(f'   - 架構: {platform.machine()}'); print(f'   - Streamlit: {streamlit.__version__}'); print(f'   - Pandas: {pandas.__version__}'); print(f'   - NumPy: {numpy.__version__}')" 2>/dev/null || echo "   ⚠️  套件檢查失敗"
echo ""

# 啟動 Streamlit
echo "✅ 正在啟動應用程式..."
echo "📍 應用程式將在瀏覽器中開啟: http://localhost:8501"
echo ""
echo "💡 提示："
echo "   - 按 Ctrl+C 可以停止應用程式"
echo "   - 修改程式碼後會自動重新載入"
echo ""

# 從專案根目錄執行，使用正確架構的 Python
$VENV_PYTHON -m streamlit run code/streamlit_app/taiwan_lda_explorer.py
