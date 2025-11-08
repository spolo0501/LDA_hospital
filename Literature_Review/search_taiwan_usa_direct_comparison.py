#!/usr/bin/env python3
"""
Taiwan-USA Healthcare Direct Comparison Literature Search
專門搜尋台灣與美國醫療直接比較的文獻
"""

import sys
import os
import time

# 加入 LiteratureReview 目錄到路徑
sys.path.insert(0, '/Users/simon/Downloads/Claude_code/LiteratureReview')

from wos_scraper_api import WOSScraperAPI

def main():
    print("\n" + "="*80)
    print("Taiwan-USA Healthcare Direct Comparison Literature Search")
    print("台美醫療比較專門文獻搜尋 - 4 組搜尋，目標 50-80 篇")
    print("="*80 + "\n")

    # 輸出目錄
    output_dir = "/Users/simon/Library/CloudStorage/Dropbox/paper/Working paper/Hospitals/LDA_hospital/Literature_Review/Chapter_2.3_Healthcare_Systems"

    # 定義 4 組搜尋
    searches = [
        {
            "id": "2.3-TW-USA-1",
            "query": "Taiwan AND (USA OR 'United States' OR America) AND healthcare AND (quality OR service)",
            "max_results": 30,
            "description": "台美醫療品質直接比較",
            "year_filter": "(2015-2024)"
        },
        {
            "id": "2.3-TW-USA-2",
            "query": "Taiwan AND 'United States' AND ('health system' OR 'healthcare system') AND comparison",
            "max_results": 20,
            "description": "台美醫療體系比較",
            "year_filter": "(2015-2024)"
        },
        {
            "id": "2.3-TW-USA-3",
            "query": "(Asian OR Asia) AND (American OR 'United States') AND healthcare AND comparison AND quality",
            "max_results": 20,
            "description": "亞美醫療品質比較",
            "year_filter": "(2015-2024)"
        },
        {
            "id": "2.3-TW-USA-4",
            "query": "('national health insurance' OR 'universal healthcare') AND ('market based' OR 'private insurance') AND comparison",
            "max_results": 20,
            "description": "全民健保vs市場制度比較",
            "year_filter": "(2015-2024)"
        }
    ]

    # 創建抓取器
    scraper = WOSScraperAPI(headless=False)

    try:
        # 獲取 Session（只需一次）
        print("🔐 正在獲取 WOS Session ID...")
        print("⏳ 請在接下來的 30 秒內確認已登入 Web of Science")
        print("   (如果瀏覽器自動打開 WoS 頁面，請確認已登入)\n")

        if not scraper.get_session(wait_time=30):
            print("❌ 無法獲取 Session ID")
            print("   請確認：")
            print("   1. 您的機構有 Web of Science 訂閱")
            print("   2. 已透過機構網路或 VPN 連線")
            print("   3. 瀏覽器中已成功登入 WoS")
            return

        print("\n" + "="*80)
        print("✅ Session 獲取成功！開始執行 4 組台美比較搜尋...")
        print("="*80 + "\n")

        all_results = []
        total_papers = 0

        # 執行每組搜尋
        for i, search in enumerate(searches, 1):
            print(f"\n{'='*80}")
            print(f"搜尋 {i}/4: {search['description']}")
            print(f"查詢: {search['query']}")
            print(f"年份: {search['year_filter']}")
            print(f"目標: {search['max_results']} 篇")
            print('='*80)

            # 執行搜尋
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

                # 顯示前 5 篇
                print(f"\n前 5 篇文獻:")
                for j, paper in enumerate(papers[:5], 1):
                    print(f"  {j}. [{paper['citations']} 引用] {paper['title'][:80]}...")

                # 檢查是否同時包含 Taiwan 和 USA
                taiwan_usa_count = 0
                for paper in papers:
                    text = (paper.get('title', '') + ' ' + paper.get('abstract', '')).lower()
                    if 'taiwan' in text and ('usa' in text or 'united states' in text or 'america' in text):
                        taiwan_usa_count += 1

                print(f"\n   ⭐ 其中同時提到台灣和美國: {taiwan_usa_count} 篇")

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

        # 檢查同時包含台灣和美國的文獻
        taiwan_usa_papers = []
        for paper in all_results:
            text = (paper.get('title', '') + ' ' + paper.get('abstract', '')).lower()
            if 'taiwan' in text and ('usa' in text or 'united states' in text or 'america' in text):
                taiwan_usa_papers.append(paper)

        print(f"\n⭐ 同時提到台灣和美國的文獻: {len(taiwan_usa_papers)} 篇")

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

        # 台美直接比較的高引用文獻
        if taiwan_usa_papers:
            taiwan_usa_high_cited = sorted(taiwan_usa_papers, key=lambda x: x['citations'], reverse=True)[:5]
            print(f"\n🎯 台美直接比較的高引用文獻 (Top 5):")
            for i, paper in enumerate(taiwan_usa_high_cited, 1):
                print(f"  {i}. [{paper['citations']} 引用] {paper['title'][:70]}...")
                print(f"     {paper['journal']}, {paper['year']}")

        print("\n" + "="*80)
        print("💾 所有結果已保存到:")
        print(f"   {output_dir}")
        print("="*80)

        # 建議下一步
        print("\n📋 下一步建議:")
        print(f"  1. 優先閱讀 {len(taiwan_usa_papers)} 篇台美直接比較文獻")
        print(f"  2. 閱讀高引用文獻（Top 10）")
        print(f"  3. 整合到 Chapter 2.3（醫療體系比較）")
        print(f"  4. 如果文獻不足，考慮調整關鍵字再搜尋")

    except Exception as e:
        print(f"\n❌ 發生錯誤: {e}")
        import traceback
        traceback.print_exc()

    finally:
        scraper.close()
        print("\n🔒 瀏覽器已關閉")


if __name__ == "__main__":
    main()
