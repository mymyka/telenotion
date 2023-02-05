import os


class Config:
    @classmethod
    @property
    def token(cls):
        return os.getenv('NOTION_TOKEN')
