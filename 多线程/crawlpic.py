import requests
import os
import threading
import wrapper

#爬取北忘川壁纸：https://www.beiwangshan.com/wp/
#爬取4k专区的图片，主要分为两步：
# 第一步解析出每个图片的url，并存到列表中
# 第二步，根据url解析图片，并保存到本地。


#第一步：解析4K图片的url
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

file_path = '../../../pics/test1/'

if not os.path.exists(file_path):
    os.mkdir(file_path)


def crawl_pic_url(url):
    #获取url中的高清图片的url，并以列表的形式返回
    #发起请求
    page_json = requests.get(url=url, headers=headers).json()

    #解析json数据，获取图片链接
    url_list = [page_json['data'][x]['url'] for x in range(len(page_json['data']))]

    #获取的列表并不是最高画质的图片，所以需要转化以下，把链接里的像素数据，比如__85就是像素数据，更换成0_0_100就是最清晰的图片了
    #这个规律是通过对比不同的链接发现的。
    #k_img_list表示存储高清图片链接的列表
    k_img_list = [x.replace('__85','0_0_100') for x in url_list]
    return k_img_list


def save_img(img_src):
    """
    输入一个包含图片链接的列表，将这些图片保存到file_path输入的位置中。
    :param img_src_list:
    :param file_path:
    :param headers: 默认为headers
    :return: 无返回值
    """

    #请求到了图片的二级制数据
    img_data = requests.get(url=img_src,headers=headers).content
    #生成图片名称
    img_name = img_src.split('/')[-1]
    #图片最终存储的路径
    img_path = file_path + img_name
    #print('图片名称：',img_name)
    with open(img_path,'wb') as fp:
        fp.write(img_data)
        print(img_name,'下载完成！')

@wrapper.log_start
@wrapper.calculate_time
@wrapper.log_end
def single_save_img(img_src_list):
    #print(img_src_list)
    for each in img_src_list:
        save_img(each)

@wrapper.log_start
@wrapper.calculate_time
@wrapper.log_end
def multi_save_img(img_src_list):
    """
    输入一个包含图片链接的列表，将这些图片保存到file_path输入的位置中。
    :param img_src_list:
    :param file_path:
    :param headers: 默认为headers
    :return: 无返回值
    """
    thread_list = []
    for url in img_src_list:
        thread_list.append(
            threading.Thread(target=save_img, args=(url,))
        )

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()



if __name__ == '__main__':
    #参数输入：
    start_pagen = 18 #从第几页开始爬取
    num = 3 #一共爬取几页的内容
    #创建图片需要存放的目录

    file_path = '../../../pics/test1/'

    if not os.path.exists(file_path):
        os.mkdir(file_path)

    #url中cid表示壁纸的类型，36表示4k，start表示从多少开始，count表示返回多少个图片。这里默认是30
    urls =['https://api.vvhan.com/api/360wallpaperApi.php?cid=36&start={start}&count=30'.format(start=x*30)
           for x in range(start_pagen,start_pagen+num)
           ]
    #https://api.vvhan.com/api/360wallpaperApi.php?cid=36&start=1&count=30
    #存放所有
    pic_urls=[]
    for url in urls:
        #print(url)
        pic_urls += crawl_pic_url(url=url)
    #单线程爬取90张图片，耗时：5分45秒
    #single_save_img(pic_urls)

    #多线程爬取90张图片，耗时：4分30秒。
    #多线程提速不明显，可能是因为线程开启太多，可以使用线程池和生产者&消费者框架试试。
    #线程池可以重复利用线程，减少了线程开启和关闭的时间
    #生产者&消费者框架可以减少爬取的时间。
    multi_save_img(pic_urls)

