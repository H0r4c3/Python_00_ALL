'''
Example 9: Type Text
New instruction: page.fill("textarea[name='q']", "Playwright Python")
What it does:
•	Finds the search box using the selector
•	Types the text "Playwright Python" into it
•	Like typing on your keyboard
Expected result: You should see "Playwright Python" appear in Google's search box.

'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.com")
    page.fill("textarea[name='q']", "Playwright Python")
    print("Text typed!")
    browser.close()
