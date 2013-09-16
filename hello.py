

import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/varun')
def greet_varun():
    return 'Hello Varun ! Nice to see you here. Yay! :)'
