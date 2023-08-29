from fastapi import FastAPI
from aiogram import Bot, types

from core import config

from loader import bot, dispatcher
import database

from api.routers import router

api = FastAPI()
api.include_router(router = router)

@api.on_event('startup')
async def on_startup() -> None:
    await database.create_connection(
        url = config.database.database,
        timezone = config.database.timezone
    )

    webhook_info = await bot.get_webhook_info()

    if webhook_info.url != config.api.bot_webhook_url:  
        await bot.set_webhook(config.api.bot_webhook_url)

@api.on_event('shutdown')
async def on_shutdown() -> None:
    await database.close_connection()

    await bot.delete_webhook()
    session = await bot.get_session()

    await session.close()

@api.post(path = config.api.bot_webhook_path)
async def process_webhook(request : dict) -> None:
    update = types.Update(**request)
    Bot.set_current(bot)

    await dispatcher.process_update(update)