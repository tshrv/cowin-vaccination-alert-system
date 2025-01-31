# syntax=docker/dockerfile:1
FROM python:3.9.5

WORKDIR /app
COPY requirements requirements
RUN pip install -r requirements/production.txt

COPY . .
