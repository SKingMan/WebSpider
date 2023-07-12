import cnblog
import threading
import wrapper



@wrapper.log_start
@wrapper.calculate_time
@wrapper.log_end
def single_thread_crawl():
    for url in cnblog.urls:
        cnblog.crawl(url)



@wrapper.log_start
@wrapper.calculate_time
@wrapper.log_end
def multi_thread_crawl():
    threads = []
    for url in cnblog.urls:
        threads.append(
            threading.Thread(target=cnblog.crawl,args=(url,))
        )
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()





if __name__ == '__main__':

    single_thread_crawl()


    multi_thread_crawl()

