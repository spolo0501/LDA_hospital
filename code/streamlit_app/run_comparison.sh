#!/bin/bash

# 台美醫院評論比較分析系統 - 啟動腳本
# Taiwan-USA Hospital Review Comparison System - Launch Script

echo "======================================================"
echo "🌏 台美醫院評論跨文化比較分析系統"
echo "   Taiwan-USA Hospital Review Cross-Cultural Comparison"
echo "======================================================"
echo ""

# 設定路徑
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# 檢查 Python
if ! command -v python3 &> /dev/null; then
    echo "❌ 錯誤: 找不到 Python 3"
    echo "   請先安裝 Python 3"
    exit 1
fi

echo "✅ Python 版本: $(python3 --version)"

# 檢查 Streamlit
if ! python3 -m streamlit version &> /dev/null; then
    echo "❌ 錯誤: 找不到 Streamlit"
    echo "   請執行: pip3 install streamlit"
    exit 1
fi

echo "✅ Streamlit 版本: $(python3 -m streamlit version | head -1)"

# 檢查必要套件
echo ""
echo "📦 檢查必要套件..."

PACKAGES=("plotly" "pandas" "numpy" "gensim" "matplotlib" "seaborn")
MISSING_PACKAGES=()

for package in "${PACKAGES[@]}"; do
    if python3 -c "import $package" 2>/dev/null; then
        echo "  ✅ $package"
    else
        echo "  ❌ $package (缺少)"
        MISSING_PACKAGES+=("$package")
    fi
done

if [ ${#MISSING_PACKAGES[@]} -ne 0 ]; then
    echo ""
    echo "⚠️  發現缺少套件，請執行以下命令安裝:"
    echo "   pip3 install ${MISSING_PACKAGES[@]}"
    echo ""
    read -p "是否現在安裝? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        pip3 install "${MISSING_PACKAGES[@]}" --user
    else
        echo "請先安裝必要套件後再執行此腳本"
        exit 1
    fi
fi

# 檢查資料檔案
echo ""
echo "📁 檢查資料檔案..."

if [ ! -f "../../results/taiwan_lda_k7/lda_k7_lda_model.pkl" ]; then
    echo "❌ 錯誤: 找不到台灣 LDA 模型"
    echo "   路徑: ../../results/taiwan_lda_k7/lda_k7_lda_model.pkl"
    exit 1
fi
echo "  ✅ 台灣 LDA K=7 模型"

if [ ! -f "../../results/usa_lda_k7/usa_gensim_lda_k6_model.pkl" ]; then
    echo "❌ 錯誤: 找不到美國 LDA 模型"
    echo "   路徑: ../../results/usa_lda_k7/usa_gensim_lda_k6_model.pkl"
    exit 1
fi
echo "  ✅ 美國 LDA K=6 模型"

if [ ! -f "../../results/usa_lda_k7/usa_k6_topic_analysis_20251107_122236.csv" ]; then
    echo "❌ 錯誤: 找不到美國評論資料"
    echo "   路徑: ../../results/usa_lda_k7/usa_k6_topic_analysis_20251107_122236.csv"
    exit 1
fi
echo "  ✅ 美國評論資料"

# 啟動應用程式
echo ""
echo "======================================================"
echo "🚀 啟動應用程式..."
echo "======================================================"
echo ""
echo "📊 資料集資訊:"
echo "  🇹🇼 台灣: 5,007 則評論, 26 家醫院, K=7 主題"
echo "  🇺🇸 美國: 3,240 則評論, K=6 主題"
echo ""
echo "🌐 應用程式將在瀏覽器中開啟"
echo "   本地網址: http://localhost:8503"
echo ""
echo "⚠️  按 Ctrl+C 可停止應用程式"
echo "======================================================"
echo ""

# 啟動 Streamlit
python3 -m streamlit run taiwan_usa_comparison.py --server.port 8503

# 如果 Streamlit 異常退出
if [ $? -ne 0 ]; then
    echo ""
    echo "❌ 應用程式啟動失敗"
    echo "   請檢查上方錯誤訊息"
    exit 1
fi
