from app import app
from route.blog_route import *
if __name__ == '__main__':
    app.run(debug=True, port=5000)