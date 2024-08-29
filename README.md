# CLI Caching Proxy Tool

A command-line tool that sets up a caching proxy server. The server forwards requests to an origin server, caches the responses, and serves cached responses for repeated requests. It also provides functionality to clear the cache.

**project url:** https://roadmap.sh/projects/caching-server

## Features

- **Start a Caching Proxy Server:** Run the proxy server on a specified port and forward requests to an origin server.
- **Cache Responses:** Cache responses from the origin server and serve them for repeated requests to reduce latency and server load.
- **Cache Headers:** Include headers in the response to indicate whether it was served from the cache or the origin server.
- **Clear Cache:** Clear the cache with a command to reset the stored responses.

## Installation

### Prerequisites

- Python 3.7+
- Redis server (for caching backend)
- Redis Python client (`redis-py`)


## Usage

### Start the Server
```bash
python main.py --port 3000 --origin https://catfact.ninja/fact --redis-host localhost --redis-port 6379 --redis-db 0
```
### Clear the Cache
```bash
python main.py --clear-cache --redis-host localhost --redis-port 6379 --redis-db 0 --port 3000 --origin https://catfact.ninja/fact
```