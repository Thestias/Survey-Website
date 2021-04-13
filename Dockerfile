# pull official base image
FROM python:3.8-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

# install psycopg2
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk del build-deps \
    && apk add postgresql-dev \
    && pip install psycopg2

# install dependencies
COPY ./requeriments.txt .
RUN pip install -r requeriments.txt

# copy project
COPY . .

RUN python manage.py collectstatic --settings=SurveyWebsite.settings.prod --noinput

# add and run as non-root user
RUN adduser -D surveyU
USER surveyU
