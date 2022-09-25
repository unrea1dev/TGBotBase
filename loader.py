from aiogram import Dispatcher, Bot
from aiogram.utils.executor import Executor

from core import config

bot = Bot(token = config.bot.token, parse_mode = 'HTML')
dispatcher = Dispatcher(bot = bot)

executor = Executor(dispatcher = dispatcher, skip_updates = True)