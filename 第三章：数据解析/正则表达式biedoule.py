#需求：爬取别逗了网站中首页下的所有图片

import requests
import re
import os

if __name__ == '__main__':
    #创建图片需要存放的目录
    file_path = './BieDouLe/'
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    #指定url
    url = 'https://www.biedoul.com/pic/'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'

    }
    #使用通用爬虫对url对应的一整张页面进行爬取

    #发送请求
    page_text = requests.get(url=url,headers=headers).text
    #print(type(page_text))

    #打印响应数据的前一部分
    #print(page_text[1183:5000])
    #page_text_body = page_text[1183:5000]
    #使用聚焦爬虫将页面中所有的图片进行解析/提取


    #----------------------------------总结-------------------------------
    #费劲千辛万苦终于把我需要的内容解析出来了，之前一直为空列表的原因就是正则表达式写错了，通过打印page_text前一部分的内容，
    #我发现前端显示的标签都是小写的，但是通过打印发现很多标签都是大写的，而正则表达式是严格区分大小写的。当然也可以不让它
    #区分大小写，可以设置参数re.I,就是不区分大小写。
    #下面这段代码就是实现了不区分大小写的方式。
    # pattern = re.compile(ex4,re.I)#不区分大小写的模式
    # img_list = pattern.findall(page_text_body,re.S)
    # print(img_list)
    #-----------------------------------/总结------------------------------


    #定义正则表达式
    ex4 = '<DD>.*?<img src="(.*?)".*?</DD>'

    img_src_list = re.findall(ex4,page_text,re.S)
    #print(img_src_list)
    for each in img_src_list:
        #请求到了图片的二级制数据
        img_data = requests.get(url=each,headers=headers).content
        #生成图片名称
        img_name = each.split('/')[-1]
        #图片最终存储的路径
        img_path = file_path + img_name
        #print('图片名称：',img_name)
        with open(img_path,'wb') as fp:
            fp.write(img_data)
            print(img_name,'下载完成！')
