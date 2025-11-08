# 🔧 Numpy 導入錯誤故障排除指南

## 📋 問題描述

### 錯誤訊息
```
ImportError: Unable to import required dependencies:
numpy: Error importing numpy: you should not try to import numpy from
        its source directory; please exit the numpy source tree, and relaunch
        your python interpreter from there.
```

### 症狀
- ✅ 在**外部 Terminal** 運行正常
- ❌ 在 **Cursor IDE Terminal** 運行失敗
- ❌ 使用 `subprocess.run()` 調用子進程時失敗

---

## 🎯 根本原因

### 問題根源：環境變量污染

IDE Terminal 啟動時可能設定了錯誤的環境變量：
```bash
export PYTHONPATH="/some/path:$PYTHONPATH"
export PYTHONHOME="/wrong/path"
```

### 影響鏈
```
IDE Terminal 啟動
  ↓ 設定污染的 PYTHONPATH/PYTHONHOME
你的 Shell Session
  ↓ 繼承污染的環境變量
batch_scrape_hospitals_20.py (父進程)
  ↓ subprocess.run() 繼承父進程環境
working_scraper.py (子進程)
  ↓ import pandas/numpy
  ❌ 使用污染的搜尋路徑失敗
```

---

## 🔍 快速診斷

### 步驟 1：運行診斷工具
```bash
python3 diagnose_env.py
```

### 步驟 2：檢查關鍵指標

#### ✅ 正常環境應該顯示：
```
🔧 5. 套件安裝位置
   ✅ numpy 1.26.4
      位置: /Users/simon/Library/Python/3.10/lib/python/site-packages/numpy/__init__.py
   ✅ pandas 2.3.3
      位置: /Users/simon/Library/Python/3.10/lib/python/site-packages/pandas/__init__.py

🧪 6. 測試子進程導入
   ✅ 子進程導入成功
```

#### ❌ 問題環境會顯示：
```
🔧 5. 套件安裝位置
   ❌ numpy 導入失敗: Error importing numpy...
   ❌ pandas 導入失敗: Unable to import required dependencies...

🧪 6. 測試子進程導入
   ❌ 子進程導入失敗
```

---

## ✅ 解決方案

### 方案 1：一鍵修復（推薦）⭐

```bash
./fix_ide_env.sh
```

**這個腳本會：**
1. 清除 Python 快取（`__pycache__`, `.pyc` 檔案）
2. **清除污染的環境變量**（`PYTHONPATH`, `PYTHONHOME`）
3. 驗證 Python 環境
4. 測試套件導入
5. 如果需要，重新安裝套件

---

### 方案 2：手動修復

#### 在 IDE Terminal 中執行：

```bash
# 1. 清除環境變量（最重要！）
unset PYTHONPATH
unset PYTHONHOME

# 2. 清除 Python 快取
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null
find . -name "*.pyc" -delete 2>/dev/null

# 3. 驗證修復
python3 -c "import numpy; import pandas; print('✅ 修復成功！')"

# 4. 如果還是失敗，重新安裝套件
python3 -m pip install --force-reinstall --no-cache-dir "numpy>=1.18.5,<2.0" pandas
```

---

### 方案 3：重啟 IDE Terminal

有時最簡單的方法最有效：

1. 關閉 Cursor IDE 的 Terminal 標籤
2. 開啟新的 Terminal (`Cmd+` 或 `Ctrl+`)
3. 運行診斷：`python3 diagnose_env.py`

---

### 方案 4：使用安全包裝腳本

如果上述方法都無效，使用包裝腳本確保乾淨環境：

```bash
./run_batch_safe.sh
```

這個腳本會：
- 自動清除環境變量
- 使用絕對路徑運行 Python
- 驗證套件後再運行

---

## 🛡️ 預防措施

### 1. 檢查 Shell 配置

編輯 `~/.zshrc` 或 `~/.bashrc`，檢查是否有問題設定：

```bash
# ❌ 避免這樣設定
export PYTHONPATH="/some/project:$PYTHONPATH"

# ✅ 如果需要，使用專案特定的虛擬環境
# alias myproject="cd /path && source venv/bin/activate"
```

### 2. 使用虛擬環境（推薦）

```bash
# 創建虛擬環境
python3 -m venv venv

# 啟動虛擬環境
source venv/bin/activate

# 安裝套件
pip install numpy pandas requests

# 運行腳本
python batch_scrape_hospitals_20.py

# 離開虛擬環境
deactivate
```

### 3. 配置 IDE Python 設定

在 Cursor IDE 中：
1. 打開 Settings (Cmd+, 或 Ctrl+,)
2. 搜尋 "Python: Python Path"
3. 設定為：`/usr/local/bin/python3`

---

## 📊 為什麼外部 Terminal 總是正常？

| 特性 | 外部 Terminal | IDE Terminal |
|------|---------------|--------------|
| 環境來源 | 直接從 shell 配置 | IDE + shell 配置 |
| PYTHONPATH | 通常未設定 | 可能被 IDE 設定 |
| 啟動順序 | shell → 程式 | IDE → shell → 程式 |
| 環境污染風險 | 低 | 中-高 |

---

## 🎯 完整檢查清單

使用這個清單來診斷問題：

- [ ] 1. 運行 `python3 diagnose_env.py` 診斷
- [ ] 2. 檢查 `PYTHONPATH` 和 `PYTHONHOME` 環境變量
- [ ] 3. 確認 Python 解釋器位置：`which python3`
- [ ] 4. 檢查套件安裝：`python3 -c "import numpy, pandas"`
- [ ] 5. 測試子進程導入：看診斷腳本輸出
- [ ] 6. 如果失敗，運行 `./fix_ide_env.sh`
- [ ] 7. 重新運行診斷驗證修復
- [ ] 8. 如果還是失敗，考慮使用虛擬環境

---

## 🚀 快速參考命令

```bash
# 診斷問題
python3 diagnose_env.py

# 一鍵修復
./fix_ide_env.sh

# 手動清除環境變量
unset PYTHONPATH; unset PYTHONHOME

# 驗證修復
python3 -c "import numpy, pandas; print('✅ OK')"

# 使用安全腳本運行
./run_batch_safe.sh

# 外部 Terminal 直接運行（推薦用於大規模任務）
python3 batch_scrape_hospitals_20.py

# 後台運行
nohup python3 batch_scrape_hospitals_20.py > scraping.log 2>&1 &
tail -f scraping.log
```

---

## 💡 關鍵學習點

### 1. **環境變量是隱形殺手**
- 不會顯示在錯誤訊息中
- 會傳播到子進程
- IDE 可能會自動設定

### 2. **子進程繼承父進程環境**
- `subprocess.run()` 會繼承所有環境變量
- 即使父進程正常，子進程可能失敗
- 需要測試完整的執行鏈

### 3. **IDE Terminal ≠ 外部 Terminal**
- IDE 會修改環境
- 可能注入額外變量
- 需要額外的故障排除步驟

### 4. **清除環境變量 > 重新安裝套件**
- `unset PYTHONPATH` 比 `pip install --force-reinstall` 更有效
- 環境問題不能用重新安裝解決
- 先診斷環境，再考慮重新安裝

---

## 📞 還是無法解決？

如果上述所有方法都無效：

### 終極方案：完全重置環境

```bash
# 1. 完全移除 Python 套件
python3 -m pip uninstall -y numpy pandas

# 2. 清除所有快取
rm -rf ~/.cache/pip
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null

# 3. 重新安裝
python3 -m pip install --no-cache-dir numpy==1.26.4 pandas==2.3.3

# 4. 重啟 IDE
# 完全退出並重新開啟 Cursor IDE

# 5. 驗證
python3 diagnose_env.py
```

---

## 📚 相關資源

- [NumPy Import Error Troubleshooting](https://numpy.org/devdocs/user/troubleshooting-importerror.html)
- Python subprocess 環境繼承：[docs.python.org/3/library/subprocess.html](https://docs.python.org/3/library/subprocess.html)
- 虛擬環境指南：[docs.python.org/3/tutorial/venv.html](https://docs.python.org/3/tutorial/venv.html)

---

## 📝 版本記錄

- **2025-10-28**: 首次創建
  - 記錄 IDE Terminal vs 外部 Terminal 的 numpy 導入問題
  - 解決方案：清除 PYTHONPATH 和 PYTHONHOME 環境變量
  - 工具：diagnose_env.py, fix_ide_env.sh, run_batch_safe.sh

---

**記住：環境變量是隱形的，但它們的影響是真實的！** 🎯
