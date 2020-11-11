"""Initialize Flask App using app factory"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.config import get_config

db = SQLAlchemy()

def create_app(config_name):
    app = Flask("Tor-Relay-API")
    app.config.from_object(get_config(config_name))

    db.init_app(app)
    return app