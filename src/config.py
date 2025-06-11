# https://flask.palletsprojects.com/en/stable/config/#development-production

class Config(object):
    """Base config, uses staging database server."""
    TESTING = False
    DB_NAME = "db.sqlite"
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_NAME}"


class DevelopmentConfig(Config):
    pass


class ProductionConfig(Config):
    pass


class TestingConfig(Config):
    DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True
