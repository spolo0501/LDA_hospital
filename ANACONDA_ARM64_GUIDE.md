# Anaconda ARM64 重新安裝完整指南

## 🔍 檢查結果

你的當前 Anaconda 狀態：

```
Anaconda 基礎: x86_64 (Python 3.6.6) ❌
py10 環境: x86_64 (Python 3.10.11) ❌
```

**結論：需要完全重新安裝 ARM64 版本**

---

## ✅ 解決方案：重新安裝 ARM64 Anaconda

我已經建立了兩個自動化腳本幫你完成：

### 📝 步驟總覽

1. **完全移除舊的 Anaconda**（自動）
2. **下載 ARM64 版本**（手動）
3. **安裝 ARM64 Anaconda**（自動）
4. **重建 py10 環境**（自動）

---

## 🚀 詳細步驟

### 步驟 1：執行重新安裝腳本

```bash
cd /Users/simon/Library/CloudStorage/Dropbox/paper/Working\ paper/Hospitals/LDA_hospital

./REINSTALL_ANACONDA_ARM64.sh
```

這個腳本會：
- ✅ 備份現有環境列表
- ✅ 完全移除舊的 Anaconda
- ✅ 清理 shell 設定檔
- ✅ 引導你下載正確的 ARM64 版本
- ✅ 執行安裝
- ✅ 驗證架構

### 步驟 2：下載 ARM64 版本（重要！）

腳本執行時會提示你下載，請按照以下步驟：

1. **開啟瀏覽器**前往：https://www.anaconda.com/download

2. **選擇作業系統**：macOS

3. **重要：選擇 Apple Silicon**
   ```
   ✅ Apple Silicon Installer (ARM64)  ← 選這個！
   ❌ Intel Installer (x86_64)        ← 不要選這個
   ```

4. **下載檔案**
   - 檔名應該包含 `arm64`
   - 例如：`Anaconda3-2024.10-MacOSX-arm64.sh`
   - 位置：`~/Downloads/`

5. **確認下載完成**後按 Enter 繼續

### 步驟 3：重新開啟終端機

安裝完成後：

```bash
# 關閉當前終端機視窗
# 開啟新的終端機視窗

# 驗證安裝
conda --version
python -c "import platform; print(f'架構: {platform.machine()}')"
```

應該顯示：
```
架構: arm64 ✅
```

### 步驟 4：重建 py10 環境

```bash
cd /Users/simon/Library/CloudStorage/Dropbox/paper/Working\ paper/Hospitals/LDA_hospital

./REBUILD_PY10_ARM64.sh
```

這個腳本會：
- ✅ 檢查 Anaconda 架構
- ✅ 移除舊的 py10 環境（如果存在）
- ✅ 建立新的 ARM64 py10 環境
- ✅ 驗證架構

### 步驟 5：安裝常用套件

```bash
conda activate py10
conda install numpy pandas matplotlib jupyter notebook scikit-learn -y
```

---

## 🎯 快速驗證

完成後執行這個命令驗證：

```bash
# 啟動 py10 環境
conda activate py10

# 檢查架構
python -c "
import platform
print(f'✅ Python 架構: {platform.machine()}')
print(f'✅ Python 版本: {platform.python_version()}')
print(f'✅ Conda 環境: py10')
"
```

應該顯示：
```
✅ Python 架構: arm64
✅ Python 版本: 3.10.x
✅ Conda 環境: py10
```

---

## ⚠️ 重要注意事項

### 下載時常見錯誤

❌ **錯誤的下載**：
- 檔名包含 `x86_64` 或 `x86`
- 檔名沒有 `arm64`
- 選擇了 "Intel Installer"

✅ **正確的下載**：
- 檔名包含 `arm64`
- 選擇 "Apple Silicon Installer"
- 大小約 600-700 MB

### 如何確認下載正確？

```bash
# 檢查下載的檔案
ls -lh ~/Downloads/Anaconda3-*

# 檔名應該包含 arm64
# 例如：Anaconda3-2024.10-MacOSX-arm64.sh
```

---

## 🔄 如果遇到問題

### 問題 1：找不到 arm64 安裝檔

```bash
# 列出所有 Anaconda 安裝檔
ls -la ~/Downloads/Anaconda3-*

# 確認檔名包含 arm64
```

### 問題 2：安裝後仍是 x86_64

可能原因：
- 下載了錯誤的版本
- 安裝到錯誤的位置

解決方法：
```bash
# 再次完全移除
rm -rf ~/anaconda3 ~/.conda

# 重新下載 ARM64 版本
# 重新執行安裝腳本
```

### 問題 3：conda 指令找不到

```bash
# 重新初始化 conda
~/anaconda3/bin/conda init zsh  # 如果用 zsh
~/anaconda3/bin/conda init bash # 如果用 bash

# 重新開啟終端機
```

---

## 📊 架構對比

| 項目 | 舊版 (x86_64) | 新版 (ARM64) |
|------|---------------|--------------|
| 基礎 Python | 3.6.6 | 最新 |
| 效能 | 慢（Rosetta） | 快 |
| 相容性 | 舊套件 | 新套件 |
| 耗電 | 高 | 低 |

---

## ✅ 安裝後的優勢

完成 ARM64 安裝後：

1. **更快的執行速度**
   - 原生執行，不需要 Rosetta 模擬
   - 科學計算速度提升 30-50%

2. **更好的電池續航**
   - 不需要 Rosetta 轉換
   - 更省電

3. **更好的相容性**
   - 現代套件都支援 ARM64
   - 避免架構衝突

4. **解決 Streamlit 問題**
   - 不再需要特殊的啟動腳本
   - conda 和 venv 可以並存

---

## 🎓 驗證清單

完成後檢查：

- [ ] Anaconda 基礎是 ARM64
- [ ] py10 環境是 ARM64
- [ ] conda 指令正常運作
- [ ] python 正常執行
- [ ] 可以安裝套件
- [ ] 不再有架構錯誤

---

## 💡 使用建議

### 對於 Streamlit 專案

安裝完成後，你可以選擇：

**選項 1：使用 conda py10**
```bash
conda activate py10
conda install streamlit pandas numpy gensim matplotlib -y
cd /path/to/LDA_hospital
streamlit run code/streamlit_app/taiwan_lda_explorer.py
```

**選項 2：繼續使用專案 venv**
```bash
cd /path/to/LDA_hospital
./run_streamlit_arm64.sh
```

兩者現在都是 ARM64 原生，都能正常運作！

---

## 📚 相關資源

- [Anaconda 官方下載](https://www.anaconda.com/download)
- [Apple Silicon 說明](https://support.apple.com/zh-tw/HT211861)
- [Conda 文件](https://docs.conda.io/)

---

## 🆘 需要協助？

如果遇到問題：

1. 檢查下載的檔案是否包含 `arm64`
2. 確認安裝位置是 `~/anaconda3`
3. 執行驗證命令檢查架構
4. 查看備份檔案：`~/py10_packages_backup_*.txt`

---

**建立日期**: 2025-11-11
**適用系統**: Apple Silicon Mac (M1/M2/M3/M4)
**Python 版本**: 3.10+
**Anaconda 版本**: 最新
