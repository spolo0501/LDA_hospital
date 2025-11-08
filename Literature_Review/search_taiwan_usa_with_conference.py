#!/usr/bin/env python3
"""
Taiwan-USA Healthcare Search (包含會議論文)
使用 /wos-search 命令執行
"""

import sys
import os

# 加入 LiteratureReview 目錄到路徑
sys.path.insert(0, '/Users/simon/Downloads/Claude_code/LiteratureReview')

from wos_scraper_api import WOSScraperAPI

def main():
    print("\n" + "="*80)
    print("Taiwan-USA Healthcare Literature Search (包含會議論文)")
    print("="*80 + "\n")

    # 輸出目錄
    output_dir = "/Users/simon/Library/CloudStorage/Dropbox/paper/Working paper/Hospitals/LDA_hospital/Literature_Review/Chapter_2.3_Healthcare_Systems"

    # 搜尋設定
    search = {
        "query": 'Taiwan AND ("United States" OR USA OR America) AND (healthcare OR "health care" OR hospital)',
        "max_results": 50,
        "year_start": 2015,
        "year_end": 2024,
        "exclude_conference": False,  # 包含會議論文
        "output_prefix": "2.3-TW-USA-WITH-CONF"
    }

    # 創建抓取器
    scraper = WOSScraperAPI(headless=False)

    try:
        # 獲取 Session
        print("🔐 正在獲取 WOS Session ID...")
        print("⏳ 請在接下來的 30 秒內確認已登入 Web of Science\n")

        if not scraper.get_session(wait_time=30):
            print("❌ 無法獲取 Session ID")
            return

        print("\n" + "="*80)
        print("✅ Session 獲取成功！開始搜尋...")
        print("="*80 + "\n")

        print(f"查詢: {search['query']}")
        print(f"年份: {search['year_start']}-{search['year_end']}")
        print(f"最多: {search['max_results']} 篇")
        print(f"會議論文: 包含 ✅\n")

        # 執行搜尋
        papers = scraper.search_api(
            query=search['query'],
            max_results=search['max_results'],
            exclude_conference=search['exclude_conference']
        )

        # 年份過濾
        if papers:
            papers = [p for p in papers if p.get('year') != 'N/A' and
                     search['year_start'] <= int(p['year']) <= search['year_end']]
            print(f"年份過濾後: {len(papers)} 篇\n")

        if papers:
            print(f"✅ 成功抓取 {len(papers)} 篇文獻\n")

            # 保存結果
            filename = f"{output_dir}/{search['output_prefix']}_台美醫療含會議論文"
            scraper.save_results(papers, filename)

            # 統計
            from collections import Counter

            # 文獻類型統計
            doc_types = [p.get('document_type', 'Unknown') for p in papers]
            type_counts = Counter(doc_types)

            print("📊 文獻類型分布:")
            for doc_type, count in type_counts.most_common():
                print(f"  {doc_type}: {count} 篇")

            # 年份分布
            years = [p['year'] for p in papers if p['year'] != 'N/A']
            year_counts = Counter(years)

            print(f"\n📅 年份分布:")
            for year in sorted(year_counts.keys(), reverse=True)[:10]:
                print(f"  {year}: {year_counts[year]} 篇")

            # 引用數統計
            citations = [p['citations'] for p in papers]
            if citations:
                print(f"\n📈 引用數統計:")
                print(f"  - 總引用數: {sum(citations)}")
                print(f"  - 平均引用: {sum(citations) / len(citations):.1f}")
                print(f"  - 最高引用: {max(citations)}")

            # 台美直接比較
            taiwan_usa_count = 0
            taiwan_usa_papers = []
            for paper in papers:
                text = (paper.get('title', '') + ' ' + paper.get('abstract', '')).lower()
                if 'taiwan' in text and ('usa' in text or 'united states' in text or 'america' in text):
                    taiwan_usa_count += 1
                    taiwan_usa_papers.append(paper)

            print(f"\n⭐ 同時提到台灣和美國: {taiwan_usa_count} 篇")

            # Top 10 高引用
            high_cited = sorted(papers, key=lambda x: x['citations'], reverse=True)[:10]
            print(f"\n⭐ 高引用文獻 (Top 10):")
            for i, paper in enumerate(high_cited, 1):
                print(f"  {i}. [{paper['citations']} 引用] {paper['title'][:70]}...")
                print(f"     {paper['journal']}, {paper['year']} ({paper.get('document_type', 'N/A')})")

            print("\n" + "="*80)
            print("💾 結果已保存:")
            print(f"   {filename}.csv")
            print(f"   {filename}.json")
            print("="*80)

        else:
            print("⚠️ 未找到文獻")

    except Exception as e:
        print(f"\n❌ 發生錯誤: {e}")
        import traceback
        traceback.print_exc()

    finally:
        scraper.close()
        print("\n🔒 瀏覽器已關閉")


if __name__ == "__main__":
    main()
