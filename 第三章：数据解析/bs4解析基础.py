

bs4进行数据解析
    --数据解析原理:
        --1.标签定位
        --2.提取标签、标签属性中存储的数据值
    --bs4数据解析原理:
        --1.实例化一个BeautifulSoup对象，并且将页面源码数据加载到该对象中
        --2.通过调用BeautifulSoup中对象属性和方法进行标签定位和数据提取
    如何实例化BeautifulSoup对象：
    -- from bs4 import  BeautifulSoup
    --对象的实例化：
        --1.将本地的html文档汇总的数据加载到该对象中
                fp = open('./test.html','r',encoding='utf-8')
                soup = BeautifulSoup(fp,'lxml')
        --2.将互联网上获取的页面源码加载到该对象中
                page_text = response.text
                soup = BeautifulSoup(page_text,'lxml')
    - 提供的用于数据解析的方法和属性:
        --soup.tagName:返回的是文档中第一次出现的tagName对应的标签
        --soup.find():
            -- find('tagName'):等同于soup.div#也是返回第一次出现的tagName
            -- 属性定位:
                -soup.find('div',class_='song')#通过标签定位到对应的标签里
        --soup.findall('tagName'):返回符合要求的所有标签
    - select:
        - select('某种选择器（id，class，标签...选择器)')#,返回的是一个列表，可以是表情名比如div，ur，li，可以是属性值，比如
                                                    #class的值，这个叫做 类选择器
        - 层级选择器：
                - soup.select('.tange > ur > li >a'): >表示的是一个层级
                - soup.select('.tang > ul a')#:空格表示的是多个层级,也就是说用空格可以跨越层级，比如这里就没有使用li标签，
                                            # 而是直接到a标签
    - 获取标签之间的文本数据
        - soup.a.text/string/get_text()
        - text/get_text():可以获取某一个标签中所有的文本内容
        - string：只可以获取该标签下面直系的文本内容
    - 获取标签中属性值：
        - soup.a['href']