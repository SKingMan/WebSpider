#需求：爬取别逗了网站中，给定页码下的所有图片

import requests
import re
import os


#指定url
url = 'https://www.biedoul.com/pic/'
#UA伪装
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}
#定义正则表达式
ex4 = '<DD>.*?<img src="(.*?)".*?</DD>'


def get_page(url, ex, headers=headers):
    """
    该函数通过输入的url和正则表达式，解析网页前端数据中的图片链接。
    :param url: 想要爬取的网页链接，比如https://www.biedoul.com/pic/
    :param ex: 解析当前网页的正则表达式
    :return: 返回解析出的图片链接
    """
    #使用通用爬虫对url对应的一整张页面进行爬取
    #发送请求
    page_text = requests.get(url=url, headers=headers).text

    #解析网页，获取图片链接
    img_src_list = re.findall(ex, page_text, re.S)
    return img_src_list

def save_img(img_src_list,file_path,headers=headers):
    """
    输入一个包含图片链接的列表，将这些图片保存到file_path输入的位置中。
    :param img_src_list:
    :param file_path:
    :param headers: 默认为headers
    :return: 无返回值
    """
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



if __name__ == '__main__':
    #创建图片需要存放的目录
    file_path = './BieDouLe/'
    if not os.path.exists(file_path):
        os.mkdir(file_path)

    url_list = [url+str(x)+'/' for x in range(3, 6)]
    for url in url_list:
        print('当前网页的地址为：',url)
        #调用获取网页的函数
        img_src_list = get_page(url, ex4)
        #保存图片到指定目录
        save_img(img_src_list, file_path)
    print("全部下载完成！")


