from aiogram.filters import BaseFilter
from aiogram import types

import config
from database import DB
from loader import bot
from utils import strings
from utils.class_getter import get_user_info


class IsPrivate(BoundFilter):
    async def check(self, m: types.Message):
        return m.chat.type == types.ChatType.PRIVATE

class IsNotPrivate(BoundFilter):
    async def check(self, m: types.Message):
        return m.chat.type != types.ChatType.PRIVATE

class IsAdmin(BoundFilter):
    async def check(self, m: types.Message):
        return m.from_user.id in config.ADMIN_ID

class IsClanHead(BoundFilter):
    async def check(self, message: types.Message):
        user_clan_info = await DB.get_clan_user(message.from_user.id)
        if user_clan_info is not None:
            if user_clan_info[2] == 2:
                return True
        else:
            await bot.send_message(message.from_user.id, strings.not_have_acces_head)


class IsClanHeadOrAdmin(BaseFilter):
    async def check(self, message: types.Message):
        user_clan_info = await DB.get_clan_user(message.from_user.id)
        if user_clan_info is not None:
            if user_clan_info[2] == 2 or user_clan_info[2] == 1:
                return True
        else:
            await bot.send_message(message.from_user.id, strings.not_have_acces)


class UserInClan(BaseFilter):
    async def check(self, message: types.Message):
        user_clan_info = await DB.get_clan_user(message.from_user.id)
        if user_clan_info is None:
            await bot.send_message(message.from_user.id, strings.not_in_clan)
            return False
        return True


class UserNotInClan(BaseFilter):
    async def check(self, message: types.Message):
        user_clan_info = await DB.get_clan_user(message.from_user.id)
        if user_clan_info is not None:
            await bot.send_message(message.from_user.id, strings.you_already_in_clan)
            return False
        return True



class UserInCity(BaseFilter):
    async def check(self, message: types.Message):
        user_info = await get_user_info(message.from_user.id)
        return user_info.city in strings.city_list[:-1]
