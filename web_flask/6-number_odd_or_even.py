#!/usr/bin/python3
"""My first Flask web app"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Return a greeting message"""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return 'HBNB'"""
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Return 'C' followed by formatted text"""
    formatted_text = text.replace("_", " ")
    return f"C {formatted_text}"

@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python(text="is_cool"):
    """Return 'Python' followed by formatted text or default value"""
    formatted_text = text.replace("_", " ")
    return f"Python {formatted_text}"

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Return a number and indicate if it's an integer"""
    return f"{n} is a number"

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Render a template with a given number"""
    return render_template('number_template.html', n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Render a template with a given number and indicate if it's odd or even"""
    if n % 2 == 0:
        odd_or_even = "even"
    else:
        odd_or_even = "odd"
    return render_template('number_odd_or_even.html', n=n, odd_or_even=odd_or_even)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

