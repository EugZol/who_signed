FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1

RUN python -m pip install pipenv

WORKDIR /code

COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy --ignore-pipfile

COPY main.py .

CMD pipenv run python main.py