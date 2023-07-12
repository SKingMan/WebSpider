
import threading
import queue
import crawlpic
import os
import time




def do_crawl_pic(url_queue:queue.Queue,pic_queue:queue.Queue):
    while True:
        url = url_queue.get()
        pic_list = crawlpic.crawl_pic_url(url)
        for pic_url in pic_list:
            pic_queue.put(pic_url)
        print(threading.current_thread().name,'url_queue size:',url_queue.qsize())

def do_prase(pic_queue:queue.Queue,fpath):
    while True:
        pic_url = pic_queue.get()
        crawlpic.save_img(pic_url,fpath)
        print(threading.current_thread().name,'pic_queue size:',pic_queue.qsize())




if __name__ == '__main__':
    print('-----------------程序开始执行----------------------')
    start = time.time()

    url_queue = queue.Queue()
    pic_queue = queue.Queue()

    #参数输入：
    start_pagen = 21 #从第几页开始爬取
    num = 3 #一共爬取几页的内容
    #创建图片需要存放的目录
    file_path = '../../../pics/test1/'

    if not os.path.exists(file_path):
        os.mkdir(file_path)
    urls =['https://api.vvhan.com/api/360wallpaperApi.php?cid=36&start={start}&count=30'.format(start=x*30)
           for x in range(start_pagen,start_pagen+num)
           ]

    for u in urls:
        url_queue.put(u)

    for idx in range(2):
        t = threading.Thread(target=do_crawl_pic, args=(url_queue, pic_queue),name=f'do_crawl_pic{idx}')
        t.start()

    for idx in range(10):
        t = threading.Thread(target=do_prase, args=(pic_queue, file_path),name=f'do_prase{idx}')
        t.start()