#!/usr/bin/env python
"""Application entry point"""
from flask_lambda import FlaskLambda

from app.routes import routes


def _initialize_blueprints(app) -> None:
    """Register flask route blueprints"""
    app.register_blueprint(routes)


def create_app() -> FlaskLambda:
    """Create an src by initializing FlaskLambda"""
    app = FlaskLambda(__name__)
    _initialize_blueprints(app)
    return app
