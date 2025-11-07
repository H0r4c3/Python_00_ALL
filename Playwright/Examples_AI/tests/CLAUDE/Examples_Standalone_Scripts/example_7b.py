'''
Example 7b: Screenshot in Folder
New instruction: os.makedirs("screenshots", exist_ok=True) and page.screenshot(path="screenshots/google.png")
What it does:
•	os.makedirs() creates a folder named screenshots if it doesn't exist
•	exist_ok=True means "don't give error if folder already exists"
•	Saves screenshot inside the screenshots folder
Expected result: Screenshot saved in screenshots/google.png inside your Playwright folder.

'''

from playwright.sync_api import sync_playwright
import os

os.makedirs("screenshots", exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.com")
    page.screenshot(path="screenshots/google.png")
    print("Screenshot saved in screenshots folder!")
    browser.close()


