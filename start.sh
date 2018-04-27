#!/bin/bash
echo "Upgrading pip"
pip install --upgrade pip

echo "Installing requirements"
pip install -r /webapp/requirements/dev.txt

echo "Waiting 30 second to wait the DB startup"
sleep 30

echo "Applying migrations"
python /webapp/manage.py migrate

echo "Creating superuser"
echo "from django.contrib.auth.models import User; User.objects.filter(email='admin@example.com').delete(); User.objects.create_superuser('admin', 'admin@example.com', 'clubinferno')" | python manage.py shell

echo "Running django server"
python /webapp/manage.py runserver 0.0.0.0:8000
