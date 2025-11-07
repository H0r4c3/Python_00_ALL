'''
Example 53: Scroll Element into View
New instruction: page.locator("footer").scroll_into_view_if_needed()
What it does:
•	Finds the footer element
•	.scroll_into_view_if_needed() scrolls the page until that element is visible
•	Only scrolls if the element is not already visible
•	Playwright does this automatically before clicking, but you can do it manually
Expected result: You should see the page scroll to show the footer.

'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.wikipedia.org")
    page.locator("footer").scroll_into_view_if_needed()
    print("Scrolled footer into view!")
    import time
    time.sleep(2)
    browser.close()
