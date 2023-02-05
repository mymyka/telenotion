from abc import ABC, abstractmethod
from typing import Optional, Any

from telebot import TeleBot
from telebot.types import Message

from main.telegram.repository import Repository, User
from main.telegram.config import Config


class Command(ABC):
    def __init__(self,
                 bot: Optional[TeleBot] = None,
                 message: Optional[Message] = None,
                 repository: Optional[Repository] = None):
        self._bot = bot
        self._message = message
        self._repository = repository

    @abstractmethod
    def execute(self) -> Any:
        pass


class StartCommand(Command):
    def execute(self) -> Any:
        self._bot.reply_to(self._message, Config.start_massage)


class UpdateBookmarkDatabaseCommand(Command):
    def execute(self) -> Any:
        self.__request_user_input()
        self._bot.register_next_step_handler_by_chat_id(self._message.chat.id,
                                                        self.__update_bookmark_database_id)

    def __update_bookmark_database_id(self, message):
        user: User = User(str(message.from_user.id),
                          self.__extract_database_id_from_link(message.text))
        self._repository.update_user(user)

    def __request_user_input(self):
        self._bot.reply_to(self._message,
                           Config.update_bookmarks_database_message)

    @staticmethod
    def __extract_database_id_from_link(link: str) -> str:
        return link.split('?v=')[0].split('/')[-1]
