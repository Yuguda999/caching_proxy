import http.server
import requests
from urllib.parse import urlparse

class CachingProxyHandler(http.server.BaseHTTPRequestHandler):
    def __init__(self, *args, cache=None, origin=None, **kwargs):
        self.cache = cache
        self.origin = origin
        super().__init__(*args, **kwargs)

    def do_GET(self):
        parsed_url = urlparse(self.path)
        cached_response = self.cache.get(self.path)

        if cached_response:
            # Serve from cache
            self.send_response(200)
            self.send_header('X-Cache', 'HIT')
            for header, value in cached_response['headers'].items():
                self.send_header(header, value)
            self.end_headers()
            self.wfile.write(cached_response['content'])
        else:
            # Fetch from origin server
            response = requests.get(f'{self.origin}{parsed_url.path}')
            self.send_response(response.status_code)
            self.send_header('X-Cache', 'MISS')
            for header, value in response.headers.items():
                self.send_header(header, value)
            self.end_headers()
            content = response.content
            self.wfile.write(content)

            # Store in cache
            self.cache.set(self.path, {
                'headers': response.headers,
                'content': content
            })
