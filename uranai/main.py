import datetime
import logging

from .core import generate_fortune_telling


# mainモジュールのロガーを取得する
logger = logging.getLogger(__name__)


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


def show_fortune_result(result_dict):
    """占い結果を表示する関数"""

    print("#################################")
    for key, value in result_dict.items():
        print(f"・{key}: {value}")
    print("#################################")


def run_app():
    """アプリケーションのメイン関数"""

    logger.info("アプリケーションを開始")

    # ユーザー名を取得
    user_name = get_user_name()

    # 今日の日付を取得
    today = datetime.date.today()
    today_str = today.strftime("%Y年%m月%d日")

    # ユーザーに占い結果を表示
    print(f"{user_name}さんの{today_str}の運勢は…")
    # 占い結果を取得
    result_dict = generate_fortune_telling()
    # 占い結果を表示
    show_fortune_result(result_dict)
    logger.info(f"{user_name}さんの{today_str}の運勢は{result_dict}。")

    logger.info("アプリケーションを終了")
