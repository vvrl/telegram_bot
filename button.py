from aiogram import types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


class Reply:
    kb = [
        [
            types.KeyboardButton(text="Соц сети"),
            types.KeyboardButton(text="<3"),
            types.KeyboardButton(text="Погода")
        ],

    ]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=kb)


class Inline:
    inlinekb = [
        types.InlineKeyboardButton(text="GitHub", url="https://github.com/vvrl"),
        types.InlineKeyboardButton(text="VK",url="https://vk.com/a.zhirenko")
    ]

    weather = [
        types.InlineKeyboardButton(text="погода сейчас", callback_data='weather_now'),
        #types.InlineKeyboardButton(text="погода завтра")
    ]

    inline_kb = types.InlineKeyboardMarkup()
    inline_kb.add(*inlinekb)

    weather_kb = types.InlineKeyboardMarkup()
    weather_kb.add(*weather)
    