import unittest
import redis
from caching_proxy.cache import Cache

class TestCache(unittest.TestCase):
    def setUp(self):
        self.cache = Cache(redis_db=1) 
        self.redis = redis.StrictRedis(db=1)
        self.redis.flushdb()

    def test_set_and_get_cache(self):
        path = "/test-path"
        response = {
            "headers": {"Content-Type": "application/json"},
            "content": b'{"message": "Hello, World!"}'
        }
        self.cache.set(path, response)
        cached_response = self.cache.get(path)
        self.assertEqual(cached_response, response)

    def test_clear_cache(self):
        path = "/test-path"
        response = {"headers": {}, "content": b""}
        self.cache.set(path, response)
        self.cache.clear()
        cached_response = self.cache.get(path)
        self.assertIsNone(cached_response)

if __name__ == '__main__':
    unittest.main()
