import asyncio
from time import perf_counter

from cliar import Cliar


class AsyncFunctions(Cliar):
    async def wait(self, seconds_to_wait: float = 1.0):
        t1 = perf_counter()
        await asyncio.sleep(seconds_to_wait)
        elapsed = perf_counter() - t1
        print(elapsed)

if __name__ == "__main__":
    AsyncFunctions().parse()
