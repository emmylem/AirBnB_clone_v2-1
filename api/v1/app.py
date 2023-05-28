#!/usr/bin/python3
"""
Flask App started with script.
"""
from api.v1.views import app_views
from flask import Flask, jsonify, make_respons
from flask_cors import CORS, cross_origin
from flask import Blueprint
from models import storage
import os

app = Flask(__name__)

host = os.getenv('HBNB_API_HOST', '0.0.0.0')
port = os.getenv('HBNB_API_PORT', 5000)

cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.teardown_appcontext
def teardown_app(exception):
    """
    tearsdown app context.
    """
    storage.close()


@app.errorhandler(404)
def notfound_404(exception):
    """
    handles 404 errors.
    """
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    app.run(host=host, port=port, threaded=True)
