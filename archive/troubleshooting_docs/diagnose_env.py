#!/usr/bin/env python3
"""
環境診斷工具 - 比較不同 Terminal 環境的差異
"""

import os
import sys
import subprocess

print("=" * 70)
print("🔍 Python 環境診斷工具")
print("=" * 70)
print()

print("📍 1. Python 解釋器資訊")
print(f"   執行檔位置: {sys.executable}")
print(f"   版本: {sys.version.split()[0]}")
print(f"   完整版本: {sys.version}")
print()

print("📂 2. 工作目錄")
print(f"   當前目錄: {os.getcwd()}")
print(f"   目錄內容 (與 numpy 相關):")
for item in os.listdir('.'):
    if 'numpy' in item.lower() or item == 'setup.py':
        print(f"      ⚠️  {item}")
print()

print("🌍 3. 環境變量")
print(f"   PYTHONPATH: {os.environ.get('PYTHONPATH', '未設定')}")
print(f"   PATH (前300字元): {os.environ.get('PATH', '')[:300]}...")
print(f"   VIRTUAL_ENV: {os.environ.get('VIRTUAL_ENV', '未設定')}")
print()

print("📦 4. sys.path (Python 搜尋路徑)")
for i, path in enumerate(sys.path, 1):
    indicator = " ⚠️ 當前目錄" if path == "" or path == "." else ""
    print(f"   {i}. {path if path else '(當前目錄)'}{indicator}")
print()

print("🔧 5. 套件安裝位置")
try:
    import numpy
    print(f"   ✅ numpy {numpy.__version__}")
    print(f"      位置: {numpy.__file__}")
except ImportError as e:
    print(f"   ❌ numpy 導入失敗: {e}")

try:
    import pandas
    print(f"   ✅ pandas {pandas.__version__}")
    print(f"      位置: {pandas.__file__}")
except ImportError as e:
    print(f"   ❌ pandas 導入失敗: {e}")
print()

print("🧪 6. 測試子進程導入")
test_code = "import pandas; print('pandas OK')"
result = subprocess.run(
    [sys.executable, '-c', test_code],
    capture_output=True,
    text=True,
    cwd=os.getcwd()
)
if result.returncode == 0:
    print(f"   ✅ 子進程導入成功")
else:
    print(f"   ❌ 子進程導入失敗")
    print(f"   錯誤: {result.stderr[:200]}")
print()

print("💡 診斷建議:")
# 檢查當前目錄是否有 numpy 相關檔案
has_numpy_conflict = any('numpy' in item.lower() for item in os.listdir('.'))
if has_numpy_conflict:
    print("   ⚠️  當前目錄含有 numpy 相關檔案，可能造成導入衝突")
    print("   建議：切換到不同的工作目錄運行腳本")
else:
    print("   ✅ 當前目錄沒有明顯衝突")

if sys.path[0] in ['', '.']:
    print("   ⚠️  sys.path 包含當前目錄，可能導致意外的模組導入")
else:
    print("   ✅ sys.path 設定正常")

print()
print("=" * 70)
print("🎯 在 Cursor IDE 和外部 Terminal 都運行此腳本，比較結果！")
print("=" * 70)
