'''
Example 9: Type Text
New instruction: page.fill("textarea[name='q']", "Playwright Python")
What it does:
•	Finds the search box using the selector
•	Types the text "Playwright Python" into it
•	Like typing on your keyboard
Expected result: You should see "Playwright Python" appear in Search box.

'''
from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://practicesoftwaretesting.com")
    page.fill('[data-test=\"search-query\"]', "Playwright Python")
    time.sleep(5)
    print("Text typed!")
    browser.close()
