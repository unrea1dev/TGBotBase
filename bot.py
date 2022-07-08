from aiogram import Dispatcher, Bot
from core import config

bot = Bot(token = config.bot.token, parse_mode = 'HTML')
dispatcher = Dispatcher(bot = bot)

from handlers.user import functions as user
user.install(_dispatcher = dispatcher)