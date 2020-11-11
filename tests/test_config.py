import os

from app import create_app
from app.config import SQLITE_DEV_DB, SQLITE_PROD_DB

def test_development_config():
    app = create_app("development")
    assert app.config["TESTING"]
    assert app.config["SQLALCHEMY_DATABASE_URI"] == os.getenv("DATABASE_URL", SQLITE_DEV_DB)

def test_production_config():
    app = create_app("production")
    assert not app.config["TESTING"]
    assert app.config["SQLALCHEMY_DATABASE_URI"] == os.getenv("DATABASE_URL", SQLITE_PROD_DB)