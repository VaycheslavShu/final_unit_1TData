import os
import sys
import argparse
from datetime import datetime

# Определяем путь, если он не закомментирован, иначе используем корневой каталог
# path = '/'
path = '/home/wildhunter/PycharmProjects'

def count_files(directory):
    return sum(len(files) for _, _, files in os.walk(directory))

def get_top_files_by_size(directory, top_n=10):
    file_sizes = []
    for dirpath, _, filenames in os.walk(directory):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            try:
                size = os.path.getsize(fp) / 1024  # Размер в КБ
                file_sizes.append((size, fp))
            except OSError:
                continue
    file_sizes.sort(reverse=True, key=lambda x: x[0])
    return file_sizes[:top_n]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Simple File Analyzer')
    parser.add_argument('--name', type=str, required=True, help='Vyacheslav')

    args = parser.parse_args()

    # Печатаем приветствие
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"Привет, {args.name}! Текущее время: {current_time}")

    # Вычисляем количество файлов
    total_files = count_files(path)
    print(f"Всего файлов: {total_files}")

    # Выводим топ-10 файлов по размеру
    top_files = get_top_files_by_size(path)
    print("Топ-10 файлов по размеру:")
    for size, filename in top_files:
        print(f"{filename}: {size:.2f} Кб")