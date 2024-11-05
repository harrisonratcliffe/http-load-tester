# HTTP Load Tester

A simple Python script that allows you to quickly test the load on your website by making a configurable number of concurrent requests.

## Features
- Asynchronous requests using the `aiohttp` library for efficient handling of many requests
- Ability to disable SSL verification for testing purposes
- Outputs the total time taken to complete the specified number of requests

## Usage

1. Clone the repository:
   ```
   git clone https://github.com/harrisonratcliffe/http-load-tester.git
   ```

2. Navigate to the project directory:
   ```
   cd http-load-tester
   ```

3. Update the `URL` variable in the script to the URL you want to test.

4. Adjust the `LOAD_COUNT` variable to the number of requests you want to make.

5. Set the `DISABLE_SSL` variable to `True` if you want to disable SSL verification, or `False` to keep it enabled.

6. Run the script:
   ```
   python main.py
   ```

   The script will output the total time taken to complete the specified number of requests.

## Example Code

```python
import aiohttp
import asyncio
import time

# Configuration
URL = 'https://yourdomain.com' # URL being tested
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
```