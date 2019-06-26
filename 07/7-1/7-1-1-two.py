import asyncio
from pyppeteer import launch

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('http://www.porters.vip/features/webdriver.html')
    # 定位按钮元素并点击
    await page.click('.btn.btn-primary.btn-lg')
    # 等待1秒
    await asyncio.sleep(1)
    # 网页截图保存
    await page.screenshot({'path': 'webdriver.png'})
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())