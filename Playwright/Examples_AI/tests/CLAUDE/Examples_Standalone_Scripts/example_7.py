'''
Example 7: Take a Screenshot
New instruction: page.screenshot(path="google.png")
What it does:
•	Takes a picture of the entire webpage
•	Saves it as a file named google.png in your Playwright folder
•	You can open the PNG file to see the screenshot
Expected result: After running, check your Playwright folder - you should see a new file google.png.

'''

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.com")
    page.screenshot(path="google.png")
    print("Screenshot saved!")
    browser.close()

