from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

TOKEN = '5402870697:AAEoZIwOfJfsdHZpRktMg86F7SSPDkwD5vM'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
@dp.message_handler(text=['Привет', 'Начать'])
async def answer_start_command(message: types.Message):
    await message.answer(text=f"Привет, {message['from']['first_name']}, что ты хочешь сделать?")
    # print(message.from_user.first_name)

@dp.message_handler(commands='add')
async def answer_start_command(message: types.Message):
    await message.answer(text='Позиция обавлена!')

@dp.message_handler(commands='item')
async def answer_start_command(message: types.Message):
    await message.answer(text='У нас есть: редис, помидор и капуста')

@dp.message_handler(commands='help')
async def answer_start_command(message: types.Message):
    await message.answer(text=f'/start - запуск программы\n/add - добавить позицию\n'
                            f'/item - список товаров\n/help - команды')

@dp.message_handler(text=['Редис', 'Помидор', 'Капуста'])
async def answer_start_text(message: types.Message):
    await message.answer(text=f'У нас есть {message.text}!')

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp)