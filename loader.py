from aiogram import Bot, types, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from pytube import YouTube
import logging
import time
import os

from utils.keyboards import *
from utils.start_db import CustomDB
from utils.custom_states import *
from utils.config import *
from colorama import *
from tqdm import tqdm
from utils.set_bot_commands import set_default_commands


bot = Bot(token=token, parse_mode=types.ParseMode.HTML)

storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage)

db = CustomDB()
connect = db.connect
db.connect_db()

