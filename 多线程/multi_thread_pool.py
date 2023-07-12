from concurrent.futures import ThreadPoolExecutor
import crawlpic
import os
import time

#初始url，就是刚开始时发起请求的url
#参数输入：
start_pagen = 21 #从第几页开始爬取
num = 3 #一共爬取几页的内容
#url中cid表示壁纸的类型，36表示4k，start表示从多少开始，count表示返回多少个图片。这里默认是30
urls =['https://api.vvhan.com/api/360wallpaperApi.php?cid=36&start={start}&count=30'.format(start=x*30)
       for x in range(start_pagen,start_pagen+num)
       ]



#crawl
def multi_crawl_pic(func,urls):
    with ThreadPoolExecutor() as pool:
        results = pool.map(func,urls)
        a = []
        for i in results:
            a = a + i
        return a



#prase
def multi_prase_pic(func,pic_urls):
    with ThreadPoolExecutor(max_workers=10) as pool:
        pool.map(func,pic_urls)


if __name__ == '__main__':
    print('线程池-程序开始...')
    start = time.time()
    img_list = multi_crawl_pic(func=crawlpic.crawl_pic_url,urls=urls)

    multi_prase_pic(func=crawlpic.save_img,pic_urls=img_list)
    end = time.time()
    print("multi_thread,cost:",end-start,'seconds')
    print('线程池-程序结束！！！')

