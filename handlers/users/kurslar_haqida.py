from aiogram import types

from keyboards.inline.backendchi_bot_tugmalar import backendchi_buttons
from keyboards.inline.mahsulotlar import products
from keyboards.inline.mahsulotlar import ortga
from keyboards.inline.kurslar_royhati import courses



from loader import dp

@dp.callback_query_handler(text="kompyuter")
async def savodxonlik_handler(callback:types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("📌 Kompyuter savodxonlik kursida siz:\n"
                                  "🟦Microsoft Word,\n"
                                  "🟩Microsoft Exel,\n"
                                  "🟥Microsoft PowerPoint- kabi dasturlarda ishlashni organasiz\n"
                                  "📆Davomiyligi : 2-oy\n"
                                  "💰Narxi : 350 000 so'm (oyiga)\n"
                                  "📞 Qo‘shimcha ma’lumot uchun bog‘laning. (@shoxrux_on)",reply_markup=ortga)
@dp.callback_query_handler(text="smm")
async def smm_handler(callback:types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(" SMM kursi\n"
                                  "📆 Davomiyligi: 4 oy\n"
                                  "💰 Narxi: 850 000 so‘m\n"
                                  "📌 Kurs davomida siz SMM asoslarini, ijtimoiy tarmoqlarda biznes yuritish va auditoriyani jalb qilish bo‘yicha bilim olasiz.\n"
                                  "📞 Qo‘shimcha ma’lumot uchun bog‘laning. (@shoxrux_on)",reply_markup=ortga)
@dp.callback_query_handler(text="python")
async def backend_handler(callback:types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("🐍Back-end kursi (Python)\n"
                                  "📆 Davomiyligi: 6-7 oy\n"
                                  "💰 Narxi: 650 000 so‘m\n"
                                  " 📌 Ushbu kursda siz Python dasturlash tilida back-end dasturlar yaratishni, server bilan ishlashni va ma’lumotlar bazasini boshqarishni o‘rganasiz.\n"
                                  "📞 Qo‘shimcha ma’lumot uchun bog‘laning. (@shoxrux_on)",reply_markup=ortga)

@dp.callback_query_handler(text="javascript")
async def backend_handler(callback:types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Front-end kursi \n"
                                  "📆 Davomiyligi: 6-7 oy\n"
                                  "💰 Narxi: 650 000 so‘m\n"
                                  " 📌  Ushbu kursda siz HTML, CSS, JavaScript va zamonaviy texnologiyalar yordamida web-saytlar yaratishni o‘rganasiz. Interfeyslarni dizayn qilish va foydalanuvchilar uchun qulay qilish bo‘yicha bilim olasiz\n"
                                  "📞 Qo‘shimcha ma’lumot uchun bog‘laning. (@shoxrux_on)",reply_markup=ortga)
@dp.callback_query_handler(text="robot")
async def backend_handler(callback:types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("🤖Robototexnika kursi\n"
                                  "📆 Davomiyligi: 1 yil\n"
                                  "💰 Narxi: 1 000 000 so‘m\n"
                                  "Ushbu kursda siz robotlar yaratish, dasturlash, va elektronika asoslari bo‘yicha chuqur bilimlarga ega bo‘lasiz. Amaliy mashg‘ulotlar orqali haqiqiy loyihalar ustida ishlaysiz. \n"
                                  "📞 Qo‘shimcha ma’lumot uchun bog‘laning. (@shoxrux_on)",reply_markup=ortga)
@dp.callback_query_handler(text="ortga")
async def kurs_handler(callback: types.CallbackQuery):
        await callback.message.delete()
        await callback.message.answer("Tanlang", reply_markup=courses)
@dp.callback_query_handler(text="home")
async def kurs_handler(callback: types.CallbackQuery):
        await callback.message.delete()
        await callback.message.answer("Tanlang", reply_markup=backendchi_buttons)
