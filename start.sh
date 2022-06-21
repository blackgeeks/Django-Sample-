#!/bin/bash
import multiprocessing
# Start processes
echo Starting...
#exec daphne -b 0.0.0.0 -p 8000 hailu_backend.asgi:application
#exec daphne -b 0.0.0.0 -p 8000 hailu_backend.asgi:application & celery -A hailu_backend worker -B -l info
#exec  python manage.py crontab remove & python manage.py crontab add & daphne -b 0.0.0.0 -p 8000 hailu_backend.asgi:application  & celery -A hailu_backend worker -B -l info
exec  python manage.py runserver