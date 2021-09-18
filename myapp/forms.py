
# Import the flask form base class
from flask_wtf import FlaskForm

# Import some classes that'll represet our fields
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.fields.simple import TextAreaField

# Our validators can help with ensuring that field is not submitted empty, etc
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length

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

class EditProfileForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    about_me = TextAreaField('About me', validators = [Length(min=0, max=140)])
    submit = SubmitField('Submit')

    def __init__(self, original_username):
        super().__init__()
        self.original_username = original_username

    # This may be required
    """    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username""" 

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username = self.username.data).first()
            if user is not None:
                raise ValidationError('Please use a different username.')

