'''
Example 26: Reload Page
New instruction: page.reload()
What it does:
•	Reloads/refreshes the current page
•	Like pressing F5 or clicking the refresh button in your browser
•	The page loads again from scratch
Expected result: You should see Google load, then reload.

'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.com")
    print("Page loaded")
    page.reload()
    print("Page reloaded!")
    import time
    time.sleep(2)
    browser.close()
