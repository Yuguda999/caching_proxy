# Caching Proxy Server

## Description
A simple CLI tool that starts a caching proxy server. It forwards requests to the actual server, caches the responses, and serves them from the cache if the same request is made again.

## Usage

### Start the Server
```bash
python main.py --port 3000 --origin http://dummyjson.com
```
### Clear the Cache
```bash
python main.py --clear-cache --port=3000 --origin=http://dummyjson.com
```