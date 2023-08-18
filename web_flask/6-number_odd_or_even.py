#!/usr/bin/python3
""" first flask web app """

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ returns Hello HBNB """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Returns HBNB """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ returns a text """
    text_no_underscore = text.replace("_", " ")
    return "C {}".format(text_no_underscore)


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python(text="is_cool"):
    """ freturns a text or a default value """
    text_no_underscore = text.replace("_", " ")
    return "Python {}".format(text_no_underscore)


@app.route('/number/<int:n>', strict_slashes=False)
def n(n):
    """ prints a number """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_temp(n):
    """ renders a template with a given number """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def num_odd_even(n):
    """ renders a template with a given number and tells if is even or odd"""
    if n % 2 == 0:
        odd_even = "even"
    else:
        odd_even = "odd"
    return render_template(
        '6-number_odd_or_even.html', number=n, value=odd_even)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
