import asyncio
import logging
from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile

from database import DB
from loader import bot, dp
from src import dicts
from state import states
from state.states import StartState
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
    logging.debug(f"start_game_logic called with message: {message.text}")
    if not await DB.user_check(message.from_user.id):
        logging.debug(f"User {message.from_user.id} does not exist in DB.")
        args = message.text.split(maxsplit=1)[1:]
        if args:
            try:
                main_referal_id = int(args[0])
                if await DB.check_referal(message.from_user.id, main_referal_id):
                    logging.debug(f"User {message.from_user.id} has a valid referral: {main_referal_id}.")
                    await DB.add_refelal(main_referal_id, message.from_user.id)
                    user_info = await get_user_info(main_referal_id)
                    await DB.add_item_to_inventory(user_info.nickname, "potion", "regen_1")
                    await DB.add_item_to_inventory(user_info.nickname, "potion", "potion_xp_2")
                    await bot.send_message(main_referal_id, strings.you_have_new_referal)
            except ValueError:
                logging.debug(f"Invalid referral ID: {args[0]}")

        await DB.user_add(message.from_user.id, message.from_user.username)
        file = FSInputFile('utils/images/start.jpg')
        await bot.send_photo(
            message.from_user.id,
            caption=start_NoneRegisterMessage,
            photo=file,
            reply_markup=await inline.start_game()  # Using the original function call here
        )
    else:
        logging.debug(f"User {message.from_user.id} already exists in DB.")
        user_info = await get_user_info(message.from_user.id)
        if user_info.course is None:
            logging.debug(f"User {message.from_user.id} has no course.")
            file = FSInputFile('utils/images/start.jpg')
            await bot.send_photo(
                message.from_user.id,
                caption=start_NoneRegisterMessage,
                photo=file,
                reply_markup=await inline.start_game()  # Using the original function call here
            )
        else:
            await ret_city(message.from_user.id)

# Message handler
@router.message(IsPrivate(), Command("start"))
async def start(message: types.Message):
    logging.debug(f"Received /start command from user {message.from_user.id}")
    await start_game_logic(message)

# Callback query handler for "Start Game"
@router.callback_query(F.data == "start_game")
async def start_game(call: types.CallbackQuery, state: FSMContext):
    logging.debug(f"Received callback query with data: {call.data} from user {call.from_user.id}")
    await call.answer()  # Answer the callback query to acknowledge it
    await bot.send_message(
        call.from_user.id,
        strings.start_choose_course_preview,
        reply_markup=await default.buttons_start_choose_course()  # Using the original function call here
    )
    await state.set_state(StartState.course)

# Message handler with state for choosing course
@router.message(StartState.course)
async def choose_course(message: types.Message, state: FSMContext):
    logging.debug(f"Received state message with course: {message.text} from user {message.from_user.id}")
    try:
        await DB.set_course(dicts.course_variants[message.text], message.from_user.id)
        await bot.send_message(message.from_user.id, strings.startHi)
        await state.set_state(StartState.name)
        await bot.send_message(
            message.from_user.id,
            strings.startWriteName,
            reply_markup=await default.button_start_send_nickname()  # Using the original function call here
        )
    except KeyError:
        logging.debug(f"Invalid course: {message.text}")
        await bot.send_message(
            message.from_user.id,
            strings.start_choose_course_preview,
            reply_markup=await default.buttons_start_choose_course()  # Using the original function call here
        )

    await asyncio.sleep(300)
    user_info = await get_user_info(message.from_user.id)
    if user_info.nickname is None:
        await bot.send_message(message.from_user.id, strings.startWriteNameIfWaiting)

# Message handler with state for setting nickname
@router.message(StartState.name)
async def start_game_state(message: types.Message, state: FSMContext):
    logging.debug(f"Received state message with name: {message.text} from user {message.from_user.id}")
    aviable_name = await get_name_availability(message.text)
    if aviable_name == "not busy":
        await DB.set_nickname(message.text, message.from_user.id)
        await bot.send_message(
            message.from_user.id,
            strings.startRegistrationComplite,
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Complete Registration", callback_data="complete_registration")]])
        )
        await state.clear()
    elif aviable_name == "not_aviable":
        await bot.send_message(message.from_user.id, strings.startYourNameIsInvalid)
    else:
        await bot.send_message(message.from_user.id, strings.startYourNameIsBusy)

# Register the router
dp.include_router(router)