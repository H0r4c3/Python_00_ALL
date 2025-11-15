'''
Example 18: Check a Checkbox
New instruction: page.check("input[type='checkbox']")
What it does:
•	Finds a checkbox element
•	.check() checks the checkbox (puts a checkmark in it)
•	Like clicking on an empty checkbox to mark it
Expected result: You should see the first checkbox get checked.

'''
from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    page.check("input[type='checkbox']")
    time.sleep(2)
    print("Checkbox checked!")
    time.sleep(2)
    browser.close()
