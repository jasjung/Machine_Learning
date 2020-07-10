# Celery

- https://buildwithdjango.com/blog/post/celery-progress-bars/
- https://buildwithdjango.com/projects/celery-progress/
- https://github.com/czue/celery-progress

```py
from celery import task

# this decorator is all that's needed to tell celery this is a worker task
@task
def do_work(self, list_of_work):
    for work_item in list_of_work:
        do_work_item(work_item)
    return 'work is complete'


def my_view(request):
     # the .delay() call here is all that's needed
     # to convert the function to be called asynchronously
     do_work.delay()
     # we can't say 'work done' here anymore because all we did was kick it off
     return HttpResponse('work kicked off!')


@task
def do_work(self, list_of_work, progress_observer):
    total_work_to_do = len(list_of_work)
    for i, work_item in enumerate(list_of_work):
        do_work_item(work_item)
        # tell the progress observer how many out of the total items we have processed
        progress_observer.set_progress(i, total_work_to_do)
    return 'work is complete'
```