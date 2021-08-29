# Import the Flask class
from flask import Flask 

# Used for our database
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Importing our class containing config vars
from config import Config

# Create instace of Flask class
app = Flask(__name__)

# Here we are reading and applying the config file, 
# which contains our config variables.
app.config.from_object(Config)
db = SQLAlchemy(app) # represents database
migrate = Migrate(app, db) # represents migration database

from myapp import routes, models

