#!/usr/bin/env python3

"""
Cache module.
"""

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps

def count_calls(method: Callable) -> Callable:
    """
    Decorator function to count the number of times a method is called.

    Args:
        method (Callable): The method to be decorated.

    Returns:
        Callable: The wrapped method with counting functionality.
    """
    key = method.__qualname__

    @wraps(method)
    def wrapped_method(self, *args, **kwargs):
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapped_method


def call_history(method: Callable) -> Callable:
    """
    Decorator function to store the history of inputs and outputs for a particular function.

    Args:
        method (Callable): The method to be decorated.

    Returns:
        Callable: The wrapped method with history storage functionality.
    """
    input_list_key = "{}:inputs".format(method.__qualname__)
    output_list_key = "{}:outputs".format(method.__qualname__)

    @wraps(method)
    def wrapped_method(self, *args, **kwargs):
        input_str = str(args)
        self._redis.rpush(input_list_key, input_str)

        output = method(self, *args, **kwargs)
        self._redis.rpush(output_list_key, output)

        return output

    return wrapped_method

class Cache:
    """
    Cache class for storing data in Redis.
    """

    def __init__(self):
        """
        Initialize the Cache class with a Redis client instance.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the input data in Redis using a random key (generated using uuid) and return the key.

        Args:
            data (Union[str, bytes, int, float]): The data to be stored in Redis.

        Returns:
            str: The randomly generated key used to store the data in Redis.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """
        Retrieve data from Redis using the provided key and optionally convert it using the given function.

        Args:
            key (str): The key used to retrieve data from Redis.
            fn (Optional[Callable]): A callable function to convert the retrieved data. Defaults to None.

        Returns:
            Union[str, bytes, int, float]: The retrieved data from Redis, optionally converted by the provided function.
        """
        data = self._redis.get(key)
        if data is not None and fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """
        Retrieve data from Redis using the provided key and convert it to a UTF-8 string.

        Args:
            key (str): The key used to retrieve data from Redis.

        Returns:
            str: The retrieved data as a UTF-8 string.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        Retrieve data from Redis using the provided key and convert it to an integer.

        Args:
            key (str): The key used to retrieve data from Redis.

        Returns:
            int: The retrieved data as an integer.
        """
        return self.get(key, fn=int)


def replay(method: Callable):
    """
    Function to display the history of calls of a particular function.

    Args:
        method (Callable): The method for which to display the history of calls.
    """
    # Access the Cache instance the method is bound to
    cache_instance = method.__self__

    input_list_key = "{}:inputs".format(method.__qualname__)
    output_list_key = "{}:outputs".format(method.__qualname__)

    inputs = cache_instance._redis.lrange(input_list_key, 0, -1)
    outputs = cache_instance._redis.lrange(output_list_key, 0, -1)

    print(f"{method.__qualname__} was called {len(inputs)} times:")

    for inp, out in zip(inputs, outputs):
        print(f"{method.__qualname__}{inp.decode()} -> {out.decode()}")
