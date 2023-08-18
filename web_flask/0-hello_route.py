#!/usr/bin/python3

from flask import Flask

# Create a Flask web application instance
app = Flask(__name__)

# Define a route for the root URL ("/") and allow trailing slashes


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


# Run the web application when this script is executed
if __name__ == '__main__':
    # Listen on the specified IP address and port (0.0.0.0:5000)
    app.run(host='0.0.0.0', port=5000)
