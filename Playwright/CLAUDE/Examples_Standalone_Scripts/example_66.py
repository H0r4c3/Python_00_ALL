'''
Example 66: Get Dialog Message
New instruction: dialog.message
What it does:
•	Gets the text from the dialog/alert
•	dialog.message returns the message as a string
•	You can read what the alert says before accepting/dismissing
•	Useful for verifying alert content
Expected result: You should see the alert message printed in the terminal!

'''
from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    def handle_dialog(dialog):
        print(f"Dialog message: {dialog.message}")
        dialog.accept()
    
    page.on("dialog", handle_dialog)
    
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    time.sleep(2)
    page.click("button:has-text('Click for JS Alert')")
    time.sleep(2)
    page.click("button:has-text('Click for JS Confirm')")
    time.sleep(2)
    browser.close()
