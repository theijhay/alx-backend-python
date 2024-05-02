#!/usr/bin/env python3
"""type-annotated function make_multiplier that takes a float multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiplier_func(num: float) -> float:
        """multiply the input num by the multiplier"""
        return num * multiplier
    return multiplier_func
