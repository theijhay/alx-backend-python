#!/usr/bin/env python3
"""Async Comprehensions"""

from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''makes a list of 10 random numbers between 0 and 10'''
    return [num async for num in async_generator()]
