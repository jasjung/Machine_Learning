# Print All Fields in View 

https://stackoverflow.com/questions/2217478/django-templates-loop-through-and-print-all-available-properties-of-an-object

-- models.py

```
class Manors(models.Model)
  #field declarations

  def get_fields(self):
    return [(field.name, field.value_to_string(self)) for field in Manors._meta.fields]
```

-- manor_detail.html

```
{% for name, value in manor_stats.get_fields %}
  {% if value %}
    {{ name }} => {{ value }}
  {% endif %}
{% endfor %}
```