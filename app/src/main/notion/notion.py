import json
import requests

from main.notion.config import Config


class Notion:
    __headers = {
        "Authorization": "Bearer " + Config.token,
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }
    __createUrl = 'https://api.notion.com/v1/pages'

    @classmethod
    def create_bookmark(cls, bookmark_database_id: str, link: str) -> None:
        newPageData = {
            "parent": {"database_id": bookmark_database_id},
            "properties": {
                "Tags": {
                    "id": "Nq%5Cy",
                    "type": "multi_select",
                    "multi_select": [
                        {
                            "name": "meta"
                        }
                    ]
                },
                "Name": {
                    "id": "title",
                    "type": "title",
                    "title": [
                        {
                            "type": "text",
                            "text": {
                                "content": link,
                            },
                            "annotations": {
                                "bold": False,
                                "italic": False,
                                "strikethrough": False,
                                "underline": False,
                                "code": False,
                                "color": "default"
                            },
                            "plain_text": link,

                        }
                    ]
                },
            }
        }
        data = json.dumps(newPageData)

        res = requests.request("POST", cls.__createUrl, headers=cls.__headers, data=data)