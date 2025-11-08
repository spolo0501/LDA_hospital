在儲存分析結果時，請遵循以下目錄架構（參考 CLAUDE.md）：

## 台灣 LDA 結果
- **模型檔案**（.pkl, .xlsx）→ `results/taiwan_lda_k7/`
- **視覺化圖表**（.png, .jpg）→ `results/taiwan_lda_k7/visualizations/`

範例：
```python
# 儲存模型
model.save("results/taiwan_lda_k7/lda_k7_model_updated.pkl")

# 儲存圖表
plt.savefig("results/taiwan_lda_k7/visualizations/topic_distribution_2025.png")
```

## 美國 LDA 結果
- **模型檔案** → `results/usa_lda_k7/`
- **視覺化圖表** → `results/usa_lda_k7/visualizations/`

## 台美比較結果
- **比較圖表和報告** → `results/comparison/`

範例：
```python
# 儲存比較視覺化
plt.savefig("results/comparison/Taiwan_USA_Topic_Alignment_2025.png")
```

**命名規範**：
- 模型：`[country]_lda_k[N]_[description].pkl`
- 圖表：`[country]_lda_k[N]_[chart_type]_[date].png`
- 報告：`Taiwan_USA_[Topic]_Report.md`

請告訴我您要儲存什麼類型的結果，我將依照規範執行。
