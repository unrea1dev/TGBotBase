from aiogram import Dispatcher
from loader import executor, config
import handlers, database

from misc.misc import setup_misc
from misc.logs import initialize_logging

async def on_startup(dispatcher : Dispatcher) -> None:
    await database.create_connection(
        url = config.database.database,
        timezone = config.database.timezone
    )

    await setup_misc(dispatcher = dispatcher)

async def on_shutdown(dispatcher : Dispatcher) -> None:
    await database.close_connection()

if __name__ == '__main__':
    initialize_logging(path = config.logging.path)

    executor.on_startup(on_startup)
    executor.on_shutdown(on_shutdown)

    executor.start_polling()
