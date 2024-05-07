#!/usr/bin/env python3
"""measure_runtime coroutine that will execute async_comprehension"""

import asyncio
import time
from importlib import import_module as using


async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """runs the async comprehension 4 times and returns the runtime
    """
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start
