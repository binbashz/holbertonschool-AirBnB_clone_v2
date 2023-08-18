#!/usr/bin/python3
"""Task 0. Script that starts a Flask web application
"""
from flask import Flask

# Create a Flask web application instance
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

# Run the web application when this script is executed


if __name__ == "__main__":
    # Listen on the specified IP address and port (0.0.0.0:5000)
    app.run(host="0.0.0.0", port=5000)
