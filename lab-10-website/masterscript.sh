#!/bin/bash
cd ./mysite
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver | (sleep 3; firefox 127.0.0.1:8000/homepage/)

