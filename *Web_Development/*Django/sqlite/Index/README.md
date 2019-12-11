# Index 

Improve the query performance! 




## Django Model Index Example 

- https://www.djangorocks.com/snippets/indexing-your-django-models.html


FROM 

```py
class Blog(models.Model):
    title = models.CharField(max_length=100)
    added = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
```

To 

```py 
class Blog(models.Model):
    title = models.CharField(db_index=True, max_length=100)
    added = models.DateTimeField(db_index=True, auto_now_add=True)
    body = models.TextField()
```