from app import app
from app.services.Redis.simple_redis_task import redis_task
from flask import jsonify


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
