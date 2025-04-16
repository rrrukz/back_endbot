from aiogram import types
from keyboards.inline.mahsulotlar import products
from keyboards.inline.kurslar_royhati import courses
from keyboards.inline.kitoblar_royxati import books
from loader import dp


# Kurslar tugmasi uchun handler;
@dp.callback_query_handler(text="kurs")
async def kurs_handler(callback:types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Kurslar",reply_markup=courses)

# kotoblar buttoni uchun handler
@dp.callback_query_handler(text="kitob")
async def kitob_handler(callback:types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("shulardan birortasini tanlang",reply_markup=books)

@dp.callback_query_handler(text="https://www.instagram.com/it_tat_samarkand?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==")
async def kurs_handler(callback:types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Instagram sahifamiz",reply_markup=courses)

