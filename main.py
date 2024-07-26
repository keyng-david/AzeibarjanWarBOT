import asyncio
import logging
import os
from aiohttp import web
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from utils.functions import clear_quests, schedule
from aiogram.types import Update
from handlers.start import router as start_router  # Import the start router
from handlers.inline import inline_router  # Import the inline router

logging.basicConfig(level=logging.INFO)

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

    dp.startup.register(on_startup)

    # Include the routers from start.py and inline.py
    dp.include_router(start_router)
    dp.include_router(inline_router)

    app = web.Application()
    app.router.add_post(f'/{TOKEN}', lambda request: handle_webhook(request, bot, dp))

    port = int(os.getenv("PORT", 5000))
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, port=port)
    await site.start()

    print(f'Server started at http://0.0.0.0:{port}')
    await asyncio.Event().wait()  # Keep the server running

if __name__ == '__main__':
    asyncio.run(main())