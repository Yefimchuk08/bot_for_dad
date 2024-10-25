import os
from PIL import Image

folder_name = "image_folder"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
    print(f"Папка {folder_name} створена.")
else:
    print(f"Папка {folder_name} вже існує.")
async def save_image(file_path, file_name):
    try:
        # Відкриваємо зображення та зберігаємо його у вказану папку
        img = Image.open(file_path)
        new_image_path = os.path.join(folder_name, file_name)
        img.save(new_image_path)
        print(f"Зображення збережено у '{new_image_path}'.")
    except Exception as e:
        print(f"Помилка при збереженні зображення: {e}")
        
