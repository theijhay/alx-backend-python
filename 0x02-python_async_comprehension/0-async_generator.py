#!/usr/bin/env python3
""" a python module to loop 10 times """

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''Async generator that yields a random number between 0 and 10'''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
