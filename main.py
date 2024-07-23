import asyncio
import logging
import time
from utils.functions import clear_quests, schedule
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message

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
    

    # Set webhook
    webhook_url = f"https://{os.getenv('HEROKU_APP_NAME')}.herokuapp.com/{os.getenv('TOKEN')}"
    await bot.set_webhook(webhook_url)

async def main():
    from config import TOKEN  # Make sure the BOT_TOKEN is correctly imported
    from handlers import dp  # Import the handlers

    bot = Bot(token=TOKEN)
    dp = Dispatcher()

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
        # Call the game start logic here, e.g., sending a message or initializing game state.
        # Example: await some_function_to_start_the_game(message)

    await on_startup(dp)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

