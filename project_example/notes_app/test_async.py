import time
import asyncio
import httpx

urls = [
    "http://127.0.0.1:8000/async/one/",
    "http://127.0.0.1:8000/async/two/",
    "http://127.0.0.1:8000/async/three/",
]

async def fetch(client, url):
    start = time.time()
    response = await client.get(url)
    duration = time.time() - start
    print(f"{url} → {duration:.2f} сек")

async def main():
    start_total = time.time()

    async with httpx.AsyncClient() as client:
        await asyncio.gather(
            *(fetch(client, url) for url in urls)
        )

    total_duration = time.time() - start_total
    print(f"\nЗАГАЛЬНИЙ ЧАС (async): {total_duration:.2f} сек")

asyncio.run(main())