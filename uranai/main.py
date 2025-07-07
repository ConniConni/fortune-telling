import datetime


def run_app():
    """アプリケーションのメイン関数"""
    today = datetime.date.today()
    print(f"あなたの{today.year}年{today.month}月{today.day}日の運勢は…")
