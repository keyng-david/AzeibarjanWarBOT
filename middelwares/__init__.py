from aiogram import Dispatcher
from .LastActionMiddelware import TimeLastActionMiddleware

def setup(dp: Dispatcher):
    dp.update.middleware(TimeLastActionMiddleware())
