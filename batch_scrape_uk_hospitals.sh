#!/bin/bash
# 批次抓取英國 20 家醫院 Google Reviews
# 每家醫院上限 3,000 筆評論（150 頁 x 20 筆/頁）

echo "======================================================================"
echo "🏥 英國醫院評論批次抓取"
echo "======================================================================"
echo "📊 配置: 20 家醫院，每家最多 3,000 筆評論"
echo "⏱️  預計總耗時: ~2 小時"
echo "======================================================================"
echo ""

# 定義醫院列表（名稱|URL）
HOSPITALS=(
    "St_Thomas_Hospital|https://maps.google.com/?cid=305199580624720593"
    "University_College_Hospital|https://maps.google.com/?cid=14297603414019525515"
    "Addenbrookes_Hospital|https://maps.google.com/?cid=11680960961859333519"
    "John_Radcliffe_Hospital|https://maps.google.com/?cid=9525307361114824499"
    "Royal_Victoria_Infirmary|https://maps.google.com/?cid=17332363532472313786"
    "Queen_Elizabeth_Hospital|https://maps.google.com/?cid=8234757019974419960"
    "Guys_Hospital|https://maps.google.com/?cid=2358436778919738465"
    "Chelsea_Westminster_Hospital|https://maps.google.com/?cid=10431341826040534655"
    "Freeman_Hospital|https://maps.google.com/?cid=12573166850824494384"
    "Southmead_Hospital|https://maps.google.com/?cid=14975773153703173940"
    "St_James_University_Hospital|https://maps.google.com/?cid=6169779783518962027"
    "Manchester_Royal_Infirmary|https://maps.google.com/?cid=15872913907432771823"
    "Kings_College_Hospital|https://maps.google.com/?cid=9025526130079493131"
    "Royal_Infirmary_Edinburgh|https://maps.google.com/?cid=14663317975152856317"
    "St_Georges_Hospital|https://maps.google.com/?cid=10971137890550089060"
    "Royal_London_Hospital|https://maps.google.com/?cid=15648810078149268268"
    "Nottingham_City_Hospital|https://maps.google.com/?cid=1984113241976292947"
    "Southampton_General_Hospital|https://maps.google.com/?cid=7478024969779959081"
    "Royal_Sussex_County_Hospital|https://maps.google.com/?cid=8235907532383580366"
    "Leicester_Royal_Infirmary|https://maps.google.com/?cid=9863477696507422462"
)

# 輸出目錄
OUTPUT_DIR="./google_reviews_output"

# 統計變數
TOTAL=${#HOSPITALS[@]}
SUCCESS=0
FAILED=0
START_TIME=$(date +%s)

# 創建日誌檔案
LOG_FILE="batch_scrape_$(date +%Y%m%d_%H%M%S).log"
echo "📝 日誌檔案: $LOG_FILE"
echo ""

# 開始抓取
for i in "${!HOSPITALS[@]}"; do
    NUM=$((i + 1))
    IFS='|' read -r NAME URL <<< "${HOSPITALS[$i]}"

    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "🏥 [$NUM/$TOTAL] 正在抓取: $NAME"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "📍 URL: $URL"
    echo "🎯 目標: 3,000 筆評論 (150 頁)"
    echo ""

    # 執行抓取
    python3 ~/.claude/skills/google-review-scraper/scripts/scrape_reviews.py \
        --url "$URL" \
        --name "$NAME" \
        --category hospitals \
        --region uk \
        --output-dir "$OUTPUT_DIR" \
        --max-pages 150 \
        --per-page 20 \
        --delay 2.0 \
        2>&1 | tee -a "$LOG_FILE"

    # 檢查執行結果
    if [ ${PIPESTATUS[0]} -eq 0 ]; then
        SUCCESS=$((SUCCESS + 1))
        echo "✅ [$NUM/$TOTAL] $NAME - 完成"
    else
        FAILED=$((FAILED + 1))
        echo "❌ [$NUM/$TOTAL] $NAME - 失敗"
    fi

    echo ""

    # 如果不是最後一家，等待 30 秒避免被限速
    if [ $NUM -lt $TOTAL ]; then
        echo "⏸️  等待 30 秒後繼續下一家..."
        echo ""
        sleep 30
    fi
done

# 計算總耗時
END_TIME=$(date +%s)
DURATION=$((END_TIME - START_TIME))
HOURS=$((DURATION / 3600))
MINUTES=$(((DURATION % 3600) / 60))
SECONDS=$((DURATION % 60))

# 顯示最終報告
echo ""
echo "======================================================================"
echo "📊 批次抓取完成報告"
echo "======================================================================"
echo "✅ 成功: $SUCCESS 家醫院"
echo "❌ 失敗: $FAILED 家醫院"
echo "⏱️  總耗時: ${HOURS}h ${MINUTES}m ${SECONDS}s"
echo "📁 輸出目錄: $OUTPUT_DIR/hospitals/uk/"
echo "📝 詳細日誌: $LOG_FILE"
echo "======================================================================"
echo ""

# 顯示抓取的檔案列表
echo "📂 生成的檔案:"
ls -lh "$OUTPUT_DIR/hospitals/uk/" | grep -v "^total" | awk '{printf "   %s %10s  %s\n", $6" "$7" "$8, $5, $9}'
echo ""

# 生成統計摘要
echo "📈 正在生成統計摘要..."
python3 - <<EOF
import os
import csv
from pathlib import Path

output_dir = Path("$OUTPUT_DIR/hospitals/uk/")
stats_files = list(output_dir.glob("*_stats.csv"))

print(f"\n找到 {len(stats_files)} 個統計檔案\n")
print("醫院名稱                              總評論數    平均評分")
print("─" * 70)

total_reviews = 0
for stats_file in sorted(stats_files):
    with open(stats_file, 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        data = {row[0]: row[1] for row in reader}

        name = stats_file.stem.replace('_stats', '').replace('_', ' ')
        reviews = data.get('總評論數', 'N/A')
        avg_rating = data.get('平均評分', 'N/A')

        print(f"{name[:35]:<35} {reviews:>10} {avg_rating:>12}")

        try:
            total_reviews += int(reviews)
        except:
            pass

print("─" * 70)
print(f"{'總計':<35} {total_reviews:>10}")
print()
EOF

echo "🎉 全部完成！"
