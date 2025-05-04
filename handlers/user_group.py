from aiogram import types, Router, F

group_router = Router()

restricted_words = ['персик', 'шоколад', 'фурри', 'банан']

@group_router.message(F.text)
async def cleaner(message: types.Message):
    words_lst = message.text.split(' ')
    for word in words_lst:
        if word.lower() in restricted_words:
            await message.answer(f'{message.from_user.first_name} Соблюдайте правила чата!!!')
            # await message.answer(f'@{message.from_user.username} Соблюдайте правила чата!!!')
            await message.delete()
            break
