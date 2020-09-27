# Cache

- https://docs.djangoproject.com/en/3.1/topics/cache/
- https://testdriven.io/blog/django-caching/
- https://www.tutorialspoint.com/django/django_caching.htm
- https://devcenter.heroku.com/articles/django-memcache
- https://pypi.org/project/python-memcached/
- https://data-flair.training/blogs/django-caching/
- https://docs.djangoproject.com/en/3.0/topics/cache/#the-low-level-cache-api
- https://dizballanze.com/django-project-optimization-part-3/


Terms 

- Redis vs Memcached


```sh
pip install python-memcached
```

settings.py 

```py
#DataFlair #Memcached
CACHES = {
    'default':{
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1;11211',
    }
}
```


## Database Caching

```py 
CACHES = {
    'default':{
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'dataflair_cache',
    }
}
```

```sh 
python manage.py createcachetable
```



