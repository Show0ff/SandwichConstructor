# Используйте официальный образ Python
FROM python:3.8-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Устанавливаем переменные окружения для Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Устанавливаем зависимости для работы с PostgreSQL и компиляции
RUN apt-get update && apt-get install -y libpq-dev gcc

# Устанавливаем зависимости Python
RUN pip install --upgrade pip
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Копируем проект в контейнер
COPY . /app
