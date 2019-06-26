from selenium.webdriver import Chrome
import time

browser = Chrome()
browser.get('http://www.porters.vip/features/webdriver.html')
# 定位按钮并点击
browser.find_element_by_css_selector('.btn.btn-primary.btn-lg').click()
# 定位到文章内容元素
elements = browser.find_element_by_css_selector('#content')
time.sleep(1)
# 打印文章内容
print(elements.text)
browser.close()