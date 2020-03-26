FROM python:3.7

RUN mkdir /code
WORKDIR code

COPY . /code
WORKDIR /code

RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile

ENTRYPOINT ["bash","/code/start.sh"]

