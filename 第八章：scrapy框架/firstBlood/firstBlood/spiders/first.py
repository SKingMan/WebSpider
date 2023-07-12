import scrapy


class FirstSpider(scrapy.Spider):
    #爬虫文件袋颚名称：就是爬虫源文件的一个唯一标识
    name = "first"
    #domains：域。允许的域名：用来限定start_url列表中哪些url可以进行请求发送，
    # 通常这句代码我们不去使用，因为有些图片的地址可能不在这个网页的域名下。
    #allowed_domains = ["www.xxx.com"]

    #起始的url列表:该列表中存放的url会被scrapy自动进行请求的发送，列表里可以有多个url
    start_urls = ["https://www.baidu.com/", "https://www.sogou.com"]

    #用作于数据解析：response参数表示的就是请求成功后对应的响应对象
    def parse(self, response):
        print(response)
