# Block

Blocking content allows you to inherit common html codes from the base.html so that you can reduce redundancies. For example, you can apply this to your footers and navbars. 

base.html 

```html
<!DOCTYPE html>
<html>
<head>
	<title>yo sup</title>
</head>
<body>
	Common Content 

	{% block content %}{% endblock %}
</body>

</html>
```

other.html 

```html 
{% extends "bobabook/base.html" %}

{% block content %}
	your unique content 
{% endblock content %}

```