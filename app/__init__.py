# Import the Flask class
from flask import Flask 

# Create instace of Flask class
app = Flask(__name__)

from app import routes
