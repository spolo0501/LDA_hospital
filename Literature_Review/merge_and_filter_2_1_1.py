#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
整合並篩選 2.1-1 醫療服務品質理論文獻
合併兩次搜尋結果（131+92=223篇），篩選高品質醫療相關文獻
"""

import json
import csv
import os

def load_json(file_path):
    """載入JSON檔案"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def is_healthcare_related(paper):
    """判斷是否為醫療相關文獻"""
    healthcare_keywords = [
        'health', 'hospital', 'medical', 'patient', 'clinical',
        'nursing', 'doctor', 'physician', 'care', 'healthcare',
        'treatment', 'disease', 'clinic', 'surgery', 'pharmacy'
    ]

    # 檢查標題、期刊、摘要
    text = (
        paper.get('title', '').lower() + ' ' +
        paper.get('journal', '').lower() + ' ' +
        paper.get('abstract', '').lower()
    )

    return any(kw in text for kw in healthcare_keywords)

def has_theory_keywords(paper):
    """判斷是否包含理論關鍵詞"""
    theory_keywords = [
        'SERVQUAL', 'Donabedian', 'SERVPERF', 'Parasuraman',
        'service quality theory', 'quality framework', 'quality model',
        'quality dimensions', 'quality assessment'
    ]

    text = (
        paper.get('title', '') + ' ' +
        paper.get('abstract', '') + ' ' +
        paper.get('keywords', '')
    ).upper()

    return any(kw.upper() in text for kw in theory_keywords)

def should_keep_paper(paper):
    """判斷是否應該保留此文獻"""
    citations = int(paper.get('citations', 0))

    # 保留條件（任一符合即保留）：
    # 1. 醫療相關 AND (引用>5次 OR 包含理論關鍵詞)
    # 2. 引用>10次（即使非醫療）
    # 3. 包含多個理論關鍵詞

    is_healthcare = is_healthcare_related(paper)
    has_theory = has_theory_keywords(paper)

    if citations > 10:
        return True

    if is_healthcare and (citations > 5 or has_theory):
        return True

    if has_theory and citations > 3:
        return True

    return False

def merge_and_filter():
    """合併並篩選文獻"""

    # 檔案路徑
    base_dir = "Literature_Review/Chapter_2.1_Healthcare_Service_Quality"
    file1 = f"{base_dir}/2.1-1_revised_醫療服務品質基礎理論.json"
    file2 = f"{base_dir}/2.1-1_classic_theories_經典服務品質理論.json"

    print("=" * 80)
    print("📚 整合並篩選 2.1-1 醫療服務品質理論文獻")
    print("=" * 80)

    # 載入兩個檔案
    print(f"\n📖 載入文獻...")
    papers1 = load_json(file1)
    papers2 = load_json(file2)

    print(f"   檔案1（revised）：{len(papers1)} 篇")
    print(f"   檔案2（classic）：{len(papers2)} 篇")
    print(f"   總計：{len(papers1) + len(papers2)} 篇")

    # 合併並去重（根據DOI或UID）
    print(f"\n🔄 合併並去重...")
    all_papers = {}

    for paper in papers1 + papers2:
        # 使用 DOI 或 UID 作為唯一識別
        key = paper.get('doi', '') or paper.get('uid', '')
        if key and key not in all_papers:
            all_papers[key] = paper
        elif not key:
            # 如果沒有DOI和UID，使用標題
            title_key = paper.get('title', '')
            if title_key and title_key not in [p.get('title', '') for p in all_papers.values()]:
                all_papers[title_key] = paper

    merged_papers = list(all_papers.values())
    print(f"   去重後：{len(merged_papers)} 篇")

    # 篩選高品質文獻
    print(f"\n🔍 篩選高品質醫療相關文獻...")
    print(f"   篩選條件：")
    print(f"   1. 醫療相關 AND (引用>5次 OR 包含理論關鍵詞)")
    print(f"   2. 引用>10次（即使非醫療）")
    print(f"   3. 包含理論關鍵詞 AND 引用>3次")

    filtered_papers = [p for p in merged_papers if should_keep_paper(p)]

    print(f"\n✅ 篩選結果：{len(filtered_papers)} 篇（保留率 {len(filtered_papers)/len(merged_papers)*100:.1f}%）")

    # 按引用次數排序
    filtered_papers_sorted = sorted(filtered_papers, key=lambda x: int(x.get('citations', 0)), reverse=True)

    # 統計分析
    print(f"\n📊 篩選後文獻統計：")

    # 醫療相關統計
    healthcare_count = sum(1 for p in filtered_papers_sorted if is_healthcare_related(p))
    print(f"   醫療相關：{healthcare_count} 篇（{healthcare_count/len(filtered_papers_sorted)*100:.1f}%）")

    # 理論關鍵詞統計
    theory_count = sum(1 for p in filtered_papers_sorted if has_theory_keywords(p))
    print(f"   含理論關鍵詞：{theory_count} 篇（{theory_count/len(filtered_papers_sorted)*100:.1f}%）")

    # 引用次數統計
    citations = [int(p.get('citations', 0)) for p in filtered_papers_sorted]
    print(f"   平均引用：{sum(citations)/len(citations):.1f} 次")
    print(f"   引用範圍：{min(citations)}-{max(citations)} 次")

    # 年份分布
    year_dist = {}
    for p in filtered_papers_sorted:
        year = p.get('year', 'N/A')
        year_dist[year] = year_dist.get(year, 0) + 1

    print(f"\n📅 年份分布（前10年）：")
    sorted_years = sorted(year_dist.items(), key=lambda x: x[1], reverse=True)[:10]
    for year, count in sorted_years:
        print(f"   {year}: {count} 篇")

    # 顯示高引用文獻（Top 15）
    print(f"\n🌟 高引用文獻（Top 15）：")
    print("=" * 80)
    for i, p in enumerate(filtered_papers_sorted[:15], 1):
        citations = int(p.get('citations', 0))
        title = p.get('title', 'N/A')
        year = p.get('year', 'N/A')
        journal = p.get('journal', 'N/A')

        is_hc = "🏥" if is_healthcare_related(p) else "  "
        has_th = "📚" if has_theory_keywords(p) else "  "

        print(f"\n{i}. [{year}] 被引 {citations} 次 {is_hc}{has_th}")
        print(f"   {title[:90]}...")
        print(f"   {journal[:70]}")

    print(f"\n💡 圖示說明：🏥=醫療相關 📚=含理論關鍵詞")

    # 儲存結果
    output_base = f"{base_dir}/2.1-1_FINAL_醫療服務品質基礎理論"

    # 儲存 JSON
    with open(f"{output_base}.json", 'w', encoding='utf-8') as f:
        json.dump(filtered_papers_sorted, f, ensure_ascii=False, indent=2)

    # 儲存 CSV
    if filtered_papers_sorted:
        fieldnames = ['title', 'authors', 'year', 'journal', 'doi', 'uid',
                     'countries', 'abstract', 'citations', 'references',
                     'keywords', 'subtypeDescription']

        with open(f"{output_base}.csv", 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for paper in filtered_papers_sorted:
                # 確保所有欄位都存在
                row = {field: paper.get(field, '') for field in fieldnames}
                writer.writerow(row)

    print(f"\n💾 結果已儲存：")
    print(f"   - {output_base}.json")
    print(f"   - {output_base}.csv")

    # 生成篩選報告
    report_file = f"{base_dir}/2.1-1_FILTERING_REPORT.md"
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write("# 2.1-1 醫療服務品質基礎理論文獻篩選報告\n\n")
        f.write(f"**生成時間**：{os.popen('date').read().strip()}\n\n")
        f.write("---\n\n")

        f.write("## 📊 篩選流程\n\n")
        f.write(f"1. **初始文獻**：{len(papers1) + len(papers2)} 篇\n")
        f.write(f"   - 搜尋1（revised）：{len(papers1)} 篇\n")
        f.write(f"   - 搜尋2（classic）：{len(papers2)} 篇\n\n")
        f.write(f"2. **去重後**：{len(merged_papers)} 篇\n\n")
        f.write(f"3. **篩選後**：{len(filtered_papers_sorted)} 篇\n")
        f.write(f"   - 保留率：{len(filtered_papers_sorted)/len(merged_papers)*100:.1f}%\n\n")

        f.write("---\n\n")
        f.write("## 🔍 篩選條件\n\n")
        f.write("保留文獻需符合以下**任一條件**：\n\n")
        f.write("1. **醫療相關** AND (**引用>5次** OR **包含理論關鍵詞**)\n")
        f.write("2. **引用>10次**（即使非醫療）\n")
        f.write("3. **包含理論關鍵詞** AND **引用>3次**\n\n")

        f.write("**醫療關鍵詞**：health, hospital, medical, patient, clinical, nursing, doctor, physician, care, treatment, disease, clinic, surgery, pharmacy\n\n")
        f.write("**理論關鍵詞**：SERVQUAL, Donabedian, SERVPERF, Parasuraman, service quality theory, quality framework, quality model, quality dimensions, quality assessment\n\n")

        f.write("---\n\n")
        f.write("## 📈 篩選結果統計\n\n")
        f.write(f"- **醫療相關**：{healthcare_count} 篇（{healthcare_count/len(filtered_papers_sorted)*100:.1f}%）\n")
        f.write(f"- **含理論關鍵詞**：{theory_count} 篇（{theory_count/len(filtered_papers_sorted)*100:.1f}%）\n")
        f.write(f"- **平均引用**：{sum(citations)/len(citations):.1f} 次\n")
        f.write(f"- **引用範圍**：{min(citations)}-{max(citations)} 次\n\n")

        f.write("---\n\n")
        f.write("## 🌟 Top 20 高引用文獻\n\n")
        for i, p in enumerate(filtered_papers_sorted[:20], 1):
            citations = int(p.get('citations', 0))
            title = p.get('title', 'N/A')
            year = p.get('year', 'N/A')
            journal = p.get('journal', 'N/A')

            is_hc = "🏥" if is_healthcare_related(p) else ""
            has_th = "📚" if has_theory_keywords(p) else ""

            f.write(f"### {i}. [{year}] 被引 {citations} 次 {is_hc}{has_th}\n\n")
            f.write(f"**標題**：{title}\n\n")
            f.write(f"**期刊**：{journal}\n\n")
            f.write(f"**DOI**：{p.get('doi', 'N/A')}\n\n")
            f.write("---\n\n")

    print(f"   - {report_file}")

    print(f"\n✅ 整合篩選完成！")
    print("=" * 80)

if __name__ == "__main__":
    merge_and_filter()
