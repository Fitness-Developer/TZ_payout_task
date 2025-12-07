migrate:
    docker compose run --rm web python manage.py migrate

run:
    docker compose up web

worker:
    docker compose up worker

test:
    docker compose run --rm test