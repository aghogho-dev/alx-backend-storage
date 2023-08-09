
#!/usr/bin/env python3
"""Redis module"""
from functools import wraps
import redis
from typing import Callable, Optional, Union
from uuid import uuid4



def count_calls(method: Callable) -> Callable:
    """Count call function"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function"""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    """call history function"""
    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function"""
        self._redis.rpush(inputs, str(args))
        data = method(self, *args, **kwargs)
        self._redis.rpush(outputs, str(data))
        return data
    return wrapper

def replay(method: Callable) -> None:
    """Replay function"""
    name = method.__qualname__
    cache = redis.Redis()
    calls = cache.get(name).decode("utf-8")
    print(f"{name} was called {calls} times:")
    inputs = cache.lrange(name + ":inputs", 0, -1)
    outputs = cache.lrange(name + ":outputs", 0, -1)
    for i, o in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(name, i.decode('utf-8'),
                                     o.decode('utf-8')))


class Cache:
    """Cache"""
    def __init__(self):
        """Initialize"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store method"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """Get method"""
        v = self._redis.get(key)
        return fn(value) if fn else value

    def get_str(self, key: str) -> str:
        """Get str method"""
        return self._redis.get(key).decode("utf-8")

    def get_int(self, key: str) -> int:
        """Get int method"""
        v = self._redis.get(key)
        try:
            v = int(value.decode('utf-8'))
        except Exception:
            v = 0
        return v
