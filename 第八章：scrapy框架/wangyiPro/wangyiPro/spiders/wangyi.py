import scrapy


class WangyiSpider(scrapy.Spider):
    name = "wangyi"
    #allowed_domains = ["www.xxx.com"]
    start_urls = ["https://news.163.com/"]
    modules_url = []#存放五大板块的url
    #解析五大板块对应的详情页的url
    def parse(self, response):
        li_list = response.xpath('//div[@class="bd"]/div/ul/li')
        alist = [1, 2, 3, 4, 5]
        for index in alist:
            module_url = li_list[index].xpath('./a/@href').extract_first()
            self.modules_url.append(module_url)

        #依次对每一个板块对应的页面进行请求
        for url in self.modules_url:#对每一个板块的url进行请求发送
            yield scrapy.Request(url, callback=self.parse_module)

    #每一个板块对应的新闻标题相关的内容都是动态加载
    def parse_module(self, response):#解析每一个板块页面中对应新闻标题和新闻详情页的url
        pass
