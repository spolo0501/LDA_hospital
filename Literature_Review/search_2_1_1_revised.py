#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2.1-1 修正版：醫療服務品質基礎理論文獻搜尋
年份範圍：1990-2024（35年，涵蓋經典理論）
目標數量：150篇
關鍵字：醫療專屬服務品質理論
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
        "id": "2.1-1_revised",
        "query": "(healthcare OR hospital OR medical) service quality AND (theory OR framework OR model OR dimension)",
        "max_results": 150,
        "description": "醫療服務品質基礎理論（1990-2024）- 修正版",
        "year_filter": "(1990-2024)"
    }

    print("=" * 80)
    print(f"🔍 開始執行搜尋：{search['id']}")
    print(f"📋 描述：{search['description']}")
    print(f"🔑 關鍵字：{search['query']}")
    print(f"📊 目標數量：{search['max_results']}")
    print(f"📅 年份範圍：{search['year_filter']}")
    print("=" * 80)

    try:
        # 登入 WOS
        if scraper.get_session(wait_time=30):
            print("✅ 成功登入 Web of Science")

            # 執行搜尋
            print(f"\n🔎 正在搜尋...")
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

                # 儲存結果
                output_base = f"{output_dir}/{search['id']}_醫療服務品質基礎理論"
                scraper.save_results(papers, output_base)

                print(f"\n✅ 搜尋完成！")
                print(f"📁 結果已儲存至：")
                print(f"   - {output_base}.csv")
                print(f"   - {output_base}.json")

                # 顯示統計資訊
                print(f"\n📊 文獻統計：")
                print(f"   總數：{len(papers)} 篇")

                # 年份分布
                year_dist = {}
                for p in papers:
                    year = p.get('year', 'N/A')
                    year_dist[year] = year_dist.get(year, 0) + 1

                print(f"\n📅 年份分布（前10年）：")
                sorted_years = sorted(year_dist.items(), key=lambda x: x[1], reverse=True)[:10]
                for year, count in sorted_years:
                    print(f"   {year}: {count} 篇")

                # 高引用文獻
                print(f"\n🌟 高引用文獻（Top 10）：")
                sorted_papers = sorted(papers, key=lambda x: int(x.get('citations', 0)), reverse=True)[:10]
                for i, p in enumerate(sorted_papers, 1):
                    print(f"   {i}. [{p.get('year')}] {p.get('title')[:80]}...")
                    print(f"      被引次數：{p.get('citations', 0)}")
                    print(f"      期刊：{p.get('journal', 'N/A')}")
                    print()

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
