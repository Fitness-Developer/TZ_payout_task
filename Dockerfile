FROM python:3.10-slim

# Установим рабочую директорию
WORKDIR /code

# Копируем зависимости
COPY requirements.txt /code/

# Устанавливаем зависимости
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копируем весь проект
COPY . /code

# Окружение
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SECRET_KEY=dev-secret
ENV DEBUG=1

# Команда запуска по умолчанию: миграции + uvicorn
CMD bash -c "python manage.py makemigrations payouts && \
             python manage.py migrate && \
             uvicorn app.asgi:application --host 0.0.0.0 --port 8000"