'''
Example 70: Close Specific Page/Tab
New instruction: page2.close()
What it does:
•	Closes a specific page/tab
•	browser.close() closes the entire browser
•	page.close() closes only that one tab
•	Other tabs remain open
Expected result: Two tabs open, then Wikipedia tab closes while Google stays open!

'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page1 = browser.new_page()
    page1.goto("https://www.google.com")
    
    page2 = browser.new_page()
    page2.goto("https://www.wikipedia.org")
    print("Opened 2 tabs")
    
    import time
    time.sleep(1)
    
    page2.close()
    print("Closed Wikipedia tab!")
    time.sleep(2)
    browser.close()(headless=False)
    print("Browser opened!")
    browser.close()
