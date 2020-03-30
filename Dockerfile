FROM python:3.7

RUN apt-get update && apt-get install procps build-essential libssl-dev libffi-dev python-dev libmemcached-dev --yes

RUN mkdir /code
WORKDIR code

COPY . /code
WORKDIR /code

RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile
