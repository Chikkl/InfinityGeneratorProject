# Используем базовый образ с Python
FROM python:3.10.12

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем зависимости (requirements.txt) в контейнер
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы из текущего каталога в контейнер
COPY . .

# Команда, которая будет выполнена при запуске контейнера
CMD ["python", "red_army.py"]
