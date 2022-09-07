#!/bin/bash

pip install -U pip setuptools wheel
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
