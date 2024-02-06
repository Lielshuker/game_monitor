# from celery.result import AsyncResult

from app import app
from app.services.Redis.simple_redis_task import redis_task
from flask import jsonify

from app.services.celery_beat.celery_tasks import add, celery_app


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/blog")
def get_blog():
    return jsonify(msg='pong')


@app.route("/redis_count")
def redis_counter():
    counter = redis_task()
    return "This webpage has been viewed "+counter+" time(s)"


@app.route("/add")
def celery_add_task():
    x = 1
    y = 2
    # z = add(x, y)
    task = add.delay(x, y)
    return {"result_id": task.id}
    # return jsonify({'task_id': task.result}), 202
    # return "<p>Hello, World!</p>"


@app.route("/result/<id>")
def task_result(id):
    result = celery_app.AsyncResult(id)
    return {
        "ready": result.ready(),
        "successful": result.successful(),
        "value": result.result if result.ready() else None,
    }

