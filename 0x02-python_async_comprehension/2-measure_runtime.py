#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_generator


async def measure_runtime() -> float:
    start_time = time.time()  # Record the start time
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = time.time()

    total_runtime = end_time - start_time
    return total_runtime
