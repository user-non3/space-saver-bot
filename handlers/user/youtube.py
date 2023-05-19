from aiogram import types
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
from loader import *

logging.basicConfig(level=logging.INFO)

def url_valid(url):
    try:
        YouTube(url).streams.first()
        return True
    except:
        return False
    
@dp.callback_query_handler(lambda call: call)
async def all(call):
    if call.data == "audio":
        await audio(call.message)
    elif call.data == "video":
        await video(call.message)
    
@dp.message_handler(commands=['audio'])
async def audio(message:types.Message):
    await message.reply("Отправьте ссылку на аудио и оно будет скачано. ✅")
    await DownloadAudio.downloadaud.set()

@dp.message_handler(state=DownloadAudio.downloadaud)
async def download_audio(message:types.Message, state:FSMContext):
    if url_valid(message.text) == True:
        print(Fore.GREEN, "[Download | Audio] Скачиваю аудио...")
        aud_yt = YouTube(message.text)
        await message.reply(f"*Скачиваем видео ⬇️*\n\n*Автор:* {aud_yt.author} 👤\n*Название:* {aud_yt.title}\n*Просмотры:* {aud_yt.views} 👁", parse_mode='markdown')
        audio = aud_yt.streams.filter(only_audio=True).first().download('audio', f'{aud_yt.title}.mp3')
        try:
            print(Fore.GREEN, "[Send | Audio] Отправляю аудио...")
            await message.answer("Отправляем аудио... ⬆️")
            with open(audio, 'rb') as down_audio:
                print(Fore.GREEN, "[Send | Audio] Аудио успешно отправлено!")
                await message.answer_audio(down_audio, caption="*🤖 Скачано @SpaceSaverBot*", parse_mode='markdown')
                os.remove(audio)
        except Exception as e:
            print(Fore.RED, f"[Error | Audio] Произошла ошибка: {e}")
            await message.answer("Произошла ошибка при скачивании! ❌")
            os.remove(audio)
    else:
            print(Fore.RED, "[Error | Audio] Ссылка недействительна, скачивание не возможно.")
            await message.reply("Отправленная вами ссылка недействительна. Отправьте ссылку на Youtube видео. ❌")
    await state.finish()

@dp.message_handler(commands=['video'])
async def video(message:types.Message):
    await message.reply("Отправьте ссылку на видео и оно будет скачано.")
    await DownloadVideo.download.set()

@dp.message_handler(state=DownloadVideo.download)
async def download_video(message:types.Message, state:FSMContext):
    if url_valid( message.text) == True:
        print(Fore.GREEN, "[Download | Video] Скачиваю видео...")
        yt = YouTube(message.text)
        await message.reply(f"*Скачиваем видео ⬇️*\n\n*Автор:* {yt.author} 👤\n*Название:* {yt.title}\n*Просмотры:* {yt.views} 👁", parse_mode='markdown')
        video = yt.streams.filter(progressive=True, file_extension="mp4").order_by('resolution').desc().first().download('video', f"{yt.title}.mp4")
        try:
            print(Fore.GREEN, "[Send | Video] Отправляю видео...")
            await message.answer("Отправляем видео... ⬆️")
            with open(video, 'rb') as down_video:
                print(Fore.GREEN, "[Send | Video] Видео успешно отправлено!")
                await message.answer_video(down_video, caption="*🤖 Скачано @SpaceSaverBot*", parse_mode='markdown')
                os.remove(video)
        except Exception as e:
            print(Fore.RED, f"[Error | Video] Произошла ошибка: {e}")
            await message.answer("Произошла ошибка при скачивании! ❌")
            os.remove(video)
    else:
        print(Fore.RED, "[Error | Video] Ссылка недействительна, скачивание не возможно.")
        await message.reply("Отправленная вами ссылка недействительна. Отправьте ссылку на Youtube видео. ❌")
    await state.finish()