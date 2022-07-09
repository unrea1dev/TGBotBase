import aiogram
from aiogram import types 

from database.models import User

from bot import bot

async def process_send_welcome(message : types.Message) -> None:
    user_id = message.from_user.id

    user = User.get(user_id = user_id)
    if not user:
        user = User(user_id = user_id)
        user.create()

    await bot.send_message(chat_id = user_id, text = user.user_id)

def install(_dispatcher : aiogram.Dispatcher) -> None:
    _dispatcher.register_message_handler(callback = process_send_welcome, commands = ['start', 'help'])
