import os
from pathlib import Path

currentPath = Path(__file__).parent
SQLITE_DEV_DB = f"sqlite:///{currentPath}/tor_relay_api_dev.db"
SQLITE_PROD_DB = f"sqlite:///{currentPath}/tor_relay_api_prod.db"

class Config():
    #Base Config
    SWAGGER_UI_DOC_EXPANSION = "list"
    RESTX_MASK_SWAGGER = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", SQLITE_DEV_DB)
    TESTING = True

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", SQLITE_PROD_DB)

env_config_dict = dict(
    development = DevelopmentConfig,
    production = ProductionConfig
)

def get_config(config_name):
    return env_config_dict.get(config_name, ProductionConfig)