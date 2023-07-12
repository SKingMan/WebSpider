#需求：
import requests
url = 'https://www.baidu.com/s?wd=ip'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

page_text = requests.get(url=url, headers=headers,proxies={'https':'183.165.226.80'}).text
with open('./ip.html', 'w', encoding='utf-8') as fp:
    fp.write(page_text)