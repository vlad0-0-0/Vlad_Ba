from aiogram import types, Router, F
from aiogram.types import FSInputFile

catalog_router = Router()

@catalog_router.message(F.text.lower() == 'мяч 1')
async  def product_1(messages: types.Message):
    photo = FSInputFile(r'img\catalog\first.jpg')
    await messages.answer_photo(photo, caption='Баскетбольный Мяч Wilson Fiba 3X3 WTB0533XB')


@catalog_router.message(F.text.lower() == 'мяч 2')
async  def product_2(messages: types.Message):
    photo = FSInputFile(r'img\catalog\second.jpg')
    await messages.answer_photo(photo, caption='Баскетбольный Мяч TORRES BM300 B02017')


@catalog_router.message(F.text.lower() == 'мяч 3')
async  def product_3(messages: types.Message):
    photo = FSInputFile(r'img\catalog\3.jpg')
    await messages.answer_photo(photo, caption='Баскетбольный Мяч Jogel JB-500')


@catalog_router.message(F.text.lower() == 'мяч 4')
async  def product_4(messages: types.Message):
    photo = FSInputFile(r'img\catalog\4.jpg')
    await messages.answer_photo(photo, caption='Баскетбольный Мяч Wilson NBA Minnesota Timberwolves Team')