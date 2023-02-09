from main.telegram.bot import Bot
from main.telegram.command import *


class Controller:
    @staticmethod
    @Bot.bot.message_handler(commands=['start'])
    def start(message):
        Bot.execute_command_to_message(StartCommand, message)
        Bot.execute_command_to_message(SendDefaultReplayKeyboardMarkup, message)

    @staticmethod
    @Bot.bot.message_handler(content_types=['text'], regexp='⚙️🔖 Update bookmark database')
    def update_bookmarks(message):
        Bot.execute_command_to_message(UpdateBookmarkDatabaseCommand, message)

    @staticmethod
    @Bot.bot.message_handler(content_types=['text'], regexp='🔖 Create bookmark')
    def create_bookmark(message):
        Bot.execute_command_to_message(CreateBookmarkCommand, message)
