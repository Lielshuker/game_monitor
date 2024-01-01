# from app import app
from app import app
from app.controllers.default_controller import blog_get


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/blog")
def get_blog():
    return blog_get()