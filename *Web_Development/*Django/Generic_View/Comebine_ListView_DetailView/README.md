# Combine ListView and DetailView 

https://stackoverflow.com/questions/41287431/django-combine-detailview-and-listview

```py 
class MyDetailView(generic.DetailView):
    model = Calendar
    template_name = 'koledarji/detail.html'
    def get_context_data(self, *args, **kwargs):
        context = super(MyDetailView, self).get_context_data(*args, **kwargs)
        context['calendars_list'] = Calendar.objects.all()
        return context
```

