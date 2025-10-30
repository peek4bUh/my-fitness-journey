# https://flask.palletsprojects.com/en/stable/config/#development-production

import secrets


class DefaultConfig(object):
    """Base config, uses staging database server."""
    TESTING = False
    DB_NAME = "test.db"
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_NAME}"
    SECRET_KEY = secrets.token_urlsafe(32)


class DevelopmentConfig(DefaultConfig):
    pass


class ProductionConfig(DefaultConfig):
    pass


class TestingConfig(DefaultConfig):
    DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True
