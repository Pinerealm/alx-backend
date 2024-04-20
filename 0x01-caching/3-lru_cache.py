#!/usr/bin/python3
"""LRU Caching"""
from base_caching import BaseCaching
from collections import deque


class LRUCache(BaseCaching):
    """Implements Least Recently Used caching
    """
    def __init__(self):
        """Runs upon instantiation
        """
        super().__init__()
        self.queue = deque()

    def put(self, key, item):
        """Puts a key/value pair into cache
        """
        if key and item:
            if key in self.cache_data:
                self.queue.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                discard = self.queue.popleft()
                del self.cache_data[discard]
                print("DISCARD: {}".format(discard))
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Gets the value associated with given key
        """
        if key in self.cache_data:
            self.queue.remove(key)
            self.queue.append(key)
        return self.cache_data.get(key)
