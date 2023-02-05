from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict


@dataclass
class User:
    id: str
    bookmarks_database_id: str


class Repository(ABC):
    @abstractmethod
    def get_user(self, user_id: str) -> User:
        pass

    @abstractmethod
    def update_user(self, user: User):
        pass


class RAMRepository(Repository):
    __instance: Repository = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self):
        self._dictionary: Dict[str, Dict[str, str]] = {}

    def get_user(self, user_id: str) -> User:
        return User(
            id=user_id,
            bookmarks_database_id=self._dictionary[user_id]['bookmarks_database_id']
        )

    def update_user(self, user: User):
        self._dictionary.update({
            user.id: {
                'bookmarks_database_id': user.bookmarks_database_id
            }
        })
