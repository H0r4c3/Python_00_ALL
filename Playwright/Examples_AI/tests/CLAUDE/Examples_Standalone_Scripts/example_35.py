'''
Example 35: Get Element by Text
New instruction: page.get_by_text("Login Page")
What it does:
•	Finds an element that contains the exact text "Login Page"
•	Very useful when you want to find something by what it says
•	More natural than using CSS selectors
Expected result: The script finds the "Login Page" heading on the page.

'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/login")
    page.get_by_text("Login Page").is_visible()
    print("Found 'Login Page' text!")
    import time
    time.sleep(2)
    browser.close()
