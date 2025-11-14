# Python 虛擬環境使用指南

## 🎯 為什麼需要虛擬環境？

虛擬環境可以：
- **隔離套件版本**：避免不同專案之間的套件衝突
- **解決依賴問題**：確保所有套件版本一致
- **避免系統污染**：不會影響系統的 Python 環境
- **提高穩定性**：每個專案有獨立的乾淨環境

在這個專案中，虛擬環境已經設定好並包含了所有必要的套件！

---

## 🚀 快速開始（最簡單）

**直接使用啟動腳本，它會自動處理虛擬環境：**

```bash
./code/streamlit_app/run_app.sh
```

腳本會自動：
1. 檢查虛擬環境是否存在
2. 如果不存在，自動建立並安裝套件
3. 啟動應用程式

**就這麼簡單！** 🎉

---

## 📚 手動操作（進階使用者）

如果你想手動管理虛擬環境：

### 1. 啟動虛擬環境

```bash
# 在專案根目錄執行
source venv/bin/activate
```

啟動後，你會看到命令提示字元前面多了 `(venv)`：
```
(venv) username@computer:~/LDA_hospital$
```

### 2. 使用虛擬環境

啟動後，所有 Python 指令都會使用虛擬環境：

```bash
# 檢查版本
python --version
which python

# 安裝套件
pip install 套件名稱

# 查看已安裝套件
pip list

# 執行 Python 程式
python your_script.py

# 執行 Streamlit
python -m streamlit run code/streamlit_app/taiwan_lda_explorer.py
```

### 3. 離開虛擬環境

完成工作後：

```bash
deactivate
```

---

## 🔧 重建虛擬環境

如果遇到問題，可以刪除並重建：

```bash
# 1. 刪除舊的虛擬環境
rm -rf venv

# 2. 建立新的虛擬環境
python3 -m venv venv

# 3. 啟動虛擬環境
source venv/bin/activate

# 4. 升級 pip
pip install --upgrade pip setuptools wheel

# 5. 安裝所有套件
pip install -r requirements.txt

# 6. 驗證安裝
python -c "import streamlit, pandas, numpy, gensim; print('✅ 安裝成功')"
```

---

## 📦 已安裝的套件

虛擬環境中包含以下主要套件：

| 套件 | 版本 | 用途 |
|------|------|------|
| streamlit | 1.51.0 | 互動式網頁應用程式 |
| pandas | 2.3.3 | 資料處理與分析 |
| numpy | 2.2.6 | 數值計算 |
| gensim | 4.4.0 | LDA 主題模型 |
| matplotlib | 最新 | 視覺化 |
| seaborn | 最新 | 統計視覺化 |
| jieba | 最新 | 中文分詞 |
| wordcloud | 最新 | 詞雲生成 |
| openpyxl | 最新 | Excel 檔案處理 |

---

## ❓ 常見問題

### Q1: 啟動腳本說找不到虛擬環境？
**A**: 第一次執行會自動建立，請等待它完成安裝。

### Q2: 虛擬環境啟動後，找不到某個套件？
**A**:
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### Q3: 如何確認我在虛擬環境中？
**A**:
- 看命令提示字元前面有 `(venv)`
- 或執行 `which python` 應該顯示 `.../venv/bin/python`

### Q4: 為什麼不能用系統的 Python？
**A**: 系統 Python 可能有套件版本衝突。虛擬環境提供乾淨、穩定的執行環境。

### Q5: venv 資料夾很大，會不會佔空間？
**A**:
- venv 大約 100-200 MB
- 已加入 .gitignore，不會進入版本控制
- 需要時可以刪除重建

### Q6: 在 VS Code 中如何使用虛擬環境？
**A**:
1. 按 `Cmd+Shift+P` (Mac) 或 `Ctrl+Shift+P` (Windows)
2. 輸入 "Python: Select Interpreter"
3. 選擇 `./venv/bin/python`

---

## 💡 最佳實踐

1. **總是使用啟動腳本**：讓它自動處理虛擬環境
2. **開發時保持啟動**：避免重複啟動/關閉
3. **更新套件後重建**：如果 requirements.txt 有變動
4. **不要手動修改 venv**：有問題就刪除重建

---

## 🔍 驗證虛擬環境

檢查虛擬環境是否正常：

```bash
# 啟動虛擬環境
source venv/bin/activate

# 檢查 Python 位置
which python
# 應該輸出：.../LDA_hospital/venv/bin/python

# 檢查套件
python -c "import streamlit, pandas, numpy, gensim, matplotlib, seaborn; print('✅ 所有核心套件正常')"

# 查看套件版本
pip list | grep -E "(streamlit|pandas|numpy|gensim)"
```

---

## 📝 開發工作流程範例

```bash
# 1. 開啟終端機，進入專案目錄
cd /path/to/LDA_hospital

# 2. 啟動虛擬環境
source venv/bin/activate

# 3. 開始工作（例如：啟動 Streamlit）
python -m streamlit run code/streamlit_app/taiwan_lda_explorer.py

# 4. 完成後離開虛擬環境
deactivate
```

**或更簡單：**
```bash
./code/streamlit_app/run_app.sh
```

---

**建立日期**: 2025-11-11
**Python 版本**: 3.10.11
**虛擬環境位置**: `./venv/`
