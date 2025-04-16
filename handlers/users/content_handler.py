from aiogram import types
from loader import dp,bot
from pathlib import Path



# foydalanuvchi yuborgan rasm , videolarni saqlaymiz downloads/categories/
down_path=Path().joinpath("downloads","categories")
down_path.mkdir(parents=True,exist_ok=True)
# Foydalanuvchi botga rasm yuborsa
@dp.message_handler(content_types=types.ContentType.PHOTO)
async  def photo_message(message:types.Message):
    await message.photo[-1].download(destination=down_path)
    await message.reply(message.photo[-1].file_id)
    await message.reply("bu qanaqa rasm , RASM YUBORMANG!!!")

@dp.message_handler(content_types=["video","audio","animation","document","gif","sticker"])
async  def photo_message(message:types.Message):
    if message.video:
        await message.video.download(destination=down_path)
        await message.reply("Bu qanaqa video , BUNAQA MA'LUMOT YUBORMANG!!!")
    elif message.audio:
        await message.audio.download(destination=down_path)
        await message.reply("Bu qanaqa audio , BUNAQA MA'LUMOT YUBORMANG!!!")
    elif message.document:
        await message.document.download(destination=down_path)
        await message.reply("Bu qanaqa hujjat , BUNAQA MA'LUMOT YUBORMANG!!!")
    elif message.sticker:
        await message.reply("Bu qanaqa stiker , BUNAQA MA'LUMOT YUBORMANG!!!")
    elif message.animation:
        await message.reply("Bu qanaqa animatsiya , BUNAQA MA'LUMOT YUBORMANG!!!")

