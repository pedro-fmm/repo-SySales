FROM python:3.8

WORKDIR /app

RUN ls -la && pwd

COPY ./app /app

RUN ls -la && pwd

RUN pip install --upgrade pip 
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN ls -la && pwd
