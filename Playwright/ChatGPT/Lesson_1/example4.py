'''
await page.title()	reads the text from the browser’s title bar
assert condition	checks that something is true — otherwise, Python stops with an error AssertionError
'''

import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)  # use False if you want to see it
        page = await browser.new_page()
        await page.goto("https://playwright.dev/python/")
        
        title = await page.title()        # get the title of the page
        print("Page title:", title)

        assert "Playwright" in title      # verify text inside title; if not -> AssertionError
        print("Title assertion passed!")  # only prints if test passes

        await browser.close()

asyncio.run(main())
