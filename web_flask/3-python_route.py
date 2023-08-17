#!/usr/bin/python3
"""Flask Web Application"""

# Import the Flask module
from flask import Flask

# Create a Flask web application instance
app = Flask(__name__)

# Define a route for the root URL ("/") and allow trailing slashes


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display a warm greeting"""
    return "Hello HBNB!"

# Define a route for "/hbnb" URL and allow trailing slashes


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display the magical word"""
    return "HBNB"

# Define a route for "/c/<text>" URL and allow trailing slashes


@app.route('/c/<text>', strict_slashes=False)
def c_display(text):
    """Display 'C' and the given text"""
    # Replace underscores with spaces in the text
    formatted_text = text.replace("_", " ")
    return "C " + formatted_text

# Define a route for "/python" URL with a default value for 'text'


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
# Define a route for "/python/<text>" URL and allow trailing slashes
@app.route('/python/<text>', strict_slashes=False)
def python_display(text):
    """Display 'Python' and the given text or a cool statement"""
    # Replace underscores with spaces in the text
    formatted_text = text.replace("_", " ")
    return "Python " + formatted_text

# Run the web application when this script is executed


if __name__ == "__main__":
    # Listen on the specified IP address and port (0.0.0.0:5000)
    app.run(host='0.0.0.0', port=5000)
