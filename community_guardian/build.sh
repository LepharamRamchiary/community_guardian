#!/bin/bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Create necessary directories
mkdir -p var/data var/media var/static

# Collect static files
python manage.py collectstatic --no-input

# Make migrations
python manage.py makemigrations
python manage.py migrate

# Create a superuser (optional)
# If you want to create a superuser during deployment, uncomment the next line
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'password')" | python manage.py shell