from app.services.Redis import redis


def redis_task():
    redis.incr('hits')
    counter = str(redis.get('hits'),'utf-8')
    return counter
