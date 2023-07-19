#!/usr/bin/env python3
""" Main file """

from exercise import Cache, replay

cache = Cache()

# Make some calls to the Cache.store method
s1 = cache.store("foo")
s2 = cache.store("bar")
s3 = cache.store(42)

# Print the return values of Cache.store calls
print(s1)
print(s2)
print(s3)

# Show the history of calls for Cache.store using the replay function
replay(cache.store)
