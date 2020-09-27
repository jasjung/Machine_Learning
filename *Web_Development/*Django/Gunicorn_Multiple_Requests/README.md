# Gunicorn 


## Dealing with multiple requests 

https://www.reddit.com/r/django/comments/99lu1k/how_do_you_make_django_handle_multiple_requests/


- If you use gunicorn you can either increase the number of workers and threads or switch the worker class to a non-blocking one gevent or eventlet (http://docs.gunicorn.org/en/stable/settings.html#id75).


https://stackoverflow.com/questions/38425620/gunicorn-workers-and-threads
