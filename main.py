from aiogram import Bot, Dispatcher, types
import asyncio
from aiogram.filters import CommandStart

TOKEN = '7587755001:AAGZ9bfc_kxW7q9-LVSkO4RVQS4rgxivnIA'


bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer('Привет это бот по баскетбольным мячам.')

@dp.message()
async def echo(message: types.Message):
    await message.answer('Бот пока находится в разработке.')
    user_text = message.text
    await message.answer(user_text)

async def main():
    print('Бот запущен.')
    await dp.start_polling(bot)



asyncio.run(main())