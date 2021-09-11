from flask import Flask # Import the Flask class
from flask_sqlalchemy import SQLAlchemy # Used for our database
from flask_migrate import Migrate # Used for our database
from flask_login import LoginManager # Manager user's loggin-in state. Provides a remember me functionality
from config import Config # Importing our class containing config vars

"""Create instace of Flask class
The web server passes all requests from clients to this object
for handling. We pass __name__ which represts the name of our
application"""
app = Flask(__name__)

# Here we are reading and applying the config file, 
# which contains our config variables.
app.config.from_object(Config)

db = SQLAlchemy(app) # represents database
migrate = Migrate(app, db) # represents migration database
login = LoginManager(app) # login instance of the LoginManager class
login.login_view = 'login' # The view function that handles logins
from myapp import routes, models