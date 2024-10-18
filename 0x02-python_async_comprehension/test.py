#!/usr/bin/env python3
import random
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    result = []
    async for i in async_generator():
        result.append(i)

async def main():
    print(await async_comprehension())

asyncio.run(main())