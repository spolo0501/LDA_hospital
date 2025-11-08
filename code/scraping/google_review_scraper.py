#!/usr/bin/env python3
"""
Google Maps 評論抓取器 - 核心模組
改編自 /Users/simon/Downloads/Claude_code/GoogleReviews/csv_google_reviews_scraper.py

用於抓取 Google Maps 評論並儲存為 CSV 和 JSON 格式
"""

import requests
import json
import time
import re
import csv
import base64
from datetime import datetime
from typing import List, Dict, Optional
from urllib.parse import unquote
from langdetect import detect, LangDetectException


class GoogleReviewsScraper:
    """Google Maps 評論抓取器核心類別"""

    def __init__(self, language: str = "en", region: str = "us"):
        """
        初始化抓取器

        Args:
            language: 語言設定 (zh-TW, en, ja 等)
            region: 地區設定 (tw, us, uk 等)
        """
        self.base_url = "https://www.google.com/maps/rpc/listugcposts"
        self.language = language
        self.region = region
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "*/*",
            "Accept-Language": f"{language},zh;q=0.9,en;q=0.8",
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
            "Referer": "https://www.google.com/maps/",
            "X-Requested-With": "XMLHttpRequest"
        }

    def extract_place_id_from_url(self, google_maps_url: str) -> Optional[str]:
        """
        從 Google Maps URL 提取 Place ID

        Args:
            google_maps_url: Google Maps URL (支援標準 URL 和 cid 格式)

        Returns:
            Place ID (格式: 0x123:0x456) 或 None
        """
        print(f"🔍 分析 URL...")
        decoded_url = unquote(google_maps_url)

        # 檢查是否為 cid 格式
        cid_pattern = r'[?&]cid=(\d+)'
        cid_match = re.search(cid_pattern, decoded_url)
        if cid_match:
            cid = cid_match.group(1)
            # 將 cid 轉換為十六進位格式
            cid_hex = hex(int(cid))[2:]  # 移除 '0x' 前綴
            # Google Maps 使用的格式通常是兩部分，但 cid 只有一個值
            # 我們可以嘗試直接使用 cid 值
            place_id = f"0x0:0x{cid_hex}"
            print(f"✅ 從 cid 提取地點 ID: {place_id} (cid={cid})")
            return place_id

        # 標準 Place ID 格式
        patterns = [
            r'!1s(0x[0-9a-f]+:0x[0-9a-f]+)',
            r'1s(0x[0-9a-f]+:0x[0-9a-f]+)',
            r'!3m8!1s(0x[0-9a-f]+:0x[0-9a-f]+)',
        ]

        for pattern in patterns:
            matches = re.findall(pattern, decoded_url)
            if matches:
                place_id = matches[0]
                print(f"✅ 成功提取地點 ID: {place_id}")
                return place_id

        print("❌ 無法從 URL 提取地點 ID")
        return None

    def build_params(self, place_id: str, page_token: str = "", review_count: int = 10) -> dict:
        """構建 API 請求參數"""
        pb_param = f"!1m6!1s{place_id}!6m4!4m1!1e1!4m1!1e3!2m2!1i{review_count}!2s{page_token}!5m2!1s-kDaaLrLL8a_vr0PnrbygAI!7e81!8m9!2b1!3b1!5b1!7b1!12m4!1b1!2b1!4m1!1e1!11m0!13m1!1e2"

        return {
            "authuser": "0",
            "hl": self.language,
            "gl": self.region,
            "pb": pb_param
        }

    def fetch_reviews_page(self, place_id: str, page_token: str = "", review_count: int = 10) -> Optional[Dict]:
        """
        獲取單頁評論數據

        Args:
            place_id: 地點 ID
            page_token: 分頁 token
            review_count: 每頁評論數

        Returns:
            包含評論數據的字典或 None
        """
        params = self.build_params(place_id, page_token, review_count)

        try:
            response = requests.get(self.base_url, params=params, headers=self.headers, timeout=30)

            if response.status_code == 200:
                response_text = response.text
                if response_text.startswith(')]}\''):
                    json_text = response_text[4:]
                    data = json.loads(json_text)

                    # 檢查錯誤響應
                    if isinstance(data, list) and len(data) > 0:
                        first_item = data[0]
                        if isinstance(first_item, list) and len(first_item) > 0 and first_item[0] == "er":
                            return {
                                "status": "error",
                                "message": "API 返回錯誤，可能是地點 ID 無效或無評論數據"
                            }

                    return {
                        "status": "success",
                        "next_page_token": data[1] if len(data) > 1 and data[1] else None,
                        "reviews": data[2] if len(data) > 2 else [],
                        "raw_response": data
                    }

            return {
                "status": "error",
                "message": f"HTTP {response.status_code}"
            }

        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }

    def find_in_data(self, data, target_type, condition=None):
        """在嵌套數據中查找符合條件的值"""
        results = []

        def search_recursive(obj):
            if isinstance(obj, target_type):
                if condition is None or condition(obj):
                    results.append(obj)
            elif isinstance(obj, (list, tuple)):
                for item in obj:
                    search_recursive(item)
            elif isinstance(obj, dict):
                for value in obj.values():
                    search_recursive(value)

        search_recursive(data)
        return results

    def parse_review_data(self, review_raw: List) -> Dict:
        """
        解析評論數據

        Args:
            review_raw: 原始評論數據（嵌套列表）

        Returns:
            解析後的評論字典
        """
        review = {
            "review_id": "",
            "author_name": "Unknown User",
            "rating": 0,
            "review_text": "",
            "review_date": "",
            "photos_count": 0,
            "likes_count": 0,
            "language": "unknown",
        }

        if not review_raw or not isinstance(review_raw, list) or len(review_raw) == 0:
            return review

        try:
            # Google Maps API 資料結構：
            # review_raw[0] - 主要評論資料
            # review_raw[1] - null
            # review_raw[2] - 下一頁 token

            main_data = review_raw[0] if len(review_raw) > 0 else None
            if not main_data or not isinstance(main_data, list):
                return review

            # 提取評論 ID
            if len(main_data) > 0 and isinstance(main_data[0], str):
                review["review_id"] = f"r_{hash(main_data[0]) % 1000000}"

            # 提取作者和時間資訊 - main_data[1]
            if len(main_data) > 1 and isinstance(main_data[1], list):
                author_data = main_data[1]

                # 作者名稱 - author_data[4][5][0]
                try:
                    if (len(author_data) > 4 and isinstance(author_data[4], list) and
                        len(author_data[4]) > 5 and isinstance(author_data[4][5], list) and
                        len(author_data[4][5]) > 0 and isinstance(author_data[4][5][0], str)):
                        review["author_name"] = author_data[4][5][0]
                except (IndexError, TypeError):
                    pass

                # 評論日期 - author_data[6]
                try:
                    if len(author_data) > 6 and isinstance(author_data[6], str):
                        review["review_date"] = author_data[6]
                except (IndexError, TypeError):
                    pass

            # 提取評論內容和評分 - main_data[2]
            if len(main_data) > 2 and isinstance(main_data[2], list):
                content_data = main_data[2]

                # 評分 - content_data[0][0]
                try:
                    if (len(content_data) > 0 and isinstance(content_data[0], list) and
                        len(content_data[0]) > 0 and isinstance(content_data[0][0], int)):
                        rating = content_data[0][0]
                        if 1 <= rating <= 5:
                            review["rating"] = rating
                except (IndexError, TypeError):
                    pass

                # 評論文字 - content_data[15][0][0]
                try:
                    if (len(content_data) > 15 and isinstance(content_data[15], list) and
                        len(content_data[15]) > 0 and isinstance(content_data[15][0], list) and
                        len(content_data[15][0]) > 0 and isinstance(content_data[15][0][0], str)):
                        review["review_text"] = content_data[15][0][0]
                except (IndexError, TypeError):
                    pass

            # 計算照片數量（查找 googleusercontent 或 ggpht.com）
            photo_count = len(self.find_in_data(
                review_raw,
                str,
                lambda s: 'googleusercontent' in s or 'ggpht.com' in s
            ))
            review["photos_count"] = photo_count

            # 查找按讚數（查找小的正整數）
            like_candidates = self.find_in_data(review_raw, int, lambda x: 0 <= x <= 10000 and x not in [1,2,3,4,5])
            if like_candidates:
                review["likes_count"] = like_candidates[0]

            # 語言檢測
            if review["review_text"]:
                try:
                    detected_lang = detect(review["review_text"])
                    review["language"] = detected_lang
                except LangDetectException:
                    review["language"] = "unknown"
            else:
                review["language"] = "no_text"

        except Exception as e:
            print(f"⚠️ 解析評論時遇到錯誤: {e}")
            import traceback
            traceback.print_exc()

        return review

    def scrape_all_reviews(self, place_identifier: str, max_pages: int = 10,
                          reviews_per_page: int = 10, delay: float = 2.0) -> Dict:
        """
        主要抓取函數

        Args:
            place_identifier: Google Maps URL 或 Place ID
            max_pages: 最大抓取頁數
            reviews_per_page: 每頁評論數
            delay: 每頁間延遲秒數

        Returns:
            包含所有評論的字典
        """
        # 提取 Place ID
        if place_identifier.startswith("http"):
            place_id = self.extract_place_id_from_url(place_identifier)
            if not place_id:
                return {"error": "無法從 URL 提取地點 ID"}
        else:
            place_id = place_identifier

        print(f"🚀 開始抓取地點評論...")
        print(f"📍 地點 ID: {place_id}")
        print(f"📊 配置: 最大 {max_pages} 頁，每頁 {reviews_per_page} 條，延遲 {delay}s")

        all_reviews = []
        page_token = ""
        successful_pages = 0
        start_time = time.time()

        for page_count in range(1, max_pages + 1):
            print(f"📄 正在抓取第 {page_count} 頁...")

            result = self.fetch_reviews_page(place_id, page_token, reviews_per_page)

            if result["status"] == "error":
                print(f"❌ 第 {page_count} 頁抓取失敗: {result['message']}")
                if page_count == 1:
                    break
                continue

            reviews_data = result["reviews"]
            if not reviews_data:
                print(f"✅ 第 {page_count} 頁無更多評論，抓取完成")
                break

            page_reviews = []
            for review_raw in reviews_data:
                if review_raw:
                    parsed_review = self.parse_review_data(review_raw)
                    if not parsed_review.get("error"):
                        page_reviews.append(parsed_review)

            all_reviews.extend(page_reviews)
            successful_pages += 1
            print(f"✅ 第 {page_count} 頁完成，獲得 {len(page_reviews)} 條評論")

            page_token = result["next_page_token"]
            if not page_token:
                print("✅ 已到達最後一頁")
                break

            time.sleep(delay)

        end_time = time.time()
        duration = end_time - start_time

        return {
            "place_id": place_id,
            "total_reviews": len(all_reviews),
            "pages_fetched": successful_pages,
            "reviews": all_reviews,
            "scraping_duration": duration,
            "timestamp": datetime.now().isoformat()
        }

    def save_to_json(self, data: Dict, filename: str):
        """保存到 JSON"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"💾 JSON 文件已保存: {filename}")

    def save_to_csv(self, data: Dict, filename: str):
        """
        保存到 CSV 文件

        Args:
            data: 包含評論的字典
            filename: CSV 檔案路徑
        """
        try:
            reviews = data.get("reviews", [])
            if not reviews:
                print("❌ 沒有評論數據可以保存到 CSV")
                return

            # 定義 CSV 欄位
            fieldnames = [
                "序號",
                "評論ID",
                "作者姓名",
                "評分",
                "評論內容",
                "評論日期",
                "照片數量",
                "按讚數",
                "語言"
            ]

            # 寫入 CSV
            with open(filename, 'w', newline='', encoding='utf-8-sig') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()

                for i, review in enumerate(reviews, 1):
                    writer.writerow({
                        "序號": i,
                        "評論ID": review.get("review_id", ""),
                        "作者姓名": review.get("author_name", ""),
                        "評分": review.get("rating", 0),
                        "評論內容": review.get("review_text", ""),
                        "評論日期": review.get("review_date", ""),
                        "照片數量": review.get("photos_count", 0),
                        "按讚數": review.get("likes_count", 0),
                        "語言": review.get("language", "unknown")
                    })

            print(f"📊 CSV 文件已保存: {filename}")

            # 統計資訊
            avg_rating = sum(r.get("rating", 0) for r in reviews) / len(reviews) if reviews else 0
            has_text_count = len([r for r in reviews if r.get("review_text", "")])
            has_photos_count = len([r for r in reviews if r.get("photos_count", 0) > 0])

            print(f"   包含 {len(reviews)} 條評論數據")
            print(f"   平均評分: {avg_rating:.2f} 星")
            print(f"   有文字評論: {has_text_count} 條")
            print(f"   有照片評論: {has_photos_count} 條")

            # 創建統計檔案
            stats_filename = filename.replace('.csv', '_stats.csv')
            with open(stats_filename, 'w', newline='', encoding='utf-8-sig') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["統計項目", "數值"])
                writer.writerow(["地點ID", data.get("place_id", "")])
                writer.writerow(["總評論數", data.get("total_reviews", 0)])
                writer.writerow(["抓取頁數", data.get("pages_fetched", 0)])
                writer.writerow(["抓取時間(秒)", f"{data.get('scraping_duration', 0):.2f}"])
                writer.writerow(["平均評分", f"{avg_rating:.2f}"])
                writer.writerow(["有文字評論數", has_text_count])
                writer.writerow(["有照片評論數", has_photos_count])
                writer.writerow(["抓取日期", data.get("timestamp", "").split('T')[0]])

            print(f"📈 統計文件已保存: {stats_filename}")

        except Exception as e:
            print(f"❌ 保存 CSV 文件失敗: {e}")
