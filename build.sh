#!/usr/bin/env bash
# Exit on error
set -o errexit

echo "=== INSTALANDO DEPENDENCIAS ==="
pip install --upgrade pip
pip install -r requirements.txt

echo "=== APLICANDO MIGRACIONES ==="
python manage.py migrate

echo "=== COLECTANDO ARCHIVOS ESTÁTICOS ==="
python manage.py collectstatic --no-input --clear

echo "=== BUILD COMPLETADO ==="