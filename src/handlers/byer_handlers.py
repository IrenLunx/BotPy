from aiogram import types
from aiogram.types import ReplyKeyboardRemove

from keyboards import commands_default_keyboard, see_commands_default_keyboard, info_default_keyboard
from keyboards import start_callback, navigation_callback
from keyboards import start_inline_keyboard, get_item_inline_keyboard
from loader import dp, data_manager, bot

@dp.message_handler(commands='start')
@dp.message_handler(text=['Привет', 'Начать'])
async def answer_start_command(message: types.Message):
    await message.answer(text=f"Привет, {message['from']['first_name']}, что ты хочешь сделать?",
                        reply_markup=start_inline_keyboard)
                        # reply_markup=commands_default_keyboard)
    # print(message.from_user.first_name)

@dp.callback_query_handler(start_callback.filter())
async def answer_help_command(call: types.CallbackQuery):
    await call.message.answer(text='Список команд представлен на клавиатуре',
                              reply_markup=commands_default_keyboard)
    await bot.delete_message(chat_id=call.message.chat.id,
                             message_id=call.message.message_id)

@dp.message_handler(commands=['item'])
async def answer_item_command(message: types.Message):
    _, item_info = data_manager.get_item(0)
    item_text = f'Название товара {item_info["name"]}:' \
                f'\nКоличество товара: {item_info["count"]}' \
                f'\nОписание: {item_info["description"]}'
    await message.answer(text=item_text,
                         reply_markup=get_item_inline_keyboard())

@dp.callback_query_handler(navigation_callback.filter(for_data='items'))
async def see_new_item(call: types.CallbackQuery):
    id = call.data.split(':')[-1]
    status, item_info = data_manager.get_item(int(id))
    item_text = f'Название товара {item_info["name"]}:' \
                f'\nКоличество товара: {item_info["count"]}' \
                f'\nОписание: {item_info["description"]}'
    await bot.edit_message_text(text=item_text,
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id)
    await bot.edit_message_reply_markup(reply_markup=get_item_inline_keyboard(id, status),
                                        chat_id=call.message.chat.id,
                                        message_id=call.message.message_id)

@dp.message_handler(text='Показать')
@dp.message_handler(commands='help')
async def answer_start_command(message: types.Message):
    await message.answer(text='Список команд представлен на клавиатуре',
                        reply_markup=commands_default_keyboard)

@dp.message_handler(text='Скрыть клавиатуру')
async def answer_start_command(message: types.Message):
    await message.answer(text='Мы ее спрятали!',
                        reply_markup=see_commands_default_keyboard)

@dp.message_handler(commands='add')
async def answer_start_command(message: types.Message):
    await message.answer(text='Позиция обавлена!')

# @dp.message_handler(commands='item')
# async def answer_start_command(message: types.Message):
#     await message.answer(text='У нас есть: редис, помидор и капуста')

@dp.message_handler(text=['Редис', 'Помидор', 'Капуста'])
async def answer_start_text(message: types.Message):
    await message.answer(text=f'У нас есть {message.text}!')  

@dp.message_handler(commands='info')
async def answer_start_command(message: types.Message):
    await message.answer(text='Что бы вы хотели узнать?',
                        reply_markup=info_default_keyboard)

@dp.message_handler(text=['О нас', 'Контакты', 'График работы', 'О боте', 'Меню'])
async def answer_start_text(message: types.Message):
    match message.text:
        case 'О нас':
            await message.answer(text=f'Мы представляем магазин Human - один из самых крупных овощных магазинов города!')
        case 'Контакты':
            await message.answer(text='Вы можете связаться с нами по номеру: 89233720994\n' +
                                'Также можете написать на почту: ideryusheva@inbox.ru') 
        case 'График работы':
            await message.answer(text='Работаем ПН-ПТ с 9:00 до 18:00\n' +
                                'СБ-ВС с 10:00 до 17:00')
        case 'О боте':
            await message.answer(text=f'Самый полезный бот в мире!\n' + 
                                'Для просмотра команд нажмите /help')
        case 'Меню':
            await message.answer(text='Начальное меню',
                                reply_markup=commands_default_keyboard)

@dp.message_handler(content_types=['contact'])
async def answer_start_text(message: types.Message):
    if message.from_user.id == message.contact.user_id:
        await message.answer(text='Это твой контакт!')  
    else:
        await message.answer(text='Это кто?!')
# reply_markup=ReplyKeyboardRemove()

@dp.message_handler(content_types=['location'])
async def answer_start_text(message: types.Message):
    await message.answer(text=f'Ваша геопозиция: широта - {message.location.latitude}, долгота - {message.location.longitude}')  
    print(message)