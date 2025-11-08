#!/usr/bin/env python3
"""
Google Maps 評論智能抓取器 - 包裝器
整合到 LDA_hospital 專案，自動管理目錄結構

使用範例：
    python3 scrape_reviews.py \\
        --url "Google Maps URL" \\
        --name "Hospital_Name" \\
        --category hospitals \\
        --region usa \\
        --max-pages 100
"""

import os
import sys
import argparse
from datetime import datetime
from pathlib import Path
import json

# 加入核心爬蟲模組
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from google_review_scraper import GoogleReviewsScraper


class IntelligentReviewScraper:
    """智能評論抓取器 - 與專案目錄結構整合"""

    # 專案根目錄（自動偵測）
    PROJECT_ROOT = Path(__file__).parent.parent.parent

    # 支援的資料類型
    CATEGORIES = [
        'hospitals', 'museums', 'airports', 'restaurants',
        'hotels', 'universities', 'shopping_malls', 'tourist_attractions'
    ]

    # 支援的地區
    REGIONS = [
        'taiwan', 'usa', 'uk', 'japan', 'china',
        'asia', 'europe', 'north_america'
    ]

    # 語言對應表
    LANGUAGE_MAP = {
        'taiwan': 'zh-TW',
        'china': 'zh-CN',
        'japan': 'ja',
        'usa': 'en',
        'uk': 'en',
        'asia': 'en',
        'europe': 'en',
        'north_america': 'en'
    }

    # 地區代碼對應表
    REGION_CODE_MAP = {
        'taiwan': 'tw',
        'china': 'cn',
        'japan': 'jp',
        'usa': 'us',
        'uk': 'uk',
        'asia': 'us',
        'europe': 'uk',
        'north_america': 'us'
    }

    def __init__(self, category: str, region: str, place_name: str, output_dir: str = None):
        """
        初始化智能抓取器

        Args:
            category: 資料類型 (hospitals, museums, 等)
            region: 地區 (taiwan, usa, uk, 等)
            place_name: 地點名稱 (用於檔名)
            output_dir: 自定義輸出目錄（可選，預設為專案結構）
        """
        if category not in self.CATEGORIES:
            raise ValueError(f"不支援的 category: {category}。支援的類型: {', '.join(self.CATEGORIES)}")

        if region not in self.REGIONS:
            raise ValueError(f"不支援的 region: {region}。支援的地區: {', '.join(self.REGIONS)}")

        self.category = category
        self.region = region
        self.place_name = self._sanitize_filename(place_name)

        # 設定語言和地區代碼
        self.language = self.LANGUAGE_MAP.get(region, 'en')
        self.region_code = self.REGION_CODE_MAP.get(region, 'us')

        # 初始化核心爬蟲
        self.scraper = GoogleReviewsScraper(language=self.language, region=self.region_code)

        # 設定輸出路徑
        if output_dir:
            # 使用自定義輸出目錄
            self.output_dir = Path(output_dir) / category / region
        else:
            # 使用專案預設結構
            self.output_dir = self.PROJECT_ROOT / "data" / "raw" / category / region

        self.output_dir.mkdir(parents=True, exist_ok=True)

    def _sanitize_filename(self, name: str) -> str:
        """清理檔案名稱，移除非法字元"""
        # 移除或替換非法字元
        name = name.replace('/', '_').replace('\\', '_')
        name = name.replace(':', '_').replace('*', '_')
        name = name.replace('?', '_').replace('"', '_')
        name = name.replace('<', '_').replace('>', '_')
        name = name.replace('|', '_').replace(' ', '_')
        return name

    def _generate_output_paths(self) -> dict:
        """生成輸出檔案路徑（不含時間戳，避免重複抓取）"""
        base_filename = self.place_name

        return {
            'csv': self.output_dir / f"{base_filename}.csv",
            'json': self.output_dir / f"{base_filename}.json",
            'stats': self.output_dir / f"{base_filename}_stats.csv",
            'report': self.output_dir / f"{base_filename}_report.txt"
        }

    def scrape(self, url: str, max_pages: int = 100, per_page: int = 20, delay: float = 2.0) -> dict:
        """
        執行抓取

        Args:
            url: Google Maps URL 或 Place ID
            max_pages: 最大抓取頁數
            per_page: 每頁評論數
            delay: 每頁間延遲秒數

        Returns:
            抓取結果字典
        """
        print("\n" + "=" * 70)
        print("🏥 智能評論抓取器")
        print("=" * 70)
        print(f"📂 資料類型: {self.category}")
        print(f"🌍 地區: {self.region}")
        print(f"📍 地點: {self.place_name}")
        print(f"🗂️  輸出目錄: {self.output_dir}")
        print(f"🌐 語言: {self.language}, 地區代碼: {self.region_code}")
        print("=" * 70 + "\n")

        # 檢查檔案是否已存在
        paths = self._generate_output_paths()
        if paths['csv'].exists():
            file_size = paths['csv'].stat().st_size
            print(f"⚠️  檔案已存在: {paths['csv'].name}")
            print(f"📦 檔案大小: {file_size / 1024:.1f} KB")
            print(f"⏭️  跳過抓取（避免重複）\n")
            return {
                "status": "skipped",
                "reason": "file_already_exists",
                "paths": {k: str(v) for k, v in paths.items()}
            }

        # 執行抓取
        results = self.scraper.scrape_all_reviews(
            place_identifier=url,
            max_pages=max_pages,
            reviews_per_page=per_page,
            delay=delay
        )

        if "error" in results:
            print(f"\n❌ 抓取失敗: {results['error']}")
            return results

        # 儲存檔案
        print(f"\n💾 正在儲存檔案...")
        self.scraper.save_to_csv(results, str(paths['csv']))
        self.scraper.save_to_json(results, str(paths['json']))

        # 生成抓取報告
        self._generate_report(results, paths['report'])

        print(f"\n✅ 抓取完成！")
        print(f"\n📁 生成的檔案:")
        print(f"   • CSV:    {paths['csv']}")
        print(f"   • JSON:   {paths['json']}")
        print(f"   • Stats:  {paths['stats']}")
        print(f"   • Report: {paths['report']}")

        return {
            "status": "success",
            "results": results,
            "paths": {k: str(v) for k, v in paths.items()}
        }

    def _generate_report(self, results: dict, report_path: Path):
        """生成抓取報告"""
        reviews = results.get("reviews", [])
        avg_rating = sum(r.get("rating", 0) for r in reviews) / len(reviews) if reviews else 0

        report = f"""
{'='*70}
Google Maps 評論抓取報告
{'='*70}

📊 基本資訊
{'─'*70}
資料類型:      {self.category}
地區:          {self.region}
地點:          {self.place_name}
抓取時間:      {results.get('timestamp', 'N/A')}

📈 抓取統計
{'─'*70}
總評論數:      {results.get('total_reviews', 0)}
成功頁數:      {results.get('pages_fetched', 0)}
耗時:          {results.get('scraping_duration', 0):.2f} 秒
平均評分:      {avg_rating:.2f} 星

📝 評論內容統計
{'─'*70}
有文字評論:    {len([r for r in reviews if r.get('review_text', '')])}
有照片評論:    {len([r for r in reviews if r.get('photos_count', 0) > 0])}

⭐ 評分分布
{'─'*70}
5星: {len([r for r in reviews if r.get('rating') == 5])} ({len([r for r in reviews if r.get('rating') == 5])/len(reviews)*100:.1f}%)
4星: {len([r for r in reviews if r.get('rating') == 4])} ({len([r for r in reviews if r.get('rating') == 4])/len(reviews)*100:.1f}%)
3星: {len([r for r in reviews if r.get('rating') == 3])} ({len([r for r in reviews if r.get('rating') == 3])/len(reviews)*100:.1f}%)
2星: {len([r for r in reviews if r.get('rating') == 2])} ({len([r for r in reviews if r.get('rating') == 2])/len(reviews)*100:.1f}%)
1星: {len([r for r in reviews if r.get('rating') == 1])} ({len([r for r in reviews if r.get('rating') == 1])/len(reviews)*100:.1f}%)

📁 檔案位置
{'─'*70}
輸出目錄:      {self.output_dir}
CSV檔案:       {self.place_name}_*.csv
JSON檔案:      {self.place_name}_*.json

{'='*70}
抓取完成 ✅
{'='*70}
"""

        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report)

        print(f"📄 報告已生成: {report_path}")


def main():
    """命令列介面"""
    parser = argparse.ArgumentParser(
        description="智能 Google Maps 評論抓取器",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用範例:

  # 抓取美國醫院評論
  python3 scrape_reviews.py \\
      --url "https://www.google.com/maps/place/..." \\
      --name "Mayo_Clinic" \\
      --category hospitals \\
      --region usa \\
      --max-pages 100

  # 抓取台灣博物館評論
  python3 scrape_reviews.py \\
      --url "https://www.google.com/maps/place/..." \\
      --name "National_Palace_Museum" \\
      --category museums \\
      --region taiwan \\
      --max-pages 50

支援的資料類型 (category):
  hospitals, museums, airports, restaurants, hotels, universities,
  shopping_malls, tourist_attractions

支援的地區 (region):
  taiwan, usa, uk, japan, china, asia, europe, north_america
        """
    )

    parser.add_argument("--url", required=True, help="Google Maps URL 或 Place ID")
    parser.add_argument("--name", required=True, help="地點名稱 (用於檔名)")
    parser.add_argument("--category", required=True, choices=IntelligentReviewScraper.CATEGORIES,
                       help="資料類型")
    parser.add_argument("--region", required=True, choices=IntelligentReviewScraper.REGIONS,
                       help="地區")
    parser.add_argument("--output-dir", type=str, default=None,
                       help="自定義輸出目錄（可選，預設為 ./google_reviews_output/）")
    parser.add_argument("--max-pages", type=int, default=100, help="最大抓取頁數 (預設: 100)")
    parser.add_argument("--per-page", type=int, default=20, help="每頁評論數 (預設: 20)")
    parser.add_argument("--delay", type=float, default=2.0, help="每頁間延遲秒數 (預設: 2.0)")

    args = parser.parse_args()

    try:
        # 如果沒有指定輸出目錄，使用當前目錄的 google_reviews_output
        output_dir = args.output_dir if args.output_dir else "./google_reviews_output"

        # 初始化智能抓取器
        scraper = IntelligentReviewScraper(
            category=args.category,
            region=args.region,
            place_name=args.name,
            output_dir=output_dir
        )

        # 執行抓取
        result = scraper.scrape(
            url=args.url,
            max_pages=args.max_pages,
            per_page=args.per_page,
            delay=args.delay
        )

        if result.get("status") == "success":
            print("\n🎉 所有任務完成！")
            sys.exit(0)
        else:
            print("\n❌ 抓取失敗")
            sys.exit(1)

    except Exception as e:
        print(f"\n❌ 發生錯誤: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
