#!/bin/bash

echo "Apply DB migration"
python manage.py migrate

exec "$@"