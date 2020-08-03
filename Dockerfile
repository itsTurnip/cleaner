FROM python:3.8-alpine

RUN apk add --no-cache gcc libffi-dev musl-dev openssl-dev

RUN pip install --no-cache-dir -U pip \
    && pip install --no-cache-dir poetry==1.0.9

WORKDIR /usr/src/app
COPY poetry.lock pyproject.toml /usr/src/app/

RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

COPY . /usr/src/app

CMD ["python", "/usr/src/app/run.py"]