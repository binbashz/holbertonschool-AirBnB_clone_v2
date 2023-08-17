#!/usr/bin/python3
"""
Say hello and connect port
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """say hello"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """say hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    """say c + text"""
    correct_format = text.replace("_", " ")
    return "C " + correct_format


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
