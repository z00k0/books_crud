cd books
python manage.py makemigrations --noinput
python manage.py migrate

echo """
import books.on_startapp
""" | python manage.py shell

# daphne -b 0.0.0.0 -p 8000 settings.asgi:application
python manage.py runserver 0.0.0.0:8000