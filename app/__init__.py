from flask import Flask
from flask_cors import CORS
import os

def create_app():
    app = Flask(__name__)
    # Review this and correct for your environment
    if os.environ.get('FLASK_ENV') == 'development':
        CORS(app)
    else:
        CORS(app, resources={r"/*": {"origins": "*"}})
    from app.api.routes import api_blueprint
    app.register_blueprint(api_blueprint)
    return app