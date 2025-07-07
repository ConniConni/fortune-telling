import random


FORTUNES = ["大吉", "中吉", "吉", "小吉", "末吉", "凶"]
LUCKY_COLORS = ["赤", "青", "緑", "紫", "黄", "橙", "白", "黒"]
ADVICES = [
    "挨拶をしよう!",
    "感謝の気持ちを伝えよう！",
    "慎重になろう！",
    "チャレンジしよう！",
]
RESULT_KEY = ["今日の運勢", "ラッキーカラー", "ラッキーナンバー", "一言アドバイス"]


def deco(func):
    """占い結果を強調するデコレータ関数"""

    def wrapper():
        print("#################################")
        func()
        print("#################################")

    return wrapper


@deco
def get_fortune_telling():
    """
    占い結果を取得する関数
    リストからランダムに取得し、占い結果全体を辞書型にする
    """

    result = {}

    choice_fortune = random.choice(FORTUNES)
    result[RESULT_KEY[0]] = choice_fortune
    choice_lucky_number = random.randint(1, 9)
    result[RESULT_KEY[1]] = choice_lucky_number
    choice_lucky_color = random.choice(LUCKY_COLORS)
    result[RESULT_KEY[2]] = choice_lucky_color
    choice_advice = random.choice(ADVICES)
    result[RESULT_KEY[3]] = choice_advice

    for dict in result.items():
        print(f"{dict[0]}: {dict[1]}")
