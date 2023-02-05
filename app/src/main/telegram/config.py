import os


class Config:
    @classmethod
    @property
    def token(cls) -> str:
        return os.getenv('TELEGRAM_BOT_TOKEN')

    @classmethod
    @property
    def start_massage(cls) -> str:
        return "Hello !"

    @classmethod
    @property
    def update_message(cls) -> str:
        return "Enter update info"

    @classmethod
    @property
    def update_bookmarks_database_message(cls) -> str:
        return "Input Bookmarks Database id: "
