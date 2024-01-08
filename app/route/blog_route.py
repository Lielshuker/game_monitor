from app import app
from app.controllers.default_controller import blog_get
from app.services.celery_beat.celery_tasks import add
from flask import jsonify


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/blog")
def get_blog():
    add.delay(3, 3)
    # return blog_get()
    return jsonify(msg='pong')
