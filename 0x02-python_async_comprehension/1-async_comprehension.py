#!/usr/bin/env python3
"""Async Comprehensions"""

import asyncio
from typing import List
from random import uniform


async def async_generator() -> List[float]:
    """Collect 10 random numbers using an async comprehension
    over async_generator"""
    await asyncio.sleep(1)
    return [uniform(0, 10) for _ in range(10)]


async def async_comprehension() -> List[float]:
    async_gen = await async_generator()
    return [num for num in async_gen]
