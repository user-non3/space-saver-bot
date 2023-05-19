from aiogram import types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
import logging

from utils.keyboards import *
from utils.start_db import CustomDB
from utils.custom_states import *
from utils.config import *
from colorama import *
from loader import *

logging.basicConfig(level=logging.INFO)

@dp.callback_query_handler(lambda call: call)
async def all(call):
    if call.data == "mailing":
        await mailing(call.message)

@dp.message_handler(commands=['mailing'])
async def mailing(message:types.Message):
    if message.from_user.id == admin_id:
        await message.answer("Введите текст для рассылки: ")
        await Mail.title.set()
    else:
        print(Fore.YELLOW, f"[Admin] Нету Доступа (/mailing) - {message.from_user.full_name} ({message.from_user.id})")
        await message.answer("Нет доступа ❌")

@dp.message_handler(state=Mail.title)
async def send_mailing(message:types.Message, state:FSMContext):
    cursor = connect.cursor()
    cursor.execute(f"SELECT id FROM users;")
    users_id = cursor.fetchall()
    for id in users_id:
        await bot.send_message(id[0], message.text)
    await message.answer("Рассылка окончена ✅")
    await state.finish()