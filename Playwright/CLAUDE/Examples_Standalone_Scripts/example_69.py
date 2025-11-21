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
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page1 = browser.new_page()
    page1.goto("https://practicesoftwaretesting.com/")
    print(f"Page 1: {page1.title()}")
    
    time.sleep(3)
    
    page2 = browser.new_page()
    page2.goto("https://www.wikipedia.org")
    print(f"Page 2: {page2.title()}")
    
    time.sleep(3)
    
    page1.bring_to_front()
    print("Switched to Page 1!")
    time.sleep(3)
    browser.close()
