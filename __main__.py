import config
from app import app
from app.route.blog_route import *

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=config.Config.FLASK_RUN_PORT)
    # todo remove
    # worker = worker.worker(app=celery_app)
    # options = {
    #     'broker': 'amqp://liel:1234@localhost:5672//',
    #     'loglevel': 'INFO',
    #     'traceback': True,
    # }
    # worker.run(**options)


