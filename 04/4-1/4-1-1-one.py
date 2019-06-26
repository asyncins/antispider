import requests
from parsel import Selector


url = 'http://www.porters.vip/verify/uas/index.html'
# 向目标网址发起网络请求
resp = requests.get(url)
# 打印输出状态码
print(resp.status_code)
# 如果本次请求的状态码为200则继续，否则提示失败
if resp.status_code == 200:
    sel = Selector(resp.text)
    # 根据HTML标签和属性从响应正文中提取新闻标题
    res = sel.css('.list-group-item::text').extract()
    print(res)
else:
    print('This request is fial.')