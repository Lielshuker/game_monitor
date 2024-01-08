from flask import Flask

from app.services.celery_beat import celery_init_app


def init_app():
    flask_app = Flask(__name__)
    flask_app.config.from_object('config.DevelopmentConfig')
    return flask_app


app = init_app()
celery_app = celery_init_app(app)
celery_app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'tasks.add',
        'schedule': 30.0,
        'args': (16, 16)
    },
}
celery_app.conf.timezone = 'UTC'


