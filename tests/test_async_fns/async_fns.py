import asyncio
from time import perf_counter

from cliar import Cliar


class AsyncFunctions(Cliar):
    async def wait(self, seconds_to_wait: float = 1.0):
        start = perf_counter()

        await asyncio.sleep(seconds_to_wait)

        print(perf_counter() - start)

if __name__ == "__main__":
    AsyncFunctions().parse()
