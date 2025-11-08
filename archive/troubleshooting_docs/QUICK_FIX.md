# ⚡ Numpy 導入問題快速修復卡

## 🚨 看到這個錯誤？
```
Error importing numpy: you should not try to import numpy from
its source directory
```

## ⚡ 快速修復（3 步驟）

### 1️⃣ 診斷問題
```bash
python3 diagnose_env.py
```

### 2️⃣ 一鍵修復
```bash
./fix_ide_env.sh
```

### 3️⃣ 驗證成功
```bash
python3 -c "import numpy, pandas; print('✅ 修復成功！')"
```

---

## 🔧 如果還是失敗，手動修復

```bash
# 清除環境變量（最重要！）
unset PYTHONPATH
unset PYTHONHOME

# 驗證
python3 -c "import numpy, pandas; print('✅ OK')"
```

---

## 💡 記住這個關鍵點

**問題不在套件，在環境變量！**

❌ 錯誤做法：
```bash
pip install --force-reinstall numpy  # 沒用！
```

✅ 正確做法：
```bash
unset PYTHONPATH  # 這才是關鍵！
```

---

## 📖 詳細指南

需要更多資訊？查看：
```bash
cat TROUBLESHOOTING_NUMPY_IMPORT.md
# 或
open TROUBLESHOOTING_NUMPY_IMPORT.md
```

---

## 🚀 修復後運行腳本

### 測試版（10條/醫院）
```bash
python3 batch_scrape_hospitals_20_test.py
```

### 完整版（2000條/醫院）
```bash
python3 batch_scrape_hospitals_20.py
```

### 使用安全包裝腳本
```bash
./run_batch_safe.sh
```
