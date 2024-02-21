from app import celery_app


@celery_app.task
def test(arg):
    print(arg)


@celery_app.task
def add(x, y):
    z = x + y
    return z