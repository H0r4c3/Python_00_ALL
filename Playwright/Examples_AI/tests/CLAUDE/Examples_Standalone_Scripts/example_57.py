'''
Example 57: Take Full Page Screenshot
New instruction: page.screenshot(path="full_page.png", full_page=True)
What it does:
•	Takes a screenshot of the entire page (not just visible area)
•	full_page=True captures everything, even parts you need to scroll to see
•	Without this, it only captures what's visible on screen
•	Useful for capturing long pages
Expected result: Check your folder - full_page.png will be much taller than a regular screenshot!

'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.wikipedia.org")
    page.screenshot(path="full_page.png", full_page=True)
    print("Full page screenshot saved!")
    browser.close()
