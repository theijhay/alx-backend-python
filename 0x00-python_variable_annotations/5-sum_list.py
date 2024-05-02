#!/usr/bin/env python3
"""type-annotated function sum_list which takes a list input_list"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns the sum of float in the list"""
    return sum(input_list)
