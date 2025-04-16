from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import ADMINS
from keyboards.inline.backendchi_bot_tugmalar import backendchi_buttons
from keyboards.inline.kurslar_royhati import courses
from loader import dp, bot
from states.anketa import Data2


@dp.callback_query_handler(text="about")
async def about_handler(call:types.CallbackQuery):
    text = "IT TAT o'quv markazi zamonaviy IT yo'nalishlarida ta'lim beradi\n"
    text += "Maqsadimiz - yoshlarni  zamonaviy bilimlar bilan ta'minlash\n\n"
    await call.message.edit_text(text, reply_markup=backendchi_buttons, parse_mode="Markdown")
    await call.answer()
@dp.callback_query_handler(text="news")
async def about_handler(call:types.CallbackQuery):
    text = "IT TAT O'QUV MARKAZIDA JUDA KATTA YANGILIK!!!\n"
    text += "Endilikda siz bizning markazimizda bo'lib o'tadigan xaftalik musobaqalarda qatnashib o'quv kurslarimiz uchun chegirmalar yutib olishingiz mimkin \n\n"
    await call.message.edit_text(text, reply_markup=backendchi_buttons, parse_mode="Markdown")
    await call.answer()
@dp.callback_query_handler(text="courses")
async def courses_handler(call:types.CallbackQuery):
    text = "Hozirgi kunda bizning markazimizda mavjud bo'lgan kurslar🔽\n"
    text += "\n\n"
    await call.message.edit_text(text, reply_markup=courses, parse_mode="Markdown")
    await call.answer()
@dp.callback_query_handler(text="contact")
async def contact_handler(call:types.CallbackQuery):
    text = "BIZNING MARKAZ BILAN BOG'LANISH UCHUN tel:👇\n"
    text += ("📞 +998 88 611 0440 \n "
             "📞 +998 97 958 4042 \n\n")
    await call.message.edit_text(text, reply_markup=backendchi_buttons, parse_mode="Markdown")
    await call.answer()
@dp.callback_query_handler(text="location")
async def about_handler(call:types.CallbackQuery):
    text = "IT TAT O'QUV MARKAZI:\n"
    text += ("📍manzil:Samarqand viloyati, Samarqand shaxri,temiryo'l vokzali(mo'ljal Ipoteka bank) \n \n")
    await call.message.edit_text(text, reply_markup=backendchi_buttons, parse_mode="Markdown")
    await call.answer()
@dp.callback_query_handler(text="offers")
async def about_handler(call:types.CallbackQuery):
    text = "TAKLIFLAR:\n"
    text += ("Bu yerda siz markazimiz rivojiga hissa qo'shish uchun takliflar yozib qoldirishngiz muimkin \n \n")
    await call.message.edit_text(text, reply_markup=backendchi_buttons, parse_mode="Markdown")
    await call.answer()


@dp.callback_query_handler(text="signup")
async def sign_up_handler(call:types.CallbackQuery):
    await call.message.answer("Ro'yhatdan o'tish uchun\n"
                              "ismingizni kiriting")
    await Data2.ism.set()
@dp.message_handler(state=Data2.ism)
async def fullname_get(message: types.Message, state: FSMContext):
        ism = message.text
        await state.update_data(
            {"full_name": ism}
        )

        await message.answer("Yoshingizni kiriting")
        await Data2.yosh.set()

@dp.message_handler(state=Data2.yosh)
async def age_get(message: types.Message, state: FSMContext):
        yosh = message.text
        await state.update_data(
            {"age": yosh}
        )
        await message.answer(f"O'qiysizmi yoki ishlaysizmi?")
        await Data2.kasb.set()
@dp.message_handler(state=Data2.kasb)
async def kasbi_get(message: types.Message, state: FSMContext):
        kasb = message.text
        await state.update_data(
            {"kasbi": kasb}
        )
        await message.answer(f"Qaysi hudud da yashashingizni kiriting")
        await Data2.manzil.set()

@dp.message_handler(state=Data2.manzil)
async def manzil_get(message: types.Message, state: FSMContext):
        manzil = message.text
        await state.update_data(
            {"manzil": manzil}
        )
        await message.answer("Murojat qilish uchun telefon raqamingizni kiriting:")
        await Data2.tel.set()

@dp.message_handler(state=Data2.tel)
async def aloqa_get(message: types.Message, state: FSMContext):
        tel = message.text
        await state.update_data(
            {"aloqa": tel}
        )

        data = await state.get_data()
        full_name = data.get("full_name")
        age = data.get("age")
        kasbi = data.get("kasbi")
        manzil = data.get("manzil")
        aloqa = data.get("aloqa")
        natija = f"Ro'yhatdan o'tgan\n"
        natija += (f"Ismi:{full_name}\n"
                   f"Yoshi: {age}\n"
                   f"☎️Aloqa uchun: {aloqa}\n"
                   f"📍Hudud: {manzil}\n"
                   f"👤Kasbi: {kasbi}\n"

                   f"Foydalanuvchi: @{message.from_user.username}\n")

        await bot.send_message(ADMINS[0], natija)
        await message.answer("Siz muvofaqiyatli ro'yhatdan o'tdingiz☑️\n")

        await state.finish()



