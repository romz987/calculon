# Используем базовый образ Python
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы requirements.txt и устанавливаем зависимости
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы в рабочую директорию
COPY . .

# Открываем порт
EXPOSE 5000

# Устанавливаем переменные окружения для Flask
ENV FLASK_APP=calculon_app
ENV FLASK_RUN_HOST=0.0.0.0

# Определяем команду для запуска приложения
CMD ["flask", "run"]

