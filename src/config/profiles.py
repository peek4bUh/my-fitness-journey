# https://flask.palletsprojects.com/en/stable/config/#development-production

class DefaultProfile(object):
    """Base config, uses staging database server."""
    TESTING = False
    DB_NAME = "test.db"
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_NAME}"


class DevelopmentProfile(DefaultProfile):
    pass


class ProductionProfile(DefaultProfile):
    pass


class TestingProfile(DefaultProfile):
    DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True
