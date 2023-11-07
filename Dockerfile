FROM python:3.11

LABEL org.opencontainers.image.source=https://github.com/EugZol/who_signed
LABEL org.opencontainers.image.description="Who signed bitcoin multisig transaction? This script can provide the answer."
LABEL org.opencontainers.image.licenses=MIT

ENV PYTHONDONTWRITEBYTECODE 1

RUN python -m pip install pipenv

WORKDIR /code

COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy --ignore-pipfile

COPY main.py .

CMD pipenv run python main.py