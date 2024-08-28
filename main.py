import argparse
from caching_proxy.server import CachingProxyServer
from caching_proxy.cache import Cache

def main():
    parser = argparse.ArgumentParser(description='Caching Proxy Server')
    parser.add_argument('--port', type=int, required=True, help='Port to run the caching proxy server on')
    parser.add_argument('--origin', type=str, required=True, help='Origin server URL to forward requests to')
    parser.add_argument('--clear-cache', action='store_true', help='Clear the cache')
    args = parser.parse_args()

    cache = Cache()

    if args.clear_cache:
        cache.clear()
        print('Cache cleared.')
    else:
        server = CachingProxyServer(port=args.port, origin=args.origin, cache=cache)
        server.run()

if __name__ == '__main__':
    main()
