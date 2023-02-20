#!/usr/bin/env python3
"""takes two argument start index and end index"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    end = page_size * page
    return end - page_size, end
