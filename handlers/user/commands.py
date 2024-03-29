from aiogram import types 

from loader import dispatcher
from database.models import User

@dispatcher.message_handler(commands = ['start'])
async def process_start_command(message : types.Message) -> None:
    user_id = message.chat.id

    user = await User.filter(user_id = user_id).first()
    if not user:
        user = await User.create(user_id = user_id)

    await message.answer(text = str(user_id))