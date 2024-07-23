from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
import config
from aiogram.enums import ParseMode

print("Token:", config.TOKEN)  # Ensure the token is correctly loaded

if not config.TOKEN:
    raise ValueError("Bot token is not provided or invalid")

bot = Bot(token=config.TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())