#!/usr/bin/env python3
""" a python module to loop 10 times """

import random
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Async generator that yields a random number between 0 and 10 every second,
    10 times.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
