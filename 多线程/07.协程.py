import asyncio

async def request(url):
    print("正在请求的url是：",url)
    print("请求成功，",url)
    return url
#async修饰的函数，调用之后返回的一个协程对象
c = request('www.baidu.com')

# #创建一个事件循环对象
# loop = asyncio.get_event_loop()
#
# #将协程对象注册到loop中，然后启动loop
# loop.run_until_complete(c)

# #task的使用
# #创建一个事件循环
# loop = asyncio.get_event_loop()
# #基于loop创建一个task
# task = loop.create_task(c)
# print(task)
# loop.run_until_complete(task)
# print(task)

# #future的使用
# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(c)
# print(task)
# loop.run_until_complete(task)
# print(task)

#绑定回调，什么时候绑定回调函数，在任务创建完成之后，在任务执行之前。
#绑定回调函数就是在任务执行成功之后再去执行回调函数。
def call_bakc(task):
    print('此时任务已经执行成功了，需要回调我了！')
    print(task.result())


# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(c)
# task.add_done_callback(call_bakc)
# print("此时任务还没执行")
# loop.run_until_complete(task)

#
# loop = asyncio.get_event_loop()
# task = loop.create_task(c)
# task.add_done_callback(call_bakc)
# loop.run_until_complete(task)

