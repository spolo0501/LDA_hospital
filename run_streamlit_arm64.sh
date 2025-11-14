#!/bin/bash
# ARM64 原生 Streamlit 啟動腳本
# 自動處理 conda 環境衝突

echo "🔧 準備 ARM64 原生環境..."

# 如果在 conda 環境中，先停用
if [ -n "$CONDA_DEFAULT_ENV" ]; then
    echo "⚠️  檢測到 conda 環境: $CONDA_DEFAULT_ENV (x86_64)"
    echo "   正在停用以使用 ARM64 原生環境..."

    # 停用 conda
    if [ -f "/Users/simon/anaconda3/etc/profile.d/conda.sh" ]; then
        source "/Users/simon/anaconda3/etc/profile.d/conda.sh"
        conda deactivate
    fi

    # 清理 conda 環境變數
    unset CONDA_DEFAULT_ENV
    unset CONDA_PREFIX
    unset CONDA_PYTHON_EXE

    echo "✅ 已停用 conda 環境"
    echo ""
fi

# 驗證當前架構
CURRENT_ARCH=$(arch)
if [ "$CURRENT_ARCH" = "i386" ] || [ "$CURRENT_ARCH" = "x86_64" ]; then
    echo "⚠️  當前 shell 仍在 Rosetta 模式"
    echo "   切換到 ARM64 模式..."
    echo ""

    # 在 ARM64 模式下重新執行此腳本
    exec arch -arm64 /bin/bash "$0" "$@"
fi

echo "✅ 當前架構: $(uname -m)"
echo ""

# 執行原始啟動腳本
exec ./code/streamlit_app/run_app.sh
