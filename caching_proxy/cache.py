import hashlib
import redis
import pickle

class Cache:
    def __init__(self, redis_host='localhost', redis_port=6379, redis_db=0):
        self.redis = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db)

    def _generate_key(self, path):
        return hashlib.md5(path.encode('utf-8')).hexdigest()

    def get(self, path):
        cache_key = self._generate_key(path)
        cached_response = self.redis.get(cache_key)
        if cached_response:
            return pickle.loads(cached_response)
        return None

    def set(self, path, response):
        cache_key = self._generate_key(path)
        self.redis.set(cache_key, pickle.dumps(response))

    def clear(self):
        self.redis.flushdb()
