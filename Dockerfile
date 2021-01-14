FROM python:3.7-slim as base

RUN apt-get update && apt-get install -y git

ENV PYTHONUNBUFFERED=1

WORKDIR /bot

COPY requirements ./requirements

RUN python -m venv /venv
RUN . /venv/bin/activate && pip install -r requirements/prod.txt

COPY src ./src
COPY .env docker-entrypoint.sh ./

RUN chmod +x docker-entrypoint.sh
CMD ["./docker-entrypoint.sh"]
