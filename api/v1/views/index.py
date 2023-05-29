#!/usr/bin/python3
"""
Flask route that returns json status response
"""
from api.v1.views import app_views
from flask import Flask, jsonify, request
from models import storage

app = Flask(__name__)


@app_views.route('/status', methods=['GET'])
def status():
    """
    checks status of json."""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'])
def stats():
    """
    function to return the count of all class objects
    """
    if request.method == 'GET':
        obj_response = {}
        Areas = {
            "Amenity": "amenities",
            "City": "cities",
            "Place": "places",
            "Review": "reviews",
            "State": "states",
            "User": "users"
        }
        for key, value in Areas.items():
            response[value] = storage.count(key)
        return jsonify(obj_response)


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port="5000")
