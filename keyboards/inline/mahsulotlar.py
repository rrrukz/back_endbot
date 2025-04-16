from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup


products=InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="🖥Kurslar",callback_data="kurs"),
        ],
        [
            InlineKeyboardButton(text="📖Kitoblar",callback_data="kitob"),
        ],
        [
            InlineKeyboardButton(text="🏫IT TAT markazi",url="https://www.instagram.com/it_tat_samarkand?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw=="),
        ],
        [
            InlineKeyboardButton(text="🔎Qidirish",switch_inline_query_current_chat=""),
        ],[
            InlineKeyboardButton(text="📲Ulashish",switch_inline_query="yaxshi bot ekan"),
        ],

    ]
)
ortga=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="◀️BACK", callback_data="ortga"),
        ],
        [
            InlineKeyboardButton(text="🏠HOME", callback_data="home"),
        ],
    ]
)