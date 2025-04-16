from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import ADMINS
from loader import dp,bot
from states.anketa import Data
from keyboards.default.anketa_bar import anketa_buttons



# anketa/ komandasi uchun handler
@dp.message_handler(text="Anketa")
async def anketa_handler(message:types.Message):
    await message.answer("Shulardan birini tanlang:",reply_markup=anketa_buttons)

@dp.message_handler(text="Hodim kerak")
async def ishchi_kerak_handler(message:types.Message):
    await message.answer("ismingizni kiriting")
    await Data.full_name.set()

@dp.message_handler(state=Data.full_name)
async def fullname_get(message:types.Message,state:FSMContext):
    full_name=message.text
    await state.update_data(
        {"full_name":full_name}
    )

    await message.answer("Yoshingizni kiriting")
    await Data.age.set()
@dp.message_handler(state=Data.age)
async def age_get(message:types.Message,state:FSMContext):
    age=message.text
    await state.update_data(
        {"age":age}
    )

    await message.answer("Qaysi texnologiyada ishlaydigan hodim kerak?")
    await Data.texnologiya.set()
@dp.message_handler(state=Data.texnologiya)
async def texnologiya_get(message: types.Message, state: FSMContext):
    texnologiya = message.text
    await state.update_data(
        {"texnologiya": texnologiya}
        )

    await message.answer("Murojat qilishlari uchun telefon raqamingizni kiriting:")
    await Data.aloqa.set()
@dp.message_handler(state=Data.aloqa)
async def aloqa_get(message: types.Message, state: FSMContext):
    aloqa = message.text
    await state.update_data(
        {"aloqa": aloqa}
    )
    await message.answer(f"Ish qaysi hududda ekanligini kiriting(agar online bolsa online deb yozing): ")
    await Data.hudud.set()
@dp.message_handler(state=Data.hudud)
async def hudud_get(message: types.Message, state: FSMContext):
    hudud = message.text
    await state.update_data(
        {"hudud": hudud}
    )
    await message.answer(f"Oylik maosh qancha summasini kiriting (agar pulsiz, shunchaki tajriba yig'ishni hohlaydigan ishchi izlayotgan bolsangiz , huddi shunday yozing")
    await Data.narxi.set()
@dp.message_handler(state=Data.narxi)
async def narxi_get(message: types.Message, state: FSMContext):
    narxi = message.text
    await state.update_data(
        {"narxi": narxi}
    )
    await message.answer(f"Qaysi kasb egalarini izlayapsiz?")
    await Data.kasbi.set()
@dp.message_handler(state=Data.kasbi)
async def kasbi_get(message: types.Message, state: FSMContext):
    kasbi = message.text
    await state.update_data(
        {"kasbi": kasbi}
    )
    await message.answer(f"Qaysi vaqtda murojaat qilish mumkin?\n"f"Masalan, 9:00 - 18:00")
    await Data.murojat_vaqt.set()
@dp.message_handler(state=Data.murojat_vaqt)
async def murojat_vaqti_get(message: types.Message, state: FSMContext):
    murojat_vaqti = message.text
    await state.update_data(
        {"murojat_vaqti": murojat_vaqti}
    )
    await message.answer(f"Maqsadingizni qisqacha yozib bering.")
    await Data.maqsad.set()
@dp.message_handler(state=Data.maqsad)
async def maqsad_get(message: types.Message, state: FSMContext):
    maqsad = message.text
    await state.update_data(
        {"maqsad": maqsad}
    )

    # malumotlarni qayta oqiymiz
    data = await state.get_data()
    full_name = data.get("full_name")
    age = data.get("age")
    texnologiya = data.get("texnologiya")
    aloqa = data.get("aloqa")
    hudud = data.get("hudud")
    narxi = data.get("narxi")
    kasbi = data.get("kasbi")
    murojat_vaqti = data.get("murojat_vaqti")
    maqsad = data.get("maqsad")
    natija = f"QUYIDAGI MA'LUMOTLAR OLINDI👇\n"
    natija += (f"E'lon beruvchi: {full_name}\n"
               f"Yoshi: {age}\n"
               f"Hodimga bo'lgan talablar:🔽\n"
               f"📝Texnologiya: {texnologiya}\n"
               f"☎️Aloqa uchun: {aloqa}\n"
               f"📍Hudud: {hudud}\n"
               f"💰Oylik: {narxi}\n"
               f"👤Kasbi: {kasbi}\n"
               f"⏰Murojat qilish vaqti: {murojat_vaqti}\n"
               f"🥅Maqsad: {maqsad}\n"

               f"Foydalanuvchi: @{message.from_user.username}\n")
    await bot.send_message(ADMINS[0], natija)
    await message.answer(natija)

    await state.finish()

# sherik kerak button uchun handler

@dp.message_handler(text="Sherik kerak")
async def ishchi_kerak_handler(message: types.Message):
    await message.answer("ismingizni kiriting")
    await Data.full_name.set()

@dp.message_handler(state=Data.full_name)
async def fullname_get(message: types.Message, state: FSMContext):
    full_name = message.text
    await state.update_data(
            {"full_name": full_name}
        )

    await message.answer("Yoshingizni kiriting")
    await Data.age.set()

@dp.message_handler(state=Data.age)
async def age_get(message: types.Message, state: FSMContext):
    age = message.text
    await state.update_data(
            {"age": age}
        )

    await message.answer(" sherigingiz qaysi texnologiya bilan ishlashi kerak?")
    await Data.texnologiya.set()

@dp.message_handler(state=Data.texnologiya)
async def texnologiya_get(message: types.Message, state: FSMContext):
    texnologiya = message.text
    await state.update_data(
            {"texnologiya": texnologiya}
        )

    await message.answer("Telefon raqamingizni kiriting:")
    await Data.aloqa.set()

@dp.message_handler(state=Data.aloqa)
async def aloqa_get(message: types.Message, state: FSMContext):
    aloqa = message.text
    await state.update_data(
            {"aloqa": aloqa}
        )
    await message.answer(f"Qaysi hududdansiz?\n"f"Viloyat nomi, Toshkent shahar yoki Respublikani kiriting.")
    await Data.hudud.set()

@dp.message_handler(state=Data.hudud)
async def hudud_get(message: types.Message, state: FSMContext):
    hudud = message.text
    await state.update_data(
            {"hudud": hudud}
        )
    await message.answer(f"Tolov qilasizmi yoki Tekinmi?\n"f"Kerak bo`lsa, Summani kiriting?")
    await Data.narxi.set()

@dp.message_handler(state=Data.narxi)
async def narxi_get(message: types.Message, state: FSMContext):
    narxi = message.text
    await state.update_data(
            {"narxi": narxi}
        )
    await message.answer(f"Ishlaysizmi yoki o`qiysizmi?\n"f"Masalan, Talaba")
    await Data.kasbi.set()

@dp.message_handler(state=Data.kasbi)
async def kasbi_get(message: types.Message, state: FSMContext):
    kasbi = message.text
    await state.update_data(
            {"kasbi": kasbi}
        )
    await message.answer(f"Qaysi vaqtda murojaat qilish mumkin?\n"f"Masalan, 9:00 - 18:00")
    await Data.murojat_vaqt.set()

@dp.message_handler(state=Data.murojat_vaqt)
async def murojat_vaqti_get(message: types.Message, state: FSMContext):
    murojat_vaqti = message.text
    await state.update_data(
            {"murojat_vaqti": murojat_vaqti}
        )
    await message.answer(f"Maqsadingizni qisqacha yozib bering.")
    await Data.maqsad.set()

@dp.message_handler(state=Data.maqsad)
async def maqsad_get(message: types.Message, state: FSMContext):
    maqsad = message.text
    await state.update_data(
            {"maqsad": maqsad}
        )


    # malumotlarni qayta oqiymiz
    data=await state.get_data()
    full_name=data.get("full_name")
    age=data.get("age")
    texnologiya=data.get("texnologiya")
    aloqa=data.get("aloqa")
    hudud=data.get("hudud")
    narxi=data.get("narxi")
    kasbi=data.get("kasbi")
    murojat_vaqti=data.get("murojat_vaqti")
    maqsad=data.get("maqsad")
    natija=f"Quyidagi ma'lumotlar olindi\n"
    natija+=(f"Ism Familiyasi : {full_name}\n"
             f"Yosh: {age}\n"
             f"Texnologiya: {texnologiya}\n"
             f"aloqa: {aloqa}\n"
             f"hudud: {hudud}\n"
             f"narxi: {narxi}\n"
             f"kasbi: {kasbi}\n"
             f"murojat_vaqti: {murojat_vaqti}\n"
             f"maqsad: {maqsad}\n"
             
             f"Foydalanuvchi: @{message.from_user.username}\n")
    await bot.send_message(ADMINS[0],natija)
    await state.finish()

# Ish joyi kerak buttoni uchun handler
@dp.message_handler(text="Ish joyi kerak")
async def ishchi_kerak_handler(message: types.Message):
    await message.answer("ismingizni kiriting")
    await Data.full_name.set()


@dp.message_handler(state=Data.full_name)
async def fullname_get(message: types.Message, state: FSMContext):
    full_name = message.text
    await state.update_data(
        {"full_name": full_name}
    )

    await message.answer("Yoshingizni kiriting")
    await Data.age.set()


@dp.message_handler(state=Data.age)
async def age_get(message: types.Message, state: FSMContext):
    age = message.text
    await state.update_data(
        {"age": age}
    )

    await message.answer("Qaysi texnologiyalardan foydalanasiz ?")
    await Data.texnologiya.set()


@dp.message_handler(state=Data.texnologiya)
async def texnologiya_get(message: types.Message, state: FSMContext):
    texnologiya = message.text
    await state.update_data(
        {"texnologiya": texnologiya}
    )

    await message.answer("Telefon raqamingizni kiriting:")
    await Data.aloqa.set()


@dp.message_handler(state=Data.aloqa)
async def aloqa_get(message: types.Message, state: FSMContext):
    aloqa = message.text
    await state.update_data(
        {"aloqa": aloqa}
    )
    await message.answer(f"Qaysi hududdansiz?\n"f"Viloyat nomi, Toshkent shahar yoki Respublikani kiriting.")
    await Data.hudud.set()


@dp.message_handler(state=Data.hudud)
async def hudud_get(message: types.Message, state: FSMContext):
    hudud = message.text
    await state.update_data(
        {"hudud": hudud}
    )
    await message.answer(f"Qancha oylik sizni qoniqtiradi?")
    await Data.narxi.set()


@dp.message_handler(state=Data.narxi)
async def narxi_get(message: types.Message, state: FSMContext):
    narxi = message.text
    await state.update_data(
        {"narxi": narxi}
    )
    await message.answer(f"Ishlaysizmi yoki o`qiysizmi?\n"f"Masalan, Talaba")
    await Data.kasbi.set()


@dp.message_handler(state=Data.kasbi)
async def kasbi_get(message: types.Message, state: FSMContext):
    kasbi = message.text
    await state.update_data(
        {"kasbi": kasbi}
    )
    await message.answer(f"Qaysi vaqtda murojaat qilish mumkin?\n"f"Masalan, 9:00 - 18:00")
    await Data.murojat_vaqt.set()


@dp.message_handler(state=Data.murojat_vaqt)
async def murojat_vaqti_get(message: types.Message, state: FSMContext):
    murojat_vaqti = message.text
    await state.update_data(
        {"murojat_vaqti": murojat_vaqti}
    )
    await message.answer(f"Maqsadingizni qisqacha yozib bering.")
    await Data.maqsad.set()


@dp.message_handler(state=Data.maqsad)
async def maqsad_get(message: types.Message, state: FSMContext):
    maqsad = message.text
    await state.update_data(
        {"maqsad": maqsad}
    )

    # malumotlarni qayta oqiymiz
    data = await state.get_data()
    full_name = data.get("full_name")
    age = data.get("age")
    texnologiya = data.get("texnologiya")
    aloqa = data.get("aloqa")
    hudud = data.get("hudud")
    narxi = data.get("narxi")
    kasbi = data.get("kasbi")
    murojat_vaqti = data.get("murojat_vaqti")
    maqsad = data.get("maqsad")
    natija = f"Quyidagi ma'lumotlar olindi\n"
    natija += (f"Ism Familiyasi : {full_name}\n"
               f"Yosh: {age}\n"
               f"Texnologiya: {texnologiya}\n"
               f"aloqa: {aloqa}\n"
               f"hudud: {hudud}\n"
               f"narxi: {narxi}\n"
               f"kasbi: {kasbi}\n"
               f"murojat_vaqti: {murojat_vaqti}\n"
               f"maqsad: {maqsad}\n"

               f"Foydalanuvchi: @{message.from_user.username}\n")
    await bot.send_message(ADMINS[0], natija)
    await state.finish()

# Ustoz kerak buttoni uchun handler

@dp.message_handler(text="Ustoz kerak")
async def ishchi_kerak_handler(message: types.Message):
    await message.answer("ismingizni kiriting")
    await Data.full_name.set()


@dp.message_handler(state=Data.full_name)
async def fullname_get(message: types.Message, state: FSMContext):
    full_name = message.text
    await state.update_data(
        {"full_name": full_name}
    )

    await message.answer("Yoshingizni kiriting")
    await Data.age.set()


@dp.message_handler(state=Data.age)
async def age_get(message: types.Message, state: FSMContext):
    age = message.text
    await state.update_data(
        {"age": age}
    )

    await message.answer("Texnologiyani kiriting")
    await Data.texnologiya.set()


@dp.message_handler(state=Data.texnologiya)
async def texnologiya_get(message: types.Message, state: FSMContext):
    texnologiya = message.text
    await state.update_data(
        {"texnologiya": texnologiya}
    )

    await message.answer("Telefon raqamingizni kiriting:")
    await Data.aloqa.set()


@dp.message_handler(state=Data.aloqa)
async def aloqa_get(message: types.Message, state: FSMContext):
    aloqa = message.text
    await state.update_data(
        {"aloqa": aloqa}
    )
    await message.answer(f"Qaysi hududdansiz?\n"f"Viloyat nomi, Toshkent shahar yoki Respublikani kiriting.")
    await Data.hudud.set()


@dp.message_handler(state=Data.hudud)
async def hudud_get(message: types.Message, state: FSMContext):
    hudud = message.text
    await state.update_data(
        {"hudud": hudud}
    )
    await message.answer(f"Tolov qilasizmi yoki Tekinmi?\n"f"Kerak bo`lsa, Summani kiriting?")
    await Data.narxi.set()


@dp.message_handler(state=Data.narxi)
async def narxi_get(message: types.Message, state: FSMContext):
    narxi = message.text
    await state.update_data(
        {"narxi": narxi}
    )
    await message.answer(f"Ishlaysizmi yoki o`qiysizmi?\n"f"Masalan, Talaba")
    await Data.kasbi.set()


@dp.message_handler(state=Data.kasbi)
async def kasbi_get(message: types.Message, state: FSMContext):
    kasbi = message.text
    await state.update_data(
        {"kasbi": kasbi}
    )
    await message.answer(f"Qaysi vaqtda murojaat qilish mumkin?\n"f"Masalan, 9:00 - 18:00")
    await Data.murojat_vaqt.set()


@dp.message_handler(state=Data.murojat_vaqt)
async def murojat_vaqti_get(message: types.Message, state: FSMContext):
    murojat_vaqti = message.text
    await state.update_data(
        {"murojat_vaqti": murojat_vaqti}
    )
    await message.answer(f"Maqsadingizni qisqacha yozib bering.")
    await Data.maqsad.set()


@dp.message_handler(state=Data.maqsad)
async def maqsad_get(message: types.Message, state: FSMContext):
    maqsad = message.text
    await state.update_data(
        {"maqsad": maqsad}
    )

    # malumotlarni qayta oqiymiz
    data = await state.get_data()
    full_name = data.get("full_name")
    age = data.get("age")
    texnologiya = data.get("texnologiya")
    aloqa = data.get("aloqa")
    hudud = data.get("hudud")
    narxi = data.get("narxi")
    kasbi = data.get("kasbi")
    murojat_vaqti = data.get("murojat_vaqti")
    maqsad = data.get("maqsad")
    natija = f"Quyidagi ma'lumotlar olindi\n"
    natija += (f"Ism Familiyasi : {full_name}\n"
               f"Yosh: {age}\n"
               f"Texnologiya: {texnologiya}\n"
               f"aloqa: {aloqa}\n"
               f"hudud: {hudud}\n"
               f"narxi: {narxi}\n"
               f"kasbi: {kasbi}\n"
               f"murojat_vaqti: {murojat_vaqti}\n"
               f"maqsad: {maqsad}\n"

               f"Foydalanuvchi: @{message.from_user.username}\n")
    await bot.send_message(ADMINS[0], natija)
    await state.finish()

# shogird kerak buttoni uchun handler
@dp.message_handler(text="Shogird kerak")
async def ishchi_kerak_handler(message: types.Message):
    await message.answer("ismingizni kiriting")
    await Data.full_name.set()


@dp.message_handler(state=Data.full_name)
async def fullname_get(message: types.Message, state: FSMContext):
    full_name = message.text
    await state.update_data(
        {"full_name": full_name}
    )

    await message.answer("Yoshingizni kiriting")
    await Data.age.set()


@dp.message_handler(state=Data.age)
async def age_get(message: types.Message, state: FSMContext):
    age = message.text
    await state.update_data(
        {"age": age}
    )

    await message.answer("Texnologiyani kiriting")
    await Data.texnologiya.set()


@dp.message_handler(state=Data.texnologiya)
async def texnologiya_get(message: types.Message, state: FSMContext):
    texnologiya = message.text
    await state.update_data(
        {"texnologiya": texnologiya}
    )

    await message.answer("Telefon raqamingizni kiriting:")
    await Data.aloqa.set()


@dp.message_handler(state=Data.aloqa)
async def aloqa_get(message: types.Message, state: FSMContext):
    aloqa = message.text
    await state.update_data(
        {"aloqa": aloqa}
    )
    await message.answer(f"Qaysi hududdansiz?\n"f"Viloyat nomi, Toshkent shahar yoki Respublikani kiriting.")
    await Data.hudud.set()


@dp.message_handler(state=Data.hudud)
async def hudud_get(message: types.Message, state: FSMContext):
    hudud = message.text
    await state.update_data(
        {"hudud": hudud}
    )
    await message.answer(f"Tolov qilasizmi yoki Tekinmi?\n"f"Kerak bo`lsa, Summani kiriting?")
    await Data.narxi.set()


@dp.message_handler(state=Data.narxi)
async def narxi_get(message: types.Message, state: FSMContext):
    narxi = message.text
    await state.update_data(
        {"narxi": narxi}
    )
    await message.answer(f"Ishlaysizmi yoki o`qiysizmi?\n"f"Masalan, Talaba")
    await Data.kasbi.set()


@dp.message_handler(state=Data.kasbi)
async def kasbi_get(message: types.Message, state: FSMContext):
    kasbi = message.text
    await state.update_data(
        {"kasbi": kasbi}
    )
    await message.answer(f"Qaysi vaqtda murojaat qilish mumkin?\n"f"Masalan, 9:00 - 18:00")
    await Data.murojat_vaqt.set()


@dp.message_handler(state=Data.murojat_vaqt)
async def murojat_vaqti_get(message: types.Message, state: FSMContext):
    murojat_vaqti = message.text
    await state.update_data(
        {"murojat_vaqti": murojat_vaqti}
    )
    await message.answer(f"Maqsadingizni qisqacha yozib bering.")
    await Data.maqsad.set()


@dp.message_handler(state=Data.maqsad)
async def maqsad_get(message: types.Message, state: FSMContext):
    maqsad = message.text
    await state.update_data(
        {"maqsad": maqsad}
    )

    # malumotlarni qayta oqiymiz
    data = await state.get_data()
    full_name = data.get("full_name")
    age = data.get("age")
    texnologiya = data.get("texnologiya")
    aloqa = data.get("aloqa")
    hudud = data.get("hudud")
    narxi = data.get("narxi")
    kasbi = data.get("kasbi")
    murojat_vaqti = data.get("murojat_vaqti")
    maqsad = data.get("maqsad")
    natija = f"Quyidagi ma'lumotlar olindi\n"
    natija += (f"Ism Familiyasi : {full_name}\n"
               f"Yosh: {age}\n"
               f"Texnologiya: {texnologiya}\n"
               f"aloqa: {aloqa}\n"
               f"hudud: {hudud}\n"
               f"narxi: {narxi}\n"
               f"kasbi: {kasbi}\n"
               f"murojat_vaqti: {murojat_vaqti}\n"
               f"maqsad: {maqsad}\n"

               f"Foydalanuvchi: @{message.from_user.username}\n")
    await bot.send_message(ADMINS[0], natija)
    await state.finish()