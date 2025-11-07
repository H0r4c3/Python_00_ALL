'''
Example 22: Right Click (Context Menu)
New instruction: page.click("textarea[name='q']", button="right")
What it does:
•	Finds the search box
•	.click() with button="right" right clicks on it
•	Like right-clicking with your mouse to open context menu
Expected result: You should see the right-click menu appear on the search box.

'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.com")
    page.click("textarea[name='q']", button="right")
    print("Right clicked!")
    import time
    time.sleep(2)
    browser.close()
