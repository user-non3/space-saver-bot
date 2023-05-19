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

@dp.message_handler(commands=['panel'])
async def panel(message:types.Message):
    #if message.from_user.id == admin_id:
        cursor = connect.cursor()
        cursor.execute(f"SELECT adminka FROM users WHERE id = {message.from_user.id};")
        adminka = cursor.fetchall()

        if adminka == 1:
            await message.answer("*Вы успешно авторизовались как Администратор 1 уровня! 👤*", parse_mode='markdown', reply_markup=button2)

        elif adminka == 2:
            await message.answer("*Вы успешно авторизовались как Разработчик! 👑*", parse_mode='markdown', reply_markup=button2)
        
        else:
            await message.answer("*У вас нету прав Администратора! ❌*", parse_mode='markdown')

    #else:
       # print(Fore.YELLOW, f"[Admin] Нету Доступа (/panel) - {message.from_user.full_name} ({message.from_user.id})")
        #await message.answer("Нет доступа ❌")