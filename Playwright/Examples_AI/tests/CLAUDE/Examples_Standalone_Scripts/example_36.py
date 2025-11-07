'''
Example 36: Get Element by Placeholder
New instruction: page.get_by_placeholder("Search")
What it does:
•	Finds an input field by its placeholder text
•	Placeholder is the gray text you see inside empty input fields
•	Another readable way to find elements
Expected result: You should see "Playwright" typed in Google's search box.

'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.com")
    page.get_by_placeholder("Search").fill("Playwright")
    print("Filled using placeholder!")
    import time
    time.sleep(2)
    browser.close()
