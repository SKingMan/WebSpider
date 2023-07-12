#环境安装：pip install aiohttp
#使用该模块中的ClientSession

import requests
import asyncio
import time
import aiohttp

start = time.time()

urls = [
    'https://baidu.com',
    'https://sougou.com',
    'http://goubanjia.com'
]

async def get_page(url):
    async with aiohttp.ClientSession() as session:
        #get(),post():
        #headers,params/data,proxy='http://ip:port'
        async with await session.get(url) as response:
            #text()返回字符串形式的响应数据
            #read（）返回的二进制形式的响应数据
            #json()返回的就是json对象
            #注意：获取响应操作之前一定要使用await进行手动挂起
            page_text = await response.text()
            print(url,len(page_text))
tasks = []
for url in urls:
    c = get_page(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
print('总耗时：',end-start)

            

