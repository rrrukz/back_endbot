from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

books=InlineKeyboardMarkup(
      inline_keyboard=[
          [
              InlineKeyboardButton(text="🐍The quick PYTHON book",url="https://www.manning.com/books/the-quick-python-book-fourth-edition?utm_source=qpb3e&utm_medium=affiliate&utm_campaign=book_ceder5_the_4_23_24&a_aid=qpb3e&a_bid=8b55ad45&chan=mm_email"),
          ],
          [
              InlineKeyboardButton(text="JavaScript", url="https://books.google.co.uz/books?id=NPbkDwAAQBAJ&printsec=frontcover&hl=ru#v=onepage&q&f=false"),
          ],
          [
              InlineKeyboardButton(text="modern PHP",url="https://books.google.co.uz/books?id=rnSpBgAAQBAJ&printsec=frontcover&hl=ru#v=onepage&q&f=false"),
          ],
          [
              InlineKeyboardButton(text="◀BACK", callback_data="back"),
          ],
    ]

)
