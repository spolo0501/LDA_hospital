#!/bin/bash

# Zotero 快速啟動腳本
# 用途：安裝完 Zotero 後，自動開啟並準備匯入文獻

echo "======================================"
echo "Zotero 快速啟動腳本"
echo "======================================"
echo ""

# 檢查 Zotero 是否已安裝
if [ -d "/Applications/Zotero.app" ]; then
    echo "✅ Zotero 已安裝"
else
    echo "❌ Zotero 未安裝，請先執行："
    echo "   brew install --cask zotero"
    exit 1
fi

# 開啟 Zotero
echo "🚀 正在開啟 Zotero..."
open -a Zotero

sleep 3

# 顯示下一步指示
echo ""
echo "======================================"
echo "📋 接下來的步驟："
echo "======================================"
echo ""
echo "1. 在 Zotero 中：File → Import"
echo ""
echo "2. 選擇檔案："
echo "   /Users/simon/Library/CloudStorage/Dropbox/paper/Working paper/Hospitals/LDA_hospital/manuscripts/references/all_references.ris"
echo ""
echo "3. 確認選項："
echo "   ✅ Place imported collections and items into new collection"
echo ""
echo "4. 點擊 'Import' 按鈕"
echo ""
echo "5. 等待匯入完成（應該看到 75 筆文獻）"
echo ""
echo "======================================"
echo "💡 提示："
echo "======================================"
echo ""
echo "- 匯入完成後，記得連接學校 VPN"
echo "- 然後選擇全部文獻（Cmd+A）"
echo "- 右鍵 → Find Available PDFs"
echo "- 等待自動下載（約 20-30 分鐘）"
echo ""
echo "======================================"
echo ""

# 詢問是否開啟 RIS 檔案所在資料夾
read -p "是否開啟 RIS 檔案所在的資料夾？(y/n) " -n 1 -r
echo ""
if [[ $REPLY =~ ^[Yy]$ ]]; then
    open "/Users/simon/Library/CloudStorage/Dropbox/paper/Working paper/Hospitals/LDA_hospital/manuscripts/references/"
    echo "✅ 已開啟資料夾"
fi

echo ""
echo "✅ 完成！祝您使用順利！"
echo ""
