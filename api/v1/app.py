#!/usr/bin/python3
"""
Flask App started with script.
"""
from api.v1.views import app_views
from flask import Flask, jsonify, make_response
from flask_cors import CORS, cross_origin
from flask import Blueprint
from models import storage
from werkzeug.exceptions import HTTPException
from flasgger import Swagger
import os

app = Flask(__name__)

host = os.getenv('HBNB_API_HOST', '0.0.0.0')
port = os.getenv('HBNB_API_PORT', '5000')

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
swagger = Swagger(app)
app.url_map.strict_slashes = False

app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "0.0.0.0"}})


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
