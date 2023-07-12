import asyncio
import time
import aiohttp
import requests
import os
import json
import aiofiles

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}


file_path = '../../../pics/test1/'

if not os.path.exists(file_path):
    os.mkdir(file_path)

#返回的是协程对象，前面都要加await，这句话的理解就是如果调用的是方法，也就是带括号的属性，就需要加await，自己定义的函数调用也要加。
async def get_img_src(url):
    try:

        async with aiohttp.ClientSession() as session:
            async with await session.get(url) as response:
                page_json = await response.text()
                page_json = json.loads(page_json)

                url_list = [page_json['data'][x]['url'] for x in range(len(page_json['data']))]
                k_img_list = [x.replace('__85','0_0_100') for x in url_list]
                #print(k_img_list)

                for img_src in k_img_list:
                    await save_img(img_src)
    except aiohttp.ClientPayloadError:
        async with aiohttp.ClientSession() as session:
            async with await session.get(url) as response:
                page_json = await response.text()
                page_json = json.loads(page_json)

                url_list = [page_json['data'][x]['url'] for x in range(len(page_json['data']))]
                k_img_list = [x.replace('__85','0_0_100') for x in url_list]
                #print(k_img_list)

                for img_src in k_img_list:
                    await save_img(img_src)

#持久化存储函数
async def save_img(img_src):
    """
    输入一个包含图片链接的列表，将这些图片保存到file_path输入的位置中。
    :param img_src_list:
    :return: 无返回值
    """
    #请求到了图片的二级制数据
    async with aiohttp.ClientSession() as session:
        async with await session.get(img_src) as response:
            #print(response.status)
            if response.status == 200:
                content = await response.content.read()

                #生成图片名称
                img_name = img_src.split('/')[-1]
                #图片最终存储的路径
                img_path = file_path + img_name
                #return await save_date(content,img_path)
                #print('图片名称：',img_name)
                async with aiofiles.open(img_path,'wb') as fp:
                    await fp.write(content)
                    print(img_name,'下载完成！')

async def save_date(content,img_path):
    with open(img_path,'wb') as fp:
        fp.write(content)
        print(img_path.split('/')[-1],'下载完成！')

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



if __name__ == '__main__':
    start = time.time()
    #参数输入：
    start_pagen = 18 #从第几页开始爬取
    num = 3 #一共爬取几页的内容
    #创建图片需要存放的目录
    #url中cid表示壁纸的类型，36表示4k，start表示从多少开始，count表示返回多少个图片。这里默认是30
    urls =['https://api.vvhan.com/api/360wallpaperApi.php?cid=36&start={start}&count=30'.format(start=x*30)
           for x in range(start_pagen,start_pagen+num)]
    #存放所有图片url,一共90个url。
    pic_urls=[]
    for url in urls:
        pic_urls += crawl_pic_url(url=url)
    tasks = []
    print('middle time:',time.time()-start,'seconds')
    for url in pic_urls:
        #获得协程对象，其实也可以直接将协程对象放到事件循环中，这里是把协程封装到task里
        con = save_img(url)
        #封装到task里
        task = asyncio.ensure_future(con)
        tasks.append(task)
    #创建事件循环，也可以不创建，直接使用asyncio.run()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    end = time.time()
    print('总耗时：',end-start,'seconds')