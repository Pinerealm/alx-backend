#!/usr/bin/python3
"""FIFO caching"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO Cache"""

    def __init__(self):
        """Runs on instantiation"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Puts a key/value pair into cache"""
        if key and item:
            if key in self.cache_data:
                self.queue.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                discard = self.queue.pop(0)
                del self.cache_data[discard]
                print("DISCARD: {}".format(discard))
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Gets the value associated with given key"""
        return self.cache_data.get(key)
