import scrapy
from imgPro.items import ImgproItem

class ImgSpider(scrapy.Spider):
    name = "img"
    #allowed_domains = ["www.xxx.com"]
    start_urls = ["https://sc.chinaz.com/tupian/"]
    img_src_list = []
    def parse(self, response):
        div_list = response.xpath('/html/body/div[3]/div[2]/div')
        for div in div_list:
            img_src = 'https:'+div.xpath('./img/@data-original')[0].extract()

            item = ImgproItem()
            item['src'] = img_src
            yield item
            # self.img_src_list.append(img_src)
            # print(img_src)

