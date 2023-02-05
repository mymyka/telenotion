from dataclasses import dataclass
from typing import List


@dataclass
class Bookmark:
    cover: str
    favicon: str
    title: str
    link: str
    tags: List[str]
