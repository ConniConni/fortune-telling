from uranai import main
from uranai import logger_config


if __name__ == "__main__":
    # ログの設定を行う
    logger_config.setup_logging()
    # アプリケーションを実行する
    main.run_app()
