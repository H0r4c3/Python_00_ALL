'''
Example 19: Uncheck a Checkbox
New instruction: page.uncheck("input[type='checkbox']:checked")
What it does:
•	Finds a checkbox that is already checked (:checked)
•	.uncheck() removes the checkmark
•	Like clicking on a checked checkbox to unmark it
Expected result: You should see the second checkbox (which is already checked) get unchecked.

'''
from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    page.uncheck("input[type='checkbox']:checked")
    time.sleep(2)
    print("Checkbox unchecked!")
    time.sleep(2)
    browser.close()
