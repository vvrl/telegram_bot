from datetime import datetime
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
import button as b
from parsing import parsing_weather
from config import API_TOKEN
import callback



bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет!\nОтправь мне любое сообщение, а я тебе обязательно отвечу.", reply_markup=b.Reply.keyboard)


@dp.message_handler(Text('Соц сети'))
async def send_social_media(message: types.Message):
    await message.answer("Ссылки на мои социальные сети",reply_markup=b.Inline.inline_kb)

@dp.message_handler(Text('Погода'))
async def send_weather(message: types.Message):
    await message.answer("ПОГОДА",reply_markup=b.Inline.weather_kb)

@dp.message_handler(Text('<3'))
async def send_heart(message: types.Message):
    await message.answer_sticker(r'CAACAgIAAxkBAAEIQctkHMsEFr1NuPceMjoXrfluWJuFpQACoBwAAipooUjogwEq_q_PRy8E')


@dp.message_handler(commands=['date'])
async def send_date(message: types.Message):
    dt = datetime.now()
    await message.reply(dt.strftime("%A, %d. %B %Y %I:%M%p"))
    
# @dp.callback_query_handler(lambda c: c.data == 'weather_now')
# # async def send_weather_now(message: types.Message):
# #     await message.reply(parsing_weather())
# async def send_weather_now(callback_query: types.CallbackQuery):
#     await callback_query.message.answer(parsing_weather())

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)
 
if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)