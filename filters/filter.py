from aiogram.filters import BaseFilter
from aiogram import types

import config
from database import DB
from loader import bot
from utils import strings
from utils.class_getter import get_user_info


class IsPrivate(BaseFilter):
    async def __call__(self, message: types.Message) -> bool:
        return message.chat.type == types.ChatType.PRIVATE

class IsNotPrivate(BaseFilter):
    async def __call__(self, message: types.Message) -> bool:
        return message.chat.type != types.ChatType.PRIVATE

class IsAdmin(BaseFilter):
    async def __call__(self, message: types.Message) -> bool:
        return message.from_user.id in config.ADMIN_ID

class IsClanHead(BaseFilter):
    async def __call__(self, message: types.Message) -> bool:
        user_clan_info = await DB.get_clan_user(message.from_user.id)
        if user_clan_info is not None:
            if user_clan_info[2] == 2:
                return True
        else:
            await bot.send_message(message.from_user.id, strings.not_have_acces_head)
        return False

class IsClanHeadOrAdmin(BaseFilter):
    async def __call__(self, message: types.Message) -> bool:
        user_clan_info = await DB.get_clan_user(message.from_user.id)
        if user_clan_info is not None:
            if user_clan_info[2] == 2 or user_clan_info[2] == 1:
                return True
        else:
            await bot.send_message(message.from_user.id, strings.not_have_acces)
        return False

class UserInClan(BaseFilter):
    async def __call__(self, message: types.Message) -> bool:
        user_clan_info = await DB.get_clan_user(message.from_user.id)
        if user_clan_info is None:
            await bot.send_message(message.from_user.id, strings.not_in_clan)
            return False
        return True

class UserNotInClan(BaseFilter):
    async def __call__(self, message: types.Message) -> bool:
        user_clan_info = await DB.get_clan_user(message.from_user.id)
        if user_clan_info is not None:
            await bot.send_message(message.from_user.id, strings.you_already_in_clan)
            return False
        return True

class UserInCity(BaseFilter):
    async def __call__(self, message: types.Message) -> bool:
        user_info = await get_user_info(message.from_user.id)
        return user_info.city in strings.city_list[:-1]