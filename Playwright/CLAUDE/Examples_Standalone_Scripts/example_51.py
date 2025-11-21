'''
Example 51: Scroll Page Down
New instruction: page.evaluate("window.scrollBy(0, 500)")
What it does:
•	Uses JavaScript to scroll the page
•	window.scrollBy(0, 500) scrolls down 500 pixels (0 = horizontal, 500 = vertical)
•	Negative numbers scroll up: (0, -500)
•	Like using your mouse wheel to scroll
Expected result: You should see the page scroll down.

'''
from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.wikipedia.org")
    time.sleep(2)
    page.evaluate("window.scrollBy(0, 500)")
    print("Scrolled down 500 pixels!")
    time.sleep(2)
    browser.close()
