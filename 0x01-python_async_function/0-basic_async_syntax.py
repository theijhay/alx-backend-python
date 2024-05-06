#!/usr/bin/env python3
"""Contains a coroutine that delays a certain amount of time and returns it"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''Waits for another random number'''
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
