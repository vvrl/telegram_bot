from aiogram import types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton


class Echo:
    kb = [
        [
            types.KeyboardButton(text="Сможешь повторить это?"),
            types.KeyboardButton(text="<3")
        ],

    ]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=kb)
