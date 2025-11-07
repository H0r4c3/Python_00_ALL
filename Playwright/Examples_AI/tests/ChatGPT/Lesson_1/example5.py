'''
Path("artifacts")	creates a folder path using Python’s pathlib

.mkdir(exist_ok=True)	makes the folder if it doesn’t exist

page.screenshot(path=...)	saves a PNG image of the current page

Now Playwright will always create and save artifacts/homepage.png
in the same folder as your Python file (for example, right next to example5.py)
'''

import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://playwright.dev/python/")

        out_path = Path(__file__).parent / "artifacts" # 
        
        print(Path(__file__)) # the path of the file (example5.py)
        print(Path(__file__).parent) # the path of the parent of the file
        
        out_path.mkdir(exist_ok=True)
        screenshot_path = out_path / "homepage.png"

        await page.screenshot(path=str(screenshot_path))  # take screenshot
        print("Screenshot saved to:", screenshot_path)

        await browser.close()

asyncio.run(main())
