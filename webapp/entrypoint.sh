#!/bin/sh

export SECRET='123456'
# gunicorn -w "${GUNICORN_WORKERS:-3}" -b "${GUNICORN_BIND:-127.0.0.1:5000}" wsgi:app
python wsgi.py