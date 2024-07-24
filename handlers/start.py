from aiogram import types, Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils.callback_data import CallbackData

router = Dispatcher()

# Define the callback data factory
callback_factory = CallbackData("action", "data")

class StartState(StatesGroup):
    course = State()

@router.message(Command("start"))
async def start_game_logic(message: types.Message):
    await message.answer(
        "Welcome! Click the button below to start the game.",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[[InlineKeyboardButton(text="Start Game", callback_data=callback_factory.new(action="start_game", data=""))]]
        )
    )

@router.callback_query(Text(equals=callback_factory.filter(action="start_game")))
async def start(call: CallbackQuery, callback_data: dict):
    await call.message.answer(
        "Choose your course:",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[[InlineKeyboardButton(text="Choose Course", callback_data=callback_factory.new(action="choose_course", data=""))]]
        )
    )
    await StartState.course.set()

if __name__ == "__main__":
    bot = Bot(token="YOUR_BOT_TOKEN")
    dp = Dispatcher(bot, storage=MemoryStorage(), allowed_updates=["message", "callback_query"])
    dp.include_router(router)
    dp.run_polling()