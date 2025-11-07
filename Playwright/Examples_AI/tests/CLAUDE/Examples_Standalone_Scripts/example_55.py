'''
Example 55: Set Viewport Size (Window Size)
New instruction: page.set_viewport_size({"width": 800, "height": 600})
What it does:
•	Changes the browser window size
•	width: 800 pixels wide
•	height: 600 pixels tall
•	Useful for testing responsive design (mobile, tablet, desktop sizes)
Expected result: You should see a smaller browser window (800x600).

'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.set_viewport_size({"width": 800, "height": 600})
    page.goto("https://www.google.com")
    print("Viewport set to 800x600!")
    import time
    time.sleep(2)
    browser.close()
