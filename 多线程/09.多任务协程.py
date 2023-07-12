import asyncio
import time

async def request(url):
    print("正在请求的url是：",url)
    #在异步协程中如果出现了同步模块相关的代码，那么就无法实现异步。
    #time.sleep(2)
    #当在asyncio中遇到阻塞时，需要手动挂起。
    await asyncio.sleep(2)
    print("请求成功，",url)
start = time.time()
urls = [
    'www.baidu.com',
    'www.sougou.com',
    'www.goubanjia.com'
]
tasks = []
for url in urls:
    c = request(url)
    task = asyncio.ensure_future(c)
    #task = asyncio.create_task(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

print('总耗时：',time.time()-start,'s')