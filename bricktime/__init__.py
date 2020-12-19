import os
from flask import Flask
from .database.db import initialize_db
from auth import login_manager

def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.DevConfig')

    # Initialize Plugins
    initialize_db(app)
    login_manager.init_app(app)

    with app.app_context():
        # Include our Routes
        from . import routes

        # Register Blueprints
        #app.register_blueprint(auth.auth_bp)

        return app
