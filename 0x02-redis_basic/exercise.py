
#!/usr/bin/env python3
"""Redis module"""
from functools import wraps
import redis
from typing import Callable, Optional, Union
from uuid import uuid4



class Cache:
    """Cache"""
    def __init__(self):
        """Initialize"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, btyes, int, float]) -> str:
        """Store method"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key
