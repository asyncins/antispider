from selenium import webdriver
browser = webdriver.Chrome()
# 访问指定URL
browser.get('http://www.porters.vip/captcha/mousemove.html')
# 定位页面中的first按钮
button = browser.find_element_by_class_name('button1')
# 点击first按钮
button.click()