#!/usr/bin/env python3
"""
Chapter 2.4 WOS Literature Search
Online Reviews as a Data Source for Service Quality Research - 5 組搜尋
"""

import sys
import os
import time

# 加入 LiteratureReview 目錄到路徑
sys.path.insert(0, '/Users/simon/Downloads/Claude_code/LiteratureReview')

from wos_scraper_api import WOSScraperAPI

def main():
    print("\n" + "="*80)
    print("Chapter 2.4: Online Reviews as a Data Source for Service Quality Research")
    print("WOS 文獻搜尋 - 5 組搜尋，目標 170 篇")
    print("="*80 + "\n")

    # 輸出目錄
    output_dir = "/Users/simon/Library/CloudStorage/Dropbox/paper/Working paper/Hospitals/LDA_hospital/Literature_Review/Chapter_2.4_Online_Reviews"

    # 定義 5 組搜尋
    searches = [
        {
            "id": "2.4-1",
            "query": "online reviews AND (healthcare OR hospital)",
            "max_results": 50,
            "description": "線上評論研究",
            "year_filter": "(2018-2024)"
        },
        {
            "id": "2.4-2",
            "query": "(Google Maps AND healthcare) OR (Yelp AND healthcare)",
            "max_results": 30,
            "description": "平台特定研究",
            "year_filter": "(2018-2024)"
        },
        {
            "id": "2.4-3",
            "query": "patient feedback AND social media AND healthcare",
            "max_results": 30,
            "description": "社交媒體回饋",
            "year_filter": "(2018-2024)"
        },
        {
            "id": "2.4-4",
            "query": "online ratings AND (physician OR hospital)",
            "max_results": 30,
            "description": "線上評分研究",
            "year_filter": "(2018-2024)"
        },
        {
            "id": "2.4-5",
            "query": "user-generated content AND healthcare quality",
            "max_results": 30,
            "description": "用戶生成內容",
            "year_filter": "(2018-2024)"
        }
    ]

    # 創建抓取器
    scraper = WOSScraperAPI(headless=False)

    try:
        # 獲取 Session（只需一次）
        print("🔐 正在獲取 WOS Session ID...")
        print("⏳ 請在接下來的 30 秒內確認已登入 Web of Science\n")

        if not scraper.get_session(wait_time=30):
            print("❌ 無法獲取 Session ID")
            return

        print("\n" + "="*80)
        print("✅ Session 獲取成功！開始執行 5 組搜尋...")
        print("="*80 + "\n")

        all_results = []
        total_papers = 0

        # 執行每組搜尋
        for i, search in enumerate(searches, 1):
            print(f"\n{'='*80}")
            print(f"搜尋 {i}/5: {search['description']}")
            print(f"查詢: {search['query']} AND PY={search['year_filter']}")
            print(f"目標: {search['max_results']} 篇")
            print('='*80)

            # 執行搜尋（先不加年份過濾）
            papers = scraper.search_api(
                query=search['query'],
                max_results=search['max_results'],
                exclude_conference=True
            )

            # 手動過濾年份
            if papers and search.get('year_filter'):
                year_range = search['year_filter'].strip('()')
                start_year, end_year = map(int, year_range.split('-'))
                papers = [p for p in papers if p.get('year') != 'N/A' and start_year <= int(p['year']) <= end_year]
                print(f"   (年份過濾後剩餘 {len(papers)} 篇)")

            if papers:
                print(f"✅ 成功抓取 {len(papers)} 篇文獻")

                # 保存結果
                filename = f"{output_dir}/{search['id']}_{search['description'].replace(' ', '_')}"
                scraper.save_results(papers, filename)

                all_results.extend(papers)
                total_papers += len(papers)

                # 顯示前 3 篇
                print(f"\n前 3 篇文獻:")
                for j, paper in enumerate(papers[:3], 1):
                    print(f"  {j}. [{paper['citations']} 引用] {paper['title'][:60]}...")

            else:
                print(f"⚠️  未找到文獻")

            # 避免請求過快
            if i < len(searches):
                print(f"\n⏳ 等待 3 秒後繼續下一組搜尋...")
                time.sleep(3)

        # 最終統計
        print("\n" + "="*80)
        print("🎉 所有搜尋完成！")
        print("="*80)
        print(f"\n📊 總計:")
        print(f"  - 執行搜尋組數: {len(searches)} 組")
        print(f"  - 抓取文獻總數: {total_papers} 篇")

        # 年份分布
        from collections import Counter
        years = [p['year'] for p in all_results if p['year'] != 'N/A']
        year_counts = Counter(years)

        print(f"\n📅 年份分布:")
        for year in sorted(year_counts.keys(), reverse=True)[:10]:
            print(f"  {year}: {year_counts[year]} 篇")

        # 引用數統計
        citations = [p['citations'] for p in all_results]
        if citations:
            print(f"\n📈 引用數統計:")
            print(f"  - 總引用數: {sum(citations)}")
            print(f"  - 平均引用: {sum(citations) / len(citations):.1f}")
            print(f"  - 最高引用: {max(citations)}")
            print(f"  - 中位數: {sorted(citations)[len(citations)//2]}")

        # 高引用文獻（Top 10）
        high_cited = sorted(all_results, key=lambda x: x['citations'], reverse=True)[:10]
        print(f"\n⭐ 高引用文獻 (Top 10):")
        for i, paper in enumerate(high_cited, 1):
            print(f"  {i}. [{paper['citations']} 引用] {paper['title'][:70]}...")
            print(f"     {paper['journal']}, {paper['year']}")

        print("\n" + "="*80)
        print("💾 所有結果已保存到:")
        print(f"   {output_dir}")
        print("="*80)

    except Exception as e:
        print(f"\n❌ 發生錯誤: {e}")
        import traceback
        traceback.print_exc()

    finally:
        scraper.close()
        print("\n🔒 瀏覽器已關閉")


if __name__ == "__main__":
    main()
