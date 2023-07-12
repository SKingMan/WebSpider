import queue
import threading
import  cnblog
import time
import random


def do_crawl(url_queue:queue.Queue,html_queue:queue.Queue):
    while True:


        url = url_queue.get()
        html_text = cnblog.crawl(url)
        html_queue.put(html_text)
        print(threading.current_thread().name, f'crawl: {url}',
              'url_queue size:', url_queue.qsize())
        time.sleep(random.randint(1,2))


def do_parse(html_queue:queue.Queue,rount):
    while True:


        results = cnblog.parse(html_queue.get())
        for result in results:
            rount.write(str(result) + '\n')
        print(threading.current_thread().name, f'results size: ', len(results),
          'html_queue size:', html_queue.qsize())
        time.sleep(random.randint(1,2))

if __name__ == '__main__':
    url_queue = queue.Queue()
    html_queue = queue.Queue()

    for u in cnblog.urls:
        url_queue.put(u)

    for idx in range(3):
        t = threading.Thread(target=do_crawl, args=(url_queue, html_queue), name= f'do_crawl{idx}')
        t.start()


    rount = open('data.txt','w')

    for idx in range(2):
        t = threading.Thread(target=do_parse, args=(html_queue, rount), name= f'do_parse{idx}')
        t.start()