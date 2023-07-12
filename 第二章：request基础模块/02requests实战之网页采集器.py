#requests实战，网页采集器
#输入一个关键字，搜狗搜索到的页面就是我们要采集的页面，其实就是给搜狗传入一个关键字参数
#需求：爬取搜狗指定词条赌赢的搜索结果页面（简易网页采集器）

#UA检测：门户网站的服务器会检测对应请求的载体身份表示，如果检测到请求的载体身份便是为某一款浏览器
#说明当前请求是一个正常的请求。但是，如果检测到请求的载体身份标识不是基于某一款浏览器的，则表示该请求
#为不正常的请求（爬虫），则服务器端就很有可能拒绝该请求。

#UA伪装：让爬虫伪装为一款浏览器

#UA：User-Agent ()

import requests
import os

if __name__ == "__main__":
    #UA伪装：将对应的User-Agent封装到一个字典中
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }

    #处理url携带的参数：封装到字典中
    key = input("请输入您要搜索的关键字")
    param = {
        'query':key
    }

    #step1:指定url
    url = "https://sogou.com/web?"

    #step2:发起请求
    response = requests.get(url = url,params=param,headers=headers)
    print(response.status_code)
    #step3:获取响应数据
    page_text = response.text

    #step4:持久化存储
    #创建存储采集页面的文件夹--采集器结果集
    filePath = './采集器结果集/'
    #如果文件夹不存在则创建文件夹
    if not os.path.exists(filePath):
        os.mkdir(filePath)
    fileName = '%s%s.html'%(filePath,key)
    with open(fileName,'w',encoding='utf-8') as fp:
        fp.write(page_text)

    print(fileName,"采集完成！！！")