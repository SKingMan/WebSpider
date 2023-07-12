import concurrent.futures
import cnblog

#crawl
with concurrent.futures.ThreadPoolExecutor() as pool:
    htmls = pool.map(cnblog.crawl,cnblog.urls)

    htmls = list(zip(cnblog.urls,list(htmls)))
    for url,html in htmls:
        print(url,len(html))

#parse
with concurrent.futures.ThreadPoolExecutor() as pool:
    features = {}
    for url,html in htmls:
        feature = pool.submit(cnblog.parse,html)
        features[feature] = url

    # for feature,url in features.items():
    #     print(url,feature.result())

    for feature in concurrent.futures.as_completed(features):
        print(features[feature],feature.result())
