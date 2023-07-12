#需求：爬取三国演义小说所有的章节标题和章节内容 https://www.shicimingju.com/book/sanguoyanyi.html
import requests
from bs4 import BeautifulSoup
import lxml


if __name__ == '__main__':
    #对首页的页面数据进行爬取
    #指定url
    url = 'https://sanguo.5000yan.com/'
    #UA伪装
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }

    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf-8'#修改response对象的编码，防止出现中文乱码
    page_text = response.text
    #在首页中解析出章节的标题和详情页的url
    #1.实例化BeautifulSoup对象，需要将页面源码数据加载到对应的对象中
    soup = BeautifulSoup(page_text, 'lxml')
    #解析章节标题和详情页的url
    a_list = soup.select('.paiban > li > a')

    #打开一个文件，将内容解析到指定位置
    fp = open('./sanguo.txt','w',encoding='utf-8')
    for each in a_list:
        title = each.string
        detail_url = each['href']

        #对详情页发起请求，解析出章节内容
        detail_response = requests.get(url=detail_url, headers=headers)
        detail_response.encoding = 'utf-8'
        detail_page_text = detail_response.text
        #解析出详情页中相关的章节内容
        detail_soup = BeautifulSoup(detail_page_text, 'lxml')#实例化BeautifulSoup对象
        div_tag = detail_soup.find('div', class_='grap')
        #解析到了章节的内容
        content = div_tag.text

        #持久化存储
        fp.write(title+":\n"+content+'\n')
        print(title,'爬取成功！')
    print('全部爬取完成！')
    fp.close()
    #print(title_url)