import os
from aiogram import Bot, Dispatcher, types
import asyncio
from dotenv import load_dotenv, find_dotenv

from User_private import user_private_router

load_dotenv(find_dotenv())
allow_updates = ['message, edited_message']
bot = Bot(token=os.getenv('API_TOKEN'))
dp = Dispatcher()

dp.include_router(user_private_router)


async def main():
    print('Server start')
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=allow_updates)


asyncio.run(main())
