import aiohttp
import asyncio
import time

# Configuration
URL = '' # URL being tested
LOAD_COUNT = 1000 # Number of requests
DISABLE_SSL = True # Disable SSL verification (set to False to enable)

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        # Disable SSL verification if configured
        ssl_option = False if DISABLE_SSL else True
        async with session.get(url, ssl=ssl_option) as response:
            return await response.text()

async def main(url, count):
    tasks = []
    for _ in range(count):
        tasks.append(fetch(url))
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(main(URL, LOAD_COUNT))
    print(f"Completed {LOAD_COUNT} requests in {time.time() - start_time:.2f} seconds.")
