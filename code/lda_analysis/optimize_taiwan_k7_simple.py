#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
台灣醫院評論 K=7 參數優化測試 - 簡化穩定版
測試5組最關鍵的參數配置
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
import os

warnings.filterwarnings('ignore')
os.environ['OMP_NUM_THREADS'] = '1'  # 限制OpenMP線程

def train_single_model(config, corpus, dictionary, texts):
    """訓練單個LDA模型並評估"""
    test_name = config['name']
    alpha = config['alpha']
    eta = config['eta']
    iterations = config['iter']
    passes = config['passes']
    description = config['desc']

    print(f"\n▶ {test_name}: {description}")
    print(f"  參數: alpha={alpha}, eta={eta}, iterations={iterations}, passes={passes}")

    start_time = time.time()

    try:
        # 訓練模型
        lda_model = LdaModel(
            corpus=corpus,
            id2word=dictionary,
            num_topics=7,
            alpha=alpha,
            eta=eta,
            iterations=iterations,
            passes=passes,
            random_state=42,
            per_word_topics=False
        )

        # 計算coherence（單進程）
        coherence_model = CoherenceModel(
            model=lda_model,
            texts=texts,
            dictionary=dictionary,
            coherence='c_v',
            processes=1
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
        for idx in range(min(3, 7)):  # 只顯示前3個主題
            topic_words = lda_model.show_topic(idx, topn=5)
            keywords = ', '.join([word for word, prob in topic_words])
            print(f"    主題{idx+1}: {keywords}")

        return {
            'test_name': test_name,
            'description': description,
            'alpha': str(alpha),
            'eta': str(eta),
            'iterations': iterations,
            'passes': passes,
            'coherence': coherence_score,
            'perplexity': perplexity_score,
            'training_time_sec': training_time,
            'status': 'Success',
            'model': lda_model
        }

    except Exception as e:
        print(f"  ✗ 錯誤: {str(e)}")
        return {
            'test_name': test_name,
            'description': description,
            'alpha': str(alpha),
            'eta': str(eta),
            'iterations': iterations,
            'passes': passes,
            'coherence': None,
            'perplexity': None,
            'training_time_sec': None,
            'status': f'Failed: {str(e)}',
            'model': None
        }

def main():
    print("\n" + "="*80)
    print("台灣醫院評論 K=7 LDA 參數優化測試 - 簡化版")
    print("Taiwan Hospital Reviews K=7 LDA Parameter Optimization")
    print("="*80)

    # ========================================================================
    # 1. 載入資料
    # ========================================================================
    print("\n【步驟1】載入前處理資料...")
    with open('../../data/processed/taiwan/reviews_for_lda.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    texts = [line.strip().split() for line in lines if line.strip()]
    print(f"✓ 已載入 {len(texts)} 筆評論")

    # ========================================================================
    # 2. 建立字典和語料庫
    # ========================================================================
    print("\n【步驟2】建立字典和語料庫...")
    dictionary = corpora.Dictionary(texts)
    dictionary.filter_extremes(no_below=3, no_above=0.5, keep_n=None)
    dictionary.compactify()
    corpus = [dictionary.doc2bow(text) for text in texts]
    print(f"✓ 語料庫建立完成: {len(dictionary)} 詞彙, {len(corpus)} 文檔")

    # ========================================================================
    # 3. 定義測試配置（只測試5組最關鍵的）
    # ========================================================================
    print("\n【步驟3】定義5組關鍵參數測試...")
    test_configs = [
        {'name': 'Baseline', 'alpha': 'symmetric', 'eta': 'auto', 'iter': 100, 'passes': 10,
         'desc': '當前參數（基準）'},
        {'name': 'Test-1-Asymmetric', 'alpha': 'asymmetric', 'eta': 'auto', 'iter': 100, 'passes': 10,
         'desc': 'Asymmetric alpha'},
        {'name': 'Test-2-LowEta', 'alpha': 'symmetric', 'eta': 0.01, 'iter': 100, 'passes': 10,
         'desc': '低eta (0.01)'},
        {'name': 'Test-3-Combo', 'alpha': 'asymmetric', 'eta': 0.01, 'iter': 100, 'passes': 10,
         'desc': 'Asymmetric + 低eta'},
        {'name': 'Test-4-AllOpt', 'alpha': 'asymmetric', 'eta': 0.01, 'iter': 150, 'passes': 15,
         'desc': '全面優化'},
    ]

    # ========================================================================
    # 4. 執行測試
    # ========================================================================
    print("\n【步驟4】開始參數優化測試...")
    print("-" * 80)

    results = []
    for config in test_configs:
        result = train_single_model(config, corpus, dictionary, texts)
        results.append(result)
        # 保存成功的模型
        if result['status'] == 'Success' and result['model'] is not None:
            model_path = f"../../results/taiwan_lda_k7/optimized_{result['test_name'].lower()}_model.pkl"
            result['model'].save(model_path)
            print(f"  ✓ 模型已保存: {model_path}")
        # 從結果中移除模型對象（避免序列化問題）
        result.pop('model', None)

    # ========================================================================
    # 5. 結果分析
    # ========================================================================
    print("\n" + "="*80)
    print("【步驟5】參數優化結果匯總")
    print("="*80)

    results_df = pd.DataFrame(results)
    successful = results_df[results_df['status'] == 'Success'].copy()

    if len(successful) == 0:
        print("\n❌ 所有測試都失敗了")
        return

    successful_sorted = successful.sort_values('coherence', ascending=False)
    baseline_coh = successful[successful['test_name']=='Baseline']['coherence'].values[0]

    print("\n📊 測試結果排名:")
    print("-" * 80)
    for idx, row in successful_sorted.iterrows():
        rank = list(successful_sorted.index).index(idx) + 1
        improvement = ((row['coherence'] - baseline_coh) / baseline_coh * 100)
        print(f"\n【#{rank}】{row['test_name']}")
        print(f"  Coherence: {row['coherence']:.4f} (相對基準 {improvement:+.2f}%)")
        print(f"  Perplexity: {row['perplexity']:.4f}")
        print(f"  時間: {row['training_time_sec']:.1f}秒")

    # ========================================================================
    # 6. 與K=5比較
    # ========================================================================
    print("\n" + "="*80)
    print("【步驟6】與K=5比較")
    print("="*80)

    k5_coh = 0.4326
    best_k7_coh = successful_sorted.iloc[0]['coherence']
    gap = k5_coh - best_k7_coh
    gap_pct = (gap / k5_coh) * 100

    print(f"\nK=5最優: {k5_coh:.4f}")
    print(f"K=7基準: {baseline_coh:.4f}")
    print(f"K=7優化: {best_k7_coh:.4f}")
    print(f"\n差距: {gap:.4f} ({gap_pct:.2f}%)")
    print(f"改善: {(best_k7_coh - baseline_coh):.4f} ({(best_k7_coh - baseline_coh)/baseline_coh*100:+.2f}%)")

    if gap_pct < 3:
        print("\n✅ 差距 < 3%，統計上可接受！")
    elif gap_pct < 5:
        print("\n⚠️ 差距 < 5%，需強調K=7額外價值")
    else:
        print("\n⚠️ 差距較大，需詳細論證")

    # ========================================================================
    # 7. 保存結果
    # ========================================================================
    print("\n【步驟7】保存結果...")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    csv_file = f'../../results/taiwan_lda_k7/param_optimization_results_{timestamp}.csv'
    results_df.to_csv(csv_file, index=False, encoding='utf-8-sig')
    print(f"✓ 已保存: {csv_file}")

    print("\n" + "="*80)
    print("✅ 優化完成！")
    print("="*80)
    print(f"\n🏆 最佳: {successful_sorted.iloc[0]['test_name']}")
    print(f"   Coherence: {successful_sorted.iloc[0]['coherence']:.4f}")

if __name__ == '__main__':
    main()
