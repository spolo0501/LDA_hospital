# Apple Silicon (M1/M2/M3/M4) 架構問題解決方案

## 🍎 問題說明

如果你在 Apple Silicon Mac 上遇到這個錯誤：

```
ImportError: dlopen(...) (mach-o file, but is an incompatible architecture
(have 'x86_64', need 'arm64'))
```

這是因為 **Python 套件的 CPU 架構不匹配**。

---

## 🎯 根本原因

### 你的 Mac 有兩種執行模式：

1. **ARM64 (原生模式)** - 為 Apple Silicon 優化
2. **x86_64 (Rosetta 2)** - 為 Intel 處理器設計，透過模擬執行

### 問題發生原因：

你的 Terminal 或 Python 在 **Rosetta 2 (x86_64) 模式**下運行，但：
- macOS 系統期望使用 **ARM64** 的原生二進制檔案
- 安裝的 Python 套件是 **x86_64** 版本
- 導致架構不匹配錯誤

---

## ✅ 解決方案（已修復）

### 我已經完成以下修復：

1. **重建虛擬環境（ARM64 原生）**
   ```bash
   # 刪除舊的 x86_64 環境
   rm -rf venv

   # 建立 ARM64 原生環境
   arch -arm64 python3 -m venv venv
   ```

2. **安裝 ARM64 套件**
   ```bash
   # 使用 ARM64 架構安裝
   arch -arm64 venv/bin/pip install -r requirements.txt
   ```

3. **更新啟動腳本**
   - 自動檢測 Apple Silicon (M1/M2/M3/M4)
   - 強制使用 ARM64 架構
   - 避免 Rosetta 2 模擬

---

## 🚀 現在可以正常啟動了

直接執行啟動腳本：

```bash
./code/streamlit_app/run_app.sh
```

你會看到：

```
🏥 啟動台灣醫院 LDA 分析系統...
================================

🍎 檢測到 Apple Silicon (Apple M4)
✅ 找到虛擬環境
🔍 檢查套件狀態...

📂 工作目錄: /path/to/LDA_hospital
🐍 Python: arch -arm64 venv/bin/python
📦 套件版本:
   - 架構: arm64 ✅
   - Streamlit: 1.51.0
   - Pandas: 2.3.3
   - NumPy: 1.26.4

✅ 正在啟動應用程式...
```

---

## 🔍 驗證架構

確認虛擬環境使用正確的架構：

```bash
cd /path/to/LDA_hospital
arch -arm64 venv/bin/python -c "import platform; print(f'架構: {platform.machine()}')"
```

應該顯示：
```
架構: arm64
```

---

## 🛠️ 如果還有問題

### 重建虛擬環境

```bash
cd /path/to/LDA_hospital

# 1. 刪除舊環境
rm -rf venv

# 2. 強制使用 ARM64 建立
arch -arm64 python3 -m venv venv

# 3. 安裝套件
arch -arm64 venv/bin/pip install --upgrade pip setuptools wheel
arch -arm64 venv/bin/pip install -r requirements.txt

# 4. 驗證
arch -arm64 venv/bin/python -c "import streamlit, pandas, numpy; print('✅ 成功')"
```

### 檢查 Terminal 模式

確認 Terminal 不是在 Rosetta 模式：

```bash
# 檢查當前 shell 架構
uname -m
# 如果顯示 x86_64，代表在 Rosetta 模式

# 檢查實際 CPU
sysctl -n machdep.cpu.brand_string
# 應該顯示 "Apple M1/M2/M3/M4"
```

如果 Terminal 在 Rosetta 模式：
1. 關閉 Terminal
2. 在應用程式中找到 Terminal.app
3. 右鍵點擊 > 取得資訊
4. 取消勾選「使用 Rosetta 開啟」
5. 重新開啟 Terminal

---

## 📚 為什麼會這樣？

### Apple Silicon 的特殊性：

1. **Universal Binary**
   - 某些 Python 可以同時支援 x86_64 和 ARM64
   - 但預設可能使用錯誤的架構

2. **Rosetta 2**
   - 允許執行 Intel 應用程式
   - 但會導致架構混淆

3. **Native ARM64**
   - 為 Apple Silicon 優化
   - 效能更好、更穩定

---

## 💡 最佳實踐

### 在 Apple Silicon Mac 上：

1. **總是使用 ARM64 原生 Python**
   ```bash
   arch -arm64 python3 --version
   ```

2. **檢查虛擬環境架構**
   ```bash
   file venv/bin/python
   # 應該包含 "arm64"
   ```

3. **使用啟動腳本**
   - 已經內建架構檢測
   - 自動使用正確架構

4. **避免混合架構**
   - 不要混用 x86_64 和 ARM64 套件
   - 重建環境時刪除舊的

---

## 🎓 技術細節

### 錯誤訊息解析

```
(have 'x86_64', need 'arm64')
```

意思是：
- **have 'x86_64'**: 安裝的套件是 Intel 版本
- **need 'arm64'**: 系統需要 Apple Silicon 版本

### 為什麼 NumPy 2.x 也會有問題？

NumPy 2.x 的二進制接口改變：
- 某些依賴套件還沒完全支援
- 降級到 1.26.4 可以避免相容性問題
- 無論 x86_64 或 ARM64 都建議使用 1.x

---

## ✅ 檢查清單

確認環境正確：

- [x] CPU 是 Apple Silicon (M1/M2/M3/M4)
- [x] 虛擬環境使用 ARM64 Python
- [x] 套件安裝時使用 ARM64
- [x] 啟動腳本自動檢測架構
- [x] 所有套件正常導入
- [x] NumPy 使用 1.26.4

---

## 📞 相關資源

- [Apple Silicon 指南](https://support.apple.com/zh-tw/HT211861)
- [Python 在 Apple Silicon 上的使用](https://www.python.org/downloads/macos/)
- [Rosetta 2 說明](https://support.apple.com/zh-tw/HT211861)

---

## 🎉 總結

**問題已解決！** 你的環境現在使用：
- ✅ ARM64 原生 Python
- ✅ ARM64 原生套件
- ✅ 自動架構檢測
- ✅ 優化的效能

直接執行 `./code/streamlit_app/run_app.sh` 就可以了！

---

**建立日期**: 2025-11-11
**適用機型**: Apple Silicon Mac (M1/M2/M3/M4)
**Python 版本**: 3.10.11
**已測試**: Apple M4
