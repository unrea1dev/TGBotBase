from aiogram import Dispatcher

from core import config
import database

async def setup_misc(dispatcher : Dispatcher) -> None:
    pass

async def on_startup(dispatcher : Dispatcher) -> None:
    await database.create_connection(
        url = config.database.database,
        timezone = config.database.timezone
    )

    await setup_misc(dispatcher = dispatcher)

async def on_shutdown(dispatcher : Dispatcher) -> None:
    await database.close_connection()