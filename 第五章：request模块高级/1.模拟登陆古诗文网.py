#编码流程：
#1，验证码的识别，获取验证码图片的文字数据
#2.对post请求进行发送（处理请求参数）
#3.对响应数据进行持久化存储

import requests
from lxml import html
from CodeClass import Chaojiying_Client

#封装识别验证码图片的函数
def getCodeText(imgPath,codeType):
    chaojiying = Chaojiying_Client('1270623490', 'Wang0326', '947633')	#用户中心>>软件ID 生成一个替换 96001
    im = open(imgPath, 'rb').read()													#本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    result = chaojiying.PostPic(im, codeType)
    print(result)												#1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
    #print chaojiying.PostPic(base64_str, 1902)  #此处为传入 base64代码
    #{'err_no': 0, 'err_str': 'OK', 'pic_id': '2212217501117220003', 'pic_str': '0x23', 'md5': '1de550c6df65263f779ae2a7f543595c'}
    return result


if __name__ == '__main__':

    #下载登录页面验证码图片，并解析验证码
    url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    page_text = requests.get(url=url, headers=headers).text
    tree = html.etree.HTML(page_text)
    code_url = 'https://so.gushiwen.cn' + tree.xpath('//*[@id="imgCode"]/@src')[0]
    code_data = requests.get(url=code_url, headers=headers).content
    code_pic_path = './code.jpg'
    with open(code_pic_path, 'wb') as fp:
        fp.write(code_data)
    #调用第三方接口，获取验证码
    code_text = getCodeText(code_pic_path, 1902)['pic_str']
    print(code_text)


    #2.对post请求进行发送（处理请求参数）
    session = requests.Session()

    login_url = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
    param = {
        '_VIEWSTATE': '+1j8WGs2ZKXHnxAerYOvkhimr3EXehtDiV3uzkuqzv5a0X+KXTk8BHxw+'\
                     'nfscRN19Oovx0PJKJBMB4BfeGgw2bow75q3jdl2GLlQ9G8iZ+U39rtX'\
                     'Yrh1MYXkz7LPpRtXys5Y1alX1qNITHsWzVi9vQiRIqk=',
        '__VIEWSTATEGENERATOR': 'C93BE1AE',
        'from': 'http://so.gushiwen.cn/user/collect.aspx',
        'email': '1270623490@qq.com',
        'pwd': 'Wang0326',
        'code': code_text,
        'denglu': '登录'
    }
    #使用session进行post请求发送
    response = session.post(url=login_url, data=param, headers=headers)
    print('模拟登录状态码：',response.status_code)
    login_data = response.text
    with open('gushiwen_login.html', 'w', encoding='utf-8') as fp:
        fp.write(login_data)
    #print('模拟登录完成！')
    #print(response[:3000])

    #爬取当前用户的个人主页对应的页面数据
    detail_url = 'https://so.gushiwen.cn/shiwens/'
    # #手动处理cookie
    # headers = {
    #     'Cookie':'xxx'
    # }
    #使用携带cookie的session进行get请求的发送
    detail_page_text = session.get(url=detail_url,headers=headers).text
    with open('./detail.html','w',encoding='utf-8') as fp:
        fp.write(detail_page_text)




# _VIEWSTATE:+1j8WGs2ZKXHnxAerYOvkhimr3EXehtDiV3uzkuqzv5a0X+KXTk8BHxw+nfscRN19Oovx0PJKJBMB4BfeGgw2bow75q3jdl2GLlQ9G8iZ+U39rtXYrh1MYXkz7LPpRtXys5Y1alX1qNITHsWzVi9vQiRIqk=
# __VIEWSTATEGENERATOR:C93BE1AE
# from:http://so.gushiwen.cn/user/collect.aspx
# email:1270623490@qq.com
# pwd:Wang0326
# code:8afq
# denglu:登录

