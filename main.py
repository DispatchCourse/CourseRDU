import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = "PASTE_YOUR_TOKEN_HERE"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: types.Message):
    await message.reply("Hello! I'm your remote dispatcher bot.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
