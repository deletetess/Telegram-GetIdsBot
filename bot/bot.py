import asyncio
from os import environ
from dotenv import load_dotenv
from aiogram import Dispatcher, Bot
from router import router
import logging
from middlewares import setup

env = load_dotenv()
token = environ.get("BOT_TOKEN")

async def main():
    bot = Bot(token, parse_mode="HTML", disable_web_page_preview=True)
    dp = Dispatcher()
    
    dp.include_router(router)
    
    setup(dp)
    # await bot.delete_webhook(drop_pending_updates=True) # Не обрабатывает полностью
    await bot.get_updates(offset=-1) # Только последнее сообщение
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.error("BOT CLOSED!")