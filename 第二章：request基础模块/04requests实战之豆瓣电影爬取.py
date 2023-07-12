#requests实战之豆瓣电影爬取
#需求：爬取豆瓣电影网页的电影相关数据并保存到本地

import requests
import json

if __name__ == '__main__':
    #1,指定url
    url = 'https://movie.douban.com/j/chart/top_list?'
    param = {
        'type':'24',
        'interval_id':'100:90',
        'action':'',
        'start':'0',#从库中的第几部电影开始取
        'limit':'20',#一次取出多少个
    }
    #UA伪装：将对应的User-Agent封装到一个字典中
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }

    #2.发送请求
    response = requests.get(url=url,params=param,headers=headers)

    #3.获取响应的数据
    list_data = response.json()

    #4,持久化存储
    fp = open('./douban.json','w',encoding='utf-8')
    json.dump(list_data,fp=fp,ensure_ascii=False)

    print('over!!!')