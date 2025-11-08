#!/usr/bin/env python3
"""
Chapter 2.5 WOS Literature Search
Text Mining and Topic Modeling - 4 組搜尋
"""

import sys
import os
import time

# 加入 LiteratureReview 目錄到路徑
sys.path.insert(0, '/Users/simon/Downloads/Claude_code/LiteratureReview')

from wos_scraper_api import WOSScraperAPI

def main():
    print("\n" + "="*80)
    print("Chapter 2.5: Text Mining and Topic Modeling")
    print("WOS 文獻搜尋 - 4 組搜尋，目標 170 篇")
    print("="*80 + "\n")

    # 輸出目錄
    output_dir = "/Users/simon/Library/CloudStorage/Dropbox/paper/Working paper/Hospitals/LDA_hospital/Literature_Review/Chapter_2.5_Text_Mining"

    # 定義 4 組搜尋
    searches = [
        {
            "id": "2.5-1",
            "query": "topic modeling AND (healthcare OR patient OR medical)",
            "max_results": 50,
            "description": "Topic_modeling_應用",
            "year_filter": "(2018-2024)"
        },
        {
            "id": "2.5-2",
            "query": "LDA OR \"latent dirichlet allocation\" AND healthcare",
            "max_results": 40,
            "description": "LDA_在醫療",
            "year_filter": "(2015-2024)"
        },
        {
            "id": "2.5-3",
            "query": "text mining AND (patient feedback OR patient reviews)",
            "max_results": 40,
            "description": "文本挖掘方法",
            "year_filter": "(2018-2024)"
        },
        {
            "id": "2.5-4",
            "query": "natural language processing AND healthcare quality",
            "max_results": 40,
            "description": "NLP_應用",
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
        print("✅ Session 獲取成功！開始執行 4 組搜尋...")
        print("="*80 + "\n")

        all_results = []
        total_papers = 0

        # 執行每組搜尋
        for i, search in enumerate(searches, 1):
            print(f"\n{'='*80}")
            print(f"搜尋 {i}/4: {search['description']}")
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
                filename = f"{output_dir}/{search['id']}_{search['description']}"
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
