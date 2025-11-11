'''
Example 2: Launch a Browser
New instruction: browser = p.chromium.launch(headless=False)
What it does:
•	p.chromium tells Playwright to use Chrome browser
•	.launch() actually opens/starts the browser
•	headless=False makes the browser window visible
•	browser stores the opened browser so you can use it
Expected result: Chrome browser window opens briefly, then closes.

'''

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    print("Browser opened!")
    browser.close()