# Heroku  

- cli: https://devcenter.heroku.com/articles/heroku-cli
- pipelines: https://devcenter.heroku.com/articles/pipelines

```sh  
brew tap heroku/brew && brew install heroku
```

## Django  

- [Corey Schafer: Python Django Tutorial: Deploying Your Application (Option #2) - Deploy using Heroku
](https://www.youtube.com/watch?v=6DI_7Zja8Zc)
  
There are changes you need to make in your django code so that it works with heroku

- add `requirements.txt` file to the main folder 
- creating environmental variables to hide secrets (optional but should have)
  
  ```sh 
  # locally 
  open ~/.zshrc # vi ~/.zshrc # vi ~/.bash_profile
  export DJANGO_DEBUG_VALUE="True" 
  
  # on heroku  
  heroku config:set DJANGO_DEBUG_VALUE="True" 
  
  # update on settings.py
  import os  
  os.environ.get('DJANGO_DEBUG_VALUE') 
  ```
  
- `settings.py` static root folder https://youtu.be/6DI_7Zja8Zc?t=1058
- `settings.py` - add allowed hosts 
  ```sh
   
  ```
- add `Procfile` 
- creating django user

```sh
heroku addons:create heroku-postgresql:hobby-dev
pip install django-heroku 

```

heroku logs --tail

python manage.py collectstatic --noinput 


## Deploy django app in heroku with poetry environment

- https://elements.heroku.com/buildpacks/moneymeets/python-poetry-buildpack
- https://stackoverflow.com/questions/67206439/deploy-django-app-in-heroku-with-poetry-environment

```shell
heroku buildpacks:clear
heroku buildpacks:add https://github.com/moneymeets/python-poetry-buildpack.git
heroku buildpacks:add heroku/python
```

