from aiogram import Bot, Dispatcher, types
import asyncio


TOKEN = '7587755001:AAGZ9bfc_kxW7q9-LVSkO4RVQS4rgxivnIA'


bot = Bot(token=TOKEN)
dp = Dispatcher()


from handlers.user_private import user_router
dp.include_router(user_router)

async def main():
    print('Бот запущен.')
    await dp.start_polling(bot)



asyncio.run(main())