from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from lxml import html
import re

#url地址
url = 'https://www.pearvideo.com/video_1047530'

# 定义chrome驱动地址
path = Service('chromedriver.exe')
#实例化一个浏览器对象（传入浏览器的驱动程序）
bro = webdriver.Chrome(service=path)
bro.get(url)
page_text = bro.page_source
ex = '<video.*?src="(.*?).*?" style'
re.findall(ex,page_text)
# tree = html.etree.HTML(page_text)
# video_tag = tree.xpath('//div[@id="JprismPlayer"]/video/text()')

#print(video_tag)
print(type(page_text))

#time.sleep(5)
bro.quit()
