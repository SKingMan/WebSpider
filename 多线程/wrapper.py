#装饰器，在不改变函数内容的情况下，增加函数的功能，比如打印函数的开始和结束日志，
#打印函数的执行时间。

import time

def log_start(func):
    #打印输入函数的开始和结束标识，写语法糖的时候，应该写在最上面
    def wrapper(*params):
        print('------------程序运行开始------------')
        func(*params)

    return wrapper

def log_end(func):
    #打印输入函数的开始和结束标识，写语法糖的时候，应该写在最上面
    def wrapper(*params):
        func(*params)
        print('------------程序运行结束------------')
    return wrapper


def calculate_time(func):
    def wrapper(*params):
        start = time.time()
        func(*params)
        end = time.time()
        count = end-start
        minutes = int(count / 60)
        seconds = count % 60
        print('程序运行时间：{0}分{1}秒'.format(minutes,seconds))
    return wrapper


if __name__ == '__main__':
    @log_start
    @calculate_time
    @log_end
    def eat(name):
        time.sleep(66)
        print('%s吃完了！'%name)

    eat('小王')