from aiogram import types
from aiogram.dispatcher.middlewares.base import BaseMiddleware

from database import DB

class TimeLastActionMiddleware(BaseMiddleware):
    def __init__(self) -> None:
        super().__init__()

    async def on_pre_process_message(self, message: types.Message, data: dict):
        if await DB.user_check(message.from_user.id):
            await DB.update_last_action(round(message.date.timestamp()), message.from_user.id)

    async def __call__(self, handler, event, data):
        if isinstance(event, types.Message):
            await self.on_pre_process_message(event, data)
        return await handler(event, data)

