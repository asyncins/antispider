from selenium import webdriver

url = 'http://www.porters.vip/verify/sign'
# 初始化浏览器对象
browser = webdriver.Chrome()
# 向指定网址发起GET请求
browser.get(url)
# 使用CSS选择器定位按钮，并点击按钮
browser.find_element_by_css_selector('#fetch_button').click()
# 使用CSS选择器定位文本，并取出文本内容
resp = browser.find_element_by_css_selector('#content').text
print(resp)
# 程序退出，关闭浏览器
browser.quit()