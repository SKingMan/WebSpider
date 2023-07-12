#requests破解百度翻译
#需求：破解百度翻译
#   --post请求（携带参数）
#   --响应数据是一组json数据

import requests
import json

if __name__ == '__main__':
    #1,指定url
    post_url = 'https://fanyi.baidu.com/sug'

    #2,UA伪装
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }

    #3,post请求参数处理（同get请求一致）
    data = {
        'kw':'dog'
    }
    #4，请求发送
    response = requests.post(url=post_url,data=data,headers=headers)
    #print(response.status_code)
    #5.获取响应数据：json（）方法返回的是obj（如果确认响应数据是json类型的。才可以使用json方法
    dic_obj = response.json()
    print(dic_obj)

    #6.持久化存储
    fp = open('./dog.json','w',encoding='utf-8')
    json.dump(dic_obj,fp=fp,ensure_ascii=False)
    print('over!!!')