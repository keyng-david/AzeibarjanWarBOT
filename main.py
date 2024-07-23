import asyncio
import logging
import os
import time
from aiohttp import web
from aiogram import Bot, Dispatcher, types
from aiogram.types import Update, Message
from utils.functions import clear_quests, schedule

logging.basicConfig(level=logging.INFO)

# Dictionary to store the timestamp of the last command usage
user_last_command_time = {}

async def on_startup(dispatcher: Dispatcher):
    import middelwares  # Ensure this is the correct path
    from database import DB

    await DB.set_clan_war_next_war()
    asyncio.create_task(schedule())
    asyncio.create_task(clear_quests(2 * 60 * 60))
    middelwares.setup(dispatcher)

async def handle_webhook(request):
    try:
        data = await request.json()
        update = Update(**data)
        await dp.process_update(update)
        return web.Response(status=200)
    except Exception as e:
        logging.error(f"Error handling webhook: {e}")
        return web.Response(status=500)

async def main():
    from config import TOKEN  # Make sure the BOT_TOKEN is correctly imported
    from handlers import dp  # Import the handlers

    bot = Bot(token=TOKEN)
    dp = Dispatcher(bot)

    @dp.message(Command(commands=['start']))
    async def start_handler(message: Message):
        user_id = message.from_user.id
        current_time = time.time()
        throttle_rate = 2  # 2 seconds throttle rate

        if user_id in user_last_command_time:
            last_time = user_last_command_time[user_id]
            if current_time - last_time < throttle_rate:
                await message.reply(f"Too many requests! Try again in {throttle_rate - (current_time - last_time):.2f} seconds.")
                return

        user_last_command_time[user_id] = current_time
        await message.reply("Welcome! Let's start the game.")

    await on_startup(dp)

    app = web.Application()
    app.router.add_post(f'/{TOKEN}', handle_webhook)
    port = int(os.getenv("PORT", 5000))
    web.run_app(app, port=port)

if __name__ == '__main__':
    asyncio.run(main())
