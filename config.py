class Config(object):
    TESTING = False
    DEBUG = False
    FLASK_APP = '__main__.py'
    FLASK_RUN_PORT = 5000
    FLASK_RUN_HOST = '127.0.0.1'
    REDIS_HOST = 'redis'


class CeleryConfig(Config):
    # celery
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_BACKEND_URL = 'redis://localhost:6379/0'
    CELERY_IMPORTS = 'app.services.celery_beat.celery_tasks'
    CELERY_ACCEPT_CONTENT = ['json', 'msgpack', 'yaml']
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_TIMEZONE = 'UTC+02:00'
    CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
        'task': 'tasks.add',
        'schedule': 30.0,
        'args': (16, 16)},
    }
    # List of modules to import when the Celery worker starts.
    # imports = ('myapp.tasks',)
    ## Using the database to store task state and results.
    # result_backend = 'db+sqlite:///results.db'
    # task_annotations = {'tasks.add': {'rate_limit': '10/s'}}


class ProductionConfig(Config):
    DEBUG = False
    DATABASE_URI = 'mysql://user@localhost/foo'


class DevelopmentConfig(Config):
    # TODO TRUE
    DEBUG = False
    ENV = 'development'
    DATABASE_URI = "sqlite:////tmp/foo.db"
    REDIS_HOST = "127.0.0.1"



class TestingConfig(Config):
    ENC = 'testing'
    # DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True
