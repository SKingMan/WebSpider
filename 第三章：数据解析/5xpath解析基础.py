
from lxml import html

if __name__ == '__main__':
    #实例化一个etree对象，且将江西的源码将在到该对象中
    tree = html.etree.parse('test.html')
    # r = tree.xpath('/html/body/div')
    # r = tree.xpath('/html//div')
    #r = tree.xpath('//div')
    #r = tree.xpath('//div[@class="song"]')#属性定位
    #r = tree.xpath('//div[@class="song"]/p[3]')
    # r = tree.xpath('//div[@class="tang"]//li[5]/a/text()')
    r = tree.xpath('//li[7]//text()')

print(r)

