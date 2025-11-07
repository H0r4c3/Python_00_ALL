'''
open a page and go to Playwright’s site

browser.new_page()	opens a new browser tab

page.goto(url)	tells that tab to load the given website

Every real test begins this way:
open browser → create page → navigate to a URL → check something.
'''

import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()               # open a new tab
        await asyncio.sleep(3)
        await page.goto("https://playwright.dev/python/")  # go to the URL
        print("Page opened!")
        await asyncio.sleep(3)  # keep it open 3 s so you can see it
        await browser.close()

asyncio.run(main())
