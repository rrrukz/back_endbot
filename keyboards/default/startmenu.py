from aiogram.types import KeyboardButton,ReplyKeyboardMarkup


menu_start=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Mahsulotlar"),],
        [KeyboardButton(text="Yordam"),],
        [KeyboardButton(text="Anketa"), ],

    ],
    resize_keyboard=True
)