#!/usr/bin/env python3
"""This module contains async_comprehension() function"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
            Generate numbers with async comprenhension

            Args:
                void

            Return:
                float random numbers
        """
    nums = []
    async for num in async_generator():
        nums.append(num)
    return nums
