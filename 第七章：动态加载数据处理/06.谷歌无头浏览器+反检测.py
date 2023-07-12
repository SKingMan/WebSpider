#无头浏览器就是在爬取数据的时候，不让浏览器显示，而是在后台运行

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver import ChromeOptions

# #无头浏览器属性设置
# options = ChromeOptions()
# options.add_argument('--headless')
#反检测
options = ChromeOptions()
#以最高权限运行
options.add_argument('--no-sandbox')
# navigator.webdriver 设置为False
options.add_argument('--disable-blink-features=AutomationControlled')
# 隐藏"Chrome正在受到自动软件的控制"提示
options.add_experimental_option("excludeSwitches",["enable-automation"])
options.add_experimental_option("useAutomationExtension",False)

path = Service('chromedriver.exe')
bro = webdriver.Chrome(service=path, options=options)


url = 'https://www.baidu.com'
bro.get(url=url)
print(bro.page_source)
sleep(5)
bro.quit()