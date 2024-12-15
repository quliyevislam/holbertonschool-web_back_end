#!/usr/bin/env python3
"""This module contains async_comprehension() function"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
       Asynchronously collects values from an async generator and returns
       them as a list.

       It iterates over values produced by the `async_generator()`
       and appends them to a list.
        args:
            void
       Returns:
           List[float]: A list of float values from the async generator.
       """
    nums = []
    async for num in async_generator():
        nums.append(num)
    return nums
