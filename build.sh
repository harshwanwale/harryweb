#!/bin/bash
#build the project
echo"Building the Project...."
python -m pip install -r requirments.txt

echo "Make Migrations..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "Collect static..."
python manage.py collectstatic  --noinput --clear