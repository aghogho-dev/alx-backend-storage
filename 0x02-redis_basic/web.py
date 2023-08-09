#!/usr/bin/env python3
"""Web module"""
from functools import wraps
import redis
import requests
from typing import Callable


r = redis.Redis()

def count_requests(method: Callable) -> Callable:
    """Count request function"""
    @wraps(method)
    def wrapper(url):
        """Wrapper function"""
        r.incr(f"count:{url}")
        c = r.get(f"cached:{url}")
        if c:
            return c.decode("utf-8")
        html = method(url)
        r.setex(f"cached:{url}", 10, html)
        return html
    return wrapper

@count_requests
def get_page(url: str) -> str:
    """Get page URL"""
    return requests.get(url).text
