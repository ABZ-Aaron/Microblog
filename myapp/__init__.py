# Import the Flask class
from flask import Flask 

# Importing our class containing config vars
from config import Config

# Create instace of Flask class
app = Flask(__name__)

# Here we are reading and applying the config file, 
# which contains are config variables.
app.config.from_object(Config)

from myapp import routes

