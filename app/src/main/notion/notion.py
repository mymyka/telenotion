import json
import requests

from main.notion.config import Config
from main.notion.page import Page


class Notion:
    __headers = {
        "Authorization": "Bearer " + Config.token,
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }
    __createUrl = 'https://api.notion.com/v1/pages'

    @classmethod
    def create_page(cls, page: Page) -> None:
        data = json.dumps(page.json)
        requests.request("POST",
                         cls.__createUrl,
                         headers=cls.__headers,
                         data=data)
