from aiogram import Router, Bot
from aiogram.types import Message

import config

main_router = Router()

@main_router.message()
async def all_messages(message: Message, bot: Bot):
    msg_text = f'В чате {message.chat.id} пользователь {message.from_user.full_name} написал: \n{message.text}'
    await bot.send_message(
        chat_id=config.ADMIN_ID,
        text=msg_text,
    )
    # print(msg_text)
