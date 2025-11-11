'''
Example 10: Press a Key
New instruction: page.press("textarea[name='q']", "Enter")
What it does:
•	Finds the search box
•	Presses the Enter key (like hitting Enter on your keyboard)
•	This submits the search and shows results
Expected result: The text is typed, then Enter is pressed, and Google search results appear!

'''
from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://practicesoftwaretesting.com")
    page.fill('[data-test=\"search-query\"]', "Playwright Python")
    time.sleep(5)
    page.press("[data-test=\"search-submit\"]", "Enter")
    print("Enter key pressed!")
    time.sleep(5)
    browser.close()