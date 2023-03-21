from datetime import datetime
from aiogram import Bot, Dispatcher, executor, types
from button import Echo
from config import API_TOKEN



bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет!\nЯ Эхобот от Skillbox!\nОтправь мне любое сообщение, а я тебе обязательно отвечу.", reply_markup=Echo.keyboard)



@dp.message_handler(commands=['date'])
async def send_date(message: types.Message):
    dt = datetime.now()
    await message.reply(dt.strftime("%A, %d. %B %Y %I:%M%p"))
    


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)
 
if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)