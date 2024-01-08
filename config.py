class Config(object):
    TESTING = False
    DEBUG = False
    FLASK_RUN_PORT = 5000
    FLASK_RUN_HOST = '127.0.0.1'


class CeleryConfig(Config):
    # celery
    CELERY_BROKER_URL = 'amqp://liel:1234@localhost:5672//'
    CELERY_IMPORTS = 'app.services.celery_beat.celery_tasks'
    CELERY_ACCEPT_CONTENT = ['json', 'msgpack', 'yaml']
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_TIMEZONE = 'UTC+02:00'
    CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
        'task': 'tasks.add',
        'schedule': 30.0,
        'args': (16, 16)
    },
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


class TestingConfig(Config):
    ENC = 'testing'
    # DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True
