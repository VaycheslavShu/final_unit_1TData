import os
import sys
from datetime import datetime

   # Определите путь; по умолчанию это корневой каталог.
path = "/home/wildhunter/practicum_python/"  # Раскомментируйте и укажите нужный путь, если требуется другой
path = os.getenv('SEARCH_PATH', '/')  # Позволяет использовать переменную окружения

def count_files(path):
    return sum([len(files) for r, d, files in os.walk(path)])

def get_top_10_files(path):
    file_sizes = {}
    for root, dirs, files in os.walk(path):
        for name in files:
            filepath = os.path.join(root, name)
            try:
                file_size = os.path.getsize(filepath) / 1024  # размер в килобайтах
                file_sizes[filepath] = file_size
            except FileNotFoundError:
                continue

    top_10_files = sorted(file_sizes.items(), key=lambda item: item[1], reverse=True)[:10]
    return top_10_files

def greet_user(name):
    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f"Привет, {name}! Текущая дата и время: {current_datetime}"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        name = sys.argv[1]
        print(greet_user(name))
    print(f"Количество файлов в '{path}': {count_files(path)}")
    print("Топ-10 файлов по размеру:")
    for filepath, size in get_top_10_files(path):
        print(f"{filepath}: {size:.2f} КБ")