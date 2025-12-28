import asyncio
import datetime
import aiohttp 

# 1.1 и 1.2: Асинхронные часы 
async def async_clock():
    while True:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"\r{now}", end="", flush=True)
        await asyncio.sleep(1)

# 1.5: Веб-скрапер 
class AsyncScraper:
    async def fetch(self, session, url):
        async with session.get(url) as response:
            return await response.text()

    async def run(self, urls):
        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch(session, url) for url in urls]
            return await asyncio.gather(*tasks) 