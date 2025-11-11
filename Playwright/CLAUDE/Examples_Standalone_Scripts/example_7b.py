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
from pathlib import Path

# Get script's directory
script_dir = Path(__file__).parent
#os.makedirs(script_dir/"screenshots", exist_ok=True) # why do I need this???????

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://practicesoftwaretesting.com")
    page.screenshot(path=script_dir/"screenshots/screenshot7.png")
    print(f"Screenshot saved here: {script_dir}\\screenshots")
    context.close()
    browser.close()


