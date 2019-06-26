import requests
import json

# Splash 接口
render = 'http://www.porters.vip:8050/execute'
url = 'http://www.porters.vip/confusion/movie.html'
# 需要执行的命令
script = """
    function main(splash)
      assert(splash:go('%s'))
      assert(splash:wait(0.5))
      -- 截取票房
      total_png = splash:select('.movie-index-content.box .stonefont'):png()
      return {
       -- 将图片信息以键值对的形式返回
        total = total_png
      }
    end
""" % url
# 设置请求头
header = {'content-type': 'application/json'}
# 按照Splash规定提交命令
data = json.dumps({"lua_source": script})
# 向Splash接口发出请求并携带上请求头和命令参数
resp = requests.post(render, data=data, headers=header)
# 将Splash返回结果赋值给
images = resp.json()

import base64
import os
import pytesseract
for key, value in images.items():
    # Splash返回的图片使用了base64进行编码，所以我们需要解码
    image_body = base64.b64decode(value)
    filename = '%s.png' % key
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
    with open(filename, 'wb') as f:
        f.write(image_body)
    print(pytesseract.image_to_string(filename))