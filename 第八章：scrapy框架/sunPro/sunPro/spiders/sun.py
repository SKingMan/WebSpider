import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class SunSpider(CrawlSpider):
    name = "sun"
    #allowed_domains = ["www.xxx.com"]
    start_urls = ["https://wz.sun0769.com/political/index/politicsNewest"]

    #连接提取器：根据指定规则（allow=“正则”)进行指定连接的提取
    link = LinkExtractor(allow=r'type=4&page=\d+')

    rules = (
        #规则解析器：将连接提取器提取到的链接进行指定规则的解析操作
        Rule(link, callback="parse_item", follow=True),
        #follow=True：可以将连接提取器，继续作用到连接提取器提取到的链接 所对应的链接中
    )
    #解析新闻编号和新闻标题
    def parse_item(self, response):
        #注意：xpath表达式中不可以出现tbody标签
        li_list = response.xpath('/html/body/div[2]/div[3]/ul[2]/li')
        for li in li_list:
            new_num = li.xpath('./span[1]').extract_first()
            new_title = li.xpath('./span[3]/a').extract_first()