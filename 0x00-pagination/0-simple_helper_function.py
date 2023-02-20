#!/usr/bin/env python3
"""takes two argument start index and end index"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """function to return start and end index"""
    end = page_size * page
    return end - page_size, end
