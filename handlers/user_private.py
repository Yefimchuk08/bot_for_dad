from aiogram.types import Message
from aiogram import  F, Router
from aiogram.filters import CommandStart, Command
import common.function as fun
import os

router = Router()

@router.message(CommandStart())
async def commandStart(message:Message):
    await message.answer("Привіт, я бот який допоможе тобі зберегти твоє зображення у папку. Для початку роботи нажми на команду: /save або напиши цю команду на панелі введення.")
    
@router.message(Command("save"))
async def print(message:Message):
    await message.answer("Клас ти активував команду 'save' а тепер скидай фото яке треба зберегти в папку")
    
@router.message(F.photo)
async def handle_photo(message: Message):
    # Отримуємо найкраще за якістю фото (останнє у списку)
    photo = message.photo[-1]

    # Запитуємо користувача про назву файлу
    await message.answer("Введи назву для файлу:")

    # Далі вам потрібно отримати текст з наступного повідомлення
    @router.message(F.text)
    async def handle_file_name(message: Message):
        # Отримуємо назву файлу від користувача
        name = message.text  # Отримуємо текст повідомлення

        # Створюємо унікальний ідентифікатор для імені файлу
        import uuid
        unique_id = str(uuid.uuid4())

        # Завантажуємо файл з Telegram серверів
        file = await message.bot.get_file(photo.file_id)

        # Вказуємо шлях для збереження з унікальним ідентифікатором
        file_path = os.path.join(fun.folder_name, f"{name}_{unique_id}.jpg")

        # Завантажуємо та зберігаємо файл
        await message.bot.download_file(file.file_path, file_path)

        # Відповідаємо користувачу, що зображення збережене
        await message.answer(f"Фото збережено у папку: {file_path}")