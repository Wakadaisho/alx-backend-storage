#!/usr/bin/env python3
"""
Redis Cache module
"""
import uuid
from typing import Union, Callable, List
from functools import wraps

import redis


def count_calls(method: Callable) -> Callable:
    """
    Decorator that counts how many times
    methods of the Cache class are called
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """A wrapper function"""
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator to store the history of inputs and
    outputs for a particular function.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """A wrapper function"""
        input = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", input)
        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", output)
        return output
    return wrapper


class Cache:
    """Class that manages a redis cache instance"""
    def __init__(self):
        self._redis = redis.Redis()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in the redis cache"""
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int,
                                                          float]:
        """Retrieve data from the redis store
        converted through fn to correct type"""
        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self, key: str) -> str:
        """Retrive string data from redis store"""
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """Retrieve integer data from redis store"""
        return self.get(key, int)


def replay(method: Callable):
    """
    Returns history of input commands with their corresponding outputs
    """
    _redis = redis.Redis()
    key: str = method.__qualname__
    print("{} was called {} times".format(key,  int(_redis.get(key))))
    inputs: List[str] = _redis.lrange(key + ":inputs", 0, -1)
    outputs: List[str] = _redis.lrange(key + ":outputs", 0, -1)
    for i, o in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(key, i.decode("utf-8"),
                                     o.decode("utf-8")))
