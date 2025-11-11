'''
Example 30: Wait for Timeout (Pause)
New instruction: page.wait_for_timeout(3000)
What it does:
•	Pauses the script for a specific time
•	Time is in milliseconds (1000 = 1 second)
•	3000 = 3 seconds
•	Similar to time.sleep() but specifically for Playwright
Expected result: It waits 3 seconds between the two print messages.

'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.com")
    print("Waiting...")
    page.wait_for_timeout(3000)
    print("3 seconds passed!")
    browser.close()
