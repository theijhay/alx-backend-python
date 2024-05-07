#!/usr/bin/env python3
"""Take the code from wait_n and alter it into a new function task_wait_n"""

from typing import List
import asyncio
from random import uniform


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''Performs task_wait_random n times'''
    times = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(times)
