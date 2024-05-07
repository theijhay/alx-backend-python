#!/usr/bin/env python3
"""Async Comprehensions"""

import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
    Collect 10 random numbers using an async comprehension
    over async_generator.
    """
    result = [num async for num in async_generator()]
    return result
