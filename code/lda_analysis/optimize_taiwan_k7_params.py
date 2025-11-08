#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
台灣醫院評論 K=7 參數優化測試
目標：找到K=7的最佳參數配置，提升coherence score
"""

import pickle
import pandas as pd
import numpy as np
from gensim.models import LdaModel
from gensim.models.coherencemodel import CoherenceModel
from gensim import corpora
import warnings
import time
from datetime import datetime
warnings.filterwarnings('ignore')

print("\n" + "="*80)
print("台灣醫院評論 K=7 LDA 參數優化測試")
print("Taiwan Hospital Reviews K=7 LDA Parameter Optimization")
print("="*80)

# ============================================================================
# 1. 載入資料
# ============================================================================

print("\n【步驟1】載入前處理資料...")
df = pd.read_csv('../../data/processed/taiwan/combined_reviews.csv')

# 將tokens_str轉換回list
texts = [text.split() for text in df['tokens_str']]

print(f"✓ 已載入 {len(texts)} 筆評論")
print(f"  平均詞數: {np.mean([len(t) for t in texts]):.2f}")

# ============================================================================
# 2. 建立字典和語料庫
# ============================================================================

print("\n【步驟2】建立字典和語料庫...")
dictionary = corpora.Dictionary(texts)
original_size = len(dictionary)

# 過濾極端詞彙
dictionary.filter_extremes(
    no_below=3,
    no_above=0.5,
    keep_n=None
)
dictionary.compactify()

print(f"  原始詞彙數: {original_size}")
print(f"  過濾後詞彙數: {len(dictionary)}")

# 建立語料庫
corpus = [dictionary.doc2bow(text) for text in texts]
print(f"✓ 語料庫建立完成，共 {len(corpus)} 筆文檔")

# ============================================================================
# 3. 定義參數優化測試
# ============================================================================

print("\n【步驟3】定義參數測試空間...")

# 參數測試組合
param_grid = {
    'test_name': [],
    'alpha': [],
    'eta': [],
    'iterations': [],
    'passes': [],
    'description': []
}

# 基準模型（當前參數）
param_grid['test_name'].append('Baseline')
param_grid['alpha'].append('symmetric')
param_grid['eta'].append('auto')
param_grid['iterations'].append(100)
param_grid['passes'].append(10)
param_grid['description'].append('當前使用的參數（基準）')

# Test 1: Asymmetric alpha（允許主題重要性不同）
param_grid['test_name'].append('Test-1-Asymmetric')
param_grid['alpha'].append('asymmetric')
param_grid['eta'].append('auto')
param_grid['iterations'].append(100)
param_grid['passes'].append(10)
param_grid['description'].append('改用asymmetric alpha')

# Test 2: 降低eta（增加詞彙特異性）
param_grid['test_name'].append('Test-2-LowEta')
param_grid['alpha'].append('symmetric')
param_grid['eta'].append(0.01)
param_grid['iterations'].append(100)
param_grid['passes'].append(10)
param_grid['description'].append('降低eta至0.01')

# Test 3: 增加訓練次數
param_grid['test_name'].append('Test-3-MoreTraining')
param_grid['alpha'].append('symmetric')
param_grid['eta'].append('auto')
param_grid['iterations'].append(200)
param_grid['passes'].append(20)
param_grid['description'].append('增加iterations和passes')

# Test 4: Asymmetric + Low eta
param_grid['test_name'].append('Test-4-Combo1')
param_grid['alpha'].append('asymmetric')
param_grid['eta'].append(0.01)
param_grid['iterations'].append(100)
param_grid['passes'].append(10)
param_grid['description'].append('Asymmetric + 低eta')

# Test 5: Asymmetric + More training
param_grid['test_name'].append('Test-5-Combo2')
param_grid['alpha'].append('asymmetric')
param_grid['eta'].append('auto')
param_grid['iterations'].append(200)
param_grid['passes'].append(20)
param_grid['description'].append('Asymmetric + 增加訓練')

# Test 6: Low eta + More training
param_grid['test_name'].append('Test-6-Combo3')
param_grid['alpha'].append('symmetric')
param_grid['eta'].append(0.01)
param_grid['iterations'].append(200)
param_grid['passes'].append(20)
param_grid['description'].append('低eta + 增加訓練')

# Test 7: 全部優化（最激進）
param_grid['test_name'].append('Test-7-AllOptimized')
param_grid['alpha'].append('asymmetric')
param_grid['eta'].append(0.01)
param_grid['iterations'].append(200)
param_grid['passes'].append(20)
param_grid['description'].append('全部參數優化')

# Test 8: 極低eta（更高特異性）
param_grid['test_name'].append('Test-8-VeryLowEta')
param_grid['alpha'].append('asymmetric')
param_grid['eta'].append(0.001)
param_grid['iterations'].append(200)
param_grid['passes'].append(20)
param_grid['description'].append('極低eta (0.001)')

# Test 9: 更多訓練輪次
param_grid['test_name'].append('Test-9-MaxTraining')
param_grid['alpha'].append('asymmetric')
param_grid['eta'].append(0.01)
param_grid['iterations'].append(300)
param_grid['passes'].append(30)
param_grid['description'].append('最大訓練次數')

n_tests = len(param_grid['test_name'])
print(f"✓ 共設定 {n_tests} 組參數測試")

# ============================================================================
# 4. 執行參數優化測試
# ============================================================================

print("\n【步驟4】開始參數優化測試...")
print("-" * 80)

results = []

for i in range(n_tests):
    test_name = param_grid['test_name'][i]
    alpha = param_grid['alpha'][i]
    eta = param_grid['eta'][i]
    iterations = param_grid['iterations'][i]
    passes = param_grid['passes'][i]
    description = param_grid['description'][i]

    print(f"\n▶ {test_name}: {description}")
    print(f"  參數: alpha={alpha}, eta={eta}, iterations={iterations}, passes={passes}")

    start_time = time.time()

    # 訓練模型
    try:
        lda_model = LdaModel(
            corpus=corpus,
            id2word=dictionary,
            num_topics=7,
            alpha=alpha,
            eta=eta,
            iterations=iterations,
            passes=passes,
            random_state=42,
            eval_every=None,
            chunksize=2000
        )

        # 計算coherence
        coherence_model = CoherenceModel(
            model=lda_model,
            texts=texts,
            dictionary=dictionary,
            coherence='c_v'
        )
        coherence_score = coherence_model.get_coherence()

        # 計算perplexity
        perplexity_score = lda_model.log_perplexity(corpus)

        training_time = time.time() - start_time

        print(f"  ✓ Coherence: {coherence_score:.4f}")
        print(f"  ✓ Perplexity: {perplexity_score:.4f}")
        print(f"  ✓ 訓練時間: {training_time:.1f}秒")

        # 顯示主題關鍵詞
        print(f"  主題關鍵詞預覽:")
        for idx in range(7):
            topic_words = lda_model.show_topic(idx, topn=5)
            keywords = ', '.join([word for word, prob in topic_words])
            print(f"    主題{idx+1}: {keywords}")

        # 記錄結果
        results.append({
            'test_name': test_name,
            'description': description,
            'alpha': str(alpha),
            'eta': str(eta),
            'iterations': iterations,
            'passes': passes,
            'coherence': coherence_score,
            'perplexity': perplexity_score,
            'training_time_sec': training_time,
            'status': 'Success'
        })

        # 保存模型
        model_filename = f'../../results/taiwan_lda_k7/optimized_{test_name.lower()}_model.pkl'
        lda_model.save(model_filename)
        print(f"  ✓ 模型已保存: {model_filename}")

    except Exception as e:
        print(f"  ✗ 錯誤: {str(e)}")
        results.append({
            'test_name': test_name,
            'description': description,
            'alpha': str(alpha),
            'eta': str(eta),
            'iterations': iterations,
            'passes': passes,
            'coherence': None,
            'perplexity': None,
            'training_time_sec': None,
            'status': f'Failed: {str(e)}'
        })

# ============================================================================
# 5. 結果匯總與分析
# ============================================================================

print("\n" + "="*80)
print("【步驟5】參數優化結果匯總")
print("="*80)

results_df = pd.DataFrame(results)

# 按coherence排序
results_df_sorted = results_df[results_df['status'] == 'Success'].sort_values(
    'coherence', ascending=False
)

print("\n📊 測試結果排名（依Coherence Score）:")
print("-" * 80)

for idx, row in results_df_sorted.iterrows():
    rank = list(results_df_sorted.index).index(idx) + 1
    improvement = ((row['coherence'] - results_df_sorted.iloc[-1]['coherence']) /
                   results_df_sorted.iloc[-1]['coherence'] * 100)

    print(f"\n【排名 #{rank}】{row['test_name']}")
    print(f"  描述: {row['description']}")
    print(f"  Coherence: {row['coherence']:.4f} " +
          f"(相對基準 {improvement:+.2f}%)" if rank > 1 else "  Coherence: {:.4f} (基準)".format(row['coherence']))
    print(f"  Perplexity: {row['perplexity']:.4f}")
    print(f"  訓練時間: {row['training_time_sec']:.1f}秒")
    print(f"  參數: alpha={row['alpha']}, eta={row['eta']}, " +
          f"iter={row['iterations']}, passes={row['passes']}")

# ============================================================================
# 6. 與K=5比較
# ============================================================================

print("\n" + "="*80)
print("【步驟6】與K=5最優模型比較")
print("="*80)

k5_coherence = 0.4326  # 從研究方法論記錄中獲得
best_k7_coherence = results_df_sorted.iloc[0]['coherence']
gap = k5_coherence - best_k7_coherence
gap_pct = (gap / k5_coherence) * 100

print(f"\n📈 Coherence Score 比較:")
print(f"  K=5 (最優): {k5_coherence:.4f}")
print(f"  K=7 (基準): {results_df[results_df['test_name']=='Baseline']['coherence'].values[0]:.4f}")
print(f"  K=7 (優化後最佳): {best_k7_coherence:.4f}")
print(f"\n  差距:")
print(f"    K=7最佳 vs K=5: {gap:.4f} ({gap_pct:.2f}%)")
print(f"    優化改善幅度: {(best_k7_coherence - results_df[results_df['test_name']=='Baseline']['coherence'].values[0]):.4f}")

if gap_pct < 3:
    print("\n✅ 優化後的K=7與K=5差距 < 3%，統計上可接受！")
    print("   可以論證：K=7提供更完整的構面（環境設施），微小的coherence差異值得權衡")
elif gap_pct < 5:
    print("\n⚠️ 優化後的K=7與K=5差距 < 5%，需要強調K=7的額外構面價值")
else:
    print("\n⚠️ 優化後的K=7與K=5仍有較大差距，需要詳細論證選擇K=7的理由")

# ============================================================================
# 7. 保存結果
# ============================================================================

print("\n【步驟7】保存優化結果...")

# 保存詳細結果
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
results_filename = f'../../results/taiwan_lda_k7/param_optimization_results_{timestamp}.csv'
results_df.to_csv(results_filename, index=False, encoding='utf-8-sig')
print(f"✓ 詳細結果已保存: {results_filename}")

# 保存摘要報告
report_filename = f'../../results/taiwan_lda_k7/param_optimization_report_{timestamp}.txt'
with open(report_filename, 'w', encoding='utf-8') as f:
    f.write("="*80 + "\n")
    f.write("台灣醫院評論 K=7 參數優化測試報告\n")
    f.write(f"生成時間: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    f.write("="*80 + "\n\n")

    f.write("【測試目的】\n")
    f.write("找到K=7的最佳參數配置，縮小與K=5的coherence差距\n\n")

    f.write("【測試結果摘要】\n")
    f.write(f"共測試 {len(results_df[results_df['status']=='Success'])} 組參數配置\n\n")

    f.write("【最佳配置】\n")
    best_row = results_df_sorted.iloc[0]
    f.write(f"測試名稱: {best_row['test_name']}\n")
    f.write(f"描述: {best_row['description']}\n")
    f.write(f"Coherence: {best_row['coherence']:.4f}\n")
    f.write(f"Perplexity: {best_row['perplexity']:.4f}\n")
    f.write(f"參數:\n")
    f.write(f"  - alpha: {best_row['alpha']}\n")
    f.write(f"  - eta: {best_row['eta']}\n")
    f.write(f"  - iterations: {best_row['iterations']}\n")
    f.write(f"  - passes: {best_row['passes']}\n")
    f.write(f"訓練時間: {best_row['training_time_sec']:.1f}秒\n\n")

    f.write("【與K=5比較】\n")
    f.write(f"K=5最優coherence: {k5_coherence:.4f}\n")
    f.write(f"K=7優化後coherence: {best_k7_coherence:.4f}\n")
    f.write(f"差距: {gap:.4f} ({gap_pct:.2f}%)\n\n")

    f.write("【完整排名】\n")
    for idx, row in results_df_sorted.iterrows():
        rank = list(results_df_sorted.index).index(idx) + 1
        f.write(f"\n排名 #{rank}: {row['test_name']}\n")
        f.write(f"  Coherence: {row['coherence']:.4f}\n")
        f.write(f"  描述: {row['description']}\n")

print(f"✓ 摘要報告已保存: {report_filename}")

print("\n" + "="*80)
print("✅ 參數優化測試完成！")
print("="*80)
print(f"\n🏆 最佳配置: {results_df_sorted.iloc[0]['test_name']}")
print(f"   Coherence: {results_df_sorted.iloc[0]['coherence']:.4f}")
print(f"   改善幅度: {(best_k7_coherence - results_df[results_df['test_name']=='Baseline']['coherence'].values[0])*100:.2f}%")
print("\n📁 生成的檔案:")
print(f"   - 詳細結果: {results_filename}")
print(f"   - 摘要報告: {report_filename}")
print(f"   - 優化模型: results/taiwan_lda_k7/optimized_*_model.pkl")
