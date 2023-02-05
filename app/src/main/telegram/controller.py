from main.telegram.bot import Bot
from main.telegram.command import *


class Controller:
    @staticmethod
    @Bot.bot.message_handler(commands=['start'])
    def start(message):
        Bot.execute_command_to_message(StartCommand, message)

    @staticmethod
    @Bot.bot.message_handler(commands=['update_bookmarks'])
    def update_bookmarks(message):
        Bot.execute_command_to_message(UpdateBookmarkDatabaseCommand, message)
