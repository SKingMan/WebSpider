#需求：爬取梨视频的视频数据

import requests
from lxml import html

if __name__ == '__main__':

    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    #原则：线程池处理的是阻塞且耗时的操作

    #对下述url发起请求解析出视频详情页的url和视频的名称
    url = 'https://www.pearvideo.com/category_1'
    page_text = requests.get(url=url, headers=headers).text
    tree = html.etree.HTML(page_text)
    li_list = tree.xpath('//ul[@id="listvideoListUl"]/li')

    #详情页搜索mp4就可以找到视频的url！！！
    dic = {}#保存详情页的url和视频名称
    for li in li_list:
        dic['detail_url'] = 'https://www.pearvideo.com/' + li.xpath('./div/a/@href')[0]
        dic['name'] = li.xpath('./div/a/div[2]/text()')[0]
        text_url = 'https://www.pearvideo.com/videoStatus.jsp?contId=1205711&mrd=0.022732039179074848'
        detail_json = requests.get(url=text_url, headers=headers).json()
        print(detail_json)
        video_url = detail_json['srcUrl']
        #https://video.pearvideo.com/mp4/short/20161221/cont-1017719-10103158-hd.mp4
        video_data = requests.get(url=video_url,headers=headers).content
        with open(dic['name']+'.html','w') as fp:
            fp.write(video_data)
