# https://flask.palletsprojects.com/en/stable/config/#development-production

class DefaultConfig(object):
    """Base config, uses staging database server."""
    TESTING = False
    DB_NAME = "test.db"
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_NAME}"


class DevelopmentConfig(DefaultConfig):
    pass


class ProductionConfig(DefaultConfig):
    pass


class TestingConfig(DefaultConfig):
    DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True
