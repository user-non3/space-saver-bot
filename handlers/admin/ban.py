from aiogram import types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from loader import *

from utils.keyboards import *
from utils.start_db import CustomDB
from utils.custom_states import *
from utils.config import *
from colorama import *
import logging

logging.basicConfig(level=logging.INFO)

@dp.callback_query_handler(lambda call: call)
async def all(call):
    if call.data == "blacklist":
        await addblock(call.message)

@dp.message_handler(commands=['addblock'])
async def addblock(message:types.Message):
    if message.from_user.id == admin_id:
        await message.answer("Введите ID аккаунта 🆔")
        await AddBlock.title.set()
    else:
        print(Fore.YELLOW, f"[Admin] Нету Доступа (/addblock) - {message.from_user.full_name} ({message.from_user.id})")
        await message.answer("Нет доступа ❌")

@dp.message_handler(state=AddBlock.title)
async def add_blocklist(message:types.Message, state:FSMContext):
    if message.text == "Отмена❌":
        await message.answer("Действие отменено! ✅", reply_markup=button)
        await state.finish()

    else:
        if message.text.isdigit():
            cursor = connect.cursor()
            cursor.execute(f"SELECT block FROM users WHERE id = {message.text}")
            user = cursor.fetchall()
            if len(user) == 0:
                await message.answer(f"Пользователь с таким ID не был найден в Базе Данных!")
                await state.finish()

            else:
                a = user[0]
                id = a[0]
                if id == 0:
                    cursor.execute(f"UPDATE users SET block = 1 WHERE id = {message.text};")
                    connect.commit()
                    await message.answer("Пользователь занесён в Чёрный Список ✅", reply_markup=button)
                    print(Fore.GREEN, f"[AddBlock] Пользователь занесён в Чёрный Список | {message.text}")
                    await state.finish()
                    await bot.send_message(message.text, f'*Здравствуйте! 👋*\n\nВы были заблокированны *Администратором* [{message.from_user.first_name}]({message.from_user.full_name})', parse_mode='markdown')
                
                else:
                    await message.reply("Пользователь с таким ID уже заблокированнын ❌")
                    await state.finish()

        else:
            await message.answer('*Ошибка* ❌\n\nВы вводите буквы, введите цифры!', parse_mode='markdown')

@dp.message_handler(commands=['deleteblock'])
async def deleteblock(message:types.Message):
    if message.from_user.id == admin_id:
        await message.answer("Введите ID аккаунта 🆔")
        await DeleteBlock.title.set()
    else:
        print(Fore.YELLOW, f"[Admin] Нету Доступа (/deleteblock) - {message.from_user.full_name} ({message.from_user.id})")
        await message.answer("Нет доступа ❌")

@dp.message_handler(state=DeleteBlock.title)
async def delete_blocklist(message:types.Message, state:FSMContext):
    if message.text.isdigit():
        cursor = connect.cursor()
        cursor.execute(f"SELECT block FROM users WHERE id = {message.text}")
        user = cursor.fetchone()
        connect.commit()

        if len(user) == 0:
            await message.answer(f"Пользователь с таким ID не был найден в Базе Данных!")
            await state.finish()
            
        else:
            a = user[0]
            id = a[0]
            if id == 1:
                cursor = connect.cursor()
                cursor.execute(f"UPDATE users SET block = 0 WHERE id = {message.text};")
                user = cursor.fetchone()
                connect.commit()
                await message.answer("Пользователь вынесен из Чёрный Список ✅")
                print(Fore.GREEN, f"[DeleteBlock] Пользователь вынесен из Чёрного списка | {message.text}")
                await state.finish()
                await bot.send_message(message.text, f'*Здравствуйте! 👋*\n\nВы были разблокированны *Администратором* [{message.from_user.first_name}]({message.from_user.full_name})', parse_mode='markdown')

            else:
                await message.reply(f"Пользователь с таким ID не был найден в Заблокированных!")
                await state.finish()
    else:
        await message.answer('*Ошибка* ❌\n\nВы вводите буквы, введите цифры!', parse_mode='markdown')