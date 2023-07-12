import scrapy
from biedouPro.items import BiedouproItem

class BiedouSpider(scrapy.Spider):
    name = "biedou"
    #allowed_domains = ["www.xxx.com"]
    start_urls = ["https://www.biedoul.com/wenzi/"]

    #
    # #基于终端指令持久化存储：scrapy crawl biedou -o biedou.csv
    # def parse(self, response):
    #     #解析：段子的标题和段子的内容一定是Selector类型的对象
    #     dl_list = response.xpath('//div[@class="nr"]/dl')
    #     all_data = []#存放所有数据的类别
    #     for dl in dl_list:
    #         #xpath返回的是列表，但是列表元素
    #         #extract可以将Selector对象中的data参数存储的字符串提取出来,官方提供的方法是get()和getall()
    #         #extract_first(),将列表中第0个元素的字符串取出来。
    #         title = dl.xpath('.//strong/text()')[0].get()
    #         #列表调用了extract之后，则表示将列表中每一个Selector对象中data对应的字符串提取出来，返回的是一个列表
    #         content = dl.xpath('./dd/text()')[0].extract()
    #         print(title, content)
    #
    #         dic = {
    #             'title':title,
    #             'content':content
    #         }
    #         all_data.append(dic)
    #     return all_data




    #基于管道的持久化存储
    def parse(self, response):
        #解析：段子的标题和段子的内容一定是Selector类型的对象
        dl_list = response.xpath('//div[@class="nr"]/dl')
        all_data = []#存放所有数据的类别
        for dl in dl_list:
            #xpath返回的是列表，但是列表元素
            #extract可以将Selector对象中的data参数存储的字符串提取出来,官方提供的方法是get()和getall()
            #extract_first(),将列表中第0个元素的字符串取出来。
            title = dl.xpath('.//strong/text()')[0].get()
            #列表调用了extract之后，则表示将列表中每一个Selector对象中data对应的字符串提取出来，返回的是一个列表
            content = dl.xpath('./dd/text()')[0].extract()
            #print(title, content)

            item = BiedouproItem()
            item['title'] = title
            item['content'] = content

            yield item#这一步就是将item提交给了管道
