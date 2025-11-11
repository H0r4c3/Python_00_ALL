'''
Example 37: Get Element by Label
New instruction: page.get_by_label("Username")
What it does:
•	Finds an input field by its label (the text next to it)
•	Labels are the text that describe what the field is for
•	Very useful for forms
Expected result: You should see "tomsmith" typed in the username field.

'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/login")
    page.get_by_label("Username").fill("tomsmith")
    print("Filled using label!")
    import time
    time.sleep(2)
    browser.close()
