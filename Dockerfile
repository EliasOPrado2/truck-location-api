FROM python:3.8.12
ENV PYTHONUNBUFFERED 1

WORKDIR  /usr/src/app
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install django-redis django-nose
RUN pip install -r requirements.txt


ENTRYPOINT ["bash", "docker-entrypoint.sh" ]

