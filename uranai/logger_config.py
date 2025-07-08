import logging


def setup_logging():
    """ロギングを設定する関数"""

    # ロガーを取得する
    logger = logging.getLogger()

    # ログレベルを設定する
    logger.setLevel(logging.INFO)

    # ログのフォーマットを定義
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        "%Y-%m-%d %H:%M:%S",  # タイムスタンプの書式
    )

    # ハンドラを設定する
    file_handler = logging.FileHandler("fortune_telling_log.txt", encoding="utf-8")
    file_handler.setFormatter(formatter)

    # ロガーにハンドラを追加する
    if not logger.handlers:
        logger.addHandler(file_handler)
