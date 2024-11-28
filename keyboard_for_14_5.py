from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

"""создание клавиатуры и четырёх кнопок (главное меню)"""
start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Рассчитать"),
            KeyboardButton(text="Информация"),
            KeyboardButton(text='Регистрация')
        ],
        [KeyboardButton(text="Купить")]
    ], resize_keyboard=True
)

"""создание Inline меню из 4-х кнопок"""
catalog_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Product1', callback_data="product_buying"),
            InlineKeyboardButton(text='Product2', callback_data="product_buying"),
            InlineKeyboardButton(text='Product3', callback_data="product_buying"),
            InlineKeyboardButton(text='Product4', callback_data="product_buying")
        ]
    ]
)

