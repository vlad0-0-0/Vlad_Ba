from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

back_btn = KeyboardButton(text='назад')

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Каталог'), KeyboardButton(text='Про нас')],
        [KeyboardButton(text='Контакты'), KeyboardButton(text='Адреса')]
    ],
    resize_keyboard=True,
    input_field_placeholder='Нажмите на кнопку ниже'
)

catalog_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='мяч 1'), KeyboardButton(text='мяч 2')],
        [KeyboardButton(text='мяч 3'), KeyboardButton(text='мяч 4')],
        [back_btn]
    ],
    resize_keyboard=True
)