# Elastic BeanStalk 

```sh 
pip install awsebcli --upgrade --user
pip uninstall awsebcli
```
## Tutorial 

https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html


```sh 
virtualenv ~/eb-virt
source ~/eb-virt/bin/activate
pip install django==2.1.1
pip install pandas 
pip install numpy 


```

### Configure Your Django Application for Elastic Beanstalk

Elastic Beanstalk looks for a file named application.py to start your application

```sh 
django-admin startproject ebdjango
cd ebdjango

mkdir .ebextensions

vi .ebextensions/django.config
# add this 
option_settings:
  aws:elasticbeanstalk:container:python:
    WSGIPath: ebdjango/wsgi.py
```

### Deploy 

```sh
eb init -p python-3.6 django-tutorial
eb create django-env
eb status
```

