from aiogram import types
from loader import dp,bot


# /photo rasm yuborish
@dp.message_handler(commands="photo")
async def send_photo(message:types.Message):
    photo1="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRCXkXRa6Locr_3lCyclQXjQuo2DJizNsn66Q&s"
    photo2="AgACAgQAAxkDAAIH6mf5CFh8O9itT61Nt8Yb3N5jQUpHAAKDtzEbEivUU8rx-kSMAAGjRgEAAwIAA20AAzYE"

    with open("D:/jjjjj/downloads/categories/photos/file_3.jpg","rb") as photo3:
        await message.answer_photo(photo3)
        await message.answer_photo(photo1)
        await message.answer_photo(photo2)

# /photo_media rasm yuborish
@dp.message_handler(commands="photo_media")
async def send_photo(message:types.Message):
    album=types.MediaGroup()
    photo_1="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSSVIgTk4D22BF0PSAITCFZYEi7rZ6FsLN1sg&s"
    photo_2="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQfuTJJb6eDfipOffWD8Ig45mlMirQiLJkK6A&s"
    photo_3="https://www.datocms-assets.com/48401/1628644950-javascript.png"
    album.attach_photo(photo_1)
    album.attach_photo(photo_2)
    album.attach_photo(photo_3)
    await message.reply_media_group(media=album)