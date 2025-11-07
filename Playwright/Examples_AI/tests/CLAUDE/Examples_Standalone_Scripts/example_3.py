'''
Example 3: Open a Page (Tab)
New instruction: page = browser.new_page()
What it does:
•	Opens a new tab/page in the browser
•	Like clicking "New Tab" manually
•	Stores the page in variable page so you can use it
Expected result: Chrome opens with a blank tab, then closes.

'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    print("New page opened!")
    browser.close()
