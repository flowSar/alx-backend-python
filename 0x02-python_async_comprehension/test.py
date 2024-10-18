#!/usr/bin/env python3
import random
import asyncio
from typing import List
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime():
    start_time = time.time()
    await asyncio.gather(async_comprehension(),
                   async_comprehension(),
                   async_comprehension(),
                   async_comprehension())
    
    end_time = time.time()
    result = end_time - start_time
    return result

async def main():
    return await(measure_runtime())

print(
    asyncio.run(main())
)