import datetime


def run_app():
    """
    アプリケーションのメイン関数。処理は以下２つ。
    1. ユーザー名を尋ねる
    2. ユーザーに占い結果を表示する
    """

    while True:
        print("お名前を教えてください")
        input_user_name = input(">>> ")
        user_name = input_user_name.strip()

        if not user_name:
            print("名前は1文字以上で入力してください")
            continue

        break

    today = datetime.date.today()
    print(f"{user_name}さんの{today.year}年{today.month}月{today.day}日の運勢は…")
