
# Import the flask form base class
from flask_wtf import FlaskForm

# Import some classes that'll represet our fields
from wtforms import StringField, PasswordField, BooleanField, SubmitField

# Our validators can help with ensuring that field is not submitted empty, etc
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from myapp.models import User

"""The flask-wtf extension uses Python classes to represent forms. 
A form class simply defines the fields of the form as class variables.
Let's now create a form."""

 # For each field, an object is created as a class variable in the LoginForm class
class LoginForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    password2 = PasswordField('Repeat Password', validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user is not None:
            raise ValidationError("Please use a different username.")

    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if user is not None:
            raise ValidationError("Please use a different email address.")

