#!/usr/bin/env python3
"""This module contains async_generator() function"""
import asyncio
import random


async def async_generator():
    """
    Generates random values between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
