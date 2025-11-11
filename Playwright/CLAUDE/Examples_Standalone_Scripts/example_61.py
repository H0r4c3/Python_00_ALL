'''
Example 61: Check if Element is Hidden
New instruction: is_hidden = page.locator("div#nonexistent").is_hidden()
What it does:
•	Checks if an element is hidden or doesn't exist
•	.is_hidden() returns True if hidden or not found, False if visible
•	Opposite of .is_visible()
•	Useful for checking if elements are properly hidden
Expected result: You should see: Element is hidden: True (because the element doesn't exist).

'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.com")
    is_hidden = page.locator("div#nonexistent").is_hidden()
    print(f"Element is hidden: {is_hidden}")
    browser.close()
