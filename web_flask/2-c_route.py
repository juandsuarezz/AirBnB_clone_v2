#!/usr/bin/python3
"""Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Displays hello message"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays the name"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def croute(text):
    """Displays C with custom text"""
    return "C %s" % text.replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
