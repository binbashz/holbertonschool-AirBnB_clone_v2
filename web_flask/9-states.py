#!/usr/bin/python3
""" first flask web app """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_storage(e):
    storage.close()


@app.route('/states/<id>', strict_slashes=False)
@app.route('/states', strict_slashes=False)
def states_list(id=None):
    if not id:
        states = storage.all(State)
        flag = False
    else:
        states = storage.all(State)
        state_exists = False
        for key, value in states.items():
            if key.split(".")[1] == id:
                states = value
                state_exists = True
        if not state_exists:
            states = None
        flag = True
    return render_template('9-states.html', states=states, flag=flag)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
