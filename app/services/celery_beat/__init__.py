from celery import Celery

import config


def celery_init_app():
    celery_app = Celery(__name__, backend=config.CeleryConfig.CELERY_BACKEND_URL,
                        broker=config.CeleryConfig.CELERY_BROKER_URL)
    return celery_app


