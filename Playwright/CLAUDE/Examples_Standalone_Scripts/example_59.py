'''
Example 59: Wait for Selector
New instruction: page.wait_for_selector("h3")
What it does:
•	Waits until an element matching the selector appears on the page
•	"h3" waits for any heading element
•	Stops waiting once it finds at least one
•	Useful when content loads dynamically
Expected result: The script waits for search results to appear before printing.

'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.com")
    page.fill("textarea[name='q']", "Playwright Python")
    page.press("textarea[name='q']", "Enter")
    page.wait_for_selector("h3")
    print("Search results appeared!")
    browser.close()
