from aiogram import types
import button as b
from main import dp
from parsing import parsing_weather



@dp.callback_query_handler(lambda c: c.data == 'weather_now')
async def send_weather_now(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text =parsing_weather())