# Git 快速參考指南

**不需要 GitHub Desktop，Claude Code 可以幫您執行所有 Git 操作！**

---

## 🚀 日常工作流程

### 每次開始工作前

```bash
# 1. 拉取最新版本（避免衝突）
git pull origin main
```

### 完成工作後

```bash
# 2. 查看變更
git status

# 3. 加入所有變更
git add .

# 4. 提交變更（記得寫清楚做了什麼）
git commit -m "新增 XXX 功能"

# 5. 推送到 GitHub
git push origin main
```

---

## 📋 常用命令

### 查看狀態

```bash
# 查看目前變更
git status

# 簡短版本
git status -s

# 查看差異
git diff

# 查看已暫存的差異
git diff --staged
```

### 加入檔案

```bash
# 加入所有變更
git add .

# 加入特定檔案
git add 檔案名稱

# 加入特定資料夾
git add 資料夾名稱/

# 加入所有 .py 檔案
git add *.py
```

### 提交變更

```bash
# 基本提交
git commit -m "提交訊息"

# 多行訊息
git commit -m "標題" -m "詳細說明"

# 修改上一個提交（還沒 push 的話）
git commit --amend -m "新訊息"
```

### 推送到 GitHub

```bash
# 推送到 main 分支
git push origin main

# 強制推送（小心使用！）
git push -f origin main

# 推送所有分支
git push --all origin
```

### 拉取更新

```bash
# 拉取並合併
git pull origin main

# 只拉取，不合併
git fetch origin
```

---

## 🌿 分支操作

### 查看分支

```bash
# 查看本地分支
git branch

# 查看所有分支（包含遠端）
git branch -a

# 查看目前分支
git branch --show-current
```

### 建立和切換分支

```bash
# 建立新分支
git branch 新分支名稱

# 切換到分支
git checkout 分支名稱

# 建立並切換（快捷方式）
git checkout -b 新分支名稱

# 新版 Git 語法
git switch 分支名稱
git switch -c 新分支名稱
```

### 合併分支

```bash
# 切換到 main
git checkout main

# 合併其他分支到 main
git merge 分支名稱

# 刪除已合併的分支
git branch -d 分支名稱
```

---

## ⏪ 復原操作

### 取消暫存

```bash
# 取消所有暫存
git restore --staged .

# 取消特定檔案
git restore --staged 檔案名稱
```

### 放棄變更

```bash
# ⚠️ 放棄所有未提交的變更（無法復原！）
git restore .

# 放棄特定檔案的變更
git restore 檔案名稱
```

### 回到之前的版本

```bash
# 查看提交歷史
git log --oneline

# 回到特定 commit（保留變更）
git reset --soft commit代碼

# 回到特定 commit（不保留變更）
git reset --hard commit代碼

# 回到上一個 commit
git reset --hard HEAD~1
```

---

## 🔍 查看歷史

```bash
# 查看提交歷史
git log

# 簡短版本（一行顯示）
git log --oneline

# 圖形化顯示
git log --graph --oneline --all

# 查看特定檔案的歷史
git log -- 檔案名稱

# 查看最近 5 筆
git log -5
```

---

## 🏷️ 標籤操作

```bash
# 建立標籤
git tag v1.0.0

# 建立帶訊息的標籤
git tag -a v1.0.0 -m "版本 1.0.0"

# 推送標籤到 GitHub
git push origin v1.0.0

# 推送所有標籤
git push --tags

# 查看所有標籤
git tag
```

---

## 🔧 設定

### 使用者資訊

```bash
# 設定全域名稱
git config --global user.name "您的名字"

# 設定全域 email
git config --global user.email "您的email"

# 查看目前設定
git config --global --list
```

### 認證設定

```bash
# macOS 使用鑰匙圈儲存密碼
git config --global credential.helper osxkeychain

# 查看遠端 repository
git remote -v

# 更改遠端 URL
git remote set-url origin 新的URL
```

---

## ⚠️ GitHub 認證方式

**重要**：GitHub 已不支援密碼登入！

### 使用 Personal Access Token

1. **建立 Token**：
   - 前往：https://github.com/settings/tokens/new
   - 勾選 `repo` 權限
   - 點擊 "Generate token"
   - **立即複製**（只會顯示一次！）

2. **使用 Token**：
   ```bash
   git push origin main

   Username: spolo0501
   Password: [貼上 Token]
   ```

3. **macOS 會自動儲存**到鑰匙圈，之後不需再輸入

---

## 📝 .gitignore 常用規則

```gitignore
# Python
__pycache__/
*.pyc
*.pyo
.Python
venv/
*.egg-info/

# 資料檔案
*.csv
*.xlsx
*.pkl
data/

# 結果檔案
results/
*.png
*.jpg

# 系統檔案
.DS_Store
Thumbs.db

# IDE
.vscode/
.idea/
*.swp

# Log
*.log

# 壓縮檔
*.zip
*.tar.gz
```

---

## 🎯 實用技巧

### 1. 一鍵推送（alias）

```bash
# 設定別名
git config --global alias.acp '!git add . && git commit -m "$1" && git push'

# 使用
git acp "提交訊息"
```

### 2. 美化 log 顯示

```bash
git config --global alias.lg "log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"

# 使用
git lg
```

### 3. 快速查看狀態

```bash
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.cm commit

# 使用
git st   # = git status
git co main   # = git checkout main
```

---

## 🆘 常見問題

### Q1: Push 被拒絕（rejected）

```bash
# 先 pull 合併遠端變更
git pull origin main

# 解決衝突後再 push
git push origin main
```

### Q2: 誤刪檔案想復原

```bash
# 如果還沒 commit
git restore 檔案名稱

# 如果已經 commit
git checkout HEAD~1 -- 檔案名稱
```

### Q3: 想放棄所有變更重來

```bash
# ⚠️ 會刪除所有未提交的變更！
git reset --hard HEAD
git clean -fd
```

### Q4: 忘記加入 .gitignore 就 commit 了

```bash
# 移除已追蹤的檔案（但保留本地檔案）
git rm --cached 檔案名稱

# 更新 .gitignore
echo "檔案名稱" >> .gitignore

# 重新 commit
git add .gitignore
git commit -m "更新 gitignore"
```

---

## 🎓 Claude Code 可以幫您做的事

您只要說：

- "幫我推送到 GitHub"
- "查看目前的 Git 狀態"
- "建立一個新分支叫 feature-xyz"
- "合併 develop 分支到 main"
- "回到上一個 commit"
- "顯示最近 10 筆 commit"

**我會直接幫您執行所有 Git 命令！完全不需要 GitHub Desktop！**

---

## 📚 延伸學習

- Git 官方文件：https://git-scm.com/doc
- GitHub 指南：https://guides.github.com/
- 互動式 Git 學習：https://learngitbranching.js.org/

---

**最後更新**：2025-11-13
**適用專案**：LDA Hospital Analysis
