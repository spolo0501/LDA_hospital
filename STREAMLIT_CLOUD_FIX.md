# 🔧 Streamlit Cloud 路徑問題修正

**問題**: Streamlit Cloud 找不到 LDA 模型檔案

**原因**: 大型模型檔案（`lda_k7_lda_model.pkl`）被 `.gitignore` 排除，只有 `results_demo/` 目錄中的小型 demo 模型被上傳到 GitHub

**解決方案**: 自動偵測 Streamlit Cloud 環境並使用 demo 資料

---

## ✅ 已完成的修正

### 修改檔案: `code/streamlit_app/taiwan_lda_explorer.py`

**第 44-49 行**：新增自動偵測邏輯

```python
# 自動偵測 Streamlit Cloud 環境
IS_STREAMLIT_CLOUD = os.getenv('STREAMLIT_SHARING_MODE') is not None or \
                      os.path.exists('/mount/src')

USE_DEMO = os.getenv('USE_DEMO_DATA', 'false').lower() == 'true' or \
           (st.secrets.get('USE_DEMO_DATA', False) if hasattr(st, 'secrets') and st.secrets else False) or \
           IS_STREAMLIT_CLOUD
```

**偵測機制**：
1. 檢查環境變數 `STREAMLIT_SHARING_MODE`（Streamlit Cloud 特有）
2. 檢查 `/mount/src` 路徑是否存在（Streamlit Cloud 的掛載點）
3. 如果在 Cloud 環境，自動使用 `results_demo/` 資料

---

## 📤 下一步：推送到 GitHub

**已完成**：
```bash
git add code/streamlit_app/taiwan_lda_explorer.py
git commit -m "Fix Streamlit Cloud path issue - auto-detect cloud environment and use demo data"
```

**待完成**：使用 GitHub Desktop 推送

### 使用 GitHub Desktop 推送步驟：

1. 開啟 GitHub Desktop
2. 確認看到新的 commit: "Fix Streamlit Cloud path issue..."
3. 點擊 "Push origin" 按鈕
4. 等待推送完成

### Streamlit Cloud 自動重新部署

推送成功後，Streamlit Cloud 會自動：
1. 偵測到新的 commit
2. 重新部署應用程式
3. 這次會正確載入 `results_demo/taiwan_lda_k7/lda_k7_lda_model.pkl`

---

## 🧪 測試

### 本機測試（已通過 ✅）
- ✅ 本機運行正常（http://localhost:8504）
- ✅ 使用完整資料 `results/taiwan_lda_k7/`
- ✅ 不受此修改影響

### Streamlit Cloud 測試（推送後）
推送成功後，請檢查：
1. 應用程式能否正常啟動
2. 主題總覽頁面顯示正常
3. 不再出現「找不到 K=7 的 LDA 模型」錯誤

---

## 📊 Demo 資料說明

`results_demo/taiwan_lda_k7/lda_k7_lda_model.pkl` 包含：
- 完整的 LDA K=7 模型
- 26 家台灣醫院
- 5,007 則評論
- 與完整版本相同的模型參數

**為什麼可以放在 Git？**
- 檔案大小：569 KB（壓縮後更小）
- GitHub 單檔限制：100 MB
- ✅ 完全符合 GitHub 限制

---

## 🔍 故障排除

### 如果推送後 Streamlit Cloud 仍有問題：

#### 方法 1：在 Streamlit Cloud 設定環境變數
1. 進入 Streamlit Cloud 專案設定
2. 找到 "Secrets" 或 "Environment variables"
3. 新增：`USE_DEMO_DATA = true`

#### 方法 2：清除 Streamlit Cloud 快取
1. 在 Streamlit Cloud 介面中
2. 點擊 "Reboot app"
3. 強制重新載入所有資料

#### 方法 3：檢查 Git 檔案
確認 demo 模型有被推送：
```bash
git ls-files | grep "results_demo/taiwan_lda_k7/lda_k7_lda_model.pkl"
```

應該看到：
```
results_demo/taiwan_lda_k7/lda_k7_lda_model.pkl
```

---

## 📝 commit 訊息

```
Fix Streamlit Cloud path issue - auto-detect cloud environment and use demo data

- Add automatic detection of Streamlit Cloud environment
- Check for STREAMLIT_SHARING_MODE env var and /mount/src path
- Automatically use demo data (results_demo/) when on Cloud
- Fixes "找不到 K=7 的 LDA 模型" error on Streamlit Cloud
- Local development unaffected, continues to use full data
```

---

## ✅ 總結

**修正內容**：
- ✅ 新增 Streamlit Cloud 環境自動偵測
- ✅ Cloud 環境自動使用 demo 資料
- ✅ 本機開發不受影響
- ✅ 已建立 git commit

**待完成動作**：
1. 使用 GitHub Desktop 推送 commit
2. 等待 Streamlit Cloud 自動重新部署（約 2-3 分鐘）
3. 測試應用程式是否正常運作

**預期結果**：
- 🌐 Streamlit Cloud 應用程式正常運作
- 📊 顯示完整的台灣 K=7 LDA 分析
- ✅ 不再出現路徑錯誤

---

**建立時間**: 2025-11-12
**狀態**: 等待推送到 GitHub
