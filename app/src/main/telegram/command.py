from abc import ABC, abstractmethod
from typing import Optional, Any

from telebot import TeleBot
from telebot.types import Message

from main.telegram.repository import Repository
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
