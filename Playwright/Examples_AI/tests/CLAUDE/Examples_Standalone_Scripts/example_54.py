'''
Example 54: Get Page Content (HTML)
New instruction: html = page.content()
What it does:
•	Gets the complete HTML source code of the page
•	Returns everything as a string
•	[:200] prints only first 200 characters (the full HTML is very long)
•	Like viewing "Page Source" in browser
Expected result: You should see the length and beginning of Google's HTML code.

'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.com")
    html = page.content()
    print(f"HTML length: {len(html)} characters")
    print(html[:200])
    browser.close()
