from myapp import app
from flask import render_template
from myapp.forms import LoginForm
# Here we are associating the top level URL (/)
# with this function.
@app.route('/')
@app.route('/index')
def index():
    user = {"username" : "Aaron"}
    posts = [
                {
                    'author' : {'username' : 'John'},
                    'body' : 'Beautiful day in Portland'
                },
                {
                    'author' : {'username' : 'Jane'},
                    'body' : 'The Avegers movie was so cool'
                }
    ]
    return render_template("index.html", title = "home", user = user, posts = posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template("login.html", title = 'Sign In', form = form)
