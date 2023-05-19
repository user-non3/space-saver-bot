from utils.keyboards import *
from utils.start_db import CustomDB
from utils.custom_states import *
from utils.config import *
from colorama import *
from aiogram.dispatcher import FSMContext
from loader import *
from aiogram import types

logging.basicConfig(level=logging.INFO)

@dp.callback_query_handler(lambda call: call)
async def all(call):
    if call.data == "vip_1":
        await vip_1(call.message)
    elif call.data == "vip_2":
        await vip_2(call.message)
    elif call.data == "vip_3":
        await vip_3(call.message)

@dp.message_handler(commands=['vip'])
async def vip(message: types.Message):
    if message.chat.type == 'private':
        cursor = connect.cursor()
        cursor.execute(f"SELECT vip FROM users WHERE id = {message.from_user.id}")
        cursor.execute(f"SELECT vip_time FROM users WHERE id = {message.from_user.id}")
        vip = cursor.fetchall()
        vip_time = cursor.fetchall()

        if vip == 1:
            await message.reply(f'*У вас VIP Бронза 🥉*\n\nДействует до {vip_time}', parse_mode='markdown')

        elif vip == 2:
            await message.reply(f'*У вас VIP Серебро 🥈*\n\nДействует до {vip_time}', parse_mode='markdown')

        elif vip == 3:
            await message.reply(f'*У вас VIP Золото 🥇*\n\nДействует до {vip_time}', parse_mode='markdown')

        else:
            await message.reply(f'*У вас отсутствует VIP ❌*\n\n*Что дает VIP? 🤔*\n- Пропадает ограничение скачивании 10 видео в день\n\n*Что бы купить VIP-статус нажмите на кнопки ниже!', parse_mode='markdown', reply_markup=vip_btn)


@dp.message_handler(commands=['vip_1'])
async def vip_1(message: types.Message):
    if message.chat.type == 'private':
        cursor = connect.cursor()
        cursor.execute(f"SELECT vip FROM users WHERE id = {message.from_user.id}")
        cursor.execute(f"SELECT vip_time FROM users WHERE id = {message.from_user.id}")
        vip = cursor.fetchall()
        vip_time = cursor.fetchall()
        if vip != 0:
            await message.answer(f"*У вас уже имеется статус VIP {vip}*\n\nАктивен до {vip_time}", parse_mode='markdown')
        
        else:
            admin_btn = InlineKeyboardMarkup(
                inline_keyboard=[
                    [InlineKeyboardButton(text="Администратор 👤", callback_data=f"")]
                ]
            )
            await message.answer(f"*Что бы купить VIP статус, вы должны отписать Администратору бота:* @akbaraliev.110", parse_mode='markdown', reply_markup=admin_btn)

@dp.message_handler(commands=['vip_2'])
async def vip_2(message: types.Message):
    if message.chat.type == 'private':
        cursor = connect.cursor()
        cursor.execute(f"SELECT vip FROM users WHERE id = {message.from_user.id}")
        cursor.execute(f"SELECT vip_time FROM users WHERE id = {message.from_user.id}")
        vip = cursor.fetchall()
        vip_time = cursor.fetchall()
        if vip != 0:
            await message.answer(f"*У вас уже имеется статус VIP {vip}*\n\nАктивен до {vip_time}", parse_mode='markdown')
        
        else:
            admin_btn = InlineKeyboardMarkup(
                inline_keyboard=[
                    [InlineKeyboardButton(text="Администратор 👤", callback_data=f"")]
                ]
            )
            await message.answer(f"*Что бы купить VIP статус, вы должны отписать Администратору бота:* @akbaraliev.110", parse_mode='markdown', reply_markup=admin_btn)

@dp.message_handler(commands=['vip_3'])
async def vip_3(message: types.Message):
    if message.chat.type == 'private':
        cursor = connect.cursor()
        cursor.execute(f"SELECT vip FROM users WHERE id = {message.from_user.id}")
        cursor.execute(f"SELECT vip_time FROM users WHERE id = {message.from_user.id}")
        vip = cursor.fetchall()
        vip_time = cursor.fetchall()
        if vip != 0:
            await message.answer(f"*У вас уже имеется статус VIP {vip}*\n\nАктивен до {vip_time}", parse_mode='markdown')
        
        else:
            admin_btn = InlineKeyboardMarkup(
                inline_keyboard=[
                    [InlineKeyboardButton(text="Администратор 👤", callback_data=f"")]
                ]
            )
            await message.answer(f"*Что бы купить VIP статус, вы должны отписать Администратору бота:* @akbaraliev.110", parse_mode='markdown', reply_markup=admin_btn)

        
        