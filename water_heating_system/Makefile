DJANGO_PROJECT=water_heating_system
DJANGO_SETTINGS_MODULE=water_heating_system.settings

all:
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver

clean:
    rm -rf *.pyc
    rm -rf __pycache__

shell:
    python manage.py shell

runserver:
    python manage.py runserver 0.0.0.0:8000

migrate:
    python manage.py migrate

makemigrations:
	python manage.py makemigrations
