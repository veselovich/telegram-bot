from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6382580621:AAEPJWxXd57Df0kxEj0pSw-4vuCDLbi2lis'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет!\nЭто Эхо-бот\nОтправь мне любое сообщение, а я тебе обязательно отвечу.")

@dp.message_handler()
async def echo(message: types.Message):
   await message.answer(message.text)

if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)