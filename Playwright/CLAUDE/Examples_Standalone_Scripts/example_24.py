'''
Example 24: Go Back in Browser History
New instruction: page.go_back()
What it does:
•	Goes back to the previous page in browser history
•	Like clicking the back arrow button in your browser
Expected result: You should see it go to Wikipedia, then back to Google.

'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.com")
    page.goto("https://www.wikipedia.org")
    print("On Wikipedia")
    page.go_back()
    print("Went back to Google")
    import time
    time.sleep(2)
    browser.close()
