# Flask 

- https://www.youtube.com/watch?v=MwZwr5Tvyxo
- http://flask.pocoo.org/docs/1.0/quickstart/#quickstart
- http://flask.pocoo.org/docs/1.0/quickstart/#accessing-request-data
- **User_Input**: [https://stackoverflow.com/questions/37345215/retrieve-text-from-textarea-in-flask?answertab=active#tab-top](https://stackoverflow.com/questions/37345215/retrieve-text-from-textarea-in-flask?answertab=active#tab-top)
- **PythonAnywhere_for_Hosting**: [https://www.pythonanywhere.com](https://www.pythonanywhere.com)
- **Reddit_Hosting**: [https://www.reddit.com/r/flask/comments/2321oc/easiest_and_fastest_way_to_host_flask_python/](https://www.reddit.com/r/flask/comments/2321oc/easiest_and_fastest_way_to_host_flask_python/)
- **Deployment**: [http://flask.pocoo.org/docs/0.12/deploying/](http://flask.pocoo.org/docs/0.12/deploying/)
- [pythonanywhere.com](pythonanywhere.com)


## Part 1 

```
pip install flask 

# test 
python 
import flask 
```

```
mkdir flast_tutoral 

virtualenv flask_blog 

source flask_blog

flask run  
```

Debug Mode. Refreshes the changes. 

```
export FLASK_DEBUG=1 
flask run 
```

### App.py 

```py 
from flask import Flask, render_template
app = Flask(__name__)

posts = [
	{ 'authoer': 'jason',
	'title': 'yo',
	'content':'first post' ,
	'date':'5/1'
	},
	
	{ 'authoer': 'sam',
	'title': 'yo2',
	'content':'second post' ,
	'date':'5/1'
	}
]

@app.route('/')
@app.route('/home') 
def home():
    #return 'Hello, World!'
    #return render_template('home.html')
    return render_template('home.html',posts=posts)

# about page 
@app.route('/about')
def about():
    # return '<h1>About Page</h1>'
    return render_template('about.html')

# only true if we run this script directly. 
if __name__ == '__main__':
	app.run(debug=True)	
```

instead of running `flask run`, run 
`python flaskblog.py`

```
$ export FLASK_APP=hello.py
$ flask run
 * Running on http://127.0.0.1:5000/
```

## Part 2 

More html, and using templates 

```mkdir templates``` and make `home.html` and `about.html`. 

### home.html 

```html 
<!DOCTYPE html>
<html>
<head>
	<title> 'hello word' </title>
</head>
<body>

</body>
</html>
```

### about.html 

```html 
<!DOCTYPE html>
<html>
<head>
	<title> 'about page' </title>
</head>
<body>

</body>
</html>
```

## Button to Function 

https://stackoverflow.com/questions/42601478/flask-calling-python-function-on-button-onclick-event


## Search Bar 

https://www.blog.pythonlibrary.org/2017/12/13/flask-101-how-to-add-a-search-form/

## HTML in Flask String 

https://stackoverflow.com/questions/49685697/how-to-include-html-tag-with-flask-string

```html
{{ a|safe }}
```