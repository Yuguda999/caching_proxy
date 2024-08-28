import hashlib

class Cache:
    def __init__(self):
        self.cache = {}

    def _generate_key(self, path):
        return hashlib.md5(path.encode('utf-8')).hexdigest()

    def get(self, path):
        cache_key = self._generate_key(path)
        return self.cache.get(cache_key, None)

    def set(self, path, response):
        cache_key = self._generate_key(path)
        self.cache[cache_key] = response

    def clear(self):
        self.cache.clear()
