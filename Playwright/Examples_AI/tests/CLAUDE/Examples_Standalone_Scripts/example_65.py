'''
Example 65: Dismiss Alert/Dialog
New instruction: page.on("dialog", lambda dialog: dialog.dismiss())
What it does:
•	Sets up a listener for dialogs
•	dialog.dismiss() clicks "Cancel" on the dialog
•	Opposite of .accept()
•	Used for confirm dialogs where you want to say "No"
Expected result: The confirm dialog appears and is automatically dismissed (cancelled)!

'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    page.on("dialog", lambda dialog: dialog.dismiss())
    
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    page.click("button:has-text('Click for JS Confirm')")
    print("Alert dismissed!")
    import time
    time.sleep(2)
    browser.close()
