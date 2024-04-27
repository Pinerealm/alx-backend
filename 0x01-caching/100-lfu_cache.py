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

            elif len(self.cache_data) >= self.MAX_ITEMS:
                min_freq = min(self.freq.values())
                # Get keys with min frequency
                min_freq_keys = [k for k, v in self.freq.items()
                                 if v == min_freq]

                # If there's more than one key with the same min frequency
                if len(min_freq_keys) > 1:
                    # Get the least recently used key
                    min_freq_keys = sorted(min_freq_keys,
                                           key=lambda x: self.queue.index(x))
                discard = min_freq_keys[0]

                self.queue.remove(discard)
                del self.cache_data[discard]
                del self.freq[discard]
                print("DISCARD: {}".format(discard))

            self.queue.append(key)
            self.cache_data[key] = item
            self.freq[key] = self.freq.get(key, 0) + 1

    def get(self, key):
        """Gets the value associated with given key
        """
        if key in self.cache_data:
            self.queue.remove(key)
            self.queue.append(key)
            self.freq[key] += 1
        return self.cache_data.get(key)
