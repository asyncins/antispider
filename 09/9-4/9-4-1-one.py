from selenium import webdriver
browser = webdriver.Chrome()
# 驱动Chrome浏览器打开滑动验证码示例页面
browser.get('http://www.porters.vip/captcha/jigsaw.html')
# 定位滑块
jigsawCircle = browser.find_element_by_css_selector('#jigsawCircle')
action = webdriver.ActionChains(browser)
# 点击并保持不松开
action.click_and_hold(jigsawCircle).perform()
# 返回当前页面的html代码
html = browser.page_source

import re
from parsel import Selector
sel = Selector(html)
# 获取圆角矩形和缺口的CSS样式
mbk_style = sel.css('#missblock::attr("style")').get()
tbk_style = sel.css('#targetblock::attr("style")').get()
# 编写用于从CSS样式中提取left属性值的匿名函数
extract = lambda x: ''.join(re.findall('left: (\d+|\d+.\d+)px', x))
# 调用匿名函数获取CSS样式中的left属性值
mbk_left = extract(mbk_style)
tbk_left = extract(tbk_style)
# 计算当前拼图验证码滑块所需移动的距离
distance = float(tbk_left) - float(mbk_left)

action.move_by_offset(distance, 0)  # 设置滑动距离
action.release().perform()  # 松开鼠标