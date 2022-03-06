FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
# RUN apk update \
#    && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/