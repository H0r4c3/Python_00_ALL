'''
Example 68: Handle Multiple Pages/Tabs
New instruction: with page.expect_popup() as popup_info: and new_page = popup_info.value
What it does:
•	expect_popup() waits for a new tab/window to open
•	Captures the new page when it opens
•	popup_info.value gets the new page object
•	Now you can control the new tab with new_page
Expected result: A new tab opens and you see its title printed!

'''

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/windows")
    
    with page.expect_popup() as popup_info:
        page.click("a:has-text('Click Here')")
    
    new_page = popup_info.value
    print(f"New page title: {new_page.title()}")
    import time
    time.sleep(2)
    browser.close()

