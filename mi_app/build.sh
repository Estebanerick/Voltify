#!/usr/bin/env bash
# Exit on error
set -o errexit

# Apply migrations
python manage.py migrate

# Create superuser (opcional, solo para desarrollo)
# echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'admin123') if not User.objects.filter(username='admin').exists() else None" | python manage.py shell

# Collect static files
python manage.py collectstatic --no-input

# Load initial data if exists
# python manage.py loaddata initial_data.json 2>/dev/null || true