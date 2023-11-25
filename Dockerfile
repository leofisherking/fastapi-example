FROM python:3.11.5
LABEL authors="Lev"

RUN mkdir /fastapi-example

WORKDIR /fastapi-example

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

WORKDIR .

RUN chmod a+x ./*.sh