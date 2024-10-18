#!/usr/bin/env python3
"""multiple coroutines at the same time with async"""
import heapq

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n, max_delay):
    delays = []
    for i in range(n):
        delay = delays.append(await wait_random(max_delay))
        heapq.heappush(delays, delay)
    return delays
