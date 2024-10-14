#!/usr/bin/env python3
"""measures the total execution time"""
import time
import asyncio
from previous_file import wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measures the total execution time"""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    return total_time / n
