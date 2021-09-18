import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os
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

if not app.debug:
    if app.config['MAIL_SERVER']:
        auth = None
        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        secure = None
        if app.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr='no-reply@' + app.config['MAIL_SERVER'],
            toaddrs=app.config['ADMINS'], subject='Microblog Failure',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)


    # Create log directory if it doesn't exist
    if not os.path.exists('logs'):
        os.mkdir('logs')
    
    # This rotates the logs, ensuring they don't grow too large. In this case, we're setting the size of each log to 10KB and keeping last
    # 10 logs as backup
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240, backupCount=10)

    # This provides formatting of logs
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))

    # Here we're lowing logging category to INFO for botha application and file logger
    # Options are DEBUG, INFO, WARNING, ERROR, and CRITICAL
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')

from myapp import routes, models, errors