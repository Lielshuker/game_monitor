class Config(object):
    TESTING = False
    DEBUG = True
    FLASK_RUN_PORT = 5000
    FLASK_RUN_HOST = "127.0.0.1"


class ProductionConfig(Config):
    DEBUG = False
    DATABASE_URI = 'mysql://user@localhost/foo'


class DevelopmentConfig(Config):
    ENV = 'development'
    DATABASE_URI = "sqlite:////tmp/foo.db"


class TestingConfig(Config):
    ENC = 'testing'
    # DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True
