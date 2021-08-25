from app import app
# Here we are associating the top level URL (/)
# with this function.
@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"