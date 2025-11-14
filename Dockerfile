# 1. Базовый образ
FROM python:3.12-slim

# 2. Рабочая директория
WORKDIR /app

# 3. Копируем файлы проекта
COPY . /app

# 4. Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# 5. Команда запуска
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]