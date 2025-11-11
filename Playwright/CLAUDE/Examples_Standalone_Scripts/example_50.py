'''
Example 50: Evaluate JavaScript
New instruction: page.evaluate("() => document.title")
What it does:
•	Runs JavaScript code in the browser
•	"() => document.title" JavaScript that gets the page title
•	Returns the result to Python
•	Useful for accessing things Playwright can't directly get
Expected result: You should see the page title retrieved using JavaScript.

'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.com")
    result = page.evaluate("() => document.title")
    print(f"Page title via JavaScript: {result}")
    browser.close()
