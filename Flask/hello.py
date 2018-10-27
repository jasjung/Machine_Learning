from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home') 
def home():
    # return 'Hello, World!'
    #return render_template('home.html')
    # return render_template('home.html')
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    # return 'You entered: {}'.format(request.form['text'])
    text = request.form['text']
    # run another function 
    # function(text)
    return 'you typed %s' % text 

# about page 
@app.route('/about')
def about():
    return '<h1>About Page</h1>'
    # return render_template('about.html')

# button to function 
@app.route("/function", methods=['POST'])
def button_function():
    #Moving forward code
    forward_message = "You pressed the button"
    return render_template('form.html', message=forward_message);
    # return 'pressed a button'

# only true if we run this script directly. 
if __name__ == '__main__':
    app.run(debug=True) 
