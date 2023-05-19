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

@dp.message_handler(commands=['admins'])
async def admins(message: types.Message):
    if message.from_user.id == admin_id:
        cursor = connect.cursor()
        cursor.execute(f"SELECT adminka FROM users;")
        results = cursor.fetchall()
        await message.answer(f'*Администраторы 👤*\n\n1 уровень: {len(results)}', parse_mode='markdown')

    else:
        print(Fore.YELLOW, f"[Admin] Нету Доступа (/admins) - {message.from_user.full_name} ({message.from_user.id})")
        await message.answer("Нет доступа ❌")

@dp.message_handler(commands=['addadmin'])
async def addadmin(message:types.Message):
    if message.from_user.id == admin_id:
        await message.answer("Введите ID аккаунта 🆔", reply_markup=cancel_button)
        await AddAdmin.title.set()
    else:
        print(Fore.YELLOW, f"[Admin] Нету Доступа (/addadmin) - {message.from_user.full_name} ({message.from_user.id})")
        await message.answer("Нет доступа ❌")

@dp.message_handler(state=AddAdmin.title)
async def send_addadmin(message:types.Message, state:FSMContext):
    if message.text == "Назад ❌":
        await message.answer("Действие отменено! ✅", reply_markup=button)
        await state.finish()

    else:
        if message.text.isdigit():
            cursor = connect.cursor()
            cursor.execute(f"SELECT admin FROM users WHERE id = {AddAdmin.title};")
            user = cursor.fetchall()
            cursor.execute(f"INSERT INTO adminka")
            if len(user) == 0:
                await message.answer(f"Пользователь с таким ID не был найден в Базе Данных!")
                await state.finish()

            else:
                a = user[0]
                id = a[0]
                if id == 0:
                    cursor.execute(f"UPDATE users SET adminka 1 WHERE id = {AddAdmin.title}")
                    connect.commit()
                    await message.answer("Администратор успешно добавлен ✅")
                    print(Fore.GREEN, f"[MakeAdmin] Администратор успешно добавлен | {AddAdmin.title}")
                    await state.finish()
                    await bot.send_message(DeleteBlock.title, f'*Здравствуйте! 👋*\n\nВам были выданы права *Администратора* 1 уровня от Создателя!')

                else:
                    await message.answer('У данного пользователя уже есть права Администратора 1 уровня\n\nЧто бы повысить нажмите на кнопку снизу!')
        
        else:
            await message.answer('*Ошибка* ❌\n\nВы вводите буквы, введите цифры!', parse_mode='markdown')

        

@dp.message_handler(commands=['deleteadmin'])
async def deleteadmin(message:types.Message):
    if message.from_user.id == admin_id:
        await message.answer("Введите ID аккаунта 🆔", reply_markup=cancel_button)
        await DeleteAdmin.title.set()
    else:
        print(Fore.YELLOW, f"[Admin] Нету Доступа (/deleteadmin) - {message.from_user.full_name} ({message.from_user.id})")
        await message.answer("Нет доступа ❌")

@dp.message_handler(state=DeleteAdmin.title)
async def send_deleteadmin(message:types.Message, state:FSMContext):
    if message.text == "Отмена ❌":
        await message.answer("Действие отменено! ✅", reply_markup=button)
        await state.finish()

    else:
        if message.text.isdigit():
            cursor = connect.cursor()
            cursor.execute(f"SELECT adminka FROM users WHERE id = {DeleteAdmin.title};")
            user = cursor.fetchall()
            connect.commit()
            
            if len(user) == 0:
                await message.answer(f"Пользователь с таким ID не был найден в Базе Данных!")
                await state.finish()
            
            else:
                a = user[0]
                id = a[0]

                if id == 1:
                    cursor = connect.cursor()
                    cursor.execute(f"UPDATE users SET adminka = 0 WHERE id = {DeleteAdmin.title};")
                    await message.answer("Администратор успешно снят ✅")
                    print(Fore.GREEN, f"[DeleteAdmin] Администратор успешно снят | {DeleteAdmin.title}")
                    await state.finish()
                    await bot.send_message(DeleteBlock.title, f'*Здравствуйте! 👋*\n\nВы были сняты Создателем!')

                else:
                    await message.answer("У данного пользователя нету прав Администратора!")
    
        else:
            await message.answer('*Ошибка* ❌\n\nВы вводите буквы, введите цифры!', parse_mode='markdown')
            