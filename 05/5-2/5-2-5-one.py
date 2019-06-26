from selenium import webdriver

url = 'http://www.ituring.com.cn/'
# 初始化浏览器对象
browser = webdriver.Chrome()
# 向指定网址发起GET请求
browser.get(url)
# 使用CSS选择器定位搜索框，并输入文字
browser.find_element_by_css_selector('.key').send_keys('Python')