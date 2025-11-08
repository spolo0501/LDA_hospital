#!/bin/bash
# 修復 IDE Terminal 環境的腳本

echo "🔧 修復 IDE Terminal 環境..."
echo ""

# 1. 清除當前目錄的 Python 快取
echo "1️⃣ 清除 Python 快取..."
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null
find . -name "*.pyc" -delete 2>/dev/null
find . -name "*.pyo" -delete 2>/dev/null
echo "   ✅ 快取已清除"
echo ""

# 2. 清除可能有問題的環境變量
echo "2️⃣ 清除環境變量..."
unset PYTHONPATH
unset PYTHONHOME
echo "   ✅ PYTHONPATH 和 PYTHONHOME 已清除"
echo ""

# 3. 驗證 Python 環境
echo "3️⃣ 驗證 Python 環境..."
python3 -c "import sys; print('   Python:', sys.executable)"
python3 -c "import sys; print('   版本:', sys.version.split()[0])"
echo ""

# 4. 測試 numpy 和 pandas 導入
echo "4️⃣ 測試套件導入..."
if python3 -c "import numpy; import pandas" 2>/dev/null; then
    python3 -c "import numpy, pandas; print('   ✅ numpy', numpy.__version__); print('   ✅ pandas', pandas.__version__)"
else
    echo "   ❌ 導入失敗，嘗試重新安裝..."
    python3 -m pip install --force-reinstall --no-cache-dir "numpy>=1.18.5,<2.0" pandas
fi
echo ""

echo "🎉 修復完成！請重新運行你的腳本。"
echo ""
echo "💡 如果問題持續，請："
echo "   1. 完全關閉並重新開啟 Cursor IDE"
echo "   2. 或使用外部 Terminal 運行腳本"
