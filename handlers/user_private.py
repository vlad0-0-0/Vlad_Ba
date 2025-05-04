from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command

user_router = Router()

@user_router.message(CommandStart())
async def start(message: types.Message):
    await message.answer('Привет это бот по баскетбольным мячам.')


@user_router.message(F.text.lower() == 'каталог')
@user_router.message(Command('catalog'))
async def catalog(messages: types.Message):
    await messages.answer("Каталог ещё не готов.")


@user_router.message(F.text.lower() == 'про нас')
@user_router.message(Command('about'))
async def about(messages: types.Message):
    await messages.answer("Нет информации.")


@user_router.message(F.text.lower() == 'контакты')
@user_router.message(Command('contacts'))
async def contacts(messages: types.Message):
    await messages.answer("Нет контактов.")


@user_router.message(F.text.lower() == 'адрес')
@user_router.message(Command('addresses'))
async def addresses(messages: types.Message):
    await messages.answer("Нет адресов.")


# @user_router.message(F.text)
# @user_router.message(F.photo)
# @user_router.message(F.text.lower() == 'доставка')
# @user_router.message(F.text.lower().contains('доставк'))
# @user_router.message(F.text.lower().startswith('как'))
# @user_router.message(F.text.lower().endswith('?'))
# @user_router.message(F.text.lower().startswith('как'), F.text.lower().endswith('?'))
# @user_router.message(F.text.lower().contains('цен') | F.text.lower().contains('стоимост'))
async def echo(message: types.Message):
    await message.answer('Бот пока находится в разработке.')
    # user_text = message.text
    # await message.answer(user_text)
