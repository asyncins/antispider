import asyncio
from pyppeteer import launch

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('http://www.porters.vip/features/browser.html')
    await page.setViewport({'width': 1000, 'height': 1000})
    await page.screenshot({'path': 'browser.png'})
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())