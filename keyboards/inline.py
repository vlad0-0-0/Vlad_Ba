from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

def addresses_kb():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text='Ул.Пушкина дом 45', callback_data='addresses_1'),
        InlineKeyboardButton(text='Ул.Пушкина дом 31', callback_data='addresses_2'),
        InlineKeyboardButton(text='Ул.Пушкина дом 67', callback_data='addresses_3'),
        width=2
    )

    return builder.as_markup()

