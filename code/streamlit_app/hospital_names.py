#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
醫院中英文名稱對照表
Hospital Name Mapping (English abbreviation to Chinese full name)
"""

HOSPITAL_NAMES = {
    # 北部醫學中心
    "NTUH": "國立臺灣大學醫學院附設醫院",
    "TVGH": "臺北榮民總醫院",
    "TSGH": "三軍總醫院",
    "Cathay": "國泰綜合醫院",
    "FEMH": "亞東紀念醫院",
    "SKH": "新光醫療財團法人新光吳火獅紀念醫院",
    "WanFang": "臺北市立萬芳醫院（委託臺北醫學大學辦理）",
    "MacKay": "臺灣基督長老教會馬偕醫療財團法人台北馬偕紀念醫院（含淡水）",
    "MacKay_Tamsui": "淡水馬偕紀念醫院",
    "ShuangHo": "衛生福利部雙和醫院（委託臺北醫學大學興建經營）",
    "TPECH": "佛教慈濟醫療財團法人台北慈濟醫院",
    "CGMH_Taipei": "長庚醫療財團法人台北長庚紀念醫院",
    "CGMH": "長庚醫療財團法人林口長庚紀念醫院(含台北長庚）",

    # 新竹
    "NTUH_Hsinchu": "國立臺灣大學醫學院附設醫院新竹臺大分院",

    # 中部醫學中心
    "CMUH": "中國醫藥大學附設醫院",
    "TCVGH": "臺中榮民總醫院",
    "CSMU": "中山醫學大學附設醫院",
    "CCH": "彰化基督教醫療財團法人彰化基督教醫院",
    "CHIMEI": "奇美醫療財團法人奇美醫院（含樹林院區精神科）",
    "CHIMEI_Liouying": "奇美醫療財團法人奇美醫院樹林院區",

    # 南部醫學中心
    "NCKUH": "國立成功大學醫學院附設醫院",
    "KSVGH": "高雄榮民總醫院",
    "KMUH": "高雄醫學大學附設中和紀念醫院",
    "CGMH_Kaohsiung": "長庚醫療財團法人高雄長庚紀念醫院",
    "EDH": "義大醫療財團法人義大醫院",

    # 東部
    "BTCH": "佛教慈濟醫療財團法人花蓮慈濟醫院",
}

# 簡短顯示名稱（用於圖表標籤）
HOSPITAL_SHORT_NAMES = {
    "NTUH": "台大醫院",
    "TVGH": "台北榮總",
    "TSGH": "三總",
    "Cathay": "國泰醫院",
    "FEMH": "亞東醫院",
    "SKH": "新光醫院",
    "WanFang": "萬芳醫院",
    "MacKay": "馬偕醫院",
    "MacKay_Tamsui": "淡水馬偕",
    "ShuangHo": "雙和醫院",
    "TPECH": "台北慈濟",
    "CGMH_Taipei": "台北長庚",
    "CGMH": "林口長庚",
    "NTUH_Hsinchu": "新竹台大",
    "CMUH": "中國附醫",
    "TCVGH": "台中榮總",
    "CSMU": "中山附醫",
    "CCH": "彰基",
    "CHIMEI": "奇美醫院",
    "CHIMEI_Liouying": "奇美樹林",
    "NCKUH": "成大醫院",
    "KSVGH": "高雄榮總",
    "KMUH": "高醫附醫",
    "CGMH_Kaohsiung": "高雄長庚",
    "EDH": "義大醫院",
    "BTCH": "花蓮慈濟",
}

def get_hospital_name(abbr, use_short=False):
    """
    取得醫院中文名稱

    Parameters:
    -----------
    abbr : str
        醫院英文縮寫
    use_short : bool
        是否使用簡短名稱（適用於圖表）

    Returns:
    --------
    str : 醫院中文名稱
    """
    if use_short:
        return HOSPITAL_SHORT_NAMES.get(abbr, abbr)
    return HOSPITAL_NAMES.get(abbr, abbr)
