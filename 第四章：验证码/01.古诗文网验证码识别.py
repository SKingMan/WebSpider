#需求：古诗文网验证码识别：https://www.gushiwen.cn/

import requests
from lxml import html
from CodeClass import Chaojiying_Client


#封装识别验证码图片的函数
def getCodeText(imgPath,codeType):
    chaojiying = Chaojiying_Client('1270623490', 'Wang0326', '947633')	#用户中心>>软件ID 生成一个替换 96001
    im = open(imgPath, 'rb').read()													#本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    print(chaojiying.PostPic(im, codeType))												#1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
    #print chaojiying.PostPic(base64_str, 1902)  #此处为传入 base64代码


#下载验证码图片
if __name__ == '__main__':

    url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    file_path = './codePic/'
    page_text = requests.get(url=url, headers=headers).text
    tree = html.etree.HTML(page_text)
    pre_url = 'https://so.gushiwen.cn'
    suf_url = tree.xpath('//*[@id="imgCode"]/@src')[0]
    code_pic_url = pre_url + suf_url
    code_pic_data = requests.get(url=code_pic_url, headers=headers).content
    with open('./code.jpg', 'wb') as fp:
        fp.write(code_pic_data)

    #调用超级鹰平台实例程序进行验证码图片数据识别
    getCodeText('./code.jpg', '1902')
