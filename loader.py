from aiogram import Dispatcher, Bot
from aiogram.utils.executor import Executor

from core import config
from misc.misc import on_startup, on_shutdown

bot = Bot(token = config.bot.token, parse_mode = 'HTML')
dispatcher = Dispatcher(bot = bot)

executor = Executor(dispatcher = dispatcher, skip_updates = True)
executor.on_startup(on_startup)
executor.on_shutdown(on_shutdown)