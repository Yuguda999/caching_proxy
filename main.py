import argparse
from caching_proxy.server import CachingProxyServer
from caching_proxy.cache import Cache

def main():
    parser = argparse.ArgumentParser(description='Caching Proxy Server')
    parser.add_argument('--port', type=int, required=True, help='Port to run the caching proxy server on')
    parser.add_argument('--origin', type=str, required=True, help='Origin server URL to forward requests to')
    parser.add_argument('--clear-cache', action='store_true', help='Clear the cache')
    parser.add_argument('--redis-host', type=str, default='localhost', help='Redis server hostname')
    parser.add_argument('--redis-port', type=int, default=6379, help='Redis server port')
    parser.add_argument('--redis-db', type=int, default=0, help='Redis database number')
    args = parser.parse_args()

    cache = Cache(redis_host=args.redis_host, redis_port=args.redis_port, redis_db=args.redis_db)

    if args.clear_cache:
        cache.clear()
        print('Cache cleared.')
    else:
        server = CachingProxyServer(port=args.port, origin=args.origin, cache=cache)
        server.run()

if __name__ == '__main__':
    main()
