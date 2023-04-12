#!/usr/bin/env python3
"""Learning Redis exercise"""

import uuid
from functools import wraps

import redis
from typing import Callable, Optional, Union


def count_calls(method: Callable) -> Callable:
    """decorator as seen in the functools docs"""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """the wrapper increments the count of __qualname__
        for that key every time the method decorated by
        my_decorator is called and returns the value returned
        by the original method."""

        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """stores the call history with rpush"""

    @wraps(method)
    def wrapper(self, *args):
        """wraps the method"""
        input_name = method.__qualname__ + ":inputs"
        output_name = method.__qualname__ + ":outputs"

        # *args are normalised to str since redis
        # can only store strings, bytes and numbers
        self._redis.rpush(input_name, str(*args))
        output = method(self, *args)
        self._redis.rpush(output_name, str(output))
        return output

    return wrapper


def replay(fn: Callable):
    """display the history of calls of a particular function."""
    r = redis.Redis()
    func_name = fn.__qualname__
    c = r.get(func_name)
    try:
        c = int(c.decode("utf-8"))
    except Exception:
        c = 0
    print("{} was called {} times:".format(func_name, c))
    inputs = r.lrange("{}:inputs".format(func_name), 0, -1)
    outputs = r.lrange("{}:outputs".format(func_name), 0, -1)
    for inp, outp in zip(inputs, outputs):
        try:
            inp = inp.decode("utf-8")
        except Exception:
            inp = ""
        try:
            outp = outp.decode("utf-8")
        except Exception:
            outp = ""
        print("{}(*{}) -> {}".format(func_name, inp, outp))


class Cache:
    def __init__(self):
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    @count_calls
    def get(self, key: str,
            fn: Optional[Callable] = None) \
            -> Union[str, bytes, int, float, None]:
        """return value of key"""
        data = self._redis.get(key)
        if not data:
            return None
        if fn is not None:
            data = fn(data)
        return data

    @count_calls
    def get_str(self, key: str) -> str:
        """ automatically parametrize Cache.get
        with the correct conversion function"""
        data = self._redis.get(key)
        return str(data.decode("utf-8"))

    @count_calls
    def get_int(self, key: str) -> int:
        """ automatically parametrize Cache.get
        with the correct conversion function"""
        data = self._redis.get(key)
        return int(data.decode("utf-8"))
