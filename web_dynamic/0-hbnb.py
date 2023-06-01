#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /hbnb: HBnB home page.
"""
from models import storage
from flask import Flask
from flask import render_template, url_for
import uuid

app = Flask(__name__)


@app.route("/0-hbnb", strict_slashes=False)
def hbnb():
    """Prints the main HBnB filters HTML page."""
    obj = storage.all('States').values()
    states = dict([state.name, state_val] for state_val in obj)
    amenities = storage.all("Amenity").values()
    places = storage.all("Place").values()
    cache_id = (str(uuid.uuid4()))
    return render_template("0-hbnb.html",
                           states=states, amenities=amenities, places=places,
                           cache_id=cache_id)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
