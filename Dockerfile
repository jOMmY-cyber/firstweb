FROM python:3-slim

RUN pip install django==3.1.5

WORKDIR /jomproject
COPY . /jomproject

EXPOSE 8000
CMD ['python', 'manage.py', 'runserver', '0.0.0.0:8000']