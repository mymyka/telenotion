from typing import List, Optional
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Property(ABC):
    @property
    @abstractmethod
    def json(self) -> dict:
        pass


@dataclass
class Tags(Property):
    tag_list: List[str]

    @property
    def json(self) -> dict:
        json = {
            "Tags": {
                "type": "multi_select",
                "multi_select": []
            }
        }
        for tag in self.tag_list:
            json["Tags"]["multi_select"].append({"name": tag})

        return json


@dataclass
class Title(Property):
    title: str

    @property
    def json(self) -> dict:
        return {
            "Title": {
                "type": "title",
                "title": [
                    {
                        "type": "text",
                        "text": {
                            "content": self.title,
                        }
                    }
                ]
            }
        }


@dataclass
class Link(Property):
    link: str

    @property
    def json(self) -> dict:
        return {
            "Link": {
                "type": "url",
                "url": self.link
            }
        }
