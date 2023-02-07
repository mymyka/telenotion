from properties import Property
from dataclasses import dataclass
from typing import List, Dict


@dataclass
class Page:
    parent: str
    properties: List[Property]

    @property
    def json(self):
        json = {
            "parent": {},
            "properties": {}
        }

        json.update({"database_id": self.parent})
        for _ in self.properties:
            json["properties"].update(_)

        return json
