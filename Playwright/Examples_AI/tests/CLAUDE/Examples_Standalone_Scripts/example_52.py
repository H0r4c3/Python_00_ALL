'''
Example 52: Scroll to Bottom of Page
New instruction: page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
What it does:
•	Uses JavaScript to scroll to the very bottom
•	document.body.scrollHeight gets the total page height
•	window.scrollTo() scrolls to that position
•	Like pressing "End" key on your keyboard
Expected result: You should see the page jump to the very bottom.

'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.wikipedia.org")
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    print("Scrolled to bottom!")
    import time
    time.sleep(2)
    browser.close()
