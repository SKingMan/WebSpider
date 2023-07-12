
#需求：爬取58二手房中的房源信息

import requests
from lxml import html

if __name__ == "__main__":

    url = 'https://sh.58.com/ershoufang/'
    #UA伪装
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    #爬取到页面的源码数据
    response = requests.get(url=url,headers=headers)
    response.encoding = 'utf-8'#修改response对象的编码，防止出现中文乱码
    page_text = response.text
    #print(page_text[:5000])
    #数据解析
    tree = html.etree.HTML(page_text)
    #存储的是div标签列表，每个元素就是一个房源信息
    div_list = tree.xpath('//section[@class="list"]/div')
    if len(div_list) == 0:
        print("爬取的内容为空！")
        exit()
    fp = open('./58house.txt','w',encoding='utf-8')
    for div in div_list:
        #因为这是在循环体内，能再用/，因为会理解为整个html的根标签，./表示的是当前标签，
        #类似 linux系统的目录，./代表当前目录。
        #局部数据解析
        title = div.xpath('./a/div[2]//h3/text()')[0]#./ 代表的就是当前的div标签

        fp.write(title+'\n')

    fp.close()
    print(div_list)




