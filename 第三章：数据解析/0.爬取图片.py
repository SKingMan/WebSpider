import requests


if __name__ == '__main__':
    #如何爬取图片
    url = 'http://tiebapic.baidu.com/forum/w%3D580/sign=d5e779296d4e251fe2f7e4f09787c9c2/f75f311f95cad1c833552734223e6709c83d51cd.jpg?tbpicau=2023-04-25-05_56a9376eb75b76e844bc9c7614b45d80'
    #content返回的是二进制形式的图片数据
    #text(字符串） content（二进制） json() (对象类型的数据）
    img_data = requests.get(url=url).content
    with open('./MM.jpg','wb') as fp:
        fp.write(img_data)