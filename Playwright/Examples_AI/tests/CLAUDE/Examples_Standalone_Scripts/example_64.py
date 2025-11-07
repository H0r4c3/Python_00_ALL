'''
Example 64: Handle Alert/Dialog
New instruction: page.on("dialog", lambda dialog: dialog.accept())
What it does:
•	Sets up a listener for popup dialogs (alerts, confirms, prompts)
•	page.on("dialog", ...) watches for dialogs
•	dialog.accept() clicks "OK" on the dialog
•	Must be set up BEFORE the dialog appears
Expected result: The alert popup appears and is automatically accepted!

'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    page.on("dialog", lambda dialog: dialog.accept())
    
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    page.click("button:has-text('Click for JS Alert')")
    print("Alert accepted!")
    import time
    time.sleep(2)
    browser.close()
