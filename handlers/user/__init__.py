from aiogram import Router
from aiogram.filters import CommandStart, StateFilter, Text

import states
from filters import ChatTypeFilter
from . import start


def prepare_router():
    user_router = Router()
    user_router.message.filter(ChatTypeFilter("private"))

    user_router.message.register(start.start, CommandStart())
    user_router.message.register(
        start.start, Text("🏠В главное меню"), StateFilter(states.user.UserMainMenu.menu)
    )

    return user_router
