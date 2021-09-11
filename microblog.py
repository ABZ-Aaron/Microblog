from myapp import app, db
from myapp.models import User, Post

# When we invoke a Python shell using 'flask shell' these will be imported.
@app.shell_context_processor
def make_shell_context():
    return {'db' : db, 'User' : User, 'Post' : Post}


"""Script is importing app from myapp, which runs the __init__.py file (constructor)
"""