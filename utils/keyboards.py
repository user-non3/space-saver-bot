from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup

inline_buttons = [
    InlineKeyboardButton('Старт', callback_data='start'),
    InlineKeyboardButton('Скачать видео', callback_data='video'),
    InlineKeyboardButton('Скачать аудио', callback_data='audio')
]

button = InlineKeyboardMarkup().add(*inline_buttons)

share_keyboards = [
    KeyboardButton('Поделиться номером', request_contact=True),
    KeyboardButton('Отправить локацию', request_location=True)
]

share_button = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(*share_keyboards)

inline_buttons = [
    InlineKeyboardButton('Рассылка 📨', callback_data='mailing'),
    InlineKeyboardButton('Статистика 📃', callback_data='stats'),
    InlineKeyboardButton('Администраторы 👤', callback_data='admins'),
    InlineKeyboardButton('Чёрный список 📋', callback_data='blacklist')
]

button2 = InlineKeyboardMarkup().add(*inline_buttons)

cancel_button = [
    KeyboardButton('Отмена ❌')
]

cancel_button = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(*cancel_button)

inline_buttons = [
    InlineKeyboardButton('VIP Бронза 🥉', callback_data='vip_1'),
    InlineKeyboardButton('VIP Серебро 🥈', callback_data='vip_2'),
    InlineKeyboardButton('VIP Золото 🥇', callback_data='vip_3')
]

vip_btn = InlineKeyboardMarkup().add(*inline_buttons)

