#基于selenium实现12306模拟登录，不过现在已经更换成滑块验证了，
# 如下代码就是破解滑块的代码！！！
# 如下代码就是破解滑块的代码！！！
# 如下代码就是破解滑块的代码！！！
# 可以试试其他用图片验证的网站，方法都是一样的

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

options = ChromeOptions()
#以最高权限运行
options.add_argument('--no-sandbox')
# navigator.webdriver 设置为False
options.add_argument('--disable-blink-features=AutomationControlled')
# 隐藏"Chrome正在受到自动软件的控制"提示
options.add_experimental_option("excludeSwitches",["enable-automation"])
options.add_experimental_option("useAutomationExtension",False)


path = Service('chromedriver.exe')
driver = webdriver.Chrome(service=path, options=options)

url = 'https://www.12306.cn/index/'
driver.get(url=url)
driver.maximize_window()#全屏显示
login_btn = driver.find_element(By.ID, 'J-btn-login')
#login_btn = driver.find_element(By.XPATH, '//a[@id="J-btn-login"]')
#//div[@class="header-right"]/ul/li[@id="J-btn-login]"/a]
#sleep(5)
#下载源码数据
# page_text = driver.page_source
# with open('./12306.txt', 'w',encoding='utf-8') as fp:
#     fp.write(page_text)
# print('网页源码下载完成！')
login_btn.click()
#输入账号
username = driver.find_element(By.ID, 'J-userName')
username.send_keys('19121717669')
sleep(1)

#输入密码
password = driver.find_element(By.ID, 'J-password')
password.send_keys('wang0326')
sleep(1)

#立即登录
login_rightnow = driver.find_element(By.ID, 'J-login')
login_rightnow.click()

#显式等待，直到条件满足则执行下一步，也就是等到滑块显示之后再进行操作
try:
    WebDriverWait(driver,10).until(
        EC.presence_of_all_elements_located(
            (By.ID, 'nc_1_n1z')
        )
    )
except selenium.common.exceptions.TimeoutException:
    print('元素加载超时')

#获取滑块标签
slider_tag = driver.find_element(By.ID, 'nc_1_n1z')
#获取滑块标签的矩形框架,包括元素的长和宽，还有坐标x，y值
slider_rect = slider_tag.rect
print(slider_rect)

#获取滑块标签
track_tag = driver.find_element(By.CLASS_NAME, 'nc-lang-cnt')
#获取滑块标签的矩形框架，包括元素的长和宽，还有坐标x，y值
track_rect = track_tag.rect
print(track_rect)
print(type(track_rect['x']))

#创建动作链
action = ActionChains(driver)
#action.move_to_element_with_offset()
#单击并长按滑块标签
action.click_and_hold(slider_tag)
action.move_by_offset(400, 0)
#执行动作链
action.perform()
#释放鼠标
action.release()
# #计算滑块需要移动的x距离，从而得出最终的坐标值
# finsh_x = track_rect['x'] + track_rect['width'] - slider_rect['width']
# finsh_y = slider_rect['y']
# print(finsh_x, finsh_y)
# #拖动到指定坐标后然后释放
# action.drag_and_drop_by_offset(slider_tag, finsh_x, finsh_y).perform()
sleep(20)
