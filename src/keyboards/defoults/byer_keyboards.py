from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

commands_default_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='/start'),
            KeyboardButton(text='/item')
        ],
        [
            KeyboardButton(text='/help'),
            KeyboardButton(text='/info')
        ],
        [
            KeyboardButton(text='Поделиться контактом',
                            request_contact=True),
            KeyboardButton(text='Поделиться геопозицией',
                            request_location=True)
        ],
        [
            KeyboardButton(text='Скрыть клавиатуру')
        ]
    ],
    resize_keyboard=True
)

see_commands_default_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Показать')
        ]
    ],
    resize_keyboard=True
)

info_default_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='О нас'),
            KeyboardButton(text='Контакты')
        ],
        [
            KeyboardButton(text='График работы'),
            KeyboardButton(text='О боте')
        ],
        [
            KeyboardButton(text='Меню')
        ]
    ],
    resize_keyboard=True
)