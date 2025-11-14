#!/bin/bash
# 重建 py10 環境（ARM64 原生）

set -e

echo "================================================"
echo "重建 py10 環境 (ARM64 原生)"
echo "================================================"
echo ""

# 檢查 conda 是否為 ARM64
echo "🔍 檢查 Anaconda 架構..."
CONDA_ARCH=$(~/anaconda3/bin/python -c "import platform; print(platform.machine())" 2>/dev/null)

if [ "$CONDA_ARCH" != "arm64" ]; then
    echo "❌ 錯誤：Anaconda 不是 ARM64 架構"
    echo "   當前架構: $CONDA_ARCH"
    echo ""
    echo "請先執行: ./REINSTALL_ANACONDA_ARM64.sh"
    exit 1
fi

echo "✅ Anaconda 是 ARM64 原生版本"
echo ""

# 檢查 py10 環境是否存在
if [ -d ~/anaconda3/envs/py10 ]; then
    echo "⚠️  偵測到現有的 py10 環境"
    echo ""
    echo "當前 py10 架構:"
    ~/anaconda3/envs/py10/bin/python -c "import platform; print(f'   架構: {platform.machine()}')" 2>/dev/null || echo "   無法檢查"
    echo ""

    read -p "是否要移除並重建？(y/n) " -n 1 -r
    echo ""

    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "🗑️  移除舊的 py10 環境..."
        ~/anaconda3/bin/conda env remove -n py10 -y
        echo "✅ 已移除"
        echo ""
    else
        echo "❌ 取消操作"
        exit 0
    fi
fi

# 建立新的 py10 環境
echo "🚀 建立新的 py10 環境 (Python 3.10, ARM64)..."
echo ""

~/anaconda3/bin/conda create -n py10 python=3.10 -y

echo ""
echo "✅ py10 環境建立完成"
echo ""

# 驗證架構
echo "🔍 驗證環境..."
echo ""

ARCH=$(~/anaconda3/envs/py10/bin/python -c "import platform; print(platform.machine())")
VERSION=$(~/anaconda3/envs/py10/bin/python -c "import platform; print(platform.python_version())")

echo "   架構: $ARCH"
echo "   Python 版本: $VERSION"
echo ""

if [ "$ARCH" = "arm64" ]; then
    echo "🎉 成功！py10 環境現在是 ARM64 原生版本"
else
    echo "⚠️  警告：架構是 $ARCH，不是 arm64"
fi

echo ""
echo "================================================"
echo "完成！"
echo "================================================"
echo ""
echo "使用方式："
echo "   conda activate py10"
echo ""
echo "安裝常用套件："
echo "   conda activate py10"
echo "   conda install numpy pandas matplotlib jupyter -y"
echo ""
