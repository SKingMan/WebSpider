import asyncio

# async def dog(name):
#     print("汪汪汪！")
#     print("我是小狗 %s"%name)
#
# #用async修改函数，会返回一个协程对象，其实就是创建协程对象的方法
# coroutine = dog('旺财')
# #创建一个事件循环
# loop = asyncio.get_event_loop()
# #将协程注册到事件循环中,然后启动事件循环
# loop.run_until_complete(coroutine)

async def func1():
    print('协程1')

async def func2():
    print('协程2')

task = [func1(),func2()]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(task))
loop.close()