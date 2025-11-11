'''
Example 8: Click a Button
New instruction: page.click("textarea[name='q']")
What it does:
•	Finds an element on the page using a selector
•	"textarea[name='q']" is a CSS selector that identifies Google's search box
•	Clicks on it (like moving your mouse and clicking)
Expected result: The browser opens Google, and the search box gets clicked (cursor appears in it).

'''

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://practicesoftwaretesting.com")
    page.click('[data-test=\"search-query\"]')
    print("Clicked in Search field!")
    browser.close()
