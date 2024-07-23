import asyncio
import logging
import os
import time
from aiohttp import web
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
from aiogram.types import Update, Message
from handlers.start import start_game_logic  # Import the function here
from utils.functions import clear_quests, schedule

logging.basicConfig(level=logging.INFO)

# Dictionary to store the timestamp of the last command usage
user_last_command_time = {}

# New class-based handler for start command
class StartHandler:
    async def __call__(self, message: Message):
        user_id = message.from_user.id
        current_time = time.time()
        throttle_rate = 2  # 2 seconds throttle rate

        if user_id in user_last_command_time:
            last_time = user_last_command_time[user_id]
            if current_time - last_time < throttle_rate:
                await message.reply(f"Too many requests! Try again in {throttle_rate - (current_time - last_time):.2f} seconds.")
                return

        user_last_command_time[user_id] = current_time
        await start_game_logic(message)

async def on_startup(dispatcher: Dispatcher):
    import middlewares  # Ensure this is the correct path
    from database import DB

    await DB.set_clan_war_next_war()
    asyncio.create_task(schedule())
    asyncio.create_task(clear_quests(2 * 60 * 60))
    middlewares.setup(dispatcher)

async def handle_webhook(request, bot, dp):
    try:
        body = await request.text()
        update = Update.parse_raw(body)
        await dp.feed_update(bot, update)
        return web.Response(status=200)
    except Exception as e:
        logging.error(f"Error handling webhook: {e}")
        return web.Response(status=500)

async def main():
    from config import TOKEN  # Make sure the BOT_TOKEN is correctly imported

    bot = Bot(token=TOKEN)
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)

    # Register the class-based start handler
    dp.message.register(StartHandler(), Command(commands=['start']))

    dp.startup.register(on_startup)

    app = web.Application()

    # Pass bot and dp to the handle_webhook function
    app.router.add_post(f'/{TOKEN}', lambda request: handle_webhook(request, bot, dp))

    port = int(os.getenv("PORT", 5000))

    # This part is adjusted to use the existing event loop
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, port=port)
    await site.start()

    print(f'Server started at http://0.0.0.0:{port}')
    await asyncio.Event().wait()  # Keep the server running

if __name__ == '__main__':
    asyncio.run(main())