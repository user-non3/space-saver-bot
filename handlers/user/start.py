import time

from utils.keyboards import *
from utils.start_db import CustomDB
from utils.custom_states import *
from utils.config import *
from colorama import *
from aiogram.dispatcher import FSMContext
from loader import *
from aiogram import types

@dp.message_handler(commands=['start'])
async def start(message:types.Message):
    cursor = connect.cursor()
    cursor.execute(f"SELECT id FROM users WHERE id = {message.from_user.id};")
    #cursor.execute(f"SELECT block FROM users WHERE id = {message.from_user.id};")
    #ban = cursor.fetchall()
    res = cursor.fetchall()
    if res == []:
        cursor.execute(f"INSERT INTO users VALUES ('{message.from_user.username}', '{message.from_user.first_name}', '{message.from_user.last_name}', {message.from_user.id}, '{time.ctime()}', '0', '0', '0', '0');")
        print(f"[User] Зарегистрирован новый пользователь! | {message.from_user.id}")

    #elif ban == 1:
        #await message.reply(f"*Вы заблокированны в боте! ❌*", parse_mode='markdown')
        #print(Fore.RED, f"[User-Blocked] Заблокированный пользователь пытался воспользоваться ботом! | {message.from_user.username} ({message.from_user.id})")

    await message.answer(f'Здравствуйте {message.from_user.full_name} 👋')
    await message.answer("Этот бот способен скачивать видео или аудио с платформы Youtube. 🎞\nЕсли запутаетесь в командах напишите /help 🆘", reply_markup=button)
    connect.commit()