#需求：爬取北忘山网站中，给定页码下的所有图片壁纸
#因为是动态加载出来的数据，每次更新数据，网址并没有改变，所以不通过正则表达式的方式获取数据，而是通过ajax接口获取数据

import requests
import os

#指定url
url = 'https://api.vvhan.com/api/360wallpaperApi.php?'
#UA伪装
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

def get_page(url, params, headers=headers):
    """
    该函数通过输入的url和正则表达式，解析网页前端数据中的图片链接。
    :param url: 想要爬取的网页链接，比如https://www.biedoul.com/pic/
    :param params: 传入参数，获取json数据或者文本文件
    :return: 返回解析出的图片链接
    """
    #使用通用爬虫对url对应的一整张页面进行爬取
    #发送请求
    page_json = requests.get(url=url, params=param, headers=headers).json()

    #解析json数据，获取图片链接
    #因为返回的是json数据，在python中是以字典的类型返回的，所以可以用data里包含了所有响应返回的链接
    #x 代表元素的位置，data里包含很多图片元素，x的url健可以获得对应图片的链接，最后用列表表达式组成url列表
    url_list = [page_json['data'][x]['url'] for x in range(len(page_json['data']))]

    #获取的列表并不是最高画质的图片，所以需要转化以下，把链接里的像素数据，比如__85就是像素数据，更换成0_0_100就是最清晰的图片了
    #这个规律是通过对比不同的链接发现的。
    #k_img_list表示存储高清图片链接的列表
    k_img_list = [x.replace('__85','0_0_100') for x in url_list]
    return k_img_list

def save_img(img_src_list,file_path,headers=headers):
    """
    输入一个包含图片链接的列表，将这些图片保存到file_path输入的位置中。
    :param img_src_list:
    :param file_path:
    :param headers: 默认为headers
    :return: 无返回值
    """
    #print(img_src_list)
    for each in img_src_list:
        #请求到了图片的二级制数据
        img_data = requests.get(url=each,headers=headers).content
        #生成图片名称
        img_name = each.split('/')[-1]
        #图片最终存储的路径
        img_path = file_path + img_name
        #print('图片名称：',img_name)
        with open(img_path,'wb') as fp:
            fp.write(img_data)
            print(img_name,'下载完成！')

if __name__ == '__main__':
    #自定义变量
    start_p = 6  #从第几页开始爬取，
    n = 12 #循环次数，一次就是获取30张图片，就是一共获取多少页的图片
    #创建图片需要存放的目录
    file_path = '../../../pics/DesktopWallpaper/'

    if not os.path.exists(file_path):
        os.mkdir(file_path)

    #每次获取30个图片，循环获取n次，就是30*n张图片
    for i in range(start_p,n):
        #自定义局部变量
        count = 30#一次获取多少个
        start_num = count*i#开始位置

        #因为该网页的数据是动态加载的，所以只能通过获取ajax接口，传入相应的参数获取数据，就像豆瓣电影那个案例一样
        #request中url的参数
        #cid中代码含义
        # 36：4k专区
        # 6：美女模特
        # 9：风景大片
        #15：小清新
        #26：动漫卡通
        #14：萌宠动物
        # 5：游戏壁纸
        #10：炫酷时尚
        param = {
            'cid':'36',
            'start':start_num,#开始位置
            'count':count#获取个数
        }
        print('当前循环为第%s次，开始下载。start_num:%s,count:%s'%(i+1, start_num, count))

        # #调用获取网页的函数,返回一个高清图片链接的列表
        img_src_list = get_page(url, param)
        # #保存图片到指定目录
        save_img(img_src_list, file_path)



    print("一共%s张图片，全部下载完成！"%(n*30))



