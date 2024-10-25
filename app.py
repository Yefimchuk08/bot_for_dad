from aiogram import Bot, Dispatcher
from dotenv import find_dotenv, load_dotenv
import os
import asyncio
from handlers.user_private import router

load_dotenv(find_dotenv())
bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher()  # Dispatcher створюється без аргументів

async def main():
    dp.include_router(router)  # Підключаємо роутер
    await dp.start_polling(bot)  # Запускаємо бота, передаючи об'єкт бота

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("End of work")
