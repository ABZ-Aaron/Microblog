from myapp import app
from flask import render_template, flash, redirect, url_for
from myapp.forms import LoginForm
from flask_login import current_user, login_user
from myapp.models import User

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

# This is a function for dealing with our login page
# We pass GET and POST are arguments. This tells Flask that this
# function accepts both of these requests. A GET request is typically 
# used for returning information from the server to the browser. A POST
# request is used for sending information to the server. If we don't include POST
# then when we try to submit the form, we'll get an error because the application
# was not configued to accept it.
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    # This will run all validation checks.
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash(f"Invalid username or password")
            return redirect(url_for('login'))
        return redirect(url_for('index'))
    return render_template("login.html", title = 'Sign In', form = form)
