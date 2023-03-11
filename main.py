from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6271398524:AAG9J3hSFvFWfRTptYi7-6yRU8Urk0OoceU'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)