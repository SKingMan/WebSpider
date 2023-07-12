from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions
from selenium.webdriver import ChromeOptions

path = Service('chromedriver.exe')
bro = webdriver.Chrome(service=path)

url = 'https://qzone.qq.com/'
bro.get(url=url)
#切换frame
bro.switch_to.frame('login_frame')
#点击账号密码登录
buttom_login = bro.find_element(By.XPATH, '//div[@id="bottom_qlogin"]/a')
buttom_login.click()
sleep(2)

#输入账号
input_tag = bro.find_element(By.XPATH, '//div[@class="uinArea"]//input')
input_tag.send_keys('1270623490')
sleep(1)

#输入密码
input_password = bro.find_element(By.XPATH, '//div[@class="pwdArea"]//input')
input_password.send_keys('wang1400875696')
sleep(1)

#点击登录
btn = bro.find_element(By.XPATH, '//div[@class="submit"]//input')
btn.click()
#滚轮，滚到指定元素
# iframe = bro.find_element(By.ID,'QM_Feeds_Iframe')
# ActionChains(bro).scroll_to_element(iframe).perform()


#显式等待，直到条件满足则执行下一步，也就是等到广告显式出来后才进行关闭广告的操作
# try:
#     WebDriverWait(bro,10).until(
#         EC.presence_of_all_elements_located(
#             (By.XPATH, '//div[@class="msg-msg-channel-wrapper"]/a')
#         )
#     )
# except selenium.common.exceptions.TimeoutException:
#     print('元素加载超时')

#关闭广告
ad_close = bro.find_element(By.XPATH,'//div[@class="msg-msg-channel-wrapper"]/a')
ad_close.click()

#按给定值滚动
action = ActionChains(bro)
for i in range(5):

    action.scroll_by_amount(0, 50).perform()
    sleep(1)
action.release()

sleep(200)