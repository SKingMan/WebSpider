from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

path = Service('chromedriver.exe')
bro = webdriver.Chrome(service=path)

url = 'https://www.taobao.com/'

#之前一直定位不到，是因为少了下面这一句，所以找不到对应的元素
bro.get(url=url)

search_input = bro.find_element(By.XPATH, '//div[@class="search-suggest-combobox"]/input')
search_input.send_keys('iphone')

#点击搜索按钮
btn = bro.find_element(By.CLASS_NAME, 'btn-search')
btn.click()

time.sleep(3)
bro.quit()
#
# # 定义chrome驱动地址
# path = Service('chromedriver.exe')
# #实例化一个浏览器对象（传入浏览器的驱动程序）
# bro = webdriver.Chrome(service=path)
#
# url = 'https://www.taobao.com/'
# bro.get(url=url)
# #标签定位
# search_input = bro.find_element(Id,by,value='q')
# #标签交互
# search_input.send_keys('iphone')
#
# btn = bro.find_element()