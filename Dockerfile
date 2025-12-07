FROM python:3.10-slim

WORKDIR /code

COPY requirements.txt /code/

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /code

ENV PYTHONUNBUFFERED=1
ENV DJANGO_SECRET_KEY=dev-secret
ENV DEBUG=1

# Команда запуска по умолчанию: миграции + uvicorn
CMD bash -c "python manage.py makemigrations payouts && \
             python manage.py migrate && \
             uvicorn app.asgi:application --host 0.0.0.0 --port 8000"