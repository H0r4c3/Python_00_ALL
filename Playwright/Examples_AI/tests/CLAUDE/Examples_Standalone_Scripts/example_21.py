'''
Example 21: Double Click
New instruction: page.dblclick("textarea[name='q']")
What it does:
•	Finds the search box
•	.dblclick() double clicks on it (clicks twice quickly)
•	Like double-clicking with your mouse
Expected result: You should see the search box get double-clicked.

'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.com")
    page.dblclick("textarea[name='q']")
    print("Double clicked!")
    import time
    time.sleep(2)
    browser.close()
