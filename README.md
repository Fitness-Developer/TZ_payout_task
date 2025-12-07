# Backend Developer | Test Task

## Описание
Проект представляет собой REST-сервис для управления заявками на выплату средств.  
Каждая заявка создаётся через API и обрабатывается асинхронно с использованием Celery.  

---

## Технологический стек
- Python 3.10+
- Django 4.2+
- Django REST Framework (DRF)
- Celery + Redis
- PostgreSQL
- Docker & Docker Compose

---

## Модель данных
Сущность **Payout** содержит следующие поля:
- `id` — идентификатор заявки
- `amount` — сумма выплаты
- `currency` — валюта (3-буквенный код ISO)
- `recipient_name` — имя получателя
- `recipient_account` — реквизиты получателя
- `status` — статус заявки (`pending`, `processing`, `completed`, `failed`, `cancelled`)
- `created_at` — дата создания
- `updated_at` — дата обновления
- `description` — опциональное описание/комментарий

Валидация:
- Обязательные поля
- Положительная сумма
- Формат валюты — 3 буквы
- Ограничения по длине и формату текстовых полей

---

## REST API

| Метод | URL | Описание |
|-------|-----|----------|
| GET | `/api/payouts/` | Получение списка заявок |
| GET | `/api/payouts/{id}/` | Получение заявки по идентификатору |
| POST | `/api/payouts/` | Создание новой заявки |
| PATCH | `/api/payouts/{id}/` | Частичное обновление заявки (например, статус) |
| DELETE | `/api/payouts/{id}/` | Удаление заявки |


- Формат ошибок и ответов корректный и предсказуемый
- Асинхронная обработка с Celery: при создании заявки запускается задача, которая обновляет статус

---

## Запуск проекта

Выполнить клонирование репозитория.
```
git clone https://github.com/Fitness-Developer/TZ_payout_task.git
cd TZ_payout_task
```

### Запуск через Docker
Создайте файл .env.docker и скопируйте содержимое для запуска -
```
DJANGO_SECRET_KEY=dev-secret-docker
DEBUG=1

POSTGRES_DB=payouts
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432

CELERY_BROKER_URL=redis://redis:6379/0
CELERY_RESULT_BACKEND=redis://redis:6379/0
```
В консоль прописываем основную команду -
```
docker-compose up --build 
```
Для обновлений в будущем - 
```
docker-compose down 
```
После запуска, проект будет доступен по адресу - http://127.0.0.1:8000/api/payouts/

Миграции и тесты уже автоматически запускаются в docker-compose, чтобы руками не прописывать долго.
Отдельно для запуска тестов можно прописать - 
```
docker compose up test
```
Все API проверял через Postman, чтобы точно убедиться в их корректной работе.
Скриншоты, если нужно, могу прислать HR в лс.
 