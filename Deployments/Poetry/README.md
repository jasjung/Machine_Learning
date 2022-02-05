# Poetry 

## Poetry with Django Project 

- https://stackoverflow.com/questions/60251799/how-to-start-a-new-django-project-using-poetry 
- https://davebaker.me/2020/07/19/setting-up-django-project-with-poetry/

```shell
poetry init --no-interaction --dependency django
poetry install
poetry run django-admin.py startproject djangodemo
# add whatever packages 
poetry add <package name>

# to run the project 
poetry run python manage.py runserver
```


## How to import requirements.txt from an existing project using Poetry

https://stackoverflow.com/questions/62764148/how-to-import-requirements-txt-from-an-existing-project-using-poetry

```shell
cat requirements.txt|xargs poetry add
```