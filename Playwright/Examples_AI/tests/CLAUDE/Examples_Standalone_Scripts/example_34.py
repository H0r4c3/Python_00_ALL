'''
Example 34: Get Element by Role
New instruction: page.get_by_role("textbox", name="username")
What it does:
•	Finds elements by their role (type) instead of CSS selector
•	"textbox" finds input fields
•	name="username" finds the one with label/name "username"
•	More readable and recommended by Playwright
Expected result: You should see "tomsmith" typed in the username field.

'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/login")
    page.get_by_role("textbox", name="username").fill("tomsmith")
    print("Username filled using role!")
    import time
    time.sleep(2)
    browser.close()
