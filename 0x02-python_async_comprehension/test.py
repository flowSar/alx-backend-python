#!/usr/bin/env python3
import random
import asyncio

async def async_generator() -> float:
    numbers = []
    for _ in range(9):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(print_yielded_values())