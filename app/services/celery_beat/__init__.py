from abc import ABC
from celery import Celery, Task


def celery_init_app(app):
#     class FlaskTask(Task, ABC):
#         # The Task subclass automatically runs task functions
#         # with a Flask app context active, so that services like your database connections are available
#         # def __call__(self, *args: object, **kwargs: object) -> object:
#         #     with app.app_context():
#         #         return self.run(*args, **kwargs)
#     celery_app = Celery(app.app.name, task_cls=FlaskTask)
#     celery_app.config_from_object("config.CeleryConfig")
#     # The Celery app is set as the default, so that it is seen during each request.
#     celery_app.set_default()
#     # app.extensions["celery"] = celery_app
#     return celery_app
    return True


