from selenium import webdriver
browser = webdriver.Chrome()

# 访问指定URL
browser.get('http://www.porters.vip/captcha/mousemove.html')
# 定位页面中的first按钮
hover = browser.find_element_by_class_name('button1')

action = webdriver.ActionChains(browser)
action.click_and_hold(hover).perform()  # 点击并保持不松开
# 设置滑动距离，横向总距离340px，纵向晃动
action.move_by_offset(100, 3)
action.move_by_offset(40, -5)
action.move_by_offset(10, 3)
action.move_by_offset(5, 2)
action.move_by_offset(10, -1)
action.move_by_offset(30, 3)
action.move_by_offset(55, -2)
action.move_by_offset(10, 1)
action.move_by_offset(30, 3)
action.move_by_offset(20, -1)
action.move_by_offset(10, -4)
action.move_by_offset(10, 2)
action.move_by_offset(10, -6)
action.release().perform()  # 松开鼠标