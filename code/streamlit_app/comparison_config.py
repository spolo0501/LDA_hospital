"""
台美醫院評論比較分析 - 配置檔案
Taiwan-USA Hospital Review Comparison - Configuration
"""

from pathlib import Path

# ============================================
# 路徑配置 (Path Configuration)
# ============================================

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# 台灣資料路徑
TAIWAN_MODEL_PATH = BASE_DIR / "results/taiwan_lda_k7/lda_k7_lda_model.pkl"
TAIWAN_DATA_PATH = BASE_DIR / "data/raw/taiwan"

# 美國資料路徑
USA_MODEL_PATH = BASE_DIR / "results/usa_lda_k7/usa_gensim_lda_k6_model.pkl"
USA_DATA_PATH = BASE_DIR / "results/usa_lda_k7/usa_k6_topic_analysis_20251107_122236.csv"

# ============================================
# 台灣主題標籤 (Taiwan Topic Labels) - K=7
# ============================================

TAIWAN_TOPICS = {
    0: {
        "label_zh": "醫療專業認可",
        "label_en": "Medical Professional Recognition",
        "emoji": "T0",
        "sentiment": "positive",
        "keywords": ["醫師", "護理師", "專業", "感謝", "謝謝", "親切", "耐心"],
        "description": "病患對醫護人員專業能力與態度的肯定"
    },
    1: {
        "label_zh": "就診流程與等候",
        "label_en": "Process & Waiting Time",
        "emoji": "T1",
        "sentiment": "negative",
        "keywords": ["時間", "報到", "看診", "掛號", "預約", "等待"],
        "description": "掛號、報到、看診流程與等候時間問題"
    },
    2: {
        "label_zh": "服務態度問題",
        "label_en": "Service Attitude Issues",
        "emoji": "T2",
        "sentiment": "negative",
        "keywords": ["態度", "病人", "護理師", "不是", "服務"],
        "description": "醫護人員與行政人員的服務態度不佳"
    },
    3: {
        "label_zh": "設施與便利性",
        "label_en": "Facility & Convenience",
        "emoji": "T3",
        "sentiment": "neutral",
        "keywords": ["停車場", "方便", "電梯", "動線", "流程"],
        "description": "醫院設施、停車、動線等便利性議題"
    },
    4: {
        "label_zh": "手術治療成功",
        "label_en": "Surgical Success",
        "emoji": "T4",
        "sentiment": "positive",
        "keywords": ["手術", "開刀", "外科", "骨科", "成功"],
        "description": "手術治療成功的正面回饋"
    },
    5: {
        "label_zh": "住院照護品質",
        "label_en": "Inpatient Care",
        "emoji": "T5",
        "sentiment": "neutral",
        "keywords": ["病房", "住院", "家屬", "護理", "出院"],
        "description": "住院期間的照護品質與家屬互動"
    },
    6: {
        "label_zh": "急診與溝通",
        "label_en": "Emergency & Communication",
        "emoji": "T6",
        "sentiment": "negative",
        "keywords": ["急診", "醫生", "知道", "問題", "檢查"],
        "description": "急診服務與醫病溝通問題"
    }
}

# ============================================
# 美國主題標籤 (USA Topic Labels) - K=6
# ============================================

USA_TOPICS = {
    0: {
        "label_zh": "重症與生命照護",
        "label_en": "Critical & Life Care",
        "emoji": "U0",
        "sentiment": "neutral",
        "keywords": ["care", "dad", "life", "patient", "surgery", "pain"],
        "description": "重症照護、生命關懷相關評論"
    },
    1: {
        "label_zh": "急診等候時間",
        "label_en": "ER Waiting Time",
        "emoji": "U1",
        "sentiment": "negative",
        "keywords": ["room", "hour", "waiting", "emergency", "time"],
        "description": "急診室長時間等候的負面評論"
    },
    2: {
        "label_zh": "門診與疼痛管理",
        "label_en": "Clinic & Pain Management",
        "emoji": "U2",
        "sentiment": "negative",
        "keywords": ["clinic", "care", "pain", "doctor", "help"],
        "description": "門診服務與疼痛管理不佳"
    },
    3: {
        "label_zh": "護理照護品質",
        "label_en": "Nursing Care Quality",
        "emoji": "U3",
        "sentiment": "negative",
        "keywords": ["nurse", "patient", "care", "room", "hour"],
        "description": "護理人員照護品質相關評論"
    },
    4: {
        "label_zh": "整體正面評價",
        "label_en": "Overall Positive Feedback",
        "emoji": "U4",
        "sentiment": "positive",
        "keywords": ["great", "thank", "staff", "amazing", "excellent"],
        "description": "對醫療團隊的整體正面評價"
    },
    5: {
        "label_zh": "預約與帳單問題",
        "label_en": "Appointment & Billing",
        "emoji": "U5",
        "sentiment": "negative",
        "keywords": ["appointment", "bill", "billing", "insurance", "service"],
        "description": "預約系統與醫療帳單問題"
    }
}

# ============================================
# 主題對應關係 (Topic Mapping)
# ============================================
# 相似度: ★★★★★ (非常相似) 到 ★☆☆☆☆ (不相似)

TOPIC_MAPPING = [
    {
        "taiwan_topic": 0,  # 醫療專業認可
        "usa_topic": 4,     # 整體正面評價
        "similarity": 5,    # ★★★★★
        "common_features": "兩者都是最主要的正面評價，強調醫護人員專業與感謝"
    },
    {
        "taiwan_topic": 1,  # 就診流程與等候
        "usa_topic": 1,     # 急診等候時間
        "similarity": 4,    # ★★★★☆
        "common_features": "都關注等候時間問題，美國更強調急診室的長時間等待"
    },
    {
        "taiwan_topic": 4,  # 手術治療成功
        "usa_topic": 0,     # 重症與生命照護
        "similarity": 3,    # ★★★☆☆
        "common_features": "都涉及重要醫療程序，台灣聚焦手術，美國強調生命照護"
    },
    {
        "taiwan_topic": 5,  # 住院照護品質
        "usa_topic": 3,     # 護理照護品質
        "similarity": 3,    # ★★★☆☆
        "common_features": "都涉及住院期間的護理照護品質"
    },
    {
        "taiwan_topic": 2,  # 服務態度問題 (台灣獨有)
        "usa_topic": None,
        "similarity": 0,
        "common_features": "台灣特有：對服務態度特別敏感，佔17.3%評論"
    },
    {
        "taiwan_topic": 6,  # 急診與溝通
        "usa_topic": 2,     # 門診與疼痛管理
        "similarity": 2,    # ★★☆☆☆
        "common_features": "都涉及溝通問題，美國更強調疼痛管理"
    },
    {
        "taiwan_topic": None,
        "usa_topic": 5,     # 預約與帳單問題 (美國獨有)
        "similarity": 0,
        "common_features": "美國特有：醫療帳單與保險問題，佔4.1%評論"
    }
]

# ============================================
# 視覺化配色 (Color Schemes)
# ============================================

COLORS = {
    "taiwan": {
        "primary": "#1f77b4",      # 藍色
        "light": "#aec7e8",
        "dark": "#0d3d62"
    },
    "usa": {
        "primary": "#d62728",      # 紅色
        "light": "#ff9896",
        "dark": "#8b0000"
    },
    "sentiment": {
        "positive": "#2ecc71",     # 綠色
        "neutral": "#f39c12",      # 橘色
        "negative": "#e74c3c"      # 紅色
    }
}

# ============================================
# 統計資訊 (Statistics)
# ============================================

DATASET_INFO = {
    "taiwan": {
        "reviews": 5007,
        "hospitals": 26,
        "topics": 7,
        "coherence": 0.4175,
        "perplexity": -7.5039,
        "model_name": "K=7 LDA Model",
        "language": "繁體中文"
    },
    "usa": {
        "reviews": 3240,
        "hospitals": "Multiple",  # 需要確認
        "topics": 6,
        "coherence": 0.4029,
        "perplexity": -7.2254,
        "model_name": "K=6 LDA Model",
        "language": "English"
    }
}

# ============================================
# 文化差異重點 (Cultural Highlights)
# ============================================

CULTURAL_INSIGHTS = {
    "taiwan_unique": [
        {
            "insight": "服務態度高度敏感",
            "topic": 2,
            "percentage": 17.3,
            "description": "台灣病患對醫護人員「態度」特別敏感，形成獨立主題"
        },
        {
            "insight": "設施便利性重視",
            "topic": 3,
            "percentage": 10.2,
            "description": "停車、電梯、動線等便利性議題明顯"
        }
    ],
    "usa_unique": [
        {
            "insight": "帳單保險問題突出",
            "topic": 5,
            "percentage": 4.1,
            "description": "醫療帳單與保險議題在美國形成獨立主題"
        },
        {
            "insight": "疼痛管理關注",
            "topic": 2,
            "percentage": 14.7,
            "description": "疼痛管理(pain management)是美國獨特關注點"
        }
    ],
    "common": [
        {
            "insight": "正面評價為主導",
            "taiwan_topic": 0,
            "usa_topic": 4,
            "description": "兩國都有佔最大比例的正面評價主題"
        },
        {
            "insight": "等候時間普遍不滿",
            "taiwan_topic": 1,
            "usa_topic": 1,
            "description": "等候時間問題在兩國都形成顯著負面主題"
        }
    ]
}

# ============================================
# Streamlit 頁面配置
# ============================================

PAGE_CONFIG = {
    "page_title": "Taiwan-USA Hospital Review Comparison",
    "page_icon": "🌏",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}

SIDEBAR_INFO = """
## 📊 資料集資訊

### 🇹🇼 台灣
- 評論數：5,007 則
- 醫院數：26 家醫療中心
- 主題數：K=7
- Coherence：0.4175

### 🇺🇸 美國
- 評論數：3,240 則
- 主題數：K=6
- Coherence：0.4029

---

## 🔍 分析方法
使用 Gensim LDA 主題模型進行跨文化比較分析
"""
