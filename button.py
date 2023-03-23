from aiogram import types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


class Echo:
    kb = [
        [
            types.KeyboardButton(text="/inline1"),
            types.KeyboardButton(text="<3")
        ],

    ]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=kb, one_time_keyboard=True)


class Inline:
    inlinekb = [
        types.InlineKeyboardButton(text="GitHub", url="https://github.com/vvrl"),
        types.InlineKeyboardButton(text="VK",url="https://vk.com/a.zhirenko")
    ]


    inline_kb = types.InlineKeyboardMarkup(row_width=1)
    inline_kb.add(*inlinekb)
    