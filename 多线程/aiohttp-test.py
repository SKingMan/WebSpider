import aiohttp
import asyncio

async def get_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print(resp.status)
            result = await resp.text()
            print("get {} length data from {}".format(len(result),url))

async def main():
    url = "http://python.org"
    #https://www.python.org/
    await get_url(url)

if __name__ == '__main__':
    asyncio.run(main())
