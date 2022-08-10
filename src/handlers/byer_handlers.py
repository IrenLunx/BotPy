from loader import dp
from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from keyboards import commands_default_keyboard

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
    await message.answer(text='У нас есть: редис, помидор и капуста',
                        reply_markup=ReplyKeyboardRemove())

@dp.message_handler(commands='help')
async def answer_start_command(message: types.Message):
    await message.answer(text='Список команд представлен на клавиатуре',
                        reply_markup=commands_default_keyboard)

@dp.message_handler(text=['Редис', 'Помидор', 'Капуста'])
async def answer_start_text(message: types.Message):
    await message.answer(text=f'У нас есть {message.text}!')  

@dp.message_handler(content_types=['contact'])
async def answer_start_text(message: types.Message):
    if message.from_user.id == message.contact.user_id:
        await message.answer(text='Это твой контакт!',
                        reply_markup=ReplyKeyboardRemove())  
    else:
        await message.answer(text='Это кто?!',
                        reply_markup=ReplyKeyboardRemove())
          

# @dp.message_handler(text='Скрыть клавиатуру')
# async def answer_start_command(message: types.Message):
#     await message.answer(text='Открыть клавиатуру')

# see_commands_default_keyboard 