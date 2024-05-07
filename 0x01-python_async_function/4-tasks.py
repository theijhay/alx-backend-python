#!/usr/bin/env python3
"""Take the code from wait_n and alter it into a new function task_wait_n"""

from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list[float]:
    """
    Spawn task_wait_random n times with the specified max_delay.
    """
    delays = []
    tasks = []

    for _ in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)

    for task in sorted(tasks, key=lambda t: t.get_name().split('-')[-1]):
        delay = await task
        delays.append(delay)

    return delays
