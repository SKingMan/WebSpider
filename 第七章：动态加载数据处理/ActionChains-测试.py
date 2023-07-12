#当选中标签的时候，动作类ActionChains中的move_by_offset的坐标是相对坐标还是绝对坐标。
#当不选择任何标签的时候，移动是相对坐标还是绝对坐标？
#我的结论是不选中任何标签的时候，move_by_offset移动的是绝对坐标，
# 当选中某个标签后move_by_offset移动的就是相对这个标签的相对坐标
#验证成功，选中某个元素后，move_by_offset里的坐标就是相对该标签的坐标，不是整个坐标系里的绝对坐标


from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#指定chrome驱动的路径
path = Service('chromedriver.exe')
#实例化一个浏览器对象
drive = webdriver.Chrome(service=path)

url = 'https://c.runoob.com/front-end/61/'

drive.get('file:///E:/PYCode/WebSpider/actionchain-test.html')
drive.maximize_window()#全屏显示
#切换frame
#drive.switch_to.frame('iframeResult')
#drive.switch_to.frame('iframeResult')
rect1 = drive.find_element(By.ID, 'rectangle1')
#创作动作链
action = ActionChains(drive)
action.click_and_hold(rect1)
action.move_by_offset(300,0)
action.perform()
sleep(1)
action.release()
sleep(3)
print(rect1.rect)