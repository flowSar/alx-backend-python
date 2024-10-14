#!/usr/bin/env python3
"""multiple coroutines at the same time with async"""
import asyncio
from typing import List
from previous_file import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """function for multiple coroutines at the same time with async"""
    delays = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)
        delays.sort()

    return delays
