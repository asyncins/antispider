import re
from selenium import webdriver
from parsel import Selector


url = 'http://www.porters.vip/captcha/clicks.html'
browser = webdriver.Chrome()
browser.get(url)
html = Selector(browser.page_source)
# 获取验证要求
require = html.css('#divTips::text').get()
# 用正则提取验证要求中的文字
target = re.findall('“(.)”', require)
print(target)