import http.server
from .handler import CachingProxyHandler

class CachingProxyServer:
    def __init__(self, port, origin, cache):
        self.port = port
        self.origin = origin
        self.cache = cache

    def run(self):
        handler = lambda *args, **kwargs: CachingProxyHandler(*args, cache=self.cache, origin=self.origin, **kwargs)
        server_address = ('', self.port)
        httpd = http.server.HTTPServer(server_address, handler)
        print(f'Starting caching proxy server on port {self.port}, forwarding to {self.origin}...')
        httpd.serve_forever()
