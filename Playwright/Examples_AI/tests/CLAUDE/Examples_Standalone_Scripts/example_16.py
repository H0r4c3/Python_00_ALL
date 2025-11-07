'''
Example 16: Get Element Attribute
New instruction: link = page.locator("h3").first.locator("..").get_attribute("href")
What it does:
•	Finds the first h3 element
•	.locator("..") goes to the parent element (the link)
•	.get_attribute("href") gets the href attribute (the URL)
•	Returns the link URL as text
Expected result: You should see the URL of the first search result.

'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.com")
    page.fill("textarea[name='q']", "Playwright Python")
    page.press("textarea[name='q']", "Enter")
    page.wait_for_load_state("networkidle")
    link = page.locator("h3").first.locator("..").get_attribute("href")
    print(f"First result link: {link}")
    browser.close()

