# psycopg2-binary

I ran into the following error while trying to run `python manage.py runserver` on Django with Poetry. 


```sh 
django.core.exceptions.ImproperlyConfigured: Error loading psycopg2 module: dlopen(/Users/jason/Library/Caches/pypoetry/virtualenvs/django-app-heroku-ag2MNBO8-py3.8/lib/python3.8/site-packages/psycopg2/_psycopg.cpython-38-darwin.so, 0x0002): symbol not found in flat namespace '_PQbackendPID'
```

This error was insanely annoying to debug. I didn't have any issues with other virtual envs, but had this issue with Poetry. Long story short, specifying the package version solved this issue. 

```sh 
poetry add psycopg2-binary = "2.9.1"
```

My pyproject.toml file looked like the following: 

```sh 
[tool.poetry.dependencies]
python = "3.8.12"
Django = "^3.2.9"
numpy = "^1.21.4"
django-crispy-forms = "^1.13.0"
django-extensions = "^3.1.5"
pandas = "^1.3.4"
pytz = "^2021.3"
python-dateutil = "^2.8.2"
whitenoise = "^5.3.0"
dj-database-url = "^0.5.0"
django-on-heroku = "^1.1.2"
django-heroku = "^0.3.1"
gunicorn = "^20.1.0"
psycopg2-binary = "2.9.1"
```