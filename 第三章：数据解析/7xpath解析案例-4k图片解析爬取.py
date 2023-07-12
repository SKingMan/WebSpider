
#需求：解析下载图片数据：https://pic.netbian.com/4kmeinv/

import requests
from lxml import html
import os

if __name__ == "__main__":

    url = 'https://pic.netbian.com/4kmeinv/'
    #UA伪装
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    #发送请求，获取网页源码数据
    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf-8'
    page_text = response.text

    #xpath解析数据
    tree = html.etree.HTML(page_text)

    #获取li标签的列表，每个元素都是一个图片
    li_list = tree.xpath('//div[@class="slist"]/ul/li')
    #将图片保存到指定位置
    file_path = './BiAnTu/'
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    for li in li_list:
        #每个li代表一个局部的li标签，现在进行局部数据解析，获取高清图片的网址
        href_url = li.xpath('./a/@href')[0]
        # https://pic.netbian.com/tupian/31524.html
        #网址拼接,也就是高清大图的网址
        hight_img_url = 'https://pic.netbian.com'+href_url
        #高清图片的页面，需要对该页面进行解析，获取高清图片的url，获取高清图片网址的源码
        img_text = requests.get(url=hight_img_url, headers=headers).text
        #xpath解析数据，获取高清图片的url
        hight_tree = html.etree.HTML(img_text)
        img_url = hight_tree.xpath('//a[@id="img"]/img/@src')[0]
        img_url = 'https://pic.netbian.com'+img_url
        img_name = img_url.split('/')[-1]

        #从高清图片的url中获取高清图片的二进制数据
        img_data = requests.get(url=img_url,headers=headers).content
        img_path = file_path + img_name
        with open(img_path, 'wb') as fp:
            fp.write(img_data)
            print(img_name, '下载完成！')
    print('全部下载完成')











