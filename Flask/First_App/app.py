'https://nordicapis.com/how-to-create-an-api-using-the-flask-framework/'

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'This is my first API call!'