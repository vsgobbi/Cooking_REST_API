#!/bin/bash

echo "Using virtual env"

source venv/bin/activate

echo "Making migrations"

./manage.py makemigrations core

sleep 2

./manage.py migrate

sleep 2

echo "Running django server..."

./manage.py runserver
