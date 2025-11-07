'''
Example 15: Wait for Element to Appear
New instruction: page.locator("h3").first.wait_for()
What it does:
•	Finds the first h3 element
•	.wait_for() waits until that element appears on the page
•	Useful when pages load slowly or content loads dynamically
Expected result: The script waits until the first search result appears before printing the message.

'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.com")
    page.fill("textarea[name='q']", "Playwright Python")
    page.press("textarea[name='q']", "Enter")
    page.locator("h3").first.wait_for()
    print("First result appeared!")
    browser.close()
