#!/usr/bin/env python3
"""measures the total execution time"""
import time
import asyncio
import time

wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    task = asyncio.create_task(wait_random(max_delay))
    return task





async def test(max_delay: int) -> float:
    task = task_wait_random(max_delay)
    await task
    print(task.__class__)

asyncio.run(test(5))
