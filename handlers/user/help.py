from aiogram import types
import logging
from utils.keyboards import *
from utils.config import *
from loader import *

logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=['help'])
async def help(message:types.Message):
    await message.answer("*Список команд 📑*\n\n*YouTube*\n/video - Скачать видео\n/audio - Скачать аудио из видео\n\n*Instagram*\n/reels - Скачать Reels\n/stories - Скачать историю\n/photo - Скачать фотографиию\
                         \n\n*TikTok*\n/tiktok - Скачать видео", parse_mode='markdown')