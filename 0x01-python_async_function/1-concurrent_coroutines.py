#!/usr/bin/env python3
"""Execute multiple coroutines at the same time with async"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """
    Spawn wait_random n times with the specified max_delay.
    """
    delays = []
    tasks = []

    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    for task in sorted(tasks, key=lambda t: t.get_name().split('-')[-1]):
        delay = await task
        delays.append(delay)

    return delays
