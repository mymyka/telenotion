from main.notion.parameters import Parameter
from dataclasses import dataclass
from typing import List


@dataclass
class Page:
    parameters: List[Parameter]

    @property
    def json(self):
        json = {}

        for _ in self.parameters:
            json.update(_.json)

        return json
