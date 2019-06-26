import requests
import json

# Splash 接口
render = 'http://www.porters.vip:8050/execute'
# 需要执行的命令
script = """
    function main(splash)
      splash:go('http://www.porters.vip/verify/sign')
      local butt = splash:select('#fetch_button')
      butt:mouse_click()
      content = splash:select('#content'):text()
      return {
        results = content
      }
    end
"""
# 设置请求头
header = {'content-type': 'application/json'}
# 按照Splash规定提交命令
data = json.dumps({"lua_source": script})
# 向Splash接口发出请求并携带上请求头和命令参数
resp = requests.post(render, data=data, headers=header)
# 打印返回的json
print(resp.json())