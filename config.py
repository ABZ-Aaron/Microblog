import os

# Here we are setting a secret key (this needs to exist for security purposes)
class Config(object):
    # The flask-wtf extension uses the secret key to protect against attacks
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-not-guess-this"