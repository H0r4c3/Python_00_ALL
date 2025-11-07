'''
Example 14: Check if Element Exists
New instruction: is_visible = page.locator("textarea[name='q']").is_visible()
What it does:
•	Finds the search box
•	.is_visible() checks if the element is visible on the page
•	Returns True if visible, False if not
Expected result: You should see: Search box visible: True
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.com")
    is_visible = page.locator("textarea[name='q']").is_visible()
    print(f"Search box visible: {is_visible}")
    browser.close()

'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.com")
    is_visible = page.locator("textarea[name='q']").is_visible()
    print(f"Search box visible: {is_visible}")
    browser.close()
