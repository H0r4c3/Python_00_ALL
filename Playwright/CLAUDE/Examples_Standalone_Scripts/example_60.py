'''
Example 60: Wait for URL
New instruction: page.wait_for_url("**/search?q=**")
What it does:
•	Waits until the URL matches a pattern
•	"**/search?q=**" - ** means "anything", so it waits for URLs containing /search?q=
•	Confirms the page has navigated to search results
•	Useful when clicking buttons that change the URL
Expected result: The script waits for the URL to change before printing.

'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.com")
    page.fill("textarea[name='q']", "Playwright Python")
    page.press("textarea[name='q']", "Enter")
    page.wait_for_url("**/search?q=**")
    print("URL changed to search results!")
    browser.close()
