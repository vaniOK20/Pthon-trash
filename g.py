# https://i.9hentai.to/images/76258/
import requests
import os
import concurrent.futures
from urllib.parse import urlparse
from pathlib import Path

def get_extension(url):
    path = urlparse(url).path
    return Path(path).suffix or ''

def download_file(num, url, folder_path, file_extension):
    full_url = f'{url}{num}{file_extension}'
    file_path = os.path.join(folder_path, f'{num}{file_extension}')

    if os.path.exists(file_path):
        return
    
    response = requests.get(full_url)

    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)

if __name__ == '__main__':
    url = input('Введіть URL файлу: ')
    folder_path = input('Введіть шлях до папки для збереження файлу: ')

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    file_extension = get_extension(url)

    if not file_extension:
        file_extension = input('Введіть розширення файлу (наприклад, "jpg"): ')
        file_extension = f'.{file_extension}'

    num_photos = int(input('Введіть кількість фотографій для скачування: '))

    num_threads = 10

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(download_file, num, url, folder_path, file_extension) for num in range(1, num_photos + 1)]
        concurrent.futures.wait(futures)
