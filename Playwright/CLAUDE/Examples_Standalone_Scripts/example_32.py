'''
Example 32: Check if Element is Enabled
New instruction: is_enabled = page.locator("textarea[name='q']").is_enabled()
What it does:
•	Checks if an element is enabled (can be used)
•	.is_enabled() returns True if enabled, False if disabled
•	Disabled elements are grayed out and can't be clicked/typed in
Expected result: You should see: Search box enabled: True

'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.com")
    is_enabled = page.locator("textarea[name='q']").is_enabled()
    print(f"Search box enabled: {is_enabled}")
    browser.close()
