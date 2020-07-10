# Tutorial 


## [Writing your first Django app, part 1](https://docs.djangoproject.com/en/2.2/intro/tutorial01/)

Check version 

```
python -m django --version
```

Start project 

```
django-admin startproject [project name]
```

polls/view.py 

```
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

polls/urls.py

```
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
]
```

mysite/urls.py

```py 
from django.contrib import admin
from django.urls import include, path
urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```

Whole-Sha-Bang 

```
django-admin startproject mysite
# test 
python manage.py runserver
# create polls app 
python manage.py startapp polls
# create file 
touch polls/urls.py

http://localhost:8000/polls/ 
```

## [Writing your first Django app, part 2](https://docs.djangoproject.com/en/2.2/intro/tutorial02/)


mysite/settings.py

```
python manage.py migrate
```

polls/models.py

```
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

mysite/settings.py

```py
INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    ...
]
```

```py 
# By running makemigrations, you’re telling Django that you’ve made some changes to your models (in this case, you’ve made new ones) and that you’d like the changes to be stored as a migration.
python manage.py makemigrations polls

# The sqlmigrate command takes migration names and returns their SQL:
python manage.py sqlmigrate polls 0001

# checks for any problems in your project without making migrations or touching the database.
python manage.py check

# run migrate again to create those model tables in your database
python manage.py migrate
```

Three-step guide to making model changes:

- Change your models (in models.py).
- Run python manage.py makemigrations to create migrations for those changes.
- Run python manage.py migrate to apply those changes to the database.


### Playing with the API 

To invoke the Python shell, use this command:

```py 
# gives Django the Python import path to your mysite/settings.py file.python manage.py shell

```

### Introducing the Django Admin

create a user who can login to the admin site

```
python manage.py createsuperuser
```

Start the development server (http://127.0.0.1:8000/admin/)

```
python manage.py runserver
```

### Make the poll app modifiable in the admin

polls/admin.py

```
from django.contrib import admin
from .models import Question
admin.site.register(Question)
```

### Create choice 

```py 
python manage.py shell

q = Question.objects.get(pk=1)

# Display any choices from the related object set -- none so far.
q.choice_set.all()

# Create three choices.
q.choice_set.create(choice_text='Not much', votes=0)
q.choice_set.create(choice_text='The sky', votes=0)
c = q.choice_set.create(choice_text='Just hacking again', votes=0)
```

## [Writing your first Django app, part 3](https://docs.djangoproject.com/en/2.2/intro/tutorial03/)

### Creating the public interface – “views.”

- polls/views.py
- polls/urls.py

```
http://127.0.0.1:8000/polls/34/results/

# returns: You're looking at the results of question 34.
```

- Each view is responsible for doing one of two things: returning an HttpResponse object containing the content for the requested page, or raising an exception such as Http404. 

polls/views.py -> displays the latest 5 poll questions in the system, separated by commas, according to publication date


### Templates 

Create a directory called templates in your polls directory. Your project’s TEMPLATES setting describes how Django will load and render templates.

```sh 
cd polls
mkdir templates 
mkdir templates/polls 
touch templates/polls/index.html
```

Then visit `http://127.0.0.1:8000/polls/`, where you see a bulleted list.

### Render()

The render() function takes the request object as its first argument, a template name as its second argument and a dictionary as its optional third argument.

### Raising a 404 error

polls/views.py 

Create template 

```
touch polls/templates/polls/detail.html
# put: {{ question }}
```

A shortcut: `get_object_or_404()`

### Template system

- The template system uses dot-lookup syntax to access variable attributes. 
- Method-calling happens in the {% for %} loop. 

### Removing hardcoded URLs in templates

- polls/index.html
- polls/url.py
- `{% url %}` template tag

### Namespacing URL names

- `polls/urls.py` -> add an `app_name` to set the application namespace.
- `polls/templates/polls/index.html` 

## [Writing your first Django app, part 4](https://docs.djangoproject.com/en/2.2/intro/tutorial04/)

- simple form processing and cutting down our code

### Write a simple form

- `polls/templates/polls/detail.html`
- Whenever you create a form that alters data server-side, use method="post".
- forloop.counter indicates how many times the for tag has gone through its loop. 
- `{% csrf_token %}` = Cross Site Request Forgeries. 
- `polls/urls.py`
- `polls/views.py` -> update vote()
 - **vote**
  - `request.POST` is a dictionary-like object that lets you access submitted data by key name (ensure that data is only altered via a POST call).
  - `request.POST['choice']`
  - you should always return an `HttpResponseRedirect` after successfully dealing with POST data.
  - `reverse()`: This function helps avoid having to hardcode a URL in the view function.
  - `request` is an HttpRequest object.
 - **results**
  
polls/results.html

    ```
    touch polls/templates/polls/results.html
    ```

Go to `/polls/1/` in your browser and vote in the question.

### Use `generic views`: Less code is better

These views represent a common case of basic Web development: 

- Getting data from the database according to a parameter passed in the URL
- Loading a template and returning the rendered template. 
- Because this is so common, Django provides a shortcut, called the “generic views” system.

To use generic views: 

- Convert the URLconf.
- Delete some of the old, unneeded views.
- Introduce new views based on Django’s generic views.


#### Amend URLconf

`polls/urls.py` -> using `as_view()`. 

#### Amend views

`polls/views.py`

- remove our old index, detail, and results views and use Django’s generic views instead.
- each generic view needs model. 
- `DetailView` 
 - display a detail page for a particular type of object
 - expects `pk` primary key value 
 - uses a template called `<app name>/<model name>_detail.html`.
- `ListView` 
 - display a list of objects 
 - `<app name>/<model name>_list.html`
 - it’s a lot easier to just tell Django to use the variable you want.


## [Writing your first Django app, part 5](https://docs.djangoproject.com/en/2.2/intro/tutorial05/)

### automated testing

- Tests are simple routines that check the operation of your code.
- “Code without tests is broken by design.”

`polls/models.py`

- `Question.was_published_recently()` has a bug with future dates. 

    ```py 
    import datetime
    from django.utils import timezone
    from polls.models import Question
    # create a Question instance with pub_date 30 days in the future
    future_question = Question(pub_date=timezone.now() + datetime.timedelta(days=30))
    # was it published recently?
    future_question.was_published_recently()
    # True
    ```

- `polls/tests.py`
 - running the test: 
    ```py 
    python manage.py test polls
    ```

### Test a view

#### Django test client

- simulate a user interacting with the code at the view level. Can use `tests.py` or `python shell`. 
- `python manage.py shell`

    ```py
    from django.test.utils import setup_test_environment
    setup_test_environment()

    from django.test import Client # only for shell method 
    # create an instance of the client for our use
    client = Client()

    # get a response from '/'
    response = client.get('/')
    # Not Found: /
    # we should expect a 404 from that address; if you instead see an "Invalid HTTP_HOST header" error and a 400 response, you probably omitted the setup_test_environment() call described earlier.
    
    response.status_code
    # 404
    # on the other hand we should expect to find something at '/polls/'

    # we'll use 'reverse()' rather than a hardcoded URL
    from django.urls import reverse
    response = client.get(reverse('polls:index'))
    response.status_code
    # 200

    response.content
    # b'\n    <ul>\n    \n        <li><a href="/polls/1/">What&#39;s up?</a></li>\n    \n    </ul>\n\n'

    response.context['latest_question_list']
    # <QuerySet [<Question: What's up?>]>
    ```

### improving view 

`polls/views.py`

- `__lte` = less than or equal to 

#### Testing our new view

`polls/tests.py`

### Testing the DetailView

- `polls/views.py`
 - `get_queryset`
- `polls/tests.py`
 - `class QuestionDetailViewTests`

### Tips 

- a separate TestClass for each model or view
- a separate test method for each set of conditions you want to test
- test method names that describe their function

### Further testing 

- `LiveServerTestCase` to work with selenium -> in-browser testing 
- continuous integration 


## [Writing your first Django app, part 6](https://docs.djangoproject.com/en/2.2/intro/tutorial06/)

- add a stylesheet and an image.
- `django.contrib.staticfiles` collects static files from each of your applications into a single location.

### Customize your app’s look and feel

```
mkdir polls/static 

mkdir polls/static/polls

# referred as polls/style.css
touch polls/static/polls/style.css 
```

- `polls/templates/polls/index.html` -> add css 
- now run `python manage.py runserver` 
- visit -> http://localhost:8000/polls/ -> links are now green. 

### Adding a background-image

```
mkdir polls/static/polls/images
```

- put image named `background.gif`
- edit: `polls/static/polls/style.css`
- Reload http://localhost:8000/polls/

## [Writing your first Django app, part 7](https://docs.djangoproject.com/en/2.2/intro/tutorial07/)

- customizing Django’s automatically-generated admin site

`polls/admin.py`

- add `class QuestionAdmin`, which reorders dub_date and question_test in the admin form.
 - `field` vs `fieldsets`.

### Adding related objects (aka adding choice in admin page)

`polls/admin.py`

- `admin.site.register(Choice)`

### add a bunch of Choices directly when you create the Question object

`polls/admin.py`

- `ChoiceInline`
- `admin.TabularInline`
- `admin.StackedInline`

### Customize the admin change list

`polls/admin.py`

- Django displays the str() of each object.
- `class QuestionAdmin`
 - `list_display` -> display individual fields. 
 - `list_filter = ['pub_date']` 
 - `search_fields = ['question_text']`

`polls/models.py`


### Customize the admin look and feel

#### Customizing your project’s templates

```
mkdir templates
```

`mysite/settings.py` -> add a DIRS option in the TEMPLATES. DIRS is a list of filesystem directories to check when loading Django templates; it’s a search path.

Copy the template admin/base_site.html from within the default Django admin template directory  and edit `{{ site_header|default:_('Django administration') }}` (Overriding a template).

	```
	mkdir templates/admin
		
	python -c "import django; print(django.__path__)"
	# this returned: /Users/ijung/anaconda3/lib/python3.6/site-packages/django
	
	python -c "import django; print(django.__path__)"
	SET django_path = !!
		
	django_path="/Users/ijung/anaconda3/lib/python3.6/site-packages/django/contrib/admin/templates/admin/base_site.html"
	cp $django_path templates/admin/
	```

#### Customizing your application’s templates

- since APP_DIRS is set to True, Django automatically looks for a templates/ subdirectory within each application package
- `django.contrib.admin`

#### Customize the admin index page

- `admin/index.html`
- `app_list` 

## [Advanced tutorial: How to write reusable apps](https://docs.djangoproject.com/en/2.2/intro/reusable-apps/)

A Django application is just a Python package that is specifically intended for use in a Django project.

```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py
    polls/
        __init__.py
        admin.py
        migrations/
            __init__.py
            0001_initial.py
        models.py
        static/
            polls/
                images/
                    background.gif
                style.css
        templates/
            polls/
                detail.html
                index.html
                results.html
        tests.py
        urls.py
        views.py
    templates/
        admin/
            base_site.html
```

```
pip install setuptools
```

### Packaging your app


```
mkdir django-polls 
cp -r intro/polls django-polls/
touch django-polls/README.rst
touch django-polls/LICENSE # many Django-compatible apps are distributed under the BSD license
touch django-polls/setup.py
touch django-polls/MANIFEST.in
mkdir django-polls/docs 

cd django-polls 
python setup.py sdist # (run from inside django-polls)
```

### Using your own package

```
pip install --user django-polls/dist/django-polls-0.1.tar.gz

pip uninstall django-polls
```

