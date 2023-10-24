#!/usr/bin/python3
"""BasicCache module"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Defines a basic cache system, inherits from BaseCaching
    """
    def put(self, key, item):
        """Adds key/value pair to cache data
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves value from key in cache data
        """
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None
