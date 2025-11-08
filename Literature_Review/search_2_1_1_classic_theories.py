#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2.1-1 補充搜尋：經典服務品質理論文獻
目標：抓取 SERVQUAL、Donabedian 等高引用經典理論文獻
年份範圍：1980-2024（45年，涵蓋所有經典）
目標數量：100篇
"""

import sys
import os
from datetime import datetime

# 添加 WOS scraper 路徑
sys.path.insert(0, '/Users/simon/Downloads/Claude_code/LiteratureReview')
from wos_scraper_api import WOSScraperAPI

def main():
    # 初始化 scraper
    scraper = WOSScraperAPI(headless=False)

    # 輸出目錄
    output_dir = "Literature_Review/Chapter_2.1_Healthcare_Service_Quality"
    os.makedirs(output_dir, exist_ok=True)

    # 搜尋定義
    search = {
        "id": "2.1-1_classic_theories",
        "query": "SERVQUAL OR Donabedian OR \"service quality dimensions\" OR SERVPERF OR \"healthcare quality framework\" OR \"patient satisfaction theory\"",
        "max_results": 100,
        "description": "經典服務品質理論文獻（1980-2024）",
        "year_filter": "(1980-2024)"
    }

    print("=" * 80)
    print(f"🔍 開始執行補充搜尋：{search['id']}")
    print(f"📋 描述：{search['description']}")
    print(f"🔑 關鍵字：{search['query']}")
    print(f"📊 目標數量：{search['max_results']}")
    print(f"📅 年份範圍：{search['year_filter']}")
    print(f"🎯 目標：抓取 SERVQUAL、Donabedian 等高引用經典理論文獻")
    print("=" * 80)

    try:
        # 登入 WOS
        if scraper.get_session(wait_time=30):
            print("✅ 成功登入 Web of Science")

            # 執行搜尋
            print(f"\n🔎 正在搜尋經典理論文獻...")
            papers = scraper.search_api(
                query=search['query'],
                max_results=search['max_results']
            )

            if papers:
                print(f"📥 初步檢索到 {len(papers)} 篇文獻")

                # 客戶端年份篩選
                if search.get('year_filter'):
                    year_range = search['year_filter'].strip('()')
                    start_year, end_year = map(int, year_range.split('-'))

                    original_count = len(papers)
                    papers = [p for p in papers if p.get('year') != 'N/A' and start_year <= int(p['year']) <= end_year]

                    print(f"📅 年份篩選：{start_year}-{end_year}")
                    print(f"   篩選前：{original_count} 篇")
                    print(f"   篩選後：{len(papers)} 篇")

                # 按引用次數排序（客戶端排序）
                papers_sorted = sorted(papers, key=lambda x: int(x.get('citations', 0)), reverse=True)

                # 儲存結果
                output_base = f"{output_dir}/{search['id']}_經典服務品質理論"
                scraper.save_results(papers_sorted, output_base)

                print(f"\n✅ 搜尋完成！")
                print(f"📁 結果已儲存至：")
                print(f"   - {output_base}.csv")
                print(f"   - {output_base}.json")

                # 顯示統計資訊
                print(f"\n📊 文獻統計：")
                print(f"   總數：{len(papers_sorted)} 篇")

                # 年份分布
                year_dist = {}
                for p in papers_sorted:
                    year = p.get('year', 'N/A')
                    year_dist[year] = year_dist.get(year, 0) + 1

                print(f"\n📅 年份分布（前10年）：")
                sorted_years = sorted(year_dist.items(), key=lambda x: x[1], reverse=True)[:10]
                for year, count in sorted_years:
                    print(f"   {year}: {count} 篇")

                # 高引用文獻（Top 20）
                print(f"\n🌟 經典高引用文獻（Top 20）：")
                print(f"{'='*80}")
                for i, p in enumerate(papers_sorted[:20], 1):
                    citations = int(p.get('citations', 0))
                    title = p.get('title', 'N/A')
                    year = p.get('year', 'N/A')
                    journal = p.get('journal', 'N/A')
                    authors = p.get('authors', 'N/A')

                    # 取第一作者
                    first_author = authors.split(';')[0] if authors != 'N/A' else 'N/A'

                    print(f"\n{i}. [{year}] 被引 {citations} 次")
                    print(f"   {title[:100]}...")
                    print(f"   作者：{first_author}")
                    print(f"   期刊：{journal}")

                # 檢查是否有經典文獻關鍵字
                print(f"\n🔍 經典理論關鍵字出現情況：")
                keywords_count = {
                    'SERVQUAL': 0,
                    'Donabedian': 0,
                    'SERVPERF': 0,
                    'Parasuraman': 0,
                    'Zeithaml': 0
                }

                for p in papers_sorted:
                    title = p.get('title', '').upper()
                    authors = p.get('authors', '').upper()
                    keywords = p.get('keywords', '').upper()

                    for key in keywords_count.keys():
                        if key.upper() in title or key.upper() in authors or key.upper() in keywords:
                            keywords_count[key] += 1

                for key, count in keywords_count.items():
                    print(f"   {key}: {count} 篇")

            else:
                print("❌ 未找到任何文獻")

        else:
            print("❌ 無法登入 Web of Science")

    except Exception as e:
        print(f"\n❌ 執行過程中發生錯誤：")
        print(f"   {str(e)}")
        import traceback
        traceback.print_exc()

    finally:
        # 關閉瀏覽器
        scraper.close()
        print("\n🔚 程式執行完畢")

if __name__ == "__main__":
    main()
