#!/bin/bash
# Anaconda ARM64 完整重新安裝腳本
# 適用於 Apple Silicon Mac (M1/M2/M3/M4)

set -e  # 遇到錯誤立即停止

echo "================================================"
echo "Anaconda ARM64 重新安裝腳本"
echo "================================================"
echo ""

# 1. 備份現有環境列表
echo "📋 步驟 1: 備份現有環境資訊..."
if [ -d ~/anaconda3 ]; then
    ~/anaconda3/bin/conda env list > ~/anaconda_env_backup_$(date +%Y%m%d).txt 2>/dev/null || true

    if [ -d ~/anaconda3/envs/py10 ]; then
        echo "   備份 py10 環境套件列表..."
        ~/anaconda3/bin/conda list -n py10 > ~/py10_packages_backup_$(date +%Y%m%d).txt 2>/dev/null || true
    fi

    echo "   ✅ 備份完成"
    echo "   備份檔案位置: ~/"
else
    echo "   ⚠️  找不到 Anaconda 安裝"
fi
echo ""

# 2. 完全移除舊的 Anaconda
echo "🗑️  步驟 2: 移除舊的 Anaconda..."
if [ -d ~/anaconda3 ]; then
    echo "   正在移除 ~/anaconda3 ..."
    rm -rf ~/anaconda3
    echo "   ✅ 已移除主目錄"
fi

if [ -d ~/.conda ]; then
    echo "   正在移除 ~/.conda ..."
    rm -rf ~/.conda
    echo "   ✅ 已移除設定目錄"
fi

if [ -d ~/.continuum ]; then
    echo "   正在移除 ~/.continuum ..."
    rm -rf ~/.continuum
    echo "   ✅ 已移除 continuum 目錄"
fi

echo "   ✅ Anaconda 移除完成"
echo ""

# 3. 清理 shell 設定檔案中的 conda 初始化
echo "🧹 步驟 3: 清理 shell 設定檔..."

for rcfile in ~/.bashrc ~/.bash_profile ~/.zshrc; do
    if [ -f "$rcfile" ]; then
        if grep -q "conda initialize" "$rcfile"; then
            echo "   清理 $rcfile ..."

            # 備份原檔案
            cp "$rcfile" "${rcfile}.backup_$(date +%Y%m%d)"

            # 移除 conda 初始化區塊
            sed -i.tmp '/# >>> conda initialize >>>/,/# <<< conda initialize <<</d' "$rcfile"
            rm -f "${rcfile}.tmp"

            echo "   ✅ 已清理 $rcfile (備份: ${rcfile}.backup_$(date +%Y%m%d))"
        fi
    fi
done

echo "   ✅ Shell 設定清理完成"
echo ""

# 4. 下載 ARM64 Anaconda
echo "📥 步驟 4: 下載 ARM64 版本的 Anaconda..."
echo ""
echo "   ⚠️  請手動完成以下步驟："
echo ""
echo "   1. 開啟瀏覽器前往: https://www.anaconda.com/download"
echo "   2. 選擇 macOS"
echo "   3. 選擇 'Apple Silicon Installer' (重要！)"
echo "   4. 下載檔案: Anaconda3-*-MacOSX-arm64.sh"
echo ""
echo "   下載完成後，檔案通常在 ~/Downloads/"
echo ""

read -p "   下載完成後按 Enter 繼續..."
echo ""

# 5. 找出下載的安裝檔
echo "🔍 步驟 5: 尋找安裝檔..."
INSTALLER=$(find ~/Downloads -name "Anaconda3-*-MacOSX-arm64.sh" -type f 2>/dev/null | head -1)

if [ -z "$INSTALLER" ]; then
    echo "   ❌ 找不到 ARM64 安裝檔"
    echo ""
    echo "   請確認："
    echo "   - 檔名包含 'arm64'"
    echo "   - 檔案在 ~/Downloads/ 目錄"
    echo "   - 檔案是 .sh 格式"
    echo ""
    echo "   找到檔案後，手動執行:"
    echo "   bash ~/Downloads/Anaconda3-YYYY.MM-MacOSX-arm64.sh"
    exit 1
fi

echo "   ✅ 找到安裝檔: $INSTALLER"
echo ""

# 6. 執行安裝
echo "🚀 步驟 6: 安裝 ARM64 Anaconda..."
echo ""
echo "   重要提示："
echo "   - 同意授權條款 (輸入 yes)"
echo "   - 安裝位置使用預設 ~/anaconda3"
echo "   - 詢問是否初始化，選擇 yes"
echo ""

bash "$INSTALLER"

echo ""
echo "   ✅ 安裝完成"
echo ""

# 7. 重新載入 shell
echo "🔄 步驟 7: 重新載入 shell 設定..."
if [ -f ~/.zshrc ]; then
    source ~/.zshrc
elif [ -f ~/.bashrc ]; then
    source ~/.bashrc
fi
echo "   ✅ 完成"
echo ""

# 8. 驗證安裝
echo "✅ 步驟 8: 驗證安裝..."
if [ -f ~/anaconda3/bin/conda ]; then
    echo "   Conda 版本:"
    ~/anaconda3/bin/conda --version

    echo ""
    echo "   Python 架構:"
    ~/anaconda3/bin/python -c "import platform; print(f'   架構: {platform.machine()}'); print(f'   版本: {platform.python_version()}')"

    ARCH=$(~/anaconda3/bin/python -c "import platform; print(platform.machine())")

    if [ "$ARCH" = "arm64" ]; then
        echo ""
        echo "   🎉 成功！Anaconda 現在是 ARM64 原生版本"
    else
        echo ""
        echo "   ⚠️  警告：架構仍是 $ARCH，不是 arm64"
        echo "   請確認下載的是 ARM64 版本"
    fi
else
    echo "   ❌ 安裝失敗，找不到 conda"
fi

echo ""
echo "================================================"
echo "安裝完成！"
echo "================================================"
echo ""
echo "下一步："
echo "1. 關閉並重新開啟終端機"
echo "2. 執行 'conda --version' 驗證"
echo "3. 執行重建 py10 環境的腳本"
echo ""
