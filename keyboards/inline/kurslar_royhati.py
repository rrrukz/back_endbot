from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

courses=InlineKeyboardMarkup(
      inline_keyboard=[
          [
              InlineKeyboardButton(text="🖥Kompyuter savodxonligi",callback_data="kompyuter"),
          ],
          [
              InlineKeyboardButton(text="📱SMM", callback_data="smm"),
          ],
          [
              InlineKeyboardButton(text="🐍BACKEND",callback_data="python"),
          ],
          [
              InlineKeyboardButton(text="FRONTEND",callback_data="javascript"),
          ],
          [
              InlineKeyboardButton(text="🤖ROBOTOTEXNIKA",callback_data="robot"),
          ],
          [
              InlineKeyboardButton(text="◀BACK", callback_data="back"),
          ],
      ]
)
