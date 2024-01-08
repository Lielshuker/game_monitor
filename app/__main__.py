from app import config, celery_app
from route.blog_route import *
from celery.bin import worker

if __name__ == '__main__':
    app.run(port=config.Config.FLASK_RUN_PORT)
    worker = worker.worker(app=celery_app)
    options = {
        'broker': 'amqp://liel:1234@localhost:5672//',
        'loglevel': 'INFO',
        'traceback': True,
    }
    worker.run(**options)


