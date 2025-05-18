from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command
from keyboards import reply, inline

user_router = Router()

@user_router.message(CommandStart())
async def start(message: types.Message):
    await message.answer('Привет! 🏀 Добро пожаловать в наш чат-бот по продаже баскетбольных мячей! Здесь вы найдете широкий ассортимент мячей для игроков любого уровня — от начинающих до профессионалов. Если у вас есть вопросы о наших товарах, хотите получить рекомендации или узнать о специальных предложениях, просто напишите мне! Давайте вместе выберем идеальный мяч для ваших тренировок и игр. Готовы начать?', reply_markup=reply.main_kb)


@user_router.message(F.text.lower() == 'каталог')
@user_router.message(Command('catalog'))
async def catalog(messages: types.Message):
    await messages.answer("Каталог", reply_markup=reply.catalog_kb)


@user_router.message(F.text.lower() == 'про нас')
@user_router.message(Command('about'))
async def about(messages: types.Message):
    await messages.answer("Нет информации.")


@user_router.message(F.text.lower() == 'контакты')
@user_router.message(Command('contacts'))
async def contacts(messages: types.Message):
    await messages.answer("Нет контактов.")


@user_router.message(F.text.lower() == 'адреса')
@user_router.message(Command('addresses'))
async def addresses(messages: types.Message):
    await messages.answer("Наши адреса", reply_markup=inline.addresses_kb())

@user_router.callback_query(F.data.lower().startswith('addresses'))
async def addresses_info(callback: types.CallbackQuery):
    query = callback.data.split('_')[1]
    if query == '1':
        await callback.message.answer('Ул.Пушкина дом 45\nНаходится между двумя красными домами.')
    elif query == '2':
        await callback.message.answer('Ул.Пушкина дом 31\nНаходится на перекрёстке возле ёлки.')
    else:
        await callback.message.answer('Ул.Пушкина дом 67\nУ дома зелёная крыша.')
    await callback.answer('Адрес отправлен.')

@user_router.message(F.text.lower() == 'назад')
async def back_menu(messages: types.Message):
    await messages.answer('Главное меню', reply_markup=reply.main_kb)


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
