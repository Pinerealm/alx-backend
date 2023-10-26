#!/usr/bin/python3
"""LFU Caching"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Implements Least Frequently Used caching
    """
    def __init__(self):
        """Runs upon instantiation
        """
        super().__init__()
        self.queue = []
        self.freq = {}

    def put(self, key, item):
        """Puts a key/value pair into cache
        """
        if key and item:
            if key in self.cache_data:
                self.queue.remove(key)
                self.freq[key] += 1
            elif len(self.cache_data) >= self.MAX_ITEMS:
                discard = min(self.freq, key=self.freq.get)
                del self.cache_data[discard]
                del self.freq[discard]
                print("DISCARD: {}".format(discard))
            self.queue.append(key)
            self.cache_data[key] = item
            self.freq[key] = 1

    def get(self, key):
        """Gets the value associated with given key
        """
        if key in self.cache_data:
            self.queue.remove(key)
            self.queue.append(key)
            self.freq[key] += 1
        return self.cache_data.get(key)
