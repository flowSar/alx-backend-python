#!/usr/bin/env python3
import random
import asyncio
import heapq

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n, max_delay):
    delays = []
    for i in range(n):
        delay = delays.append(await wait_random(max_delay))
        heapq.heappush(delays, delay)
    return delays


print(asyncio.run(wait_n(5, 5)))
print(asyncio.run(wait_n(10, 7)))
print(asyncio.run(wait_n(10, 0)))






