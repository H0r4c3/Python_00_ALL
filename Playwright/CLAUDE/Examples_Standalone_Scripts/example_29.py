'''
Example 29: Focus on Element
New instruction: page.focus("textarea[name='q']")
What it does:
•	Puts the cursor in the element (makes it active)
•	Like clicking in an input field to start typing
•	The element gets a border/outline showing it's selected
Expected result: You should see the cursor blinking in the search box.

'''
from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://practicesoftwaretesting.com")
    page.locator("[data-test=\"sort\"]").focus()
    print("Sort box focused!")
    time.sleep(2)
    page.focus("[data-test=\"search-query\"]")
    time.sleep(2)
    print("Search box focused!")
    time.sleep(2)
    browser.close()
