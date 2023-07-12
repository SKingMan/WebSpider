from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from lxml import html
import re
import requests

def browser_get_url(url):
    # 定义chrome驱动地址
    path = Service('chromedriver.exe')
    #实例化一个浏览器对象（传入浏览器的驱动程序）
    bro = webdriver.Chrome(service=path)
    bro.get(url)
    page_text = bro.page_source

    tree = html.etree.HTML(page_text)
    video_url = tree.xpath('//div[@id="JprismPlayer"]/video/@src')[0]
    return video_url

#url地址
url = 'https://www.pearvideo.com/video_1047530'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'

}


#调用模拟浏览器函数，获取video链接


video_data = requests.get(url=video_url, headers=headers).content
with open('./livideo.mp4','wb') as fp:
    fp.write(video_data)
print(video_url,'下载完成啦！')

# ex = 'src="(.*?)" style'
# video_url = re.findall(ex, page_text)
# print(video_url)
#https://video.pearvideo.com/mp4/short/20170314/cont-1047530-10276280-hd.mp4


#print(video_tag)
# print(type(video_url))
# print(video_url)

#time.sleep(5)
# bro.quit()
