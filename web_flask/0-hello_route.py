#!/usr/bin/python3

from flask import Flask  # Import the Flask class from Flask package.
app = Flask(__name__)    # Create a Flask instance with current module's name.


@app.route('/', strict_slashes=False)  # Define root URL route with / option.
def index():              # Define function 'index' for the route.
    return "Hello HBNB!"  # Return string to display in the browser.


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # Start Flask dev server.
