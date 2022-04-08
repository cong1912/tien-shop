# syntax=docker/dockerfile:1
FROM python:3.8
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt

RUN apt-get update -y
RUN apt-get install -y gettext

# python manage.py migrate

COPY . /code/
