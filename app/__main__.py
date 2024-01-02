from app import config
from route.blog_route import *
if __name__ == '__main__':
    # app.config[""]
    app.config.from_object('config.DevelopmentConfig')
    app.run(port=config.Config.FLASK_RUN_PORT)
