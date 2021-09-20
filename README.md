
## Flask Microblog

This is a Flask App I am creating as part of a [Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world).

Upon completion, this will be a web app which allows users to post blogs, as well as follow and interact with other bloggers.

### Challenges Faced

Despite being a tutorial, this has so far been a challenging project. 

Perhaps the biggest challenge was **understanding SQLAlchemy** along with the various joins (e.g. many-to-one). 
For this, it helped to read through [Flask Web Development](https://www.oreilly.com/library/view/flask-web-development/9781491991725/).
The [Pretty Printed](https://www.youtube.com/channel/UC-QDfvrRIDB6F0bIO4I4HkQ) Youtube channel also helped a lot!

I also faced challenges when it came to **unit testing**, as this was a new topic for me. For this, I worked through some [Real Python](https://realpython.com/python-testing/) articles 
to better undertsand how unit testing worked in python.

### Technologies & Skills

Python, Flask, SQLite, SQLAlchemy, Unit Testing, Docker, OOP

### Installing the Project

The get this project working, follow these steps:

* Clone project to local machine
* Navigate to project's root directory

```bash
  cd MICROBLOG
```
* Create a virtual environment

```bash
  python3 -m venv venv
```

* Activate the virtual environment

```
source venv/bin/activate
```

* Now install project dependencies inside virtual environment

```
pip install -r requirements.txt
```

(in progress....)