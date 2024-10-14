#!/usr/bin/env python3
"""task_wait_random"""
import asyncio
from 0_basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """task_wait_random"""
    task = asyncio.create_task(wait_random(max_delay))
    return task
