from aiogram import types

from data.config import ADMINS
from keyboards.default.startmenu import menu_start
from keyboards.inline.backendchi_bot_tugmalar import backendchi_buttons
from keyboards.inline.mahsulotlar import products
from utils.check_sub import user_chat_sub

from loader import bot,dp


@dp.message_handler(commands="start")
async def bot_start(message: types.Message):
    # bot ga /start bosgan userlar , malumotlarini adminga yuboramiz
    username=message.from_user.username
    id=message.from_user.id
    full_name=message.from_user.full_name


    # adminga xabar tayyorlash
    msg=f"Yangi foydalanuvchi qoshildi \n"
    msg+=f" ID : {id}\n"
    msg+=f"username : @{username}\n"
    msg+=f"full_name : {full_name}\n"

    # adminga xabar yuboramiz
    for admin in ADMINS:
        await bot.send_message(admin,msg)



    user_id=message.from_user.id
    azomi,natija=await user_chat_sub(user_id)
    if not azomi:
        await message.answer(natija)
    else:
     await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=backendchi_buttons)


# Mahsulorlar tugmasi uchun handler
# @dp.message_handler(text="Mahsulotlar")
# async def mahsulot_handler(msg:types.Message):
#     await msg.answer("Quyidagilardan birini tanlang",reply_markup=products)
#
#
#
@dp.callback_query_handler(text="back")
async def kurs_handler(callback: types.CallbackQuery):
        await callback.message.delete()
        await callback.message.answer("Tanlang", reply_markup=backendchi_buttons)