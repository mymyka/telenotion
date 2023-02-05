from typing import Type

from telebot import TeleBot
from telebot.types import Message

from main.telegram.config import Config
from main.telegram.command import Command
from main.telegram.repository import Repository


class Bot:
    bot: TeleBot = TeleBot(Config.token)
    repository: Repository = Repository()

    @classmethod
    def execute_command_to_message(cls,
                                   command_type: Type[Command],
                                   message: Message):
        command = command_type(cls.bot, message, cls.repository)
        command.execute()
