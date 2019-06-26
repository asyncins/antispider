from selenium import webdriver


browser = webdriver.Chrome()
# 驱动Chrome浏览器打开滑动验证码示例页面
browser.get('http://www.porters.vip/captcha/sliders.html')
# 定位滑块
hover = browser.find_element_by_css_selector('.hover')

action = webdriver.ActionChains(browser)
action.click_and_hold(hover).perform()  # 点击并保持不松开
action.move_by_offset(340, 0)  # 设置滑动距离，横向距离340px，纵向距离0px
action.release().perform()  # 松开鼠标