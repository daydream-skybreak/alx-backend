#!/usr/bin/env python3
""""""
import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """initializes the object"""
        self.__dataset = None

    @staticmethod
    def index_range(page: int, page_size: int) -> Tuple:
        """function to return start and end index"""
        end = page_size * page
        return end - page_size, end

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """returns the page appropriate list of data from self.__dataset"""
        if type(page) is not int or page < 1:
            raise AssertionError
        if type(page_size) is not int or page_size < 1:
            raise AssertionError
        self.dataset()
        begin, end = self.index_range(page, page_size)
        return self.__dataset[begin: end]
