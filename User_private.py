from aiogram import Router, types
from aiogram.filters import CommandStart, Command


user_private_router = Router()


@user_private_router.message(CommandStart())
async def send_welcome(message: types.Message):
    name = message.from_user.full_name
    await message.answer(f'Привет {name}, я бот Первого ТВЧ. '
                         f'\nВыбери тему сообщения и я его обязательно передам в Техподдержку')


@user_private_router.message(Command('menu'))
async def menu_cmd(message: types.Message):
    name = message.from_user.full_name
    await message.reply(f"Сейчас, {name}, я покажу тебе меню.")
