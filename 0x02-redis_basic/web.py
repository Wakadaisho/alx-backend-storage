#!/usr/bin/env python3
""" Main file """

from functools import wraps
from typing import Callable

import redis
import requests


def count_calls(method: Callable) -> Callable:
    """Count number of times a url is called"""
    @wraps(method)
    def wrapper(*args, **kwargs):
        """A wrapper function"""
        _redis = redis.Redis()
        _redis.incr("count:{}".format(args))
        _redis.expire("count:{}".format(args), 10)
        return method(*args, **kwargs)

    return wrapper


@count_calls
def get_page(url: str) -> str:
    """Use requests to get a url's contents"""
    requests.get(url)
