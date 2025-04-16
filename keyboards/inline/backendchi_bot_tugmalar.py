
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

backendchi_buttons=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="📚Mavjud kurslar",callback_data="courses"),InlineKeyboardButton(text="📋Biz haqimizda",callback_data="about"),],

        [InlineKeyboardButton(text="📞Aloqa",callback_data="contact"),InlineKeyboardButton(text="📍Manzil",callback_data="location"),],

        [InlineKeyboardButton(text="📝Ro'yhatdan o'tish",callback_data="signup"),InlineKeyboardButton(text="🗞Yangiliklar",callback_data="news"),],

                                        [InlineKeyboardButton(text="📥takliflar",callback_data="offers"),],
    ]

)

