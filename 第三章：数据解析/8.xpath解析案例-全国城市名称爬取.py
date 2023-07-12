
#项目需求：解析出所有城市名称：http://www.aqistudy.cn/historydata/


import requests
from lxml import html

if __name__ == '__main__':
    #自定义变量
    url = 'http://www.aqistudy.cn/historydata/'
    #UA伪装
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }

    page_text = requests.get(url=url, headers=headers).text
    tree = html.etree.HTML(page_text)
    # hot_city = tree.xpath('//div[@class="hot"]//li/a//text()')
    # print("热门城市：", hot_city)
    # all_city = tree.xpath('//div[@class="all"]//li/a//text()')
    # print("全部城市", all_city)
    #一次解析获取全部城市
    all_city = tree.xpath('//div[@class="bottom"]/ul//li//text()')
    print(all_city)