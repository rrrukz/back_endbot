from loader import bot
from aiogram import Bot
from typing import Union
from data.config import CHANNELS


async def check(user_id,channel:Union[str,int]):
    bot=Bot.get_current()
    member= await bot.get_chat_member(user_id=user_id,chat_id=channel)
    return member.is_chat_member()

async def user_chat_sub(user_id:int):
    natija=f"Botdan foydalanish uchun quyidagi kanallarga obuna bo'ling\n"
    azomi=True


    for channel in CHANNELS:
        status= await check(user_id,channel)
        if not status:
            azomi=False
            chat=await bot.get_chat(channel)
            link=await chat.export_invite_link()
            natija+=f"👉🏻<a href='{link}'>{chat.title}</a>\n"
    return azomi, natija