from selenium import webdriver

url = 'http://www.porters.vip/verify/sign'
# 初始化浏览器对象
browser = webdriver.Chrome()
# 向指定网址发起GET请求
browser.get(url)