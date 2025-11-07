'''
Example 4: Navigate to a Website
New instruction: page.goto("https://www.google.com")
What it does:
•	Goes to the URL you specify
•	Like typing a website address in the browser and pressing Enter
•	The browser will actually load Google's homepage
Expected result: Chrome opens, Google loads, then closes.

'''

from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    time.sleep(3)
    page = browser.new_page()
    time.sleep(5)
    page2 = browser.new_page()
    time.sleep(5)
    #page.goto("https://www.google.com")
    page.goto('https://practicesoftwaretesting.com')
    time.sleep(5)
    print("Navigated to Practice Software Testing!")
    browser.close()