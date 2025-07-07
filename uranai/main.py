import datetime

from .core import get_fortune_telling


def get_user_name():
    """有効なユーザー名を取得する関数"""

    while True:
        print("お名前を教えてください")
        input_user_name = input(">>> ")
        user_name = input_user_name.strip()

        if user_name:
            return user_name

        else:
            print("名前は1文字以上で入力してください")


def run_app():
    """アプリケーションのメイン関数"""
    user_name = get_user_name()
    today = datetime.date.today()
    print(f"{user_name}さんの{today.year}年{today.month}月{today.day}日の運勢は…")
    get_fortune_telling()
