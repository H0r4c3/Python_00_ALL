'''
Example 69: Switch Between Pages/Tabs
New instruction: page1.bring_to_front()
What it does:
•	Brings a specific page/tab to the front (makes it active)
•	Like clicking on a tab to switch to it
•	Useful when you have multiple tabs open
•	The page becomes visible and focused
Expected result: You see two tabs open, then it switches back to the first one!

'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page1 = browser.new_page()
    page1.goto("https://www.google.com")
    print(f"Page 1: {page1.title()}")
    
    page2 = browser.new_page()
    page2.goto("https://www.wikipedia.org")
    print(f"Page 2: {page2.title()}")
    
    page1.bring_to_front()
    print("Switched to Page 1!")
    import time
    time.sleep(2)
    browser.close()
