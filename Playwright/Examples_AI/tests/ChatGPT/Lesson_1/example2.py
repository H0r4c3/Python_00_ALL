'''
launch() a browser

p.chromium.launch()   ->   Open a Chromium browser

The word 'await' means “wait until this finishes, but don’t block everything else.”
'''

import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        # If you want to see the browser window appear, change to False
        browser = await p.chromium.launch(headless=False)
        print("Browser opened")
        await asyncio.sleep(3)  # wait 3 seconds to see it
        await browser.close()
        print("Browser closed")

asyncio.run(main())