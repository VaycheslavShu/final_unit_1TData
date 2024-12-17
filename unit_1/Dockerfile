# FROM docker/whalesay:latest
# LABEL Name=unit1 Version=0.0.1
# RUN apt-get -y update && apt-get install -y fortunes
# CMD ["sh", "-c", "/usr/games/fortune -a | cowsay"]
# Используем базовый образ Python
FROM python:3.9-slim

# Создаем рабочую директорию
WORKDIR /app_count

# Копируем файл app.py в рабочую директорию
COPY app.py .

# Определяем команду запуска по умолчанию
CMD ["python", "app.py", "wildhunter"]
