from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List
from main.notion.properties import Property


class Parameter(ABC):
    @property
    @abstractmethod
    def json(self):
        pass


@dataclass
class Parent(Parameter):
    id: str

    @property
    def json(self):
        return {
            "parent": {
                "database_id": self.id
            }
        }


@dataclass
class Properties(Parameter):
    properties: List[Property]

    @property
    def json(self):
        json = {
            "properties": {}
        }

        for _ in self.properties:
            json["properties"].update(_.json)

        return json


@dataclass
class Cover(Parameter):
    cover_link: str

    @property
    def json(self):
        return {
            "cover": {
                "type": "external",
                "external": {
                    "url": self.cover_link
                }
            }
        }
