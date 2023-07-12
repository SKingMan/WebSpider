import requests
from lxml import html

urls = ['https://www.cnblogs.com/#p%s'%x for x in range(1,50+1)]
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}
def crawltext(url):
    response = requests.get(url=url,headers=headers)
    print(url, len(response.text))

def crawl(url):
    response = requests.get(url=url)
    return response.text

def parse(page_text):
    tree = html.etree.HTML(page_text)
    links = tree.xpath('//a[@class="post-item-title"]')
    return [(link.xpath('./@href')[0], link.xpath('./text()')[0]) for link in links]


if __name__ == '__main__':
    # for result in parse(crawl(urls[2])):
    #     print(result)

    for url in urls:
        crawltext(url)
