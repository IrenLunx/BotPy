from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

TOKEN = '5402870697:AAEoZIwOfJfsdHZpRktMg86F7SSPDkwD5vM'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def answer_start_command(message: types.Message):
    await message.answer(text='Привет, пупс!')

@dp.message_handler(text=['Привет', 'Начать'])
async def answer_start_text(message: types.Message):
    await message.answer(text='Опа!')
    print(message)
# Объединение функции
# @dp.message_handler(commands='start')
# @dp.message_handler(text=['Привет', 'Начать'])
# async def answer_start_command(message: types.Message):
#     await message.answer(text='Привет, пупс!')

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp)