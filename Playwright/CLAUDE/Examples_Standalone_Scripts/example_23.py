'''
Example 23: Get Current URL
New instruction: current_url = page.url
What it does:
•	page.url gets the current URL of the page
•	Returns the URL as text (what you see in the address bar)
•	Notice: no parentheses () - it's a property, not a method
Expected result: You should see the Google search results URL printed (something with search?q=).

'''
from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.com")
    time.sleep(3)
    page.fill("textarea[name='q']", "Playwright Python")
    page.press("textarea[name='q']", "Enter")
    page.wait_for_load_state("networkidle")
    time.sleep(5)
    current_url = page.url
    print(f"Current URL: {current_url}")
    browser.close()
