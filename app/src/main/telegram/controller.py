from main.telegram.bot import Bot
from main.telegram.command import *


class Controller:
    @staticmethod
    @Bot.bot.message_handler(commands=['start'])
    def start(message):
        Bot.execute_command_to_message(StartCommand, message)
