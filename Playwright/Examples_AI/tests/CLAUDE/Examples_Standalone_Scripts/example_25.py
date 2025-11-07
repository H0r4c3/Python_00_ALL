'''
Example 25: Go Forward in Browser History
New instruction: page.go_forward()
What it does:
•	Goes forward to the next page in browser history
•	Like clicking the forward arrow button in your browser
•	Only works if you went back first
Expected result: You should see it go to Wikipedia, back to Google, then forward to Wikipedia again.

'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.com")
    page.goto("https://www.wikipedia.org")
    page.go_back()
    print("Went back to Google")
    page.go_forward()
    print("Went forward to Wikipedia")
    import time
    time.sleep(2)
    browser.close()
