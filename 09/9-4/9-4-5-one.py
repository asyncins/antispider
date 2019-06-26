from selenium import webdriver


browser = webdriver.Chrome()
# 驱动Chrome浏览器打开滑动验证码示例页面
browser.get('http://www.porters.vip/captcha/jigsawCanvas.html')

# 定位滑块
jigsawCircle = browser.find_element_by_css_selector('#jigsawCircle')
# 定位背景图片
jigsawCanvas = browser.find_element_by_css_selector('#jigsawCanvas')
jigsawCanvas.screenshot('before.png')
action = webdriver.ActionChains(browser)
# 点击并保持不松开
action.click_and_hold(jigsawCircle).perform()
# 执行js隐藏圆角矩形的HTML代码
scripts = """
var missblock = document.getElementById('missblock');
missblock.style['visibility'] = 'hidden';
"""
browser.execute_script(scripts)
# 再次截图
jigsawCanvas.screenshot('after.png')