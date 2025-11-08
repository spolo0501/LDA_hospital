#!/usr/bin/env python3
"""
Debug 腳本 - 查看 Google Maps API 原始回應
用於理解資料結構並修正解析邏輯
"""

import sys
import os
import json

# 加入核心爬蟲模組
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from google_review_scraper import GoogleReviewsScraper


def debug_api_response(url: str, num_reviews: int = 5):
    """
    Debug Google Maps API 回應

    Args:
        url: Google Maps URL
        num_reviews: 要抓取的評論數
    """
    print("🔍 Debug Mode - 查看 API 原始回應\n")

    scraper = GoogleReviewsScraper(language="en", region="uk")

    # 提取 Place ID
    place_id = scraper.extract_place_id_from_url(url)
    if not place_id:
        print("❌ 無法提取 Place ID")
        return

    print(f"\n📍 Place ID: {place_id}\n")
    print("=" * 70)

    # 抓取第一頁
    result = scraper.fetch_reviews_page(place_id, page_token="", review_count=num_reviews)

    if result["status"] == "error":
        print(f"❌ API 錯誤: {result['message']}")
        return

    reviews_data = result.get("reviews", [])
    print(f"\n✅ 獲得 {len(reviews_data)} 條評論\n")

    # 詳細檢查每條評論
    for i, review_raw in enumerate(reviews_data[:3], 1):  # 只看前3條
        print(f"\n{'=' * 70}")
        print(f"評論 #{i} - 原始資料結構")
        print(f"{'=' * 70}\n")

        # 將原始資料轉換為可讀格式
        print_nested_structure(review_raw, indent=0, max_depth=5)

        # 嘗試解析
        print(f"\n{'─' * 70}")
        print(f"解析結果:")
        print(f"{'─' * 70}\n")
        parsed = scraper.parse_review_data(review_raw)
        print(json.dumps(parsed, indent=2, ensure_ascii=False))
        print()


def print_nested_structure(obj, indent=0, max_depth=10, path="root"):
    """
    打印嵌套資料結構（遞迴）

    Args:
        obj: 要打印的對象
        indent: 縮排層級
        max_depth: 最大深度
        path: 目前路徑
    """
    if indent >= max_depth:
        print("  " * indent + "... (達到最大深度)")
        return

    prefix = "  " * indent

    if isinstance(obj, dict):
        print(f"{prefix}📦 Dict ({len(obj)} keys):")
        for key, value in list(obj.items())[:10]:  # 只顯示前10個 key
            print(f"{prefix}  🔑 {key}: {type(value).__name__}", end="")
            if isinstance(value, str) and len(value) < 50:
                print(f" = '{value}'")
            elif isinstance(value, (int, float, bool)):
                print(f" = {value}")
            else:
                print()
                print_nested_structure(value, indent + 2, max_depth, f"{path}.{key}")

    elif isinstance(obj, (list, tuple)):
        print(f"{prefix}📋 {type(obj).__name__} ({len(obj)} items):")
        for i, item in enumerate(obj[:5]):  # 只顯示前5個元素
            print(f"{prefix}  [{i}] {type(item).__name__}", end="")

            if isinstance(item, str):
                # 顯示字串的前50個字符
                display_str = item[:50]
                if len(item) > 50:
                    display_str += "..."
                # 檢查是否為可打印字符
                if item.isprintable() and not item.startswith('http'):
                    print(f" = '{display_str}'")
                else:
                    print(f" (長度: {len(item)})")
            elif isinstance(item, (int, float)):
                print(f" = {item}")
            elif isinstance(item, bool):
                print(f" = {item}")
            else:
                print()
                print_nested_structure(item, indent + 2, max_depth, f"{path}[{i}]")

        if len(obj) > 5:
            print(f"{prefix}  ... ({len(obj) - 5} more items)")

    elif isinstance(obj, str):
        if len(obj) < 100 and obj.isprintable():
            print(f"{prefix}📝 String: '{obj}'")
        else:
            print(f"{prefix}📝 String (長度: {len(obj)})")

    elif isinstance(obj, (int, float, bool)):
        print(f"{prefix}🔢 {type(obj).__name__}: {obj}")

    else:
        print(f"{prefix}❓ {type(obj).__name__}: {obj}")


if __name__ == "__main__":
    # 使用 St Thomas Hospital 的 URL 進行測試
    test_url = "https://maps.google.com/?cid=305199580624720593"
    debug_api_response(test_url, num_reviews=5)
