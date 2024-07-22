from aiogram import BaseMiddleware
from aiogram.types import Message
from aiogram.exceptions import Throttled
from aiogram.dispatcher.middlewares import ThrottlingMiddleware

class CustomThrottlingMiddleware(BaseMiddleware):
    def __init__(self, limit=1):
        self.rate_limit = limit
        super(CustomThrottlingMiddleware, self).__init__()

    async def __call__(self, handler, event, data):
        try:
            await self.on_process_event(event, data)
        except Throttled as t:
            await self.event_throttled(event, t)
            raise CancelHandler()

        return await handler(event, data)

    async def on_process_event(self, event, data):
        dispatcher = data['dispatcher']
        key = f"{event.from_user.id}:{event.chat.id}"
        throttling_data = await dispatcher.check_key_throttled(key, self.rate_limit)

        if throttling_data.is_throttled:
            raise Throttled(key=key, rate=self.rate_limit, user_id=event.from_user.id, chat_id=event.chat.id)

    async def event_throttled(self, event, throttled):
        delta = throttled.rate - throttled.delta
        await event.reply(f'Too many requests! Try again in {delta:.2f} seconds.')
