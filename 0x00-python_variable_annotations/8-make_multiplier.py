#!/usr/bin/env python3
"""nested functions for calc multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """nested functions for calc multiplier"""
    def multiply_by_multiplier(value: float) -> float:
        return value * multiplier
    return multiply_by_multiplier
