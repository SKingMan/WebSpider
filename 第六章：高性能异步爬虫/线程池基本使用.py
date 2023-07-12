# import time
# #使用单线程串行方式执行
#
# def get_page(str):
#     print("正在下载：", str)
#     time.sleep(2)
#     print("下载成功：", str)
#
# name_list = ['xiaozi', 'aa', 'bb', 'cc']
#
# start_list = time.time()
#
# for i in range(len(name_list)):
#     get_page(name_list[i])
#
# end_time = time.time()
# print('%d second'% (end_time-start_list))



import time
#导入线程池模块对应的类
from multiprocessing.dummy import Pool
#使用线程池方式执行

start_list = time.time()

def get_page(str):
    print("正在下载：", str)
    time.sleep(2)

    print("下载成功：", str)
    return str

name_list = ['xiaozi', 'aa', 'bb', 'cc']

#实例化一个线程池对象
#pool = Pool(2)
#将列表中每一个列表元素传递给get_page进行处理。

text = []
result = list(map(get_page, name_list))
print(result)
# for i in name_list:
#     text.append(get_page(i))
# print(text)
end_time = time.time()
print('%d second'% (end_time-start_list))