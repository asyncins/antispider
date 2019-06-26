import asyncio
from pyppeteer import launch

async def main():
    # 初始化浏览器对象
    browser = await launch()
    # 在浏览器上下文中创建新页面
    page = await browser.newPage()
    # 打开目标网址
    await page.goto('http://www.porters.vip/verify/sign')
    # 点击指定按钮
    await page.click('#fetch_button')
    # 读取页面指定位置的文本
    resp = await page.xpath('//*[@id="content"]')
    text = await(await resp[0].getProperty('textContent')).jsonValue()
    print(text)
    # 关闭浏览器对象
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())