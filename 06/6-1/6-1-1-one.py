import requests
from parsel import Selector
url = 'http://www.porters.vip/confusion/recruit.html'
# 向目标网址发起请求
resp = requests.get(url)
# 使用响应正文初始化Selector
sel = Selector(resp.text)
# 取出响应正文中的企业名称
company = sel.css('h1.interval::text').get()
print(company)