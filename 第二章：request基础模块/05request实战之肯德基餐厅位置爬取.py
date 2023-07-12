#request实战之肯德基餐厅位置爬取

import requests
import json

if __name__ == '__main__':
    #1,指定url
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    #参数处理
    keyword = input('请输入你要查询的城市名')
    data = {
        'cname':'',
        'pid':'',
        'keyword':keyword,
        'pageIndex':'1',
        'pageSize':'10',
    }
    #UA伪装
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }

    #2.发送请求
    response = requests.post(url=url,data=data,headers=header)
    #3.获取响应数据。text格式
    location_text = response.text
    print('响应数据的类型：',type(location_text))
    #dumps()，将dict对象转化为json的字符串类型
    #json_obj = json.dumps(location_text)
    with open('./kfc.json','w',encoding='utf-8') as fp:
        json.dump(location_text,fp=fp,ensure_ascii=False)

    print('over!!!')