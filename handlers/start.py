import asyncio
import logging
from aiogram import types, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton

from database import DB
from loader import bot, dp
from src import dicts
from state import StartState
from utils import strings
from utils.class_getter import get_user_info
from utils.strings import start_NoneRegisterMessage
from utils.functions import ret_city, get_name_availability
from keyboards import default, inline
from filters.filter import IsPrivate

# Initialize Router
router = Router()

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Add a function to encapsulate the start game logic
async def start_game_logic(message: types.Message):
    if not await DB.user_check(message.from_user.id):
        args = message.text.split(maxsplit=1)[1:]
        if args:
            try:
                main_referal_id = int(args[0])
                if await DB.check_referal(message.from_user.id, main_referal_id):
                    await DB.add_refelal(main_referal_id, message.from_user.id)
                    user_info = await get_user_info(main_referal_id)
                    await DB.add_item_to_inventory(user_info.nickname, "potion", "regen_1")
                    await DB.add_item_to_inventory(user_info.nickname, "potion", "potion_xp_2")
                    await bot.send_message(main_referal_id, strings.you_have_new_referal)
            except ValueError:
                pass

        await DB.user_add(message.from_user.id, message.from_user.username)
        file = FSInputFile('utils/images/start.jpg')
        await bot.send_photo(
            message.from_user.id,
            caption=start_NoneRegisterMessage,
            photo=file,
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Start Game", callback_data="start_game")]])
        )
    else:
        user_info = await get_user_info(message.from_user.id)
        if user_info.course is None:
            file = FSInputFile('utils/images/start.jpg')
            await bot.send_photo(
                message.from_user.id,
                caption=start_NoneRegisterMessage,
                photo=file,
                reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Start Game", callback_data="start_game")]])
            )
        else:
            await ret_city(message.from_user.id)

# Message handler
@router.message(IsPrivate(), Command("start"))
async def start(message: types.Message):
    await start_game_logic(message)

# Callback query handler
@router.callback_query(lambda call: call.data == "start_game")
async def start(call: types.CallbackQuery):
    logging.debug(f"Received callback query: {call.data}")
    await bot.send_message(
        call.from_user.id,
        strings.start_choose_course_preview,
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Choose Course", callback_data="choose_course")]])
    )
    await StartState.course.set()

@router.callback_query(lambda call: call.data == "start_game_complite")
async def start_complite(call: types.CallbackQuery):
    await ret_city(call.from_user.id)

# Message handler with state
@router.message(StartState.name)
async def start_game_state(message: types.Message, state: FSMContext):
    aviable_name = await get_name_availability(message.text)
    if aviable_name == "not busy":
        await state.clear()
        await DB.set_nickname(message.text, message.from_user.id)
        await bot.send_message(
            message.from_user.id,
            strings.startRegistrationComplite,
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Complete Registration", callback_data="complete_registration")]])
        )
    elif aviable_name == "not_aviable":
        await bot.send_message(message.from_user.id, strings.startYourNameIsInvalid)
    else:
        await bot.send_message(message.from_user.id, strings.startYourNameIsBusy)

# Message handler with state for choosing course
@router.message(StartState.course)
async def choose_course(message: types.Message, state: FSMContext):
    try:
        await DB.set_course(dicts.course_variants[message.text], message.from_user.id)
        await bot.send_message(message.from_user.id, strings.startHi)
        await state.clear()
        await bot.send_message(
            message.from_user.id,
            strings.startWriteName,
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Send Nickname", callback_data="send_nickname")]])
        )
        await StartState.name.set()
    except KeyError:
        await bot.send_message(
            message.from_user.id,
            strings.start_choose_course_preview,
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Choose Course", callback_data="choose_course")]])
        )

    await asyncio.sleep(300)
    user_info = await get_user_info(message.from_user.id)
    if user_info.nickname is None:
        await bot.send_message(message.from_user.id, strings.startWriteNameIfWaiting)

# Register the router
dp.include_router(router)