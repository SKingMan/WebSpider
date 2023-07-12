import cnblog
import wrapper
import threading

@wrapper.log_start
@wrapper.calculate_time
@wrapper.log_end
def singl_thread(urls):
    for url in urls:
        cnblog.crawltext(url)


@wrapper.log_start
@wrapper.calculate_time
@wrapper.log_end
def multi_thread(urls):
    theads = []
    for url in urls:
        theads.append(
            threading.Thread(target=cnblog.crawltext, args=(url,))
        )

    for t in theads:
        t.start()

    for t in theads:
        t.join()

if __name__ == '__main__':
    #单线程
    #singl_thread(cnblog.urls)

    #多线程
    multi_thread(cnblog.urls)