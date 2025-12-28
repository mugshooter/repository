FROM python:3.9-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем список зависимостей и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код приложения
COPY app.py .

# Запускаем приложение через WSGI-сервер gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]