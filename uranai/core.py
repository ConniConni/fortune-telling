import random


FORTUNES = ["大吉", "中吉", "吉", "小吉", "末吉", "凶"]
LUCKY_COLORS = ["赤", "青", "緑", "紫", "黄", "橙", "白", "黒"]
ADVICES = [
    "挨拶をしよう!",
    "感謝の気持ちを伝えよう！",
    "慎重になろう！",
    "チャレンジしよう！",
]


def generate_fortune_telling():
    """占い結果のデータを辞書型で生成して返す関数"""

    result_dict = {
        "今日の運勢": random.choice(FORTUNES),
        "ラッキーナンバー": random.randint(1, 9),
        "ラッキーカラー": random.choice(LUCKY_COLORS),
        "一言アドバイス": random.choice(ADVICES),
    }

    return result_dict
