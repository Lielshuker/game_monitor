from redis import Redis
import config

redis = Redis(host=config.DevelopmentConfig.REDIS_HOST, port=6379)
