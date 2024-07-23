import asyncio
from aiogram import types, Router
from aiogram.filters import Command
from database import DB
from loader import bot, dp
from src import dicts
from state import states
from utils import strings
from utils.class_getter import get_user_info
from utils.strings import start_NoneRegisterMessage
from utils.functions import ret_city, get_name_availability
from keyboards import default, inline
from filters.filter import IsPrivate

# Initialize Router
router = Router()

# Add a function to encapsulate the start game logic
async def start_game_logic(message: types.Message):
    if not await DB.user_check(message.from_user.id):
        args = message.get_args()
        if args:
            try:
                main_referal_id = int(args)
                if await DB.check_referal(message.from_user.id, main_referal_id):
                    await DB.add_refelal(main_referal_id, message.from_user.id)
                    user_info = await get_user_info(main_referal_id)
                    await DB.add_item_to_inventory(user_info.nickname, "potion", "regen_1")
                    await DB.add_item_to_inventory(user_info.nickname, "potion", "potion_xp_2")
                    await bot.send_message(main_referal_id, strings.you_have_new_referal)
            except ValueError:
                pass

        await DB.user_add(message.from_user.id, message.from_user.username)
        await bot.send_photo(message.from_user.id, caption=start_NoneRegisterMessage,
                             photo=types.InputFile('utils/images/start.jpg'),
                             reply_markup=await inline.start_game())
    else:
        user_info = await get_user_info(message.from_user.id)
        if user_info.course is None:
            await bot.send_photo(message.from_user.id, caption=start_NoneRegisterMessage,
                                 photo=types.InputFile("utils/images/start.jpg"), reply_markup=await inline.start_game())
        else:
            await ret_city(message.from_user.id)

# Message handler
@router.message(IsPrivate(), Command("start"))
async def start(message: types.Message):
    await start_game_logic(message)

# Callback query handler
@router.callback_query(lambda call: call.data == "start_game")
async def start(call: types.CallbackQuery):
    await bot.send_message(call.from_user.id, strings.start_choose_course_preview,
                           reply_markup=await default.buttons_start_choose_course())
    await states.StartState.course.set()

@router.callback_query(lambda call: call.data == "start_game_complite")
async def start_complite(call: types.CallbackQuery):
    await ret_city(call.from_user.id)

# Message handler with state
@router.message(state=states.StartState.name)
async def start_game_state(message: types.Message, state: FSMContext):
    aviable_name = await get_name_availability(message.text)
    if aviable_name == "not busy":
        await state.clear()
        await DB.set_nickname(message.text, message.from_user.id)
        await bot.send_message(message.from_user.id, strings.startRegistrationComplite,
                               reply_markup=await inline.start_compliteReg())
    elif aviable_name == "not_aviable":
        await bot.send_message(message.from_user.id, strings.startYourNameIsInvalid)
    else:
        await bot.send_message(message.from_user.id, strings.startYourNameIsBusy)

# Message handler with state for choosing course
@router.message(state=states.StartState.course)
async def choose_course(message: types.Message, state: FSMContext):
    try:
        await DB.set_course(dicts.course_variants[message.text], message.from_user.id)
        await bot.send_message(message.from_user.id, strings.startHi)
        await state.clear()
        await bot.send_message(message.from_user.id, strings.startWriteName,
                               reply_markup=await default.button_start_send_nickname(message) if message.from_user.username is not None else await default.get_fight_res_button(
                                   strings.choice_name))
        await states.StartState.name.set()
    except KeyError:
        await bot.send_message(message.from_user.id, strings.start_choose_course_preview,
                               reply_markup=await default.buttons_start_choose_course())

    await asyncio.sleep(300)
    user_info = await get_user_info(message.from_user.id)
    if user_info.nickname is None:
        await bot.send_message(message.from_user.id, strings.startWriteNameIfWaiting)

# Register the router
dp.include_router(router)