'''
Example 67: Type into Prompt Dialog
New instruction: dialog.accept("Hello Playwright!")
What it does:
•	Accepts a prompt dialog AND types text into it
•	"Hello Playwright!" the text to enter in the prompt
•	.accept() with text parameter fills the input field
•	Like typing in a prompt box and clicking OK
Expected result: The prompt appears, gets filled with text, and is accepted!

'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    def handle_dialog(dialog):
        dialog.accept("Hello Playwright!")
    
    page.on("dialog", handle_dialog)
    
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    page.click("button:has-text('Click for JS Prompt')")
    print("Typed into prompt!")
    import time
    time.sleep(2)
    browser.close()
