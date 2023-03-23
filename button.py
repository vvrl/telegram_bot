from aiogram import types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


class Echo:
    kb = [
        [
            types.KeyboardButton(text="Соц сети"),
            types.KeyboardButton(text="<3")
        ],

    ]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=kb)


class Inline:
    inlinekb = [
        types.InlineKeyboardButton(text="GitHub", url="https://github.com/vvrl"),
        types.InlineKeyboardButton(text="VK",url="https://vk.com/a.zhirenko")
    ]


    inline_kb = types.InlineKeyboardMarkup()
    inline_kb.add(*inlinekb)
    