import requests
import json

resp = requests.get('http://www.porters.vip:8207/api/v1/')
# 将响应正文转换成python容器对象
data = json.loads(resp.text)
print(type(data))
for i in data:
    print(i)