import os
import shutil
import re

def copy_original_photos(photo_folder, destination_folder):
    image_extensions = [".jpg", ".jpeg", ".png"]

    for root, dirs, files in os.walk(photo_folder):
        for file in files:
            if any(file.endswith(ext) for ext in image_extensions) and "_thumb" not in file:
                photo_path = os.path.join(root, file)
                destination_path = os.path.join(destination_folder, file)

                if not os.path.exists(destination_path):
                    shutil.copy(photo_path, destination_path)

def copy_original_videos(video_folder, destination_folder):
    video_extensions = [".mp4", ".avi", ".mkv"]

    for root, dirs, files in os.walk(video_folder):
        for file in files:
            if any(file.endswith(ext) for ext in video_extensions) and "_thumb" not in file:
                video_path = os.path.join(root, file)
                destination_path = os.path.join(destination_folder, file)

                if not os.path.exists(destination_path):
                    shutil.copy(video_path, destination_path)

def copy_original_stickers(stickers_folder, destination_folder):
    sticker_extensions = [".webp"]

    for root, dirs, files in os.walk(stickers_folder):
        for file in files:
            if "_thumb" not in file:
                if re.match(r".*(?<!_\d)_thumb\.webp$", file) or re.match(r".*_thumb\d*\.webp$", file):
                    sticker_path = os.path.join(root, file)
                    destination_path = os.path.join(destination_folder, file)

                    if not os.path.exists(destination_path):
                        shutil.copy(sticker_path, destination_path)

# Решта коду залишається незмінним

# Шлях до папки з фото
photo_folder = "photos"

# Шлях до папки з відео
video_folder = "video_files"

# Шлях до папки зі стікерами
stickers_folder = "stickers"

# Шлях до папки, куди потрібно скопіювати оригінальні файли
destination_folder = "photos2"

# Копіюємо оригінальні фото
copy_original_photos(photo_folder, destination_folder)

# Копіюємо оригінальні відео
copy_original_videos(video_folder, destination_folder)

# Копіюємо оригінальні стікери
copy_original_stickers(stickers_folder, destination_folder)












# "photos" "video_files" "stickers" "photos2"