FROM python:3.9-alpine

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev libffi-dev build-base \
    && rm -rf /var/cache/apk/*

WORKDIR /usr/src/app

ADD poetry.lock .
ADD pyproject.toml .
RUN pip install poetry==1.1.7 poetry-core==1.0.4 \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-dev

ADD src src

ADD docker/docker_entrypoint.sh .
RUN chmod +x /docker_entrypoint.sh
ENTRYPOINT ["/docker_entrypoint.sh"]
