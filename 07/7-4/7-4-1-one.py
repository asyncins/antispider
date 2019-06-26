import requests
from parsel import Selector
from urllib.parse import urljoin

url = 'http://www.porters.vip:8202/'
resp = requests.get(url)
text = Selector(resp.text)
# 提取商品详情的超链接
shops = text.css('.col-md-3 a::attr("href")').extract()
for s in shops:
    # 循环商品超链接列表，依次向商品详情页发出请求
    detail = urljoin(url, s)
    detail_resp = requests.get(detail)
    # 打印商品详情页响应正文
    print(detail_resp.text)