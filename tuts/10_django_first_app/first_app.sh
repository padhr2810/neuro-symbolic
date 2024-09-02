
django-admin startproject mysite
cd mysite
python3 manage.py migrate
python3 manage.py runserver
python3 manage.py runserver 127.0.0.1:8001

python3 manage.py startapp blog
python3 manage.py makemigrations blog

# now inspect SQL output of your first migration.
python3 manage.py sqlmigrate blog 0001

python3 manage.py migrate

python3 manage.py createsuperuser

python3 manage.py runserver

# to pp 26
