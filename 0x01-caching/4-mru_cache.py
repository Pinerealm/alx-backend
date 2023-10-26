#!/usr/bin/python3
"""MRU Caching"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Implements Most Recently Used caching
    """
    def __init__(self):
        """Runs upon instantiation
        """
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """Puts a key/value pair into cache
        """
        if key and item:
            if key in self.cache_data:
                self.stack.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                discard = self.stack.pop()
                del self.cache_data[discard]
                print("DISCARD: {}".format(discard))
            self.stack.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Gets the value associated with given key
        """
        if key in self.cache_data:
            self.stack.remove(key)
            self.stack.append(key)
        return self.cache_data.get(key)
