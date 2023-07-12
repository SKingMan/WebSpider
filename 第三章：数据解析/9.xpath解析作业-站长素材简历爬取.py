
#需求：爬取站长素材下的简历模板，最好可以获取多个页码下的简历
# https://sc.chinaz.com/jianli/free_2.html

import requests
from lxml import html
import os

def get_onepage_resume(url,file_path):
    #发起请求
    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf-8'
    page_text = response.text
    #实例化etree对象
    tree = html.etree.HTML(page_text)
    #xpath表达式解析数据,获取下载页码的html连接
    resume_url_list = tree.xpath('//div[@id="container"]/div/a/@href')
    #获取每个简历的名称
    resume_name_list = tree.xpath('//div[@id="container"]/div/a/img/@alt')
    #简历保存的路径

    for resume_url, resume_name in zip(resume_url_list, resume_name_list):
        resume_page_text = requests.get(url=resume_url, headers=headers).text
        resume_tree = html.etree.HTML(resume_page_text)
        down_load_url = resume_tree.xpath('//div[@class="down_wrap"]/div[2]/ul/li[1]/a/@href')[0]
        #获取文件的二进制数据

        resume_data = requests.get(url=down_load_url, headers=headers).content

        resume_path = file_path + resume_name + '.rar'
        with open(resume_path, 'wb')as fp:
            fp.write(resume_data)
            print(resume_name, "已下载完成！")

    print("当前页面的简历模板已下载完成，共20个！")

if __name__ == '__main__':
    #自定义变量
    url = 'https://sc.chinaz.com/jianli/free%s.html'
    #定义获取的总页码数，必须要大于等于2
    page_num = 3
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    file_path = './resume/'
    if not os.path.exists(file_path):
        os.mkdir(file_path)

    page_num_list = [''] + ['_' + str(x) for x in range(2, page_num)]
    page_num_list = [url%x for x in page_num_list]
    if page_num < 2 :
        print('页码数有误，需大于等于2，请重新设置页码数。')
        exit()#终止程序
    for page_url in page_num_list:
        get_onepage_resume(url=page_url, file_path=file_path)
        #print(page_url)


