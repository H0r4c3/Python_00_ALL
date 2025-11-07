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

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.com")
    page.fill("textarea[name='q']", "First text")
    print("Typed first text")
    import time
    time.sleep(1)
    page.fill("textarea[name='q']", "")
    print("Cleared the field!")
    time.sleep(2)
    browser.close()
