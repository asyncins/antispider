from selenium import webdriver
browser = webdriver.Chrome()

# 访问指定URL
browser.get('http://www.porters.vip/captcha/mousemove.html')
# 定位页面中的first按钮
hover = browser.find_element_by_class_name('button1')

action = webdriver.ActionChains(browser)
action.click_and_hold(hover).perform()  # 点击并保持不松开
action.move_by_offset(340, 5)  # 设置滑动距离，横向距离340px，纵向距离5px
action.release().perform()  # 松开鼠标