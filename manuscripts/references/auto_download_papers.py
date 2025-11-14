#!/usr/bin/env python3
"""
智能批次下載文獻 - 使用學校 VPN
特點：
1. 透過 Google Scholar 找 PDF
2. 支援多種下載源
3. 自動重命名檔案
4. 生成下載報告
"""

import json
import time
import requests
from pathlib import Path
from urllib.parse import quote
import subprocess

# 設定
BASE_DIR = Path(__file__).parent
PAPERS_DIR = BASE_DIR / "pdfs"
PAPERS_DIR.mkdir(exist_ok=True)

PRIORITY_LIST = BASE_DIR / "priority_papers.json"
DOWNLOAD_REPORT = PAPERS_DIR / "download_report.txt"

# User Agent
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def load_priority_papers():
    """載入優先下載清單"""
    with open(PRIORITY_LIST, 'r', encoding='utf-8') as f:
        return json.load(f)

def open_in_browser(url):
    """在瀏覽器中開啟 URL"""
    subprocess.run(['open', url], check=False)

def main():
    """主程式"""
    print("=" * 80)
    print("智能批次下載文獻")
    print("=" * 80)

    # 載入清單
    papers = load_priority_papers()
    print(f"\n📚 優先下載清單：{len(papers)} 篇核心文獻\n")

    downloaded = []
    failed = []

    # 檢查已下載
    print("檢查已下載的文獻...")
    existing_files = list(PAPERS_DIR.glob("*.pdf"))
    print(f"✅ 已有 {len(existing_files)} 篇 PDF\n")

    for paper in papers:
        priority = paper['priority']
        title = paper['title']
        filename = paper['filename']
        filepath = PAPERS_DIR / filename

        print(f"\n{'='*80}")
        print(f"[{priority}/10] {filename}")
        print(f"{'='*80}")
        print(f"Title: {title[:60]}...")

        # 檢查是否已存在
        if filepath.exists():
            print("  ✅ 已存在，跳過")
            downloaded.append(paper)
            continue

        # 構建 Google Scholar 搜尋 URL
        if 'doi' in paper:
            search_url = f"https://scholar.google.com/scholar?q={quote(paper['doi'])}"
        else:
            search_url = f"https://scholar.google.com/scholar?q={quote(paper['search_query'])}"

        print(f"\n  🔍 開啟 Google Scholar 搜尋...")
        print(f"  URL: {search_url}")

        # 在瀏覽器中開啟
        open_in_browser(search_url)

        print(f"\n  💡 請在瀏覽器中：")
        print(f"     1. 找到正確的文章")
        print(f"     2. 點擊 [PDF] 連結下載")
        print(f"     3. 下載完成後，按 Enter 繼續...")

        input()

        # 檢查 Downloads 資料夾中最新的 PDF
        downloads_dir = Path.home() / "Downloads"
        pdf_files = sorted(downloads_dir.glob("*.pdf"), key=lambda x: x.stat().st_mtime, reverse=True)

        if pdf_files:
            latest_pdf = pdf_files[0]
            print(f"\n  📄 找到最新下載：{latest_pdf.name}")

            # 確認是否為正確的文件
            confirm = input(f"  是否為 {filename}？(y/n): ").lower()

            if confirm == 'y':
                # 移動並重命名
                latest_pdf.rename(filepath)
                print(f"  ✅ 已儲存為：{filename}")
                downloaded.append(paper)
            else:
                print(f"  ⏭️  跳過此文件")
                failed.append(paper)
        else:
            print(f"  ❌ Downloads 資料夾中沒有找到 PDF")
            failed.append(paper)

        # 避免過快請求
        time.sleep(2)

    # 生成報告
    print(f"\n{'='*80}")
    print("下載完成報告")
    print(f"{'='*80}\n")

    print(f"✅ 成功下載：{len(downloaded)} 篇")
    print(f"❌ 失敗/跳過：{len(failed)} 篇")

    # 寫入報告
    with open(DOWNLOAD_REPORT, 'w', encoding='utf-8') as f:
        f.write("文獻下載報告\n")
        f.write("=" * 80 + "\n\n")

        f.write(f"下載時間：{time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"總數：{len(papers)} 篇\n")
        f.write(f"成功：{len(downloaded)} 篇\n")
        f.write(f"失敗：{len(failed)} 篇\n\n")

        if downloaded:
            f.write("成功下載清單：\n")
            f.write("-" * 80 + "\n")
            for paper in downloaded:
                f.write(f"[{paper['priority']}] {paper['filename']}\n")
                f.write(f"    {paper['title']}\n\n")

        if failed:
            f.write("\n需要手動下載：\n")
            f.write("-" * 80 + "\n")
            for paper in failed:
                f.write(f"[{paper['priority']}] {paper['filename']}\n")
                f.write(f"    {paper['title']}\n")
                if 'doi' in paper:
                    f.write(f"    DOI: {paper['doi']}\n")
                f.write(f"    搜尋：{paper.get('search_query', '')}\n\n")

    print(f"\n📝 報告已儲存：{DOWNLOAD_REPORT}")
    print(f"\n📁 PDF 位置：{PAPERS_DIR}")

    if failed:
        print(f"\n💡 提示：{len(failed)} 篇文獻需要手動下載")
        print(f"   請查看 _download_list.txt 獲取下載連結")

if __name__ == "__main__":
    main()
