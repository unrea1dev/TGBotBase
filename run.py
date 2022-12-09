from loader import executor, config
import handlers, database

from misc.logging import initialize_logging

async def on_startup(_) -> None:
    await database.create_connection(url = config.database.database)

async def on_shutdown(_) -> None:
    await database.close_connection()

if __name__ == '__main__':
    initialize_logging()

    executor.on_startup(on_startup)
    executor.on_shutdown(on_shutdown)

    executor.start_polling()