#!/usr/bin/env python3
"""The 0-simple_helper_function module"""


def index_range(page: int, page_size: int) -> tuple:
    """Returns the start and end indexes for pagination"""
    return ((page - 1) * page_size, page * page_size)
