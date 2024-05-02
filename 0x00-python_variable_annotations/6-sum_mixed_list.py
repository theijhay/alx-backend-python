#!/usr/bin/env python3
"""type-annotated function sum_mixed_list which takes a list mxd_lst """

from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of all int and float"""
    return sum(mxd_lst)
