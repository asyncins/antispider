import asyncio
from pyppeteer import launch


async def main():
    # 初始化浏览器对象
    browser = await launch()
    # 在浏览器上下文中创建新页面
    page = await browser.newPage()
    # 打开目标网址
    await page.goto('http://www.ituring.com.cn/')
    # 在指定位置输入文本
    await page.type('.key', 'Python')
    # 截图并保存为ituring.png
    await page.screenshot({'path': 'ituring.png'})
    # 关闭浏览器对象
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())