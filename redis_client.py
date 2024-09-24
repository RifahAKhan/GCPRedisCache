# redis_client.py
import redis

def get_redis_client(redis_host, redis_port=6378):
    return redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=False)
