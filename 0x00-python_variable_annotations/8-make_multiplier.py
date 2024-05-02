#!/usr/bin/env python3
"""type-annotated function make_multiplier that takes a float multiplier"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiplier_func(num: float) -> float:
        return num * multiplier
    """Returns the inner function"""
    return multiplier_func
