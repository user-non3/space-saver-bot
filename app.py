from aiogram import executor

from loader import *
import handlers
from utils.set_bot_commands import set_default_commands

logging.basicConfig(level=logging.INFO)

async def on_startup(dispatcher):
    await set_default_commands(dispatcher)

executor.start_polling(dp, on_startup=on_startup)