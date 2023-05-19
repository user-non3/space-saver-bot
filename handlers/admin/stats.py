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
    if call.data == "stats":
        await stats(call.message)

@dp.message_handler(commands=['stats'])
async def stats(message: types.Message, state:FSMContext):
    if message.from_user.id == admin_id:
        cursor = connect.cursor()
        cursor.execute(f"SELECT * FROM users;")
        test = cursor.fetchall()
        await message.answer(f'*Статистика 📋*\n\nАккаунты: {len(test)}', parse_mode='markdown')
    
    else:
        print(Fore.YELLOW, f"[Admin] Нету Доступа (/stats) - {message.from_user.full_name} ({message.from_user.id})")
        await message.answer("Нет доступа ❌")