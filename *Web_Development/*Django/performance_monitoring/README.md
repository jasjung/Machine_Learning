# Performance Monitoring  


- https://docs.djangoproject.com/en/3.0/topics/performance/

## django-debug-toolbar

- https://github.com/jazzband/django-debug-toolbar/
- https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#getting-the-code

```sh 
pip install django-debug-toolbar
```

### Setup 

```py 
INSTALLED_APPS = [
    # ...
    'django.contrib.staticfiles',
    # ...
    'debug_toolbar',
]

STATIC_URL = '/static/'
```

```py 
from django.conf import settings
from django.urls import include, path  # For django versions from 2.0 and up

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
```

```py 
MIDDLEWARE = [
    # ...
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # ...
]
```

```py
INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]
```