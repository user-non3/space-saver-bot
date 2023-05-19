from aiogram.dispatcher.filters.state import StatesGroup, State

class DownloadVideo(StatesGroup):
    download = State()

class DownloadAudio(StatesGroup):
    downloadaud = State()

class Mail(StatesGroup):
    title = State()

class AddAdmin(StatesGroup):
    title = State()

class DeleteAdmin(StatesGroup):
    title = State()

class AddBlock(StatesGroup):
    title = State()

class DeleteBlock(StatesGroup):
    title = State()