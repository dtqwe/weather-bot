import asyncio
from aiogram import Dispatcher, Bot
from core.handlers.basic import router
from core.utils.commands import set_commands

import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

async def start_bot(bot: Bot):
    await set_commands(bot)

async def main():
    bot = Bot(os.getenv('TOKEN'))
    dp = Dispatcher()
    dp.include_router(router)
    dp.startup.register(start_bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass