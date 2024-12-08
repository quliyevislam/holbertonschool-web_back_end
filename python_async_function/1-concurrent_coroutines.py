#!/usr/bin/env python3
wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio
from typing import List

async def wait_n(n: int, max_delay: int) -> List[float]:
    delays = []
    for _ in range(n):
        delay = await wait_random(n)
        delays.append(delay)

    return delays

print(asyncio.run(wait_n(5, 5)))
print(asyncio.run(wait_n(10, 7)))
print(asyncio.run(wait_n(10, 0)))
