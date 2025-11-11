'''
Example 56: Emulate Mobile Device
New instruction: iphone = p.devices["iPhone 12"] and page = browser.new_page(**iphone)
What it does:
•	p.devices["iPhone 12"] gets iPhone 12 settings (screen size, user agent, etc.)
•	browser.new_page(**iphone) creates a page that pretends to be an iPhone
•	The website thinks you're on a real iPhone
•	Useful for testing mobile versions of websites
Expected result: You should see Google's mobile version in a phone-sized window.

'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    iphone = p.devices["iPhone 12"]
    page = browser.new_page(**iphone)
    page.goto("https://www.google.com")
    print("Emulating iPhone 12!")
    import time
    time.sleep(3)
    browser.close()
