'''
Example 38: Click Button by Role
New instruction: page.get_by_role("button", name="Login")
What it does:
•	Finds a button by its role and name
•	"button" looks for button elements
•	name="Login" finds the button with text "Login"
•	Then .click() clicks it
Expected result: You should see the login form get filled and submitted.

'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/login")
    page.get_by_label("Username").fill("tomsmith")
    page.get_by_label("Password").fill("SuperSecretPassword!")
    page.get_by_role("button", name="Login").click()
    print("Login button clicked!")
    import time
    time.sleep(2)
    browser.close()
