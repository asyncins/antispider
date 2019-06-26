import requests
from lxml import etree

url = 'http://www.porters.vip/verify/cookie/content.html'
# 向目标网址发起网络请求
resp = requests.get(url)
# 打印输出状态码
print(resp.status_code)
# 如果本次请求的状态码为200则继续，否则提示失败
if resp.status_code == 200:
    # 将响应正文赋值给html变量
    html = etree.HTML(resp.text)
    # 根据HTML标签和样式属性从文本中标题的Element对象
    res = html.cssselect('.page-header h1')
    print(res)
else:
    print('This request is fial.')