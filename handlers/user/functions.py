from aiogram import types 
from bot import bot, dispatcher

from database.models import User

@dispatcher.message_handler(commands = ['start'])
async def process_send_welcome(message : types.Message) -> None:
    user_id = message.chat.id

    user = await User.filter(user_id = user_id).first()
    if not user:
        user = await User.create(user_id = user_id)

    await bot.send_message(chat_id = user_id, text = 'Hello!')