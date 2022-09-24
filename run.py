from aiogram import executor
from loader import dispatcher, config
import handlers, database

from utils import logging

async def on_startup(_) -> None:
    await database.create_connection(database = config.database.database)

async def on_shutdown(_) -> None:
    await database.close_connection()

if __name__ == '__main__':
    logging.create_logging(path = config.logs.path)
    executor.start_polling(dispatcher = dispatcher, skip_updates = True, on_startup = on_startup, on_shutdown = on_shutdown)