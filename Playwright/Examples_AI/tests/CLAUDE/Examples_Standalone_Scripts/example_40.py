'''
Example 40: Get Element by Title
New instruction: page.get_by_title("Search")
What it does:
•	Finds an element by its title attribute
•	Title is the tooltip text that appears when you hover over an element
•	Another way to locate elements
Expected result: You should see "Playwright" typed in the search box.

'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.com")
    page.get_by_title("Search").fill("Playwright")
    print("Filled using title attribute!")
    import time
    time.sleep(2)
    browser.close()
