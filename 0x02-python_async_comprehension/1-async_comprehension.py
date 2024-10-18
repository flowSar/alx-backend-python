#!/usr/bin/env python3
"""module for Async Comprehensions """
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Async Comprehensions"""
    result = []
    async for i in async_generator():
        result.append(i)
    return result
