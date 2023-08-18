#!/usr/bin/python3
"""Flask Web Application"""

# Import the Flask and render_template modules
from flask import Flask, render_template
from markupsafe import escape
app = Flask(__name__)

# Define a route for the root URL ("/") and allow trailing slashes


@app.route('/', strict_slashes=False)
def say_hello():
    """Display a warm greeting"""
    return "Hello HBNB!"

# Define a route for "/hbnb" URL and allow trailing slashes


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """Display the magical word"""
    return "HBNB"

# Define a route for "/c/<text>" URL and allow trailing slashes


@app.route('/c/<text>', strict_slashes=False)
def display_c_text(text):
    """Display 'C' and the given text"""
    formatted_text = text.replace("_", " ")
    return "C " + formatted_text

# Define a route for "/python" URL with a default value for 'text'


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
# Define a route for "/python/<text>" URL and allow trailing slashes


@app.route('/python/<text>', strict_slashes=False)
def display_python_text(text):
    """Display 'Python' and the given text or a cool statement"""
    formatted_text = text.replace("_", " ")
    return "Python " + formatted_text

# Define a route for "/number/<n>" URL and allow trailing slashes


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """Display n is a number if n is an integer"""
    return f"{n} is a number"

# Define a route for "/number_template/<n>" URL and allow trailing slashes


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_template(n):
    """Display a template with n if n is an integer"""
    return render_template('custom_template.html', n=n)

# Run the web application when this script is executed


if __name__ == "__main__":
    # Listen on the specified IP address and port (0.0.0.0:5000)
    app.run(host='0.0.0.0', port=5000)
