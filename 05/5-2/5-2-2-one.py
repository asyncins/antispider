from selenium import webdriver
from datetime import datetime
# 记录开始时间
starts = datetime.now()
url = 'http://www.porters.vip/verify/sign'
# 初始化浏览器对象
browser = webdriver.Chrome()
for i in range(30):
    # 循环30次访问目标url
    browser.get(url)
    resp = browser.page_source
browser.quit()
# 计算并打印耗时秒数
runtime = datetime.now() - starts
print(runtime.total_seconds())