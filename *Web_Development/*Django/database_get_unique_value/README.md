# Get unique value 

- https://stackoverflow.com/questions/2466496/select-distinct-values-from-a-table-field
- https://docs.djangoproject.com/en/2.2/topics/db/aggregation/
- https://stackoverflow.com/questions/842031/django-equivalent-of-count-with-group-by
- https://stackoverflow.com/questions/36953615/django-query-to-get-count-of-all-distinct-values-for-particular-column


Multiple ways to do this 

```py
len(np.unique(obj.values_list('<col_name>')))

obj.values('<col_name>').distinct().count()

obj.order_by('<col_name>').values_list('<col_name>').distinct().count()

obj.values('<col_name>').annotate(Count('<col_name>', distinct=True)).count()
``` 