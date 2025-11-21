'''
Example 28: Clear Input Field
New instruction: page.fill("textarea[name='q']", "")
What it does:
•	Uses .fill() with empty text ""
•	Clears all text from the input field
•	Like selecting all text and deleting it
Expected result: You should see "First text" appear, then disappear after 1 second.

'''
from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://practicesoftwaretesting.com/")
    page.fill("[data-test=\"search-query\"]", "First text")
    #page.locator("[data-test=\"search-query\"]").fill("First text")
    print("Typed first text")
    time.sleep(3)
    page.fill("[data-test=\"search-query\"]", "")
    print("Cleared the field!")
    time.sleep(2)
    browser.close()
    
    
    
