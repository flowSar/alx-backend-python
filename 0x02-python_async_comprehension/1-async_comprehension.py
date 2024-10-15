#!/usr/bin/env python3
"""module for Async Comprehensions """
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """Async Comprehensions"""
    return [number async for number in async_generator()]
