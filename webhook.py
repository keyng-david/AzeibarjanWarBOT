from aiohttp import web
from aiogram import Bot, Dispatcher
from aiogram.types import Update
import config

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

async def handle_webhook(request):
    data = await request.json()
    update = Update(**data)
    await dp.process_update(update)
    return web.Response()

app = web.Application()
app.router.add_post(f"/{config.TOKEN}", handle_webhook)

if __name__ == "__main__":
    web.run_app(app, port=int(os.getenv("PORT", 5000)))