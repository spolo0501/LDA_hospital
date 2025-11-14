#!/usr/bin/env python3
"""
自動下載文獻 PDF
需求: 已透過 VPN 連線到學校網路
"""

import re
import os
import time
import requests
from pathlib import Path
from urllib.parse import quote

# 設定
PAPERS_DIR = Path(__file__).parent / "pdfs"
PAPERS_DIR.mkdir(exist_ok=True)

# 讀取 RIS 檔案
def parse_ris_file(ris_path):
    """解析 RIS 檔案"""
    with open(ris_path, 'r', encoding='utf-8') as f:
        content = f.read()

    records = content.split('ER  -\n')
    papers = []

    for record in records:
        if not record.strip():
            continue

        paper = {}

        # 提取資訊
        type_match = re.search(r'^TY  - (.+)$', record, re.MULTILINE)
        title_match = re.search(r'^TI  - (.+)$', record, re.MULTILINE)
        author_matches = re.findall(r'^AU  - (.+)$', record, re.MULTILINE)
        year_match = re.search(r'^PY  - (\d+)$', record, re.MULTILINE)
        journal_match = re.search(r'^JO  - (.+)$', record, re.MULTILINE)
        doi_match = re.search(r'^DO  - (.+)$', record, re.MULTILINE)
        url_match = re.search(r'^UR  - (.+)$', record, re.MULTILINE)
        volume_match = re.search(r'^VL  - (.+)$', record, re.MULTILINE)
        issue_match = re.search(r'^IS  - (.+)$', record, re.MULTILINE)

        if title_match:
            paper['type'] = type_match.group(1) if type_match else 'UNKNOWN'
            paper['title'] = title_match.group(1)
            paper['authors'] = author_matches if author_matches else []
            paper['year'] = year_match.group(1) if year_match else 'Unknown'
            paper['journal'] = journal_match.group(1) if journal_match else ''
            paper['doi'] = doi_match.group(1) if doi_match else ''
            paper['url'] = url_match.group(1) if url_match else ''
            paper['volume'] = volume_match.group(1) if volume_match else ''
            paper['issue'] = issue_match.group(1) if issue_match else ''

            # 生成檔案名稱
            first_author = author_matches[0].split(',')[0] if author_matches else 'Unknown'
            year = paper['year']
            safe_title = re.sub(r'[^\w\s-]', '', paper['title'][:50])
            safe_title = re.sub(r'[-\s]+', '_', safe_title)
            paper['filename'] = f"{first_author}_{year}_{safe_title}.pdf"

            papers.append(paper)

    return papers


def construct_doi_url(doi):
    """構建 DOI URL"""
    if doi:
        return f"https://doi.org/{doi}"
    return None


def construct_scihub_url(doi=None, title=None):
    """構建 Sci-Hub URL (備用方案)"""
    if doi:
        return f"https://sci-hub.se/{doi}"
    elif title:
        return f"https://sci-hub.se/{quote(title)}"
    return None


def construct_google_scholar_url(title, author=None, year=None):
    """構建 Google Scholar 搜尋 URL"""
    query = title
    if author:
        query += f" {author}"
    if year:
        query += f" {year}"
    return f"https://scholar.google.com/scholar?q={quote(query)}"


def download_via_doi(paper, session):
    """透過 DOI 下載"""
    if not paper.get('doi'):
        return False

    doi_url = construct_doi_url(paper['doi'])
    print(f"  嘗試透過 DOI: {doi_url}")

    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        }
        response = session.get(doi_url, headers=headers, timeout=10, allow_redirects=True)

        # 檢查是否為 PDF
        if 'application/pdf' in response.headers.get('Content-Type', ''):
            filepath = PAPERS_DIR / paper['filename']
            with open(filepath, 'wb') as f:
                f.write(response.content)
            print(f"  ✅ 成功下載!")
            return True
        else:
            print(f"  ℹ️  重定向到: {response.url}")
            # 保存重定向 URL 供後續使用
            paper['publisher_url'] = response.url
            return False
    except Exception as e:
        print(f"  ❌ 失敗: {e}")
        return False


def generate_download_list(papers):
    """生成下載清單 (供手動下載)"""
    list_file = PAPERS_DIR / "_download_list.txt"

    with open(list_file, 'w', encoding='utf-8') as f:
        f.write("# 文獻下載清單\n")
        f.write("# 建議透過學校圖書館代理或 Google Scholar 下載\n\n")

        for i, paper in enumerate(papers, 1):
            f.write(f"\n{'='*80}\n")
            f.write(f"[{i}/{len(papers)}] {paper['filename']}\n")
            f.write(f"{'='*80}\n\n")

            # 基本資訊
            f.write(f"Title: {paper['title']}\n")
            if paper['authors']:
                f.write(f"Authors: {', '.join(paper['authors'][:3])}")
                if len(paper['authors']) > 3:
                    f.write(f" et al.")
                f.write("\n")
            f.write(f"Year: {paper['year']}\n")
            if paper['journal']:
                f.write(f"Journal: {paper['journal']}\n")
            if paper['volume']:
                f.write(f"Volume: {paper['volume']}\n")
            if paper['issue']:
                f.write(f"Issue: {paper['issue']}\n")

            f.write("\n下載連結:\n")

            # DOI 連結
            if paper.get('doi'):
                f.write(f"  DOI: {construct_doi_url(paper['doi'])}\n")

            # Google Scholar 連結
            first_author = paper['authors'][0].split(',')[0] if paper['authors'] else None
            scholar_url = construct_google_scholar_url(paper['title'], first_author, paper['year'])
            f.write(f"  Google Scholar: {scholar_url}\n")

            # Sci-Hub 連結 (備用)
            if paper.get('doi'):
                scihub_url = construct_scihub_url(doi=paper['doi'])
            else:
                scihub_url = construct_scihub_url(title=paper['title'])
            f.write(f"  Sci-Hub (備用): {scihub_url}\n")

            # 出版商連結
            if paper.get('publisher_url'):
                f.write(f"  Publisher: {paper['publisher_url']}\n")

            f.write("\n")

    print(f"\n📝 下載清單已生成: {list_file}")
    return list_file


def main():
    """主程式"""
    print("=" * 80)
    print("文獻自動下載程式")
    print("=" * 80)

    # 解析 RIS 檔案
    ris_file = Path(__file__).parent / "all_references.ris"
    print(f"\n📖 讀取文獻清單: {ris_file}")
    papers = parse_ris_file(ris_file)

    # 只處理期刊論文
    journal_papers = [p for p in papers if p['type'] == 'JOUR']
    print(f"✅ 找到 {len(journal_papers)} 篇期刊論文")

    # 建立 session
    session = requests.Session()

    # 統計
    success_count = 0
    failed_papers = []

    print(f"\n開始下載到: {PAPERS_DIR}\n")

    # 嘗試下載
    for i, paper in enumerate(journal_papers, 1):
        print(f"[{i}/{len(journal_papers)}] {paper['filename']}")
        print(f"  Title: {paper['title'][:60]}...")

        # 檢查是否已存在
        filepath = PAPERS_DIR / paper['filename']
        if filepath.exists():
            print(f"  ⏭️  已存在，跳過")
            success_count += 1
            continue

        # 嘗試透過 DOI 下載
        if download_via_doi(paper, session):
            success_count += 1
        else:
            failed_papers.append(paper)

        # 避免請求過快
        time.sleep(1)

    # 生成下載清單
    print("\n" + "=" * 80)
    print("下載完成!")
    print("=" * 80)
    print(f"✅ 成功下載: {success_count} 篇")
    print(f"⏸️  需要手動下載: {len(failed_papers)} 篇")

    if failed_papers:
        print(f"\n正在生成下載清單...")
        list_file = generate_download_list(failed_papers)
        print(f"\n💡 提示: 請開啟 {list_file.name} 查看下載連結")
        print(f"   建議透過學校圖書館網站或 Google Scholar 下載")

    print(f"\n📁 PDF 儲存位置: {PAPERS_DIR}")


if __name__ == "__main__":
    main()
